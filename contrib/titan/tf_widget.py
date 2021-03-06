############################################################################
##
## Copyright (C) 2006-2010 University of Utah. All rights reserved.
##
## This file is part of VisTrails.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following to ensure GNU General Public
## Licensing requirements will be met:
## http://www.opensource.org/licenses/gpl-license.php
##
## If you are unsure which license is appropriate for your use (for
## instance, you are interested in developing a commercial derivative
## of VisTrails), please contact us at contact@vistrails.org.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
############################################################################

##############################################################################
# Transfer Function Widget for VTK

from PyQt4 import QtCore, QtGui
from core.modules.constant_configuration import ConstantWidgetMixin
from core.modules.basic_modules import new_constant, init_constant, Module
from core.utils.color import ColorByName
import vtk
import math
import pickle
import copy

################################################################################
# etc

def clamp(v, mn, mx, eps=0.0):
    mn += eps
    mx -= eps
    if v < mn: return mn
    if v > mx: return mx
    return v

##############################################################################
# Transfer Function object

class TransferFunction(object):

    def __init__(self):
        self._min_range = 0.0
        self._max_range = 1.0
        self._pts = []

    def set_range(self, mn, mx):
        self._min_range = mn
        self._max_range = mx

    def set_on_vtk_volume_property(self, vtk_volume_property):
        # Builds the opacity and color functions
        of = vtk.vtkPiecewiseFunction()
        cf = vtk.vtkColorTransferFunction()
        vp = vtk_volume_property
        for pt in self._pts:
            (scalar, opacity, color) = pt
            # Map scalar to tf range
            s = self._min_range + (self._max_range - self._min_range) * scalar
            of.AddPoint(s, opacity)
            cf.AddRGBPoint(s, color[0], color[1], color[2])
        vp.SetScalarOpacity(of)
        vp.SetColor(cf)

    def add_point(self, scalar, opacity, color):
        self._pts.append((scalar, opacity, color))
        self._pts.sort()

    def get_value(self, scalar):
        """get_value(scalar): returns the opacity and color
        linearly interpolated at the value. Useful for
        adding knots."""
        ix = 0
        while ix < len(self._pts) and self._pts[ix][0] > scalar:
            ix += 1
        if ix == 0:
            return (self._pts[0][1], self._pts[0][2])
        elif ix == len(self._pts):
            return (self._pts[-1][1], self._pts[-1][2])
        else:
            u = ((self._pts[ix][0] - scalar) /
                 (self._pts[ix][0] - self._pts[ix-1][0]))
            do = self._pts[ix][1] - self._pts[ix-1][1]
            dr = self._pts[ix][2][0] - self._pts[ix-1][2][0]
            dg = self._pts[ix][2][1] - self._pts[ix-1][2][1]
            db = self._pts[ix][2][2] - self._pts[ix-1][2][2]
            return (self._pts[ix-1][1] + u * do,
                    (self._pts[ix-1][2][0] + u * dr,
                     self._pts[ix-1][2][1] + u * dg,
                     self._pts[ix-1][2][2] + u * db))

    def __copy__(self):
        result = TransferFunction()
        result._min_range = self._min_range
        result._max_range = self._max_range
        result._pts = copy.copy(self._pts)
        return result

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self._min_range != other._min_range:
            return False
        if self._max_range != other._max_range:
            return False
        for my_pt, other_pt in zip(self._pts, other._pts):
            if my_pt != other_pt:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

##############################################################################
# Graphics Items

class TransferFunctionPoint(QtGui.QGraphicsEllipseItem):

    selection_pens = { True: QtGui.QPen(QtGui.QBrush(
        QtGui.QColor(*(ColorByName.get_int('goldenrod_medium')))),0.012),
                       False: QtGui.QPen() }

    def __init__(self, scalar, opacity, color, parent=None):
        QtGui.QGraphicsEllipseItem.__init__(self, parent)
        self._scalar = scalar
        self._opacity = opacity
        self._color = QtGui.QColor(color[0]*255,
                                   color[1]*255,
                                   color[2]*255)
        self.setPen(QtGui.QPen(QtGui.QColor(0,0,0)))
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsFocusable) 
        self.setZValue(2.0)

        self._sx = 1.0
        self._sy = 1.0
        self._left_line = None
        self._right_line = None
        self._point = QtCore.QPointF(scalar, opacity)
        self.refresh()

        self.setToolTip("Double-click to change color\n"
                        "Right-click to remove point\n"
                        "Scalar: %.5f, Opacity: %.5f" % (self._scalar,
                                                         self._opacity))
        # This sets up the linked list of Lines

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace or \
           event.key() == QtCore.Qt.Key_Delete:
            self.remove_self()

    def refresh(self):
        dx = 0.025 / self._sx
        dy = 0.025 / self._sy
        # this is the setup
        self.setBrush(QtGui.QBrush(self._color))
        self.setRect(-dx,
                     -dy,
                     2 * dx, 2 * dy)
        self.setPos(self._scalar,
                    self._opacity)

    def update_scale(self, sx, sy):
        self._sx = sx
        self._sy = sy
        self.refresh()

    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemSelectedChange:
            self.setPen(self.selection_pens[value.toBool()])
        if change == QtGui.QGraphicsItem.ItemPositionChange:
            # moves point
            pt = value.toPointF()
            pt.setY(clamp(pt.y(), 0.0, 1.0))
            self._opacity = pt.y()
            self._point.setY(pt.y())
            if not self._left_line:
                pt.setX(0.0)
            elif not self._right_line:
                pt.setX(1.0)
            else:
                assert self._left_line._point_right == self
                assert self._right_line._point_left == self
                pt.setX(clamp(pt.x(),
                              self._left_line._point_left._point.x(),
                              self._right_line._point_right._point.x(),
                              1e-6))
                self._point.setX(pt.x())
                self._scalar = pt.x()
            if self._left_line:
                self._left_line.refresh()
            if self._right_line:
                self._right_line.refresh()
            if self.scene():
                self.scene()._tf_poly.setup()
            self.setToolTip("Double-click to change color\n"
                        "Right-click to remove point\n"
                        "Scalar: %.5f, Opacity: %.5f" % (self._scalar,
                                                         self._opacity))
            return QtGui.QGraphicsItem.itemChange(self, change,
                                                  QtCore.QVariant(pt))
        return QtGui.QGraphicsItem.itemChange(self, change, value)

    def remove_self(self):
        if not self._left_line or not self._right_line:
            # Ignore, self is a corner node that can't be removed
            return
        
        # Removes the right line and self, re-ties data structure
        self._left_line._point_right = self._right_line._point_right
        self._left_line._point_right._left_line = self._left_line
        
        # be friends with garbage collector
        self._right_line._point_left = None
        self._right_line._point_right = None
        self.scene()._tf_poly.setup()
        self.scene().removeItem(self._right_line)
        self.scene().removeItem(self)
        self._left_line.refresh()

    def mouseDoubleClickEvent(self, event):
        new_color = QtGui.QColorDialog.getColor(self._color)
        if not new_color.isValid():
            return
        self._color = new_color
        if self._left_line:
            self._left_line.refresh()
        if self._right_line:
            self._right_line.refresh()
        self.refresh()
        self.scene()._tf_poly.setup()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            event.accept()
            self.remove_self()
        else:
            QtGui.QGraphicsEllipseItem.mousePressEvent(self, event)
        
    def add_self_to_transfer_function(self, tf):
        tf.add_point(self._scalar,
                     self._opacity,
                     (self._color.redF(),
                      self._color.greenF(),
                      self._color.blueF()))

class TransferFunctionPolygon(QtGui.QGraphicsPolygonItem):

    def __init__(self):
        QtGui.QGraphicsPolygonItem.__init__(self)

    def setup(self):
        # This inspects the scene, finds the left-most point, and
        # then builds the polygon traversing the linked list structure
        if not self.scene():
            return
        pt = self.scene().get_leftmost_point()
        first_pt = pt
        self.setZValue(1.25)
        g = QtGui.QLinearGradient()
        g.setStart(0.0, 0.5)
        g.setFinalStop(1.0, 0.5)
        p = QtGui.QPen()
        p.setStyle(QtCore.Qt.NoPen)
        pts = [QtCore.QPointF(pt.x(), 0)]
        self.setPen(p)
        
        while 1:
            c = QtGui.QColor(pt._color)
            c.setAlphaF(pt._opacity)
            g.setColorAt(pt._scalar, c)
            pts.append(pt._point)
            # move cursor fwd
            if pt._right_line:
                pt = pt._right_line._point_right
            else:
                break
        self.setBrush(QtGui.QBrush(g))
        pts.append(QtCore.QPointF(pt.x(), 0))
        self.setPolygon(QtGui.QPolygonF(pts))

class TransferFunctionLine(QtGui.QGraphicsPolygonItem):

    def __init__(self, point_left, point_right, parent=None):
        assert point_right._scalar >= point_left._scalar
        QtGui.QGraphicsPolygonItem.__init__(self, parent)
        self._point_left = point_left
        self._point_right = point_right
        self._point_left._right_line = self
        self._point_right._left_line = self
        self.setup(1.0, 1.0)
        self._sx = 1.0
        self._sy = 1.0
        
    def setup(self, sx, sy):
        d = self._point_right._point - self._point_left._point
        d_normal = QtCore.QPointF(d.y(), -d.x())
        l = math.sqrt(d.x() * d.x() + d.y() * d.y())
        if l != 0.0:
            d_normal /= l
            d_normal *= 0.010
            d_normal.setX(d_normal.x() / sx)
            d_normal.setY(d_normal.y() / sy)
        ps = [self._point_left._point + d_normal,
              self._point_right._point + d_normal,
              self._point_right._point - d_normal,
              self._point_left._point - d_normal]
        self.setPolygon(QtGui.QPolygonF(ps))
        self.setZValue(1.5)
        # Gradient for filling
        g = QtGui.QLinearGradient()
        g.setStart(self._point_left._point)
        g.setFinalStop(self._point_right._point)
        g.setColorAt(0.0, self._point_left._color)
        g.setColorAt(1.0, self._point_right._color)
        self.setBrush(QtGui.QBrush(g))
        # Gradient for outlining
        g = QtGui.QLinearGradient()
        g.setStart(self._point_left._point)
        g.setFinalStop(self._point_right._point)
        dark_pl = QtGui.QColor(self._point_left._color.red() * 0.5,
                               self._point_left._color.green() * 0.5,
                               self._point_left._color.blue() * 0.5)
        dark_pr = QtGui.QColor(self._point_right._color.red() * 0.5,
                               self._point_right._color.green() * 0.5,
                               self._point_right._color.blue() * 0.5)
        g.setColorAt(0.0, dark_pl)
        g.setColorAt(1.0, dark_pr)
        p = QtGui.QPen()
        p.setBrush(QtGui.QBrush(g))
        self.setPen(p)

    def update_scale(self, sx, sy):
        self._sx = sx
        self._sy = sy
        self.refresh()

    def refresh(self):
        self.setup(self._sx, self._sy)

    def mouseDoubleClickEvent(self, event):
        p = event.scenePos()
        c_left = self._point_left._color
        c_right = self._point_right._color
        u = ((p.x() - self._point_left._point.x()) /
             (self._point_right._point.x() - self._point_left._point.x()))
        new_c = (u * c_right.redF() + (1-u) * c_left.redF(),
                 u * c_right.greenF() + (1-u) * c_left.greenF(),
                 u * c_right.blueF() + (1-u) * c_left.blueF())
        new_point = TransferFunctionPoint(p.x(), p.y(), new_c)
        new_line = TransferFunctionLine(new_point, self._point_right)
        new_point._left_line = self
        self._point_right = new_point
        self.scene().addItem(new_line)
        self.scene().addItem(new_point)
        new_line.update_scale(self._point_left._sx,
                              self._point_left._sy)
        new_point.update_scale(self._point_left._sx,
                               self._point_left._sy)
        new_point.refresh()
        self.refresh()

    def mousePressEvent(self, event):
        # This needs to be here, otherwise mouseDoubleClickEvent does
        # not get called.
        event.accept()
        

##############################################################################
# Scene, view, widget

class TransferFunctionScene(QtGui.QGraphicsScene):

    def __init__(self, tf, parent=None):
        QtGui.QGraphicsScene.__init__(self, parent)
        self._tf_items = []
        poly = TransferFunctionPolygon()
        poly.setup()
        self._tf_poly = poly
        self.addItem(poly)
        self.create_tf_items(tf)
        #current scale
        self._sx = 1.0
        self._sy = 1.0    
        # Add outlines
        line_color = QtGui.QColor(200, 200, 200)
        pen = QtGui.QPen(line_color)
        ps = [QtCore.QPointF(0.0, 0.0),
              QtCore.QPointF(1.0, 0.0),
              QtCore.QPointF(1.0, 1.0),
              QtCore.QPointF(0.0, 1.0)]
        outline = QtGui.QPolygonF(ps)
        self.addPolygon(outline, pen)

        for i in xrange(51):
            u = float(i) / 50.0
            self.addLine(QtCore.QLineF(u, 0.0, u, 1.0), pen)
            self.addLine(QtCore.QLineF(0.0, u, 1.0, u), pen)

    def reset_transfer_function(self, tf):
        self.create_tf_items(tf)
        self.update_scale(self._sx, self._sy)
        self._tf_poly.setup()
        
    def removeItem(self, item):
        if item in self._tf_items:
            self._tf_items.remove(item)
        QtGui.QGraphicsScene.removeItem(self, item)

    def addItem(self, item):
        # Ugly, but hey
        if isinstance(item, TransferFunctionLine) or \
           isinstance(item, TransferFunctionPoint):
            self._tf_items.append(item)
        QtGui.QGraphicsScene.addItem(self, item)

    def create_tf_items(self, tf):
        items = copy.copy(self._tf_items)
        for item in items:
            self.removeItem(item)
        self._tf_items = []
        if len(tf._pts) == 0:
            pt_left = TransferFunctionPoint(0.0, 0.0, (0.0, 0.0, 0.0))
            pt_right = TransferFunctionPoint(1.0, 0.0, (0.0, 0.0, 0.0))
            line = TransferFunctionLine(pt_left, pt_right)
            
            self.addItem(pt_left)
            self.addItem(pt_right)
            self.addItem(line)
            
        else:
            pts = [TransferFunctionPoint(*pt)
                   for pt in tf._pts]
            lines = [TransferFunctionLine(pt_l, pt_r)
                     for (pt_l, pt_r) in zip(pts[:-1], pts[1:])]
            for pt in pts:
                self.addItem(pt)
            for line in lines:
                self.addItem(line)

    def add_knot(self, scalar, opacity):
        pass

    def update_scale(self, sx, sy):
        for item in self._tf_items:
            item.update_scale(sx, sy)
        self._sx = sx
        self._sy = sy

    def get_leftmost_point(self):
        pt = None
        
        for item in self._tf_items:
            if hasattr(item, '_left_line') and not item._left_line:
                pt = item
                break
        assert pt
        return pt        

    def get_transfer_function(self):
        result = TransferFunction()
        pt = self.get_leftmost_point()
        while 1:
            pt.add_self_to_transfer_function(result)
            if pt._right_line:
                pt = pt._right_line._point_right
            else:
                break
        return result

class TransferFunctionView(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        QtGui.QGraphicsView.__init__(self, parent)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
    def resizeEvent(self, event):
        self.setMatrix(QtGui.QMatrix(event.size().width() / (10.0/9), 0,
                                     0, -event.size().height() / (10.0/9), 0, 0))
        self.scene().update_scale(event.size().width()/(2000.0/9), event.size().height()/(2000.0/9))
        
    def focusOutEvent(self, event):
        self.parent().update_parent()
        QtGui.QGraphicsView.focusOutEvent(self, event)

default_tf = TransferFunction()
default_tf.add_point(0.0, 0.0, (0.0, 0.0, 0.0))
default_tf.add_point(1.0, 0.0, (0.0, 0.0, 0.0))
    
class TransferFunctionWidget(QtGui.QWidget, ConstantWidgetMixin):

    def __init__(self, param, parent=None):
        QtGui.QWidget.__init__(self, parent)
        ConstantWidgetMixin.__init__(self, param.strValue)
        if not param.strValue:
            self._tf = copy.copy(default_tf)
        else:
            self._tf = pickle.loads(param.strValue.decode('hex'))
        self._scene = TransferFunctionScene(self._tf, self)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        self._view = TransferFunctionView()
        self._view.setScene(self._scene)
        self._view.setMinimumSize(200,200)
        self._view.show()
        self._view.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                 QtGui.QSizePolicy.Expanding)
        self._view.setMatrix(QtGui.QMatrix(180, 0, 0, -180, 0, 0))
        self.setMinimumSize(200,200)
        caption = QtGui.QLabel("Double-click on the line to add a point")
        font = QtGui.QFont('Arial', 11)
        font.setItalic(True)
        caption.setFont(font)
        layout.addWidget(self._view)
        layout.addWidget(caption)

    def contents(self):
        return pickle.dumps(self._scene.get_transfer_function()).encode('hex')
    
    def setContents(self, strValue, silent=True):
        if not strValue:
            self._tf = copy.copy(default_tf)
        else:
            self._tf = pickle.loads(strValue.decode('hex'))
        self._scene.reset_transfer_function(self._tf)
        if not silent:
            self.update_parent()    
            
##############################################################################
# Helper module to adjust range

class vtkScaledTransferFunction(Module):

    def compute(self):
        tf = self.get_input('TransferFunction')
        new_tf = copy.copy(tf)
        if self.has_input('Input'):
            port = self.get_input('Input')
            algo = port.vtkInstance.GetProducer()
            output = algo.GetOutput(port.vtkInstance.GetIndex())
            (new_tf._min_range, new_tf._max_range) = output.GetScalarRange()
        elif self.has_input('Dataset'):
            algo = self.get_input('Dataset').vtkInstance
            output = algo
            (new_tf._min_range, new_tf._max_range) = output.GetScalarRange()
        else:
            (new_tf._min_range, new_tf._max_range) = self.get_input('Range')
            
        self.set_output('TransferFunction', new_tf)

string_conversion = staticmethod(lambda x: pickle.dumps(x).encode('hex'))
conversion = staticmethod(lambda x: pickle.loads(x.decode('hex')))
validation = staticmethod(lambda x: isinstance(x, TransferFunction))
TransferFunctionConstant = new_constant('TransferFunction',
                                        conversion,
                                        default_tf,
                                        validation,
                                        TransferFunctionWidget)
TransferFunctionConstant.translate_to_string = string_conversion

##############################################################################

def initialize():
    init_constant(TransferFunctionConstant)
