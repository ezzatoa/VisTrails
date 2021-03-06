###############################################################################
##
## Copyright (C) 2014-2016, New York University.
## Copyright (C) 2011-2014, NYU-Poly.
## Copyright (C) 2006-2011, University of Utah.
## All rights reserved.
## Contact: contact@vistrails.org
##
## This file is part of VisTrails.
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are met:
##
##  - Redistributions of source code must retain the above copyright notice,
##    this list of conditions and the following disclaimer.
##  - Redistributions in binary form must reproduce the above copyright
##    notice, this list of conditions and the following disclaimer in the
##    documentation and/or other materials provided with the distribution.
##  - Neither the name of the New York University nor the names of its
##    contributors may be used to endorse or promote products derived from
##    this software without specific prior written permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
## AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
## THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
## PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
## CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
## EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
## PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
## OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
## WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
## OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
## ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
###############################################################################

##############################################################################
# Enumeration Widget for Web Services
from __future__ import division

from PyQt4 import QtCore, QtGui

from vistrails.core.modules.basic_modules import Constant
from vistrails.core.modules.module_registry import get_module_registry
from vistrails.core.modules.vistrails_module import new_module
from vistrails.gui.modules.constant_configuration import ConstantWidgetMixin

import vistrails.packages.webServices


class EnumerationWidget(QtGui.QComboBox, ConstantWidgetMixin):
    contentsChanged = QtCore.pyqtSignal(tuple)
    enumerationlist = []
    def __init__(self, param, parent=None):
        """__init__(param: core.vistrail.module_param.ModuleParam,
                    parent: QWidget)
        Initializes the line edit with contents
        """
        dictkey = param._namespace
        typedict = vistrails.packages.webServices.webServicesmodulesDict[dictkey]
        w = param._namespace.replace('|Types','')
        dictkey = w + "." + param._type
        obj = typedict[dictkey]
        self.enumerationlist = obj.ports[0][0]
        QtGui.QComboBox.__init__(self, parent)
        ConstantWidgetMixin.__init__(self, param.strValue)
        QtGui.QComboBox.clear(self)
        listqt = []
        for element in self.enumerationlist:
            listqt.append(element)
            
        QtGui.QComboBox.addItems(self, listqt)
        foundindex = self.findText(param.strValue)
        if not foundindex == -1:
            self.setCurrentIndex(foundindex)
        else:
            self.setCurrentIndex(0)
            param.strValue = self.enumerationlist[self.currentIndex()]
        self.connect(self, QtCore.SIGNAL('activated(int)'), self.change_state)

    def contents(self):
        return self.enumerationlist[self.currentIndex()]
    
    def change_state(self, state):
        self.update_parent()

    @staticmethod
    def get_widget_class():
        return EnumerationWidget

    @staticmethod
    def translate_to_python(self):
        return self


def initialize(namemodule,namespace,identifier, version):
    reg = get_module_registry()

    enumerationConstant = new_module(Constant, namemodule, {})
    enumerationConstant.name = namemodule
    enumerationConstant.isEnumeration = True
    reg.add_module(enumerationConstant, namespace=namespace, package=identifier,
                   package_version=version)

    return enumerationConstant
