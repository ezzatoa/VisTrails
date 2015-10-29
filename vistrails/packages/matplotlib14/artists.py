from vistrails.core.modules.vistrails_module import Module
from bases import MplProperties
import matplotlib.artist
import matplotlib.cbook






def translate_color(c):
    return c.tuple

def translate_MplLine2DProperties_marker(val):
    translate_dict = {'caretright': 5, 'star': '*', 'point': '.', 'mathtext': '$...$', 'triangle_right': '>', 'tickup': 2, 'hexagon1': 'h', 'plus': '+', 'hline': '_', 'vline': '|', 'tickdown': 3, 'nothing': ' ', 'caretup': 6, 'caretleft': 4, 'pentagon': 'p', 'tri_left': '3', 'tickleft': 0, 'tickright': 1, 'tri_down': '1', 'thin_diamond': 'd', 'diamond': 'D', 'caretdown': 7, 'hexagon2': 'H', 'tri_up': '2', 'square': 's', 'x': 'x', 'triangle_down': 'v', 'triangle_up': '^', 'octagon': '8', 'tri_right': '4', 'circle': 'o', 'pixel': ',', 'triangle_left': '<'}
    return translate_dict[val]
def translate_MplLine2DProperties_linestyle(val):
    translate_dict = {'solid': '-', 'dashed': '--', 'dash_dot': '-.', 'dotted': ':', 'draw nothing': ''}
    return translate_dict[val]
def translate_Mpl_AxesBaseProperties_aspect(val):
    translate_dict = {'centered': 'C', 'lower left corner': 'SW', 'middle of bottom edge': 'S', 'lower right corner': 'SE', '': 'etc.'}
    return translate_dict[val]
def translate_Mpl_AxesBaseProperties_anchor(val):
    translate_dict = {'right': 'E', 'Center': 'C', 'bottom right': 'SE', 'top right': 'NE', 'bottom': 'S', 'top left': 'NW', 'top': 'N', 'bottom left': 'SW', 'left': 'W'}
    return translate_dict[val]

class MplArtistProperties(MplProperties):
    """
    Abstract base class for someone who renders into a
    :class:`FigureCanvas`.
    
    """
    _input_ports = [
              ("picker", "basic:String",
                {'optional': True, 'docstring': "Set the epsilon for picking used by this artist\n\npicker can be one of the following:\n\nNone: picking is disabled for this artist (default)\n\nA boolean: if True then picking will be enabled and the artist will fire a pick event if the mouse event is over the artist\n\nA float: if picker is a number it is interpreted as an epsilon tolerance in points and the artist will fire off an event if it's data is within epsilon of the mouse event.  For some artists like lines and patch collections, the artist may provide additional data to the pick event that is generated, e.g., the indices of the data within epsilon of the pick event\n\nA function: if picker is callable, it is a user supplied function which determines whether the artist is hit by the mouse event:\n\nhit, props = picker(artist, mouseevent)\n\nto determine the hit test.  if the mouse event is over the artist, return hit=True and props is a dictionary of properties you want added to the PickEvent attributes."}),
              ("contains", "basic:String",
                {'optional': True, 'docstring': 'Replace the contains test used by this artist. The new picker should be a callable function which determines whether the artist is hit by the mouse event:\n\nhit, props = picker(artist, mouseevent)\n\nIf the mouse event is over the artist, return hit = True and props is a dictionary of properties you want returned with the contains test.'}),
              ("clip_on", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether artist uses clipping.\n\nWhen False artists will be visible out side of the axes which can lead to unexpected results.'}),
              ("agg_filter", "basic:String",
                {'optional': True, 'docstring': 'set agg_filter fuction.'}),
              ("visible", "basic:Boolean",
                {'optional': True, 'docstring': "Set the artist's visiblity."}),
              ("sketch_params", "basic:String",
                {'optional': True, 'docstring': '\n        Sets the the sketch parameters.\n\n        Parameters\n        ----------\n\n        scale : float, optional\n            The amplitude of the wiggle perpendicular to the source\n            line, in pixels.  If scale is `None`, or not provided, no\n            sketch filter will be provided.\n\n        length : float, optional\n             The length of the wiggle along the line, in pixels\n             (default 128.0)\n\n        randomness : float, optional\n            The scale factor by which the length is shrunken or\n            expanded (default 16.0)\n        '}),
              ("transform", "basic:String",
                {'optional': True, 'docstring': 'Set the :class:`~matplotlib.transforms.Transform` instance used by this artist.'}),
              ("axes", "basic:String",
                {'optional': True, 'docstring': 'Set the :class:`~matplotlib.axes.Axes` instance in which the artist resides, if any.'}),
              ("clip_box", "basic:String",
                {'optional': True, 'docstring': "Set the artist's clip :class:`~matplotlib.transforms.Bbox`."}),
              ("clip_path", "basic:String",
                {'optional': True, 'docstring': "Set the artist's clip path, which may be:\n\na :class:`~matplotlib.patches.Patch` (or subclass) instance\n\n\n\nNone, to remove the clipping path\n\nFor efficiency, if the path happens to be an axis-aligned rectangle, this method will set the clipping box to the corresponding rectangle and set the clipping path to None."}),
              ("lod", "basic:Boolean",
                {'optional': True, 'docstring': 'Set Level of Detail on or off.  If on, the artists may examine things like the pixel width of the axes and draw a subset of their contents accordingly'}),
              ("label", "basic:String",
                {'optional': True, 'docstring': 'Set the label to s for auto legend.'}),
              ("rasterized", "basic:Boolean",
                {'optional': True, 'docstring': "Force rasterized (bitmap) drawing in vector backend output.\n\nDefaults to None, which implies the backend's default behavior"}),
              ("gid", "basic:String",
                {'optional': True, 'docstring': 'Sets the (group) id for the artist'}),
              ("zorder", "basic:String",
                {'optional': True, 'docstring': 'Set the zorder for the artist.  Artists with lower zorder values are drawn first.'}),
              ("url", "basic:String",
                {'optional': True, 'docstring': 'Sets the url for the artist'}),
              ("path_effects", "basic:String",
                {'optional': True, 'docstring': 'set path_effects, which should be a list of instances of matplotlib.patheffect._Base class or its derivatives.'}),
              ("snap", "basic:String",
                {'optional': True, 'docstring': 'Sets the snap setting which may be:\n\nTrue: snap vertices to the nearest pixel center\n\nFalse: leave vertices as-is\n\nNone: (auto) If the path contains only rectilinear line segments, round to the nearest pixel center\n\nOnly supported by the Agg and MacOSX backends.'}),
              ("alpha", "basic:Float",
                {'optional': True, 'docstring': 'Set the alpha value used for blending - not supported on all backends.'}),
              ("animated", "basic:Boolean",
                {'optional': True, 'docstring': "Set the artist's animation state."}),
              ("figure", "basic:String",
                {'optional': True, 'docstring': 'Set the :class:`~matplotlib.figure.Figure` instance the artist belongs to.'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplArtistProperties)")]

    class Artist(MplProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplArtistProperties.Artist()
            self.set_output("value", artist)

        MplProperties.compute(self, artist)
        if self.has_input('picker'):
            artist.props['picker'] = self.get_input('picker')
        if self.has_input('contains'):
            artist.props['contains'] = self.get_input('contains')
        if self.has_input('clip_on'):
            artist.props['clip_on'] = self.get_input('clip_on')
        if self.has_input('agg_filter'):
            artist.props['agg_filter'] = self.get_input('agg_filter')
        if self.has_input('visible'):
            artist.props['visible'] = self.get_input('visible')
        if self.has_input('sketch_params'):
            artist.props['sketch_params'] = self.get_input('sketch_params')
        if self.has_input('transform'):
            artist.props['transform'] = self.get_input('transform')
        if self.has_input('axes'):
            artist.props['axes'] = self.get_input('axes')
        if self.has_input('clip_box'):
            artist.props['clip_box'] = self.get_input('clip_box')
        if self.has_input('clip_path'):
            artist.props['clip_path'] = self.get_input('clip_path')
        if self.has_input('lod'):
            artist.props['lod'] = self.get_input('lod')
        if self.has_input('label'):
            artist.props['label'] = self.get_input('label')
        if self.has_input('rasterized'):
            artist.props['rasterized'] = self.get_input('rasterized')
        if self.has_input('gid'):
            artist.props['gid'] = self.get_input('gid')
        if self.has_input('zorder'):
            artist.props['zorder'] = self.get_input('zorder')
        if self.has_input('url'):
            artist.props['url'] = self.get_input('url')
        if self.has_input('path_effects'):
            artist.props['path_effects'] = self.get_input('path_effects')
        if self.has_input('snap'):
            artist.props['snap'] = self.get_input('snap')
        if self.has_input('alpha'):
            artist.props['alpha'] = self.get_input('alpha')
        if self.has_input('animated'):
            artist.props['animated'] = self.get_input('animated')
        if self.has_input('figure'):
            artist.props['figure'] = self.get_input('figure')


class MplAxisProperties(MplArtistProperties):
    """
    Public attributes

    * :attr:`axes.transData` - transform data coords to display coords
    * :attr:`axes.transAxes` - transform axis coords to display coords
    * :attr:`labelpad` - number of points between the axis and its label
    
    """
    _input_ports = [
              ("pickradius", "basic:String",
                {'optional': True, 'docstring': 'Set the depth of the axis used by the picker'}),
              ("smart_bounds", "basic:String",
                {'optional': True, 'docstring': 'set the axis to have smart bounds'}),
              ("axes", "basic:String",
                {'optional': True}),
              ("view_interval", "basic:String",
                {'optional': True}),
              ("major_locator", "basic:String",
                {'optional': True, 'docstring': 'Set the locator of the major ticker'}),
              ("minor_formatter", "basic:String",
                {'optional': True, 'docstring': 'Set the formatter of the minor ticker'}),
              ("ticklabels", "basic:List",
                {'optional': True, 'docstring': 'Set the text values of the tick labels. Return a list of Text instances.  Use kwarg minor=True to select minor ticks. All other kwargs are used to update the text object properties. As for get_ticklabels, label1 (left or bottom) is affected for a given tick only if its label1On attribute is True, and similarly for label2.  The list of returned label text objects consists of all such label1 objects followed by all such label2 objects.\n\nThe input ticklabels is assumed to match the set of tick locations, regardless of the state of label1On and label2On.'}),
              ("clip_path", "basic:String",
                {'optional': True}),
              ("minor_locator", "basic:String",
                {'optional': True, 'docstring': 'Set the locator of the minor ticker'}),
              ("ticks", "basic:List",
                {'optional': True, 'docstring': 'Set the locations of the tick marks from sequence ticks'}),
              ("label_text", "basic:String",
                {'optional': True, 'docstring': 'Sets the text value of the axis label'}),
              ("major_formatter", "basic:String",
                {'optional': True, 'docstring': 'Set the formatter of the major ticker'}),
              ("units", "basic:String",
                {'optional': True, 'docstring': 'set the units for axis'}),
              ("tick_params", "basic:String",
                {'optional': True, 'docstring': 'Set appearance parameters for ticks and ticklabels.\n\nFor documentation of keyword arguments, see :meth:`matplotlib.axes.Axes.tick_params`.'}),
              ("label_coords", "basic:String",
                {'optional': True, 'docstring': 'Set the coordinates of the label.  By default, the x coordinate of the y label is determined by the tick label bounding boxes, but this can lead to poor alignment of multiple ylabels if there are multiple axes.  Ditto for the y coodinate of the x label.\n\nYou can also specify the coordinate system of the label with the transform.  If None, the default coordinate system will be the axes coordinate system (0,0) is (left,bottom), (0.5, 0.5) is middle, etc'}),
              ("majorTickProperties", "MplTickProperties",
                {}),
              ("minorTickProperties", "MplTickProperties",
                {}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplAxisProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                if 'major_ticks' in self.sub_props:
                    self.sub_props['major_ticks'].update_props(obj.get_major_ticks())
                if 'minor_ticks' in self.sub_props:
                    self.sub_props['minor_ticks'].update_props(obj.get_minor_ticks())

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplAxisProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('pickradius'):
            artist.props['pickradius'] = self.get_input('pickradius')
        if self.has_input('smart_bounds'):
            artist.props['smart_bounds'] = self.get_input('smart_bounds')
        if self.has_input('axes'):
            artist.constructor_props['axes'] = self.get_input('axes')
        if self.has_input('view_interval'):
            artist.props['view_interval'] = self.get_input('view_interval')
        if self.has_input('major_locator'):
            artist.props['major_locator'] = self.get_input('major_locator')
        if self.has_input('minor_formatter'):
            artist.props['minor_formatter'] = self.get_input('minor_formatter')
        if self.has_input('ticklabels'):
            artist.props['ticklabels'] = self.get_input('ticklabels')
        if self.has_input('clip_path'):
            artist.props['clip_path'] = self.get_input('clip_path')
        if self.has_input('minor_locator'):
            artist.props['minor_locator'] = self.get_input('minor_locator')
        if self.has_input('ticks'):
            artist.props['ticks'] = self.get_input('ticks')
        if self.has_input('label_text'):
            artist.props['label_text'] = self.get_input('label_text')
        if self.has_input('major_formatter'):
            artist.props['major_formatter'] = self.get_input('major_formatter')
        if self.has_input('units'):
            artist.props['units'] = self.get_input('units')
        if self.has_input('tick_params'):
            artist.props['tick_params'] = self.get_input('tick_params')
        if self.has_input('label_coords'):
            artist.props['label_coords'] = self.get_input('label_coords')
        if self.has_input('majorTickProperties'):
            artist.sub_props['major_ticks'] = self.get_input('majorTickProperties')
        if self.has_input('minorTickProperties'):
            artist.sub_props['minor_ticks'] = self.get_input('minorTickProperties')


class MplCollectionProperties(MplArtistProperties):
    """
    Base class for Collections.  Must be subclassed to be usable.

    All properties in a collection must be sequences or scalars;
    if scalars, they will be converted to sequences.  The
    property of the ith element of the collection is::

      prop[i % len(props)]

    Keyword arguments and default values:

        * *edgecolors*: None
        * *facecolors*: None
        * *linewidths*: None
        * *antialiaseds*: None
        * *offsets*: None
        * *transOffset*: transforms.IdentityTransform()
        * *offset_position*: 'screen' (default) or 'data'
        * *norm*: None (optional for
          :class:`matplotlib.cm.ScalarMappable`)
        * *cmap*: None (optional for
          :class:`matplotlib.cm.ScalarMappable`)
        * *hatch*: None
        * *zorder*: 1


    *offsets* and *transOffset* are used to translate the patch after
    rendering (default no offsets).  If offset_position is 'screen'
    (default) the offset is applied after the master transform has
    been applied, that is, the offsets are in screen coordinates.  If
    offset_position is 'data', the offset is applied before the master
    transform, i.e., the offsets are in data coordinates.

    If any of *edgecolors*, *facecolors*, *linewidths*, *antialiaseds*
    are None, they default to their :data:`matplotlib.rcParams` patch
    setting, in sequence form.

    The use of :class:`~matplotlib.cm.ScalarMappable` is optional.  If
    the :class:`~matplotlib.cm.ScalarMappable` matrix _A is not None
    (i.e., a call to set_array has been made), at draw time a call to
    scalar mappable will be made to set the face colors.
    
    """
    _input_ports = [
              ("transOffset", "basic:String",
                {'optional': True}),
              ("edgecolor", "basic:Color",
                {'optional': True, 'docstring': "Set the edgecolor(s) of the collection. c can be a matplotlib color arg (all patches have same color), or a sequence of rgba tuples; if it is a sequence the patches will cycle through the sequence.\n\nIf c is 'face', the edge color will always be the same as the face color.  If it is 'none', the patch boundary will not be drawn."}),
              ("offset_position", "basic:String",
                {'optional': True, 'docstring': "Set how offsets are applied.  If offset_position is 'screen' (default) the offset is applied after the master transform has been applied, that is, the offsets are in screen coordinates. If offset_position is 'data', the offset is applied before the master transform, i.e., the offsets are in data coordinates."}),
              ("edgecolors", "basic:String",
                {'optional': True}),
              ("facecolor", "basic:Color",
                {'optional': True, 'docstring': "Set the facecolor(s) of the collection.  c can be a matplotlib color arg (all patches have same color), or a sequence of rgba tuples; if it is a sequence the patches will cycle through the sequence.\n\nIf c is 'none', the patch will not be filled."}),
              ("linestyles", "basic:String",
                {'optional': True, 'defaults': "[u'solid']"}),
              ("offsets", "basic:List",
                {'optional': True, 'docstring': 'Set the offsets for the collection.  offsets can be a scalar or a sequence.'}),
              ("color", "basic:Color",
                {'optional': True, 'docstring': 'Set both the edgecolor and the facecolor. .. seealso:\n\n:meth:`set_facecolor`, :meth:`set_edgecolor`    For setting the edge or face color individually.'}),
              ("zorder", "basic:Integer",
                {'optional': True, 'defaults': '[1]'}),
              ("pickradius", "basic:String",
                {'optional': True}),
              ("antialiaseds", "basic:String",
                {'optional': True}),
              ("linewidths", "basic:String",
                {'optional': True}),
              ("cmap", "basic:String",
                {'optional': True}),
              ("antialiased", "basic:List",
                {'optional': True, 'docstring': 'Set the antialiasing state for rendering.'}),
              ("urls", "basic:String",
                {'optional': True}),
              ("hatch", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the hatching pattern\n\nhatch can be one of:\n\n/   - diagonal hatching \\   - back diagonal |   - vertical -   - horizontal +   - crossed x   - crossed diagonal o   - small circle O   - large circle .   - dots *   - stars\n\nLetters can be combined, in which case all the specified hatchings are done.  If same letter repeats, it increases the density of hatching of that pattern.\n\nHatching is supported in the PostScript, PDF, SVG and Agg backends only.\n\nUnlike other properties such as linewidth and colors, hatching can only be specified for the collection as a whole, not separately for each member.', 'values': '[[\'/\', "\'\\\\\'", "\'", "\'", \'-\', \'+\', \'x\', \'o\', \'O\', \'.\', \'*\']]', 'optional': True}),
              ("alpha", "basic:Float",
                {'optional': True, 'docstring': 'Set the alpha tranparencies of the collection.  alpha must be a float or None.'}),
              ("linewidth", "basic:List",
                {'optional': True, 'docstring': 'Set the linewidth(s) for the collection.  lw can be a scalar or a sequence; if it is a sequence the patches will cycle through the sequence'}),
              ("linestyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the linestyle(s) for the collection.', 'values': "[['solid', ('dashed', 'dashdot', 'dotted'), '(offset, on-off-dash-seq)']]", 'optional': True}),
              ("facecolors", "basic:String",
                {'optional': True}),
              ("norm", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplCollectionProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplCollectionProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('transOffset'):
            artist.constructor_props['transOffset'] = self.get_input('transOffset')
        if self.has_input('edgecolor'):
            artist.props['edgecolor'] = self.get_input('edgecolor')
            artist.props['edgecolor'] = translate_color(artist.props['edgecolor'])
        if self.has_input('offset_position'):
            artist.props['offset_position'] = self.get_input('offset_position')
        if self.has_input('edgecolors'):
            artist.constructor_props['edgecolors'] = self.get_input('edgecolors')
        if self.has_input('facecolor'):
            artist.props['facecolor'] = self.get_input('facecolor')
            artist.props['facecolor'] = translate_color(artist.props['facecolor'])
        if self.has_input('linestyles'):
            artist.constructor_props['linestyles'] = self.get_input('linestyles')
        if self.has_input('offsets'):
            artist.props['offsets'] = self.get_input('offsets')
        if self.has_input('color'):
            artist.props['color'] = self.get_input('color')
            artist.props['color'] = translate_color(artist.props['color'])
        if self.has_input('zorder'):
            artist.constructor_props['zorder'] = self.get_input('zorder')
        if self.has_input('pickradius'):
            artist.props['pickradius'] = self.get_input('pickradius')
        if self.has_input('antialiaseds'):
            artist.constructor_props['antialiaseds'] = self.get_input('antialiaseds')
        if self.has_input('linewidths'):
            artist.constructor_props['linewidths'] = self.get_input('linewidths')
        if self.has_input('cmap'):
            artist.constructor_props['cmap'] = self.get_input('cmap')
        if self.has_input('antialiased'):
            artist.props['antialiased'] = self.get_input('antialiased')
        if self.has_input('urls'):
            artist.props['urls'] = self.get_input('urls')
        if self.has_input('hatch'):
            artist.props['hatch'] = self.get_input('hatch')
        if self.has_input('alpha'):
            artist.props['alpha'] = self.get_input('alpha')
        if self.has_input('linewidth'):
            artist.props['linewidth'] = self.get_input('linewidth')
        if self.has_input('linestyle'):
            artist.props['linestyle'] = self.get_input('linestyle')
        if self.has_input('facecolors'):
            artist.constructor_props['facecolors'] = self.get_input('facecolors')
        if self.has_input('norm'):
            artist.constructor_props['norm'] = self.get_input('norm')


class MplFigureImageProperties(MplArtistProperties):
    """None
    """
    _input_ports = [
              ("origin", "basic:String",
                {'optional': True}),
              ("offsetx", "basic:Integer",
                {'optional': True, 'defaults': '[0]'}),
              ("offsety", "basic:Integer",
                {'optional': True, 'defaults': '[0]'}),
              ("cmap", "basic:String",
                {'optional': True}),
              ("fig", "basic:String",
                {'optional': True}),
              ("array", "basic:String",
                {'optional': True, 'docstring': 'Deprecated; use set_data for consistency with other image types.'}),
              ("data", "basic:String",
                {'optional': True, 'docstring': 'Set the image array.'}),
              ("norm", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplFigureImageProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplFigureImageProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('origin'):
            artist.constructor_props['origin'] = self.get_input('origin')
        if self.has_input('offsetx'):
            artist.constructor_props['offsetx'] = self.get_input('offsetx')
        if self.has_input('offsety'):
            artist.constructor_props['offsety'] = self.get_input('offsety')
        if self.has_input('cmap'):
            artist.constructor_props['cmap'] = self.get_input('cmap')
        if self.has_input('fig'):
            artist.constructor_props['fig'] = self.get_input('fig')
        if self.has_input('array'):
            artist.props['array'] = self.get_input('array')
        if self.has_input('data'):
            artist.props['data'] = self.get_input('data')
        if self.has_input('norm'):
            artist.constructor_props['norm'] = self.get_input('norm')


class MplFigureProperties(MplArtistProperties):
    """
    The Figure instance supports callbacks through a *callbacks*
    attribute which is a :class:`matplotlib.cbook.CallbackRegistry`
    instance.  The events you can connect to are 'dpi_changed', and
    the callback will be called with ``func(fig)`` where fig is the
    :class:`Figure` instance.

    *patch*
       The figure patch is drawn by a
       :class:`matplotlib.patches.Rectangle` instance

    *suppressComposite*
       For multiple figure images, the figure will make composite
       images depending on the renderer option_image_nocomposite
       function.  If suppressComposite is True|False, this will
       override the renderer.
    
    """
    _input_ports = [
              ("edgecolor", "basic:Color",
                {'optional': True, 'docstring': 'Set the edge color of the Figure rectangle'}),
              ("canvas", "basic:String",
                {'optional': True, 'docstring': 'Set the canvas the contains the figure'}),
              ("facecolor", "basic:Color",
                {'optional': True, 'docstring': 'Set the face color of the Figure rectangle'}),
              ("figwidth", "basic:Float",
                {'optional': True, 'docstring': 'Set the width of the figure in inches'}),
              ("frameon", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether the figure frame (background) is displayed or invisible'}),
              ("subplotpars", "basic:String",
                {'optional': True}),
              ("figheight", "basic:Float",
                {'optional': True, 'docstring': 'Set the height of the figure in inches'}),
              ("figsize", "basic:String",
                {'optional': True}),
              ("linewidth", "basic:Float",
                {'optional': True, 'defaults': '[0.0]'}),
              ("tight_layout", "basic:Boolean",
                {'entry_types': "['enum']", 'docstring': "Set whether :meth:`tight_layout` is used upon drawing. If None, the rcParams['figure.autolayout'] value will be set.\n\nWhen providing a dict containing the keys pad, w_pad, h_pad and rect, the default :meth:`tight_layout` paddings will be overridden.", 'values': '[[None]]', 'optional': True}),
              ("dpi", "basic:Float",
                {'optional': True, 'docstring': 'Set the dots-per-inch of the figure'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplFigureProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplFigureProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('edgecolor'):
            artist.props['edgecolor'] = self.get_input('edgecolor')
            artist.props['edgecolor'] = translate_color(artist.props['edgecolor'])
        if self.has_input('canvas'):
            artist.props['canvas'] = self.get_input('canvas')
        if self.has_input('facecolor'):
            artist.props['facecolor'] = self.get_input('facecolor')
            artist.props['facecolor'] = translate_color(artist.props['facecolor'])
        if self.has_input('figwidth'):
            artist.props['figwidth'] = self.get_input('figwidth')
        if self.has_input('frameon'):
            artist.props['frameon'] = self.get_input('frameon')
        if self.has_input('subplotpars'):
            artist.constructor_props['subplotpars'] = self.get_input('subplotpars')
        if self.has_input('figheight'):
            artist.props['figheight'] = self.get_input('figheight')
        if self.has_input('figsize'):
            artist.constructor_props['figsize'] = self.get_input('figsize')
        if self.has_input('linewidth'):
            artist.constructor_props['linewidth'] = self.get_input('linewidth')
        if self.has_input('tight_layout'):
            artist.props['tight_layout'] = self.get_input('tight_layout')
        if self.has_input('dpi'):
            artist.props['dpi'] = self.get_input('dpi')


class MplLegendProperties(MplArtistProperties):
    """
    Place a legend on the axes at location loc.  Labels are a
    sequence of strings and loc can be a string or an integer
    specifying the legend location

    The location codes are::

      'best'         : 0, (only implemented for axis legends)
      'upper right'  : 1,
      'upper left'   : 2,
      'lower left'   : 3,
      'lower right'  : 4,
      'right'        : 5,
      'center left'  : 6,
      'center right' : 7,
      'lower center' : 8,
      'upper center' : 9,
      'center'       : 10,

    loc can be a tuple of the normalized coordinate values with
    respect its parent.

    
    """
    _input_ports = [
              ("fancybox", "basic:String",
                {'optional': True, 'docstring': 'if True, draw a frame with a round fancybox. If None, use rc'}),
              ("handlelength", "basic:String",
                {'optional': True, 'docstring': 'the length of the legend handles'}),
              ("labels", "basic:String",
                {'optional': True}),
              ("labelspacing", "basic:String",
                {'optional': True, 'docstring': 'the vertical space between the legend entries'}),
              ("columnspacing", "basic:String",
                {'optional': True, 'docstring': 'the spacing between columns'}),
              ("handletextpad", "basic:String",
                {'optional': True, 'docstring': 'the pad between the legend handle and text'}),
              ("ncol", "basic:Integer",
                {'optional': True, 'docstring': 'number of columns', 'defaults': '[1]'}),
              ("borderaxespad", "basic:String",
                {'optional': True, 'docstring': 'the pad between the axes and legend border'}),
              ("loc", "basic:String",
                {'optional': True, 'docstring': 'a location code'}),
              ("bbox_to_anchor", "basic:String",
                {'optional': True, 'docstring': 'set the bbox that the legend will be anchored.\n\nbbox can be a BboxBase instance, a tuple of [left, bottom, width, height] in the given transform (normalized axes coordinate if None), or a tuple of [left, bottom] where the width and height will be assumed to be zero.'}),
              ("title", "basic:String",
                {'optional': True, 'docstring': 'set the legend title. Fontproperties can be optionally set with prop parameter.'}),
              ("numpoints", "basic:String",
                {'optional': True, 'docstring': 'the number of points in the legend for line'}),
              ("prop", "basic:String",
                {'optional': True, 'docstring': 'the font property'}),
              ("handles", "basic:String",
                {'optional': True}),
              ("borderpad", "basic:String",
                {'optional': True, 'docstring': 'the fractional whitespace inside the legend border'}),
              ("parent", "basic:String",
                {'optional': True}),
              ("frame_on", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether the legend box patch is drawn'}),
              ("scatterpoints", "basic:String",
                {'optional': True, 'docstring': 'the number of points in the legend for scatter plot'}),
              ("fontsize", "basic:String",
                {'optional': True, 'docstring': 'the font size (used only if prop is not specified)'}),
              ("shadow", "basic:String",
                {'optional': True, 'docstring': 'if True, draw a shadow behind legend'}),
              ("framealpha", "basic:String",
                {'optional': True, 'docstring': 'If not None, alpha channel for the frame.'}),
              ("handler_map", "basic:String",
                {'optional': True}),
              ("handleheight", "basic:String",
                {'optional': True, 'docstring': 'the height of the legend handles'}),
              ("scatteryoffsets", "basic:List",
                {'optional': True, 'docstring': 'a list of yoffsets for scatter symbols in legend'}),
              ("markerscale", "basic:String",
                {'optional': True, 'docstring': 'the relative size of legend markers vs. original'}),
              ("frameon", "basic:String",
                {'optional': True, 'docstring': 'if True, draw a frame around the legend. If None, use rc'}),
              ("mode", "basic:String",
                {'optional': True}),
              ("default_handler_map", "basic:String",
                {'optional': True, 'docstring': 'A class method to set the default handler map.'}),
              ("bbox_transform", "basic:String",
                {'optional': True, 'docstring': 'the transform for the bbox. transAxes if None.'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplLegendProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplLegendProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('fancybox'):
            artist.constructor_props['fancybox'] = self.get_input('fancybox')
        if self.has_input('handlelength'):
            artist.constructor_props['handlelength'] = self.get_input('handlelength')
        if self.has_input('labels'):
            artist.constructor_props['labels'] = self.get_input('labels')
        if self.has_input('labelspacing'):
            artist.constructor_props['labelspacing'] = self.get_input('labelspacing')
        if self.has_input('columnspacing'):
            artist.constructor_props['columnspacing'] = self.get_input('columnspacing')
        if self.has_input('handletextpad'):
            artist.constructor_props['handletextpad'] = self.get_input('handletextpad')
        if self.has_input('ncol'):
            artist.constructor_props['ncol'] = self.get_input('ncol')
        if self.has_input('borderaxespad'):
            artist.constructor_props['borderaxespad'] = self.get_input('borderaxespad')
        if self.has_input('loc'):
            artist.constructor_props['loc'] = self.get_input('loc')
        if self.has_input('bbox_to_anchor'):
            artist.props['bbox_to_anchor'] = self.get_input('bbox_to_anchor')
        if self.has_input('title'):
            artist.props['title'] = self.get_input('title')
        if self.has_input('numpoints'):
            artist.constructor_props['numpoints'] = self.get_input('numpoints')
        if self.has_input('prop'):
            artist.constructor_props['prop'] = self.get_input('prop')
        if self.has_input('handles'):
            artist.constructor_props['handles'] = self.get_input('handles')
        if self.has_input('borderpad'):
            artist.constructor_props['borderpad'] = self.get_input('borderpad')
        if self.has_input('parent'):
            artist.constructor_props['parent'] = self.get_input('parent')
        if self.has_input('frame_on'):
            artist.props['frame_on'] = self.get_input('frame_on')
        if self.has_input('scatterpoints'):
            artist.constructor_props['scatterpoints'] = self.get_input('scatterpoints')
        if self.has_input('fontsize'):
            artist.constructor_props['fontsize'] = self.get_input('fontsize')
        if self.has_input('shadow'):
            artist.constructor_props['shadow'] = self.get_input('shadow')
        if self.has_input('framealpha'):
            artist.constructor_props['framealpha'] = self.get_input('framealpha')
        if self.has_input('handler_map'):
            artist.constructor_props['handler_map'] = self.get_input('handler_map')
        if self.has_input('handleheight'):
            artist.constructor_props['handleheight'] = self.get_input('handleheight')
        if self.has_input('scatteryoffsets'):
            artist.constructor_props['scatteryoffsets'] = self.get_input('scatteryoffsets')
        if self.has_input('markerscale'):
            artist.constructor_props['markerscale'] = self.get_input('markerscale')
        if self.has_input('frameon'):
            artist.constructor_props['frameon'] = self.get_input('frameon')
        if self.has_input('mode'):
            artist.constructor_props['mode'] = self.get_input('mode')
        if self.has_input('default_handler_map'):
            artist.props['default_handler_map'] = self.get_input('default_handler_map')
        if self.has_input('bbox_transform'):
            artist.constructor_props['bbox_transform'] = self.get_input('bbox_transform')


class MplLine2DProperties(MplArtistProperties):
    """
    A line - the line can have both a solid linestyle connecting all
    the vertices, and a marker at each vertex.  Additionally, the
    drawing of the solid line is influenced by the drawstyle, e.g., one
    can create "stepped" lines in various styles.


    
    """
    _input_ports = [
              ("picker", "basic:Float",
                {'optional': True, 'docstring': 'Sets the event picker details for the line.'}),
              ("dash_capstyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the cap style for dashed linestyles', 'values': "[['butt', 'round', 'projecting']]", 'optional': True}),
              ("color", "basic:Color",
                {'optional': True, 'docstring': 'Set the color of the line'}),
              ("markevery", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the markevery property to subsample the plot when using markers.\n\n        e.g., if `every=5`, every 5-th marker will be plotted.\n        Parameters\n        ----------\n        every: None | int | length-2 tuple of int | slice | list/array of int |\n        float | length-2 tuple of float\n            Which markers to plot.\n\n            - every=None, every point will be plotted.\n            - every=N, every N-th marker will be plotted starting with\n              marker 0.\n            - every=(start, N), every N-th marker, starting at point\n              start, will be plotted.\n            - every=slice(start, end, N), every N-th marker, starting at\n              point start, upto but not including point end, will be plotted.\n            - every=[i, j, m, n], only markers at points i, j, m, and n\n              will be plotted.\n            - every=0.1, (i.e. a float) then markers will be spaced at\n              approximately equal distances along the line; the distance\n              along the line between markers is determined by multiplying the\n              display-coordinate distance of the axes bounding-box diagonal\n              by the value of every.\n            - every=(0.5, 0.1) (i.e. a length-2 tuple of float), the\n              same functionality as every=0.1 is exhibited but the first\n              marker will be 0.5 multiplied by the\n              display-cordinate-diagonal-distance along the line.\n\n        Notes\n        -----\n        Setting the markevery property will only show markers at actual data\n        points.  When using float arguments to set the markevery property\n        on irregularly spaced data, the markers will likely not appear evenly\n        spaced because the actual data points do not coincide with the\n        theoretical spacing between markers.\n\n        When using a start offset to specify the first marker, the offset will\n        be from the first data point which may be different from the first\n        the visible data point if the plot is zoomed in.\n\n        If zooming in on a plot when using float arguments then the actual\n        data points that have markers will change because the distance between\n        markers is always determined from the display-coordinates\n        axes-bounding-box-diagonal regardless of the actual axes data limits.\n\n        ', 'values': "[[None, 'length-2 tuple of int', None]]", 'optional': True}),
              ("markeredgecolor", "basic:Color",
                {'optional': True, 'docstring': 'Set the marker edge color'}),
              ("marker", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the line marker\nParameters\n-----------\n\nmarker: marker style\n    See `~matplotlib.markers` for full description of possible\n    argument', 'values': "[['caretdown', 'caretleft', 'caretright', 'caretup', 'circle', 'diamond', 'hexagon1', 'hexagon2', 'hline', 'nothing', 'octagon', 'pentagon', 'pixel', 'plus', 'point', 'square', 'star', 'thin_diamond', 'tickdown', 'tickleft', 'tickright', 'tickup', 'tri_down', 'tri_left', 'tri_right', 'tri_up', 'triangle_down', 'triangle_left', 'triangle_right', 'triangle_up', 'vline', 'x', 'mathtext']]", 'optional': True}),
              ("markerfacecoloralt", "basic:Color",
                {'optional': True, 'docstring': 'Set the alternate marker face color.'}),
              ("linewidth", "basic:Float",
                {'optional': True, 'docstring': 'Set the line width in points'}),
              ("linestyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the linestyle of the line (also accepts drawstyles)\n\n'steps' is equivalent to 'steps-pre' and is maintained for backward-compatibility.\n\n\n\nand any drawstyle in combination with a linestyle, e.g., 'steps--'.", 'values': "[['solid', 'dashed', 'dash_dot', 'dotted', 'draw nothing', 'draw nothing', 'draw nothing']]", 'optional': True}),
              ("solid_joinstyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the join style for solid linestyles', 'values': "[['miter', 'round', 'bevel']]", 'optional': True}),
              ("markerfacecolor", "basic:Color",
                {'optional': True, 'docstring': 'Set the marker face color.'}),
              ("axes", "basic:String",
                {'optional': True, 'docstring': 'Set the :class:`~matplotlib.axes.Axes` instance in which the artist resides, if any.'}),
              ("transform", "basic:String",
                {'optional': True, 'docstring': 'set the Transformation instance used by this artist'}),
              ("fillstyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the marker fill style; 'full' means fill the whole marker. 'none' means no filling; other options are for half-filled markers.", 'values': "[['full', 'left', 'right', 'bottom', 'top', 'none']]", 'optional': True}),
              ("markeredgewidth", "basic:Float",
                {'optional': True, 'docstring': 'Set the marker edge width in points'}),
              ("solid_capstyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the cap style for solid linestyles', 'values': "[['butt', 'round', 'projecting']]", 'optional': True}),
              ("dashes", "basic:List",
                {'optional': True, 'docstring': 'Set the dash sequence, sequence of dashes with on off ink in points.  If seq is empty or if seq = (None, None), the linestyle will be set to solid.'}),
              ("markersize", "basic:Float",
                {'optional': True, 'docstring': 'Set the marker size in points'}),
              ("antialiased", "basic:Boolean",
                {'optional': True, 'docstring': 'True if line should be drawin with antialiased rendering'}),
              ("xdata", "basic:String",
                {'optional': True, 'docstring': 'Set the data np.array for x'}),
              ("drawstyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the drawstyle of the plot\n\n'default' connects the points with lines. The steps variants produce step-plots. 'steps' is equivalent to 'steps-pre' and is maintained for backward-compatibility.", 'values': "[['default', 'steps', 'steps-pre', 'steps-mid', 'steps-post']]", 'optional': True}),
              ("dash_joinstyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the join style for dashed linestyles', 'values': "[['miter', 'round', 'bevel']]", 'optional': True}),
              ("pickradius", "basic:Float",
                {'optional': True, 'docstring': 'Sets the pick radius used for containment tests'}),
              ("ydata", "basic:String",
                {'optional': True, 'docstring': 'Set the data np.array for y'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplLine2DProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplLine2DProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('picker'):
            artist.props['picker'] = self.get_input('picker')
        if self.has_input('dash_capstyle'):
            artist.props['dash_capstyle'] = self.get_input('dash_capstyle')
        if self.has_input('color'):
            artist.props['color'] = self.get_input('color')
            artist.props['color'] = translate_color(artist.props['color'])
        if self.has_input('markevery'):
            artist.props['markevery'] = self.get_input('markevery')
        if self.has_input('markeredgecolor'):
            artist.props['markeredgecolor'] = self.get_input('markeredgecolor')
            artist.props['markeredgecolor'] = translate_color(artist.props['markeredgecolor'])
        if self.has_input('marker'):
            artist.props['marker'] = self.get_input('marker')
            artist.props['marker'] = translate_MplLine2DProperties_marker(artist.props['marker'])
        if self.has_input('markerfacecoloralt'):
            artist.props['markerfacecoloralt'] = self.get_input('markerfacecoloralt')
            artist.props['markerfacecoloralt'] = translate_color(artist.props['markerfacecoloralt'])
        if self.has_input('linewidth'):
            artist.props['linewidth'] = self.get_input('linewidth')
        if self.has_input('linestyle'):
            artist.props['linestyle'] = self.get_input('linestyle')
            artist.props['linestyle'] = translate_MplLine2DProperties_linestyle(artist.props['linestyle'])
        if self.has_input('solid_joinstyle'):
            artist.props['solid_joinstyle'] = self.get_input('solid_joinstyle')
        if self.has_input('markerfacecolor'):
            artist.props['markerfacecolor'] = self.get_input('markerfacecolor')
            artist.props['markerfacecolor'] = translate_color(artist.props['markerfacecolor'])
        if self.has_input('axes'):
            artist.props['axes'] = self.get_input('axes')
        if self.has_input('transform'):
            artist.props['transform'] = self.get_input('transform')
        if self.has_input('fillstyle'):
            artist.props['fillstyle'] = self.get_input('fillstyle')
        if self.has_input('markeredgewidth'):
            artist.props['markeredgewidth'] = self.get_input('markeredgewidth')
        if self.has_input('solid_capstyle'):
            artist.props['solid_capstyle'] = self.get_input('solid_capstyle')
        if self.has_input('dashes'):
            artist.props['dashes'] = self.get_input('dashes')
        if self.has_input('markersize'):
            artist.props['markersize'] = self.get_input('markersize')
        if self.has_input('antialiased'):
            artist.props['antialiased'] = self.get_input('antialiased')
        if self.has_input('xdata'):
            artist.props['xdata'] = self.get_input('xdata')
        if self.has_input('drawstyle'):
            artist.props['drawstyle'] = self.get_input('drawstyle')
        if self.has_input('dash_joinstyle'):
            artist.props['dash_joinstyle'] = self.get_input('dash_joinstyle')
        if self.has_input('pickradius'):
            artist.props['pickradius'] = self.get_input('pickradius')
        if self.has_input('ydata'):
            artist.props['ydata'] = self.get_input('ydata')


class MplPatchProperties(MplArtistProperties):
    """
    A patch is a 2D artist with a face color and an edge color.

    If any of *edgecolor*, *facecolor*, *linewidth*, or *antialiased*
    are *None*, they default to their rc params setting.
    
    """
    _input_ports = [
              ("edgecolor", "basic:Color",
                {'optional': True, 'docstring': 'Set the patch edge color'}),
              ("facecolor", "basic:Color",
                {'optional': True, 'docstring': 'Set the patch face color'}),
              ("color", "basic:Color",
                {'optional': True, 'docstring': 'Set both the edgecolor and the facecolor. .. seealso:\n\n:meth:`set_facecolor`, :meth:`set_edgecolor`    For setting the edge or face color individually.'}),
              ("hatch", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the hatching pattern\n\nhatch can be one of:\n\n/   - diagonal hatching \\   - back diagonal |   - vertical -   - horizontal +   - crossed x   - crossed diagonal o   - small circle O   - large circle .   - dots *   - stars\n\nLetters can be combined, in which case all the specified hatchings are done.  If same letter repeats, it increases the density of hatching of that pattern.\n\nHatching is supported in the PostScript, PDF, SVG and Agg backends only.', 'values': '[[\'/\', "\'\\\\\'", "\'", "\'", \'-\', \'+\', \'x\', \'o\', \'O\', \'.\', \'*\']]', 'optional': True}),
              ("joinstyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the patch joinstyle', 'values': "[['miter', 'round', 'bevel']]", 'optional': True}),
              ("antialiased", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether to use antialiased rendering'}),
              ("capstyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the patch capstyle', 'values': "[['butt', 'round', 'projecting']]", 'optional': True}),
              ("alpha", "basic:Float",
                {'optional': True, 'docstring': 'Set the alpha tranparency of the patch.'}),
              ("linewidth", "basic:Float",
                {'optional': True, 'docstring': 'Set the patch linewidth in points'}),
              ("linestyle", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the patch linestyle', 'values': "[['solid', 'dashed', 'dashdot', 'dotted']]", 'optional': True}),
              ("fill", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether to fill the patch'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplPatchProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplPatchProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('edgecolor'):
            artist.props['edgecolor'] = self.get_input('edgecolor')
            artist.props['edgecolor'] = translate_color(artist.props['edgecolor'])
        if self.has_input('facecolor'):
            artist.props['facecolor'] = self.get_input('facecolor')
            artist.props['facecolor'] = translate_color(artist.props['facecolor'])
        if self.has_input('color'):
            artist.props['color'] = self.get_input('color')
            artist.props['color'] = translate_color(artist.props['color'])
        if self.has_input('hatch'):
            artist.props['hatch'] = self.get_input('hatch')
        if self.has_input('joinstyle'):
            artist.props['joinstyle'] = self.get_input('joinstyle')
        if self.has_input('antialiased'):
            artist.props['antialiased'] = self.get_input('antialiased')
        if self.has_input('capstyle'):
            artist.props['capstyle'] = self.get_input('capstyle')
        if self.has_input('alpha'):
            artist.props['alpha'] = self.get_input('alpha')
        if self.has_input('linewidth'):
            artist.props['linewidth'] = self.get_input('linewidth')
        if self.has_input('linestyle'):
            artist.props['linestyle'] = self.get_input('linestyle')
        if self.has_input('fill'):
            artist.props['fill'] = self.get_input('fill')


class MplPcolorImageProperties(MplArtistProperties):
    """
    Make a pcolor-style plot with an irregular rectangular grid.

    This uses a variation of the original irregular image code,
    and it is used by pcolorfast for the corresponding grid type.
    
    """
    _input_ports = [
              ("A", "basic:String",
                {'optional': True}),
              ("ax", "basic:String",
                {'optional': True}),
              ("cmap", "basic:String",
                {'optional': True}),
              ("x", "basic:String",
                {'optional': True}),
              ("y", "basic:String",
                {'optional': True}),
              ("alpha", "basic:Float",
                {'optional': True, 'docstring': 'Set the alpha value used for blending - not supported on all backends'}),
              ("data", "basic:String",
                {'optional': True}),
              ("norm", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplPcolorImageProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplPcolorImageProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('A'):
            artist.constructor_props['A'] = self.get_input('A')
        if self.has_input('ax'):
            artist.constructor_props['ax'] = self.get_input('ax')
        if self.has_input('cmap'):
            artist.constructor_props['cmap'] = self.get_input('cmap')
        if self.has_input('x'):
            artist.constructor_props['x'] = self.get_input('x')
        if self.has_input('y'):
            artist.constructor_props['y'] = self.get_input('y')
        if self.has_input('alpha'):
            artist.props['alpha'] = self.get_input('alpha')
        if self.has_input('data'):
            artist.props['data'] = self.get_input('data')
        if self.has_input('norm'):
            artist.constructor_props['norm'] = self.get_input('norm')


class MplTextProperties(MplArtistProperties):
    """
    Handle storing and drawing of text in window or data coordinates.
    
    """
    _input_ports = [
              ("rotation_mode", "basic:String",
                {'optional': True, 'docstring': 'set text rotation mode. If "anchor", the un-rotated text will first aligned according to their ha and va, and then will be rotated with the alignement reference point as a origin. If None (default), the text will be rotated first then will be aligned.'}),
              ("clip_on", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether artist uses clipping.\n\nWhen False artists will be visible out side of the axes which can lead to unexpected results.'}),
              ("family", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the font family.  May be either a single string, or a list of strings in decreasing priority.  Each string may be either a real font name or a generic font class name.  If the latter, the specific font names will be looked up in the matplotlibrc file.', 'values': "[['FONTNAME', 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']]", 'optional': True}),
              ("color", "basic:Color",
                {'optional': True, 'docstring': 'Set the foreground color of the text'}),
              ("text", "basic:String",
                {'optional': True, 'docstring': 'Set the text string s\n\nIt may contain newlines (\\n) or math in LaTeX syntax.'}),
              ("clip_box", "basic:String",
                {'optional': True, 'docstring': "Set the artist's clip :class:`~matplotlib.transforms.Bbox`."}),
              ("verticalalignment", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the vertical alignment', 'values': "[['center', 'top', 'bottom', 'baseline']]", 'optional': True}),
              ("size", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the font size.  May be either a size string, relative to the default font size, or an absolute font size in points.', 'values': "[['size in points', 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']]", 'optional': True}),
              ("style", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the font style.', 'values': "[['normal', 'italic', 'oblique']]", 'optional': True}),
              ("weight", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the font weight.', 'values': "[['a numeric value in range 0-1000', 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black']]", 'optional': True}),
              ("linespacing", "basic:Float",
                {'optional': True, 'docstring': 'Set the line spacing as a multiple of the font size. Default is 1.2.'}),
              ("stretch", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the font stretch (horizontal condensation or expansion).', 'values': "[['a numeric value in range 0-1000', 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded']]", 'optional': True}),
              ("clip_path", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the artist's clip path, which may be:\n\na :class:`~matplotlib.patches.Patch` (or subclass) instance\n\n\n\nNone, to remove the clipping path\n\nFor efficiency, if the path happens to be an axis-aligned rectangle, this method will set the clipping box to the corresponding rectangle and set the clipping path to None.", 'values': "[['(:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`)', ':class:`~matplotlib.patches.Patch`']]", 'optional': True}),
              ("fontproperties", "basic:String",
                {'optional': True, 'docstring': 'Set the font properties that control the text.  fp must be a :class:`matplotlib.font_manager.FontProperties` object.'}),
              ("horizontalalignment", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the horizontal alignment to one of', 'values': "[['center', 'right', 'left']]", 'optional': True}),
              ("variant", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the font variant, either 'normal' or 'small-caps'.", 'values': "[['normal', 'small-caps']]", 'optional': True}),
              ("multialignment", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the alignment for multiple lines layout.  The layout of the bounding box of all the lines is determined bu the horizontalalignment and verticalalignment properties, but the multiline text within that box can be', 'values': "[['left', 'right', 'center']]", 'optional': True}),
              ("bbox", "basic:String",
                {'optional': True, 'docstring': 'Draw a bounding box around self.  rectprops are any settable properties for a rectangle, e.g., facecolor=\'red\', alpha=0.5.\n\nt.set_bbox(dict(facecolor=\'red\', alpha=0.5))\n\nIf rectprops has "boxstyle" key. A FancyBboxPatch is initialized with rectprops and will be drawn. The mutation scale of the FancyBboxPath is set to the fontsize.'}),
              ("backgroundcolor", "basic:Color",
                {'optional': True, 'docstring': 'Set the background color of the text by updating the bbox.'}),
              ("position", "basic:String",
                {'optional': True, 'docstring': 'Set the (x, y) position of the text'}),
              ("rotation", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the rotation of the text', 'values': "[['angle in degrees', 'vertical', 'horizontal']]", 'optional': True}),
              ("y", "basic:Float",
                {'optional': True, 'docstring': 'Set the y position of the text'}),
              ("x", "basic:Float",
                {'optional': True, 'docstring': 'Set the x position of the text'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplTextProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplTextProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('rotation_mode'):
            artist.props['rotation_mode'] = self.get_input('rotation_mode')
        if self.has_input('clip_on'):
            artist.props['clip_on'] = self.get_input('clip_on')
        if self.has_input('family'):
            artist.props['family'] = self.get_input('family')
        if self.has_input('color'):
            artist.props['color'] = self.get_input('color')
            artist.props['color'] = translate_color(artist.props['color'])
        if self.has_input('text'):
            artist.props['text'] = self.get_input('text')
        if self.has_input('clip_box'):
            artist.props['clip_box'] = self.get_input('clip_box')
        if self.has_input('verticalalignment'):
            artist.props['verticalalignment'] = self.get_input('verticalalignment')
        if self.has_input('size'):
            artist.props['size'] = self.get_input('size')
        if self.has_input('style'):
            artist.props['style'] = self.get_input('style')
        if self.has_input('weight'):
            artist.props['weight'] = self.get_input('weight')
        if self.has_input('linespacing'):
            artist.props['linespacing'] = self.get_input('linespacing')
        if self.has_input('stretch'):
            artist.props['stretch'] = self.get_input('stretch')
        if self.has_input('clip_path'):
            artist.props['clip_path'] = self.get_input('clip_path')
        if self.has_input('fontproperties'):
            artist.props['fontproperties'] = self.get_input('fontproperties')
        if self.has_input('horizontalalignment'):
            artist.props['horizontalalignment'] = self.get_input('horizontalalignment')
        if self.has_input('variant'):
            artist.props['variant'] = self.get_input('variant')
        if self.has_input('multialignment'):
            artist.props['multialignment'] = self.get_input('multialignment')
        if self.has_input('bbox'):
            artist.props['bbox'] = self.get_input('bbox')
        if self.has_input('backgroundcolor'):
            artist.props['backgroundcolor'] = self.get_input('backgroundcolor')
            artist.props['backgroundcolor'] = translate_color(artist.props['backgroundcolor'])
        if self.has_input('position'):
            artist.props['position'] = self.get_input('position')
        if self.has_input('rotation'):
            artist.props['rotation'] = self.get_input('rotation')
        if self.has_input('y'):
            artist.props['y'] = self.get_input('y')
        if self.has_input('x'):
            artist.props['x'] = self.get_input('x')


class MplTickProperties(MplArtistProperties):
    """
    Abstract base class for the axis ticks, grid lines and labels

    1 refers to the bottom of the plot for xticks and the left for yticks
    2 refers to the top of the plot for xticks and the right for yticks

    Publicly accessible attributes:

      :attr:`tick1line`
          a Line2D instance

      :attr:`tick2line`
          a Line2D instance

      :attr:`gridline`
          a Line2D instance

      :attr:`label1`
          a Text instance

      :attr:`label2`
          a Text instance

      :attr:`gridOn`
          a boolean which determines whether to draw the tickline

      :attr:`tick1On`
          a boolean which determines whether to draw the 1st tickline

      :attr:`tick2On`
          a boolean which determines whether to draw the 2nd tickline

      :attr:`label1On`
          a boolean which determines whether to draw tick label

      :attr:`label2On`
          a boolean which determines whether to draw tick label

    
    """
    _input_ports = [
              ("label1On", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("loc", "basic:String",
                {'optional': True}),
              ("major", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("label2On", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
              ("color", "basic:Color",
                {'optional': True}),
              ("axes", "basic:String",
                {'optional': True}),
              ("clip_path", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the artist's clip path, which may be:\n\na :class:`~matplotlib.patches.Patch` (or subclass) instance\n\n\n\nNone, to remove the clipping path\n\nFor efficiency, if the path happens to be an axis-aligned rectangle, this method will set the clipping box to the corresponding rectangle and set the clipping path to None.", 'values': "[['(:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`)', ':class:`~matplotlib.patches.Patch`']]", 'optional': True}),
              ("label", "basic:String",
                {'optional': True, 'docstring': 'Set the text of ticklabel'}),
              ("labelcolor", "basic:String",
                {'optional': True}),
              ("tickdir", "basic:String",
                {'optional': True}),
              ("pad", "basic:Float",
                {'optional': True, 'docstring': 'Set the tick label pad in points'}),
              ("gridOn", "basic:Boolean",
                {'optional': True, 'docstring': 'a boolean which determines whether to draw the tickline'}),
              ("zorder", "basic:String",
                {'optional': True}),
              ("tick2On", "basic:Boolean",
                {'optional': True, 'docstring': 'a boolean which determines whether to draw the 2nd tickline', 'defaults': '[True]'}),
              ("labelsize", "basic:String",
                {'optional': True}),
              ("width", "basic:String",
                {'optional': True}),
              ("tick1On", "basic:Boolean",
                {'optional': True, 'docstring': 'a boolean which determines whether to draw the 1st tickline', 'defaults': '[True]'}),
              ("size", "basic:String",
                {'optional': True}),
              ("label1Properties", "MplTextProperties",
                {'docstring': 'Set the text of ticklabel'}),
              ("label2Properties", "MplTextProperties",
                {'docstring': 'Set the text of ticklabel2'}),
              ("tick1lineProperties", "MplLine2DProperties",
                {}),
              ("tick2lineProperties", "MplLine2DProperties",
                {}),
              ("gridlineProperties", "MplLine2DProperties",
                {}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplTickProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                if 'label1' in self.sub_props:
                    self.sub_props['label1'].update_props(obj.label1)
                if 'label2' in self.sub_props:
                    self.sub_props['label2'].update_props(obj.label2)
                if 'tick1line' in self.sub_props:
                    self.sub_props['tick1line'].update_props(obj.tick1line)
                if 'tick2line' in self.sub_props:
                    self.sub_props['tick2line'].update_props(obj.tick2line)
                if 'gridline' in self.sub_props:
                    self.sub_props['gridline'].update_props(obj.gridline)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplTickProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('label1On'):
            artist.not_setp_props['label1On'] = self.get_input('label1On')
        if self.has_input('loc'):
            artist.constructor_props['loc'] = self.get_input('loc')
        if self.has_input('major'):
            artist.constructor_props['major'] = self.get_input('major')
        if self.has_input('label2On'):
            artist.not_setp_props['label2On'] = self.get_input('label2On')
        if self.has_input('color'):
            artist.constructor_props['color'] = self.get_input('color')
            artist.constructor_props['color'] = translate_color(artist.constructor_props['color'])
        if self.has_input('axes'):
            artist.constructor_props['axes'] = self.get_input('axes')
        if self.has_input('clip_path'):
            artist.props['clip_path'] = self.get_input('clip_path')
        if self.has_input('label'):
            artist.props['label'] = self.get_input('label')
        if self.has_input('labelcolor'):
            artist.constructor_props['labelcolor'] = self.get_input('labelcolor')
        if self.has_input('tickdir'):
            artist.constructor_props['tickdir'] = self.get_input('tickdir')
        if self.has_input('pad'):
            artist.props['pad'] = self.get_input('pad')
        if self.has_input('gridOn'):
            artist.not_setp_props['gridOn'] = self.get_input('gridOn')
        if self.has_input('zorder'):
            artist.constructor_props['zorder'] = self.get_input('zorder')
        if self.has_input('tick2On'):
            artist.not_setp_props['tick2On'] = self.get_input('tick2On')
        if self.has_input('labelsize'):
            artist.constructor_props['labelsize'] = self.get_input('labelsize')
        if self.has_input('width'):
            artist.constructor_props['width'] = self.get_input('width')
        if self.has_input('tick1On'):
            artist.not_setp_props['tick1On'] = self.get_input('tick1On')
        if self.has_input('size'):
            artist.constructor_props['size'] = self.get_input('size')
        if self.has_input('label1Properties'):
            artist.sub_props['label1'] = self.get_input('label1Properties')
        if self.has_input('label2Properties'):
            artist.sub_props['label2'] = self.get_input('label2Properties')
        if self.has_input('tick1lineProperties'):
            artist.sub_props['tick1line'] = self.get_input('tick1lineProperties')
        if self.has_input('tick2lineProperties'):
            artist.sub_props['tick2line'] = self.get_input('tick2lineProperties')
        if self.has_input('gridlineProperties'):
            artist.sub_props['gridline'] = self.get_input('gridlineProperties')


class Mpl_AxesBaseProperties(MplArtistProperties):
    """
    
    """
    _input_ports = [
              ("adjustable", "basic:String",
                {'entry_types': "['enum']", 'values': "[['box', 'datalim', 'box-forced']]", 'optional': True}),
              ("figure", "basic:String",
                {'optional': True, 'docstring': 'Set the class:~matplotlib.axes.Axes figure\n\naccepts a class:~matplotlib.figure.Figure instance'}),
              ("yscale", "basic:String",
                {'optional': True, 'docstring': "Call signature:\n\nset_yscale(value)\n\nSet the scaling of the y-axis: u'linear' | u'log' | u'symlog' Different kwargs are accepted, depending on the scale:\n\n'linear'\n\n'log'\n\n\n\n'symlog'"}),
              ("navigate", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether the axes responds to navigation toolbar commands'}),
              ("aspect", "basic:String",
                {'entry_types': "['enum']", 'docstring': "aspect\n\n\n\nadjustable\n\n\n\n'box' does not allow axes sharing, as this can cause unintended side effect. For cases when sharing axes is fine, use 'box-forced'.\n\nanchor", 'values': "[['centered', 'lower left corner', 'middle of bottom edge', 'lower right corner', '']]", 'optional': True}),
              ("axis_bgcolor", "basic:Color",
                {'optional': True, 'docstring': 'set the axes background color'}),
              ("ylim", "basic:List",
                {'optional': True, 'docstring': 'Call signature:\n\nset_ylim(self, *args, **kwargs):\n\nSet the data limits for the yaxis\n\nExamples:\n\nset_ylim((bottom, top)) set_ylim(bottom, top) set_ylim(bottom=1) # top unchanged set_ylim(top=1) # bottom unchanged\n\nKeyword arguments:\n\n\n\nNote, the bottom (formerly ymin) value may be greater than the top (formerly ymax). For example, suppose y is depth in the ocean. Then one might use:\n\nset_ylim(5000, 0)\n\nso 5000 m depth is at the bottom of the plot and the surface, 0 m, is at the top.\n\nReturns the current ylimits as a length 2 tuple'}),
              ("sharey", "basic:String",
                {'optional': True}),
              ("xlim", "basic:List",
                {'optional': True, 'docstring': 'Call signature:\n\nset_xlim(self, *args, **kwargs):\n\nSet the data limits for the xaxis\n\nExamples:\n\nset_xlim((left, right)) set_xlim(left, right) set_xlim(left=1) # right unchanged set_xlim(right=1) # left unchanged\n\nKeyword arguments:\n\n\n\nNote, the left (formerly xmin) value may be greater than the right (formerly xmax). For example, suppose x is years before present. Then one might use:\n\nset_ylim(5000, 0)\n\nso 5000 years ago is on the left of the plot and the present is on the right.\n\nReturns the current xlimits as a length 2 tuple'}),
              ("axisbg", "basic:String",
                {'optional': True}),
              ("label", "basic:String",
                {'optional': True, 'defaults': "[u'']"}),
              ("xticks", "basic:List",
                {'optional': True, 'docstring': 'Set the x ticks with list of ticks'}),
              ("fig", "basic:String",
                {'optional': True}),
              ("xscale", "basic:String",
                {'optional': True, 'docstring': "Call signature:\n\nset_xscale(value)\n\nSet the scaling of the x-axis: u'linear' | u'log' | u'symlog' Different kwargs are accepted, depending on the scale:\n\n'linear'\n\n'log'\n\n\n\n'symlog'"}),
              ("rasterization_zorder", "basic:String",
                {'optional': True, 'docstring': 'Set zorder value below which artists will be rasterized.  Set to None to disable rasterizing of artists below a particular zorder.'}),
              ("axes_locator", "basic:String",
                {'optional': True, 'docstring': 'set axes_locator'}),
              ("axisbelow", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether the axis ticks and gridlines are above or below most artists'}),
              ("frame_on", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether the axes rectangle patch is drawn'}),
              ("navigate_mode", "basic:String",
                {'optional': True, 'docstring': 'Set the navigation toolbar button status;\n\nthis is not a user-API function.'}),
              ("autoscalex_on", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether autoscaling for the x-axis is applied on plot commands'}),
              ("xticklabels", "basic:List",
                {'optional': True, 'docstring': "Call signature:\n\nset_xticklabels(labels, fontdict=None, minor=False, **kwargs)\n\nSet the xtick labels with list of strings labels. Return a list of axis text instances.\n\nkwargs set the :class:`~matplotlib.text.Text` properties. Valid properties are\n\nagg_filter: unknown alpha: float (0.0 transparent through 1.0 opaque) animated: [True | False] axes: an :class:`~matplotlib.axes.Axes` instance backgroundcolor: any matplotlib color bbox: rectangle prop dict clip_box: a :class:`matplotlib.transforms.Bbox` instance clip_on: [True | False] clip_path: [ (:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`) |         :class:`~matplotlib.patches.Patch` | None ] color: any matplotlib color contains: a callable function family or fontfamily or fontname or name: [FONTNAME | 'serif' | 'sans-serif' | 'cursive' | 'fantasy' |                   'monospace' ] figure: a :class:`matplotlib.figure.Figure` instance fontproperties or font_properties: a :class:`matplotlib.font_manager.FontProperties` instance gid: an id string horizontalalignment or ha: [ 'center' | 'right' | 'left' ] label: string or anything printable with '%s' conversion. linespacing: float (multiple of font size) lod: [True | False] multialignment: ['left' | 'right' | 'center' ] path_effects: unknown picker: [None|float|boolean|callable] position: (x,y) rasterized: [True | False | None] rotation: [ angle in degrees | 'vertical' | 'horizontal' ] rotation_mode: unknown size or fontsize: [size in points | 'xx-small' | 'x-small' | 'small' |                   'medium' | 'large' | 'x-large' | 'xx-large' ] sketch_params: unknown snap: unknown stretch or fontstretch: [a numeric value in range 0-1000 | 'ultra-condensed' |                   'extra-condensed' | 'condensed' | 'semi-condensed' |                   'normal' | 'semi-expanded' | 'expanded' | 'extra-expanded' |                   'ultra-expanded' ] style or fontstyle: [ 'normal' | 'italic' | 'oblique'] text: string or anything printable with '%s' conversion. transform: :class:`~matplotlib.transforms.Transform` instance url: a url string variant or fontvariant: [ 'normal' | 'small-caps' ] verticalalignment or va or ma: [ 'center' | 'top' | 'bottom' | 'baseline' ] visible: [True | False] weight or fontweight: [a numeric value in range 0-1000 | 'ultralight' | 'light' |                   'normal' | 'regular' | 'book' | 'medium' | 'roman' |                   'semibold' | 'demibold' | 'demi' | 'bold' | 'heavy' |                   'extra bold' | 'black' ] x: float y: float zorder: any number"}),
              ("autoscale_on", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether autoscaling is applied on plot commands'}),
              ("ybound", "basic:String",
                {'optional': True, 'docstring': 'Set the lower and upper numerical bounds of the y-axis. This method will honor axes inversion regardless of parameter order. It will not change the _autoscaleYon attribute.'}),
              ("rect", "basic:String",
                {'optional': True}),
              ("sharex", "basic:String",
                {'optional': True}),
              ("yticklabels", "basic:List",
                {'optional': True, 'docstring': "Call signature:\n\nset_yticklabels(labels, fontdict=None, minor=False, **kwargs)\n\nSet the y tick labels with list of strings labels.  Return a list of :class:`~matplotlib.text.Text` instances.\n\nkwargs set :class:`~matplotlib.text.Text` properties for the labels. Valid properties are\n\nagg_filter: unknown alpha: float (0.0 transparent through 1.0 opaque) animated: [True | False] axes: an :class:`~matplotlib.axes.Axes` instance backgroundcolor: any matplotlib color bbox: rectangle prop dict clip_box: a :class:`matplotlib.transforms.Bbox` instance clip_on: [True | False] clip_path: [ (:class:`~matplotlib.path.Path`,         :class:`~matplotlib.transforms.Transform`) |         :class:`~matplotlib.patches.Patch` | None ] color: any matplotlib color contains: a callable function family or fontfamily or fontname or name: [FONTNAME | 'serif' | 'sans-serif' | 'cursive' | 'fantasy' |                   'monospace' ] figure: a :class:`matplotlib.figure.Figure` instance fontproperties or font_properties: a :class:`matplotlib.font_manager.FontProperties` instance gid: an id string horizontalalignment or ha: [ 'center' | 'right' | 'left' ] label: string or anything printable with '%s' conversion. linespacing: float (multiple of font size) lod: [True | False] multialignment: ['left' | 'right' | 'center' ] path_effects: unknown picker: [None|float|boolean|callable] position: (x,y) rasterized: [True | False | None] rotation: [ angle in degrees | 'vertical' | 'horizontal' ] rotation_mode: unknown size or fontsize: [size in points | 'xx-small' | 'x-small' | 'small' |                   'medium' | 'large' | 'x-large' | 'xx-large' ] sketch_params: unknown snap: unknown stretch or fontstretch: [a numeric value in range 0-1000 | 'ultra-condensed' |                   'extra-condensed' | 'condensed' | 'semi-condensed' |                   'normal' | 'semi-expanded' | 'expanded' | 'extra-expanded' |                   'ultra-expanded' ] style or fontstyle: [ 'normal' | 'italic' | 'oblique'] text: string or anything printable with '%s' conversion. transform: :class:`~matplotlib.transforms.Transform` instance url: a url string variant or fontvariant: [ 'normal' | 'small-caps' ] verticalalignment or va or ma: [ 'center' | 'top' | 'bottom' | 'baseline' ] visible: [True | False] weight or fontweight: [a numeric value in range 0-1000 | 'ultralight' | 'light' |                   'normal' | 'regular' | 'book' | 'medium' | 'roman' |                   'semibold' | 'demibold' | 'demi' | 'bold' | 'heavy' |                   'extra bold' | 'black' ] x: float y: float zorder: any number"}),
              ("autoscaley_on", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether autoscaling for the y-axis is applied on plot commands'}),
              ("xmargin", "basic:Float",
                {'optional': True, 'docstring': 'Set padding of X data limits prior to autoscaling.\n\nm times the data interval will be added to each end of that interval before it is used in autoscaling.'}),
              ("color_cycle", "basic:Color",
                {'optional': True, 'docstring': 'Set the color cycle for any future plot commands on this Axes.\n\nclist is a list of mpl color specifiers.'}),
              ("frameon", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("xbound", "basic:String",
                {'optional': True, 'docstring': 'Set the lower and upper numerical bounds of the x-axis. This method will honor axes inversion regardless of parameter order. It will not change the _autoscaleXon attribute.'}),
              ("yticks", "basic:List",
                {'optional': True, 'docstring': 'Set the y ticks with list of ticks Keyword arguments:'}),
              ("ymargin", "basic:Float",
                {'optional': True, 'docstring': 'Set padding of Y data limits prior to autoscaling.\n\nm times the data interval will be added to each end of that interval before it is used in autoscaling.'}),
              ("position", "basic:String",
                {'optional': True, 'docstring': 'Set the axes position with:\n\npos = [left, bottom, width, height]\n\nin relative 0,1 coords, or pos can be a :class:`~matplotlib.transforms.Bbox`\n\nThere are two position variables: one which is ultimately used, but which may be modified by :meth:`apply_aspect`, and a second which is the starting point for :meth:`apply_aspect`.'}),
              ("anchor", "basic:String",
                {'docstring': 'anchor', 'values': "[['Center', 'bottom left', 'bottom', 'bottom right', 'right', 'top right', 'top', 'top left', 'left']]", 'optional': True}),
              ("titleProperties", "MplTextProperties",
                {}),
              ("xaxisProperties", "MplXAxisProperties",
                {}),
              ("yaxisProperties", "MplYAxisProperties",
                {}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(Mpl_AxesBaseProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                if 'title' in self.sub_props:
                    self.sub_props['title'].update_props(obj.title)
                if 'xaxis' in self.sub_props:
                    self.sub_props['xaxis'].update_props(obj.xaxis)
                if 'yaxis' in self.sub_props:
                    self.sub_props['yaxis'].update_props(obj.yaxis)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = Mpl_AxesBaseProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('adjustable'):
            artist.props['adjustable'] = self.get_input('adjustable')
        if self.has_input('figure'):
            artist.props['figure'] = self.get_input('figure')
        if self.has_input('yscale'):
            artist.props['yscale'] = self.get_input('yscale')
        if self.has_input('navigate'):
            artist.props['navigate'] = self.get_input('navigate')
        if self.has_input('aspect'):
            artist.props['aspect'] = self.get_input('aspect')
            artist.props['aspect'] = translate_Mpl_AxesBaseProperties_aspect(artist.props['aspect'])
        if self.has_input('axis_bgcolor'):
            artist.props['axis_bgcolor'] = self.get_input('axis_bgcolor')
            artist.props['axis_bgcolor'] = translate_color(artist.props['axis_bgcolor'])
        if self.has_input('ylim'):
            artist.props['ylim'] = self.get_input('ylim')
        if self.has_input('sharey'):
            artist.constructor_props['sharey'] = self.get_input('sharey')
        if self.has_input('xlim'):
            artist.props['xlim'] = self.get_input('xlim')
        if self.has_input('axisbg'):
            artist.constructor_props['axisbg'] = self.get_input('axisbg')
        if self.has_input('label'):
            artist.constructor_props['label'] = self.get_input('label')
        if self.has_input('xticks'):
            artist.props['xticks'] = self.get_input('xticks')
        if self.has_input('fig'):
            artist.constructor_props['fig'] = self.get_input('fig')
        if self.has_input('xscale'):
            artist.props['xscale'] = self.get_input('xscale')
        if self.has_input('rasterization_zorder'):
            artist.props['rasterization_zorder'] = self.get_input('rasterization_zorder')
        if self.has_input('axes_locator'):
            artist.props['axes_locator'] = self.get_input('axes_locator')
        if self.has_input('axisbelow'):
            artist.props['axisbelow'] = self.get_input('axisbelow')
        if self.has_input('frame_on'):
            artist.props['frame_on'] = self.get_input('frame_on')
        if self.has_input('navigate_mode'):
            artist.props['navigate_mode'] = self.get_input('navigate_mode')
        if self.has_input('autoscalex_on'):
            artist.props['autoscalex_on'] = self.get_input('autoscalex_on')
        if self.has_input('xticklabels'):
            artist.props['xticklabels'] = self.get_input('xticklabels')
        if self.has_input('autoscale_on'):
            artist.props['autoscale_on'] = self.get_input('autoscale_on')
        if self.has_input('ybound'):
            artist.props['ybound'] = self.get_input('ybound')
        if self.has_input('rect'):
            artist.constructor_props['rect'] = self.get_input('rect')
        if self.has_input('sharex'):
            artist.constructor_props['sharex'] = self.get_input('sharex')
        if self.has_input('yticklabels'):
            artist.props['yticklabels'] = self.get_input('yticklabels')
        if self.has_input('autoscaley_on'):
            artist.props['autoscaley_on'] = self.get_input('autoscaley_on')
        if self.has_input('xmargin'):
            artist.props['xmargin'] = self.get_input('xmargin')
        if self.has_input('color_cycle'):
            artist.props['color_cycle'] = self.get_input('color_cycle')
            artist.props['color_cycle'] = translate_color(artist.props['color_cycle'])
        if self.has_input('frameon'):
            artist.constructor_props['frameon'] = self.get_input('frameon')
        if self.has_input('xbound'):
            artist.props['xbound'] = self.get_input('xbound')
        if self.has_input('yticks'):
            artist.props['yticks'] = self.get_input('yticks')
        if self.has_input('ymargin'):
            artist.props['ymargin'] = self.get_input('ymargin')
        if self.has_input('position'):
            artist.props['position'] = self.get_input('position')
        if self.has_input('anchor'):
            artist.props['anchor'] = self.get_input('anchor')
            artist.props['anchor'] = translate_Mpl_AxesBaseProperties_anchor(artist.props['anchor'])
        if self.has_input('titleProperties'):
            artist.sub_props['title'] = self.get_input('titleProperties')
        if self.has_input('xaxisProperties'):
            artist.sub_props['xaxis'] = self.get_input('xaxisProperties')
        if self.has_input('yaxisProperties'):
            artist.sub_props['yaxis'] = self.get_input('yaxisProperties')


class Mpl_AxesImageBaseProperties(MplArtistProperties):
    """None
    """
    _input_ports = [
              ("origin", "basic:String",
                {'optional': True}),
              ("resample", "basic:Boolean",
                {'optional': True, 'docstring': 'Set whether or not image resampling is used'}),
              ("norm", "basic:String",
                {'optional': True}),
              ("cmap", "basic:String",
                {'optional': True}),
              ("filternorm", "basic:String",
                {'optional': True, 'docstring': 'Set whether the resize filter norms the weights -- see help for imshow'}),
              ("ax", "basic:String",
                {'optional': True}),
              ("alpha", "basic:Float",
                {'optional': True, 'docstring': 'Set the alpha value used for blending - not supported on all backends'}),
              ("array", "basic:String",
                {'optional': True, 'docstring': 'Retained for backwards compatibility - use set_data instead'}),
              ("data", "basic:String",
                {'optional': True, 'docstring': 'Set the image array'}),
              ("filterrad", "basic:Float",
                {'optional': True, 'docstring': 'Set the resize filter radius only applicable to some interpolation schemes -- see help for imshow'}),
              ("interpolation", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the interpolation method the image uses when resizing.\n\nif None, use a value from rc setting. If 'none', the image is shown as is without interpolating. 'none' is only supported in agg, ps and pdf backends and will fall back to 'nearest' mode for other backends.", 'values': "[['nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', 'none', '']]", 'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(Mpl_AxesImageBaseProperties)")]

    class Artist(MplArtistProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplArtistProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = Mpl_AxesImageBaseProperties.Artist()
            self.set_output("value", artist)

        MplArtistProperties.compute(self, artist)
        if self.has_input('origin'):
            artist.constructor_props['origin'] = self.get_input('origin')
        if self.has_input('resample'):
            artist.props['resample'] = self.get_input('resample')
        if self.has_input('norm'):
            artist.constructor_props['norm'] = self.get_input('norm')
        if self.has_input('cmap'):
            artist.constructor_props['cmap'] = self.get_input('cmap')
        if self.has_input('filternorm'):
            artist.props['filternorm'] = self.get_input('filternorm')
        if self.has_input('ax'):
            artist.constructor_props['ax'] = self.get_input('ax')
        if self.has_input('alpha'):
            artist.props['alpha'] = self.get_input('alpha')
        if self.has_input('array'):
            artist.props['array'] = self.get_input('array')
        if self.has_input('data'):
            artist.props['data'] = self.get_input('data')
        if self.has_input('filterrad'):
            artist.props['filterrad'] = self.get_input('filterrad')
        if self.has_input('interpolation'):
            artist.props['interpolation'] = self.get_input('interpolation')


class MplXAxisProperties(MplAxisProperties):
    """None
    """
    _input_ports = [
              ("view_interval", "basic:String",
                {'optional': True, 'docstring': 'If ignore is False, the order of vmin, vmax does not matter; the original axis orientation will be preserved. In addition, the view limits can be expanded, but will not be reduced.  This method is for mpl internal use; for normal use, see :meth:`~matplotlib.axes.Axes.set_xlim`.'}),
              ("ticks_position", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the ticks position (top, bottom, both, default or none) both sets the ticks to appear on both positions, but does not change the tick labels.  'default' resets the tick positions to the default: ticks on both positions, labels at bottom.  'none' can be used if you don't want any ticks. 'none' and 'both' affect only the ticks, not the labels.", 'values': "[['top', 'bottom', 'both', 'default', 'none']]", 'optional': True}),
              ("axes", "basic:String",
                {'optional': True}),
              ("label_position", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the label position (top or bottom)', 'values': "[['top', 'bottom']]", 'optional': True}),
              ("data_interval", "basic:String",
                {'optional': True, 'docstring': 'set the axis data limits'}),
              ("pickradius", "basic:Integer",
                {'optional': True, 'defaults': '[15]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplXAxisProperties)")]

    class Artist(MplAxisProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplAxisProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplXAxisProperties.Artist()
            self.set_output("value", artist)

        MplAxisProperties.compute(self, artist)
        if self.has_input('view_interval'):
            artist.props['view_interval'] = self.get_input('view_interval')
        if self.has_input('ticks_position'):
            artist.props['ticks_position'] = self.get_input('ticks_position')
        if self.has_input('axes'):
            artist.constructor_props['axes'] = self.get_input('axes')
        if self.has_input('label_position'):
            artist.props['label_position'] = self.get_input('label_position')
        if self.has_input('data_interval'):
            artist.props['data_interval'] = self.get_input('data_interval')
        if self.has_input('pickradius'):
            artist.constructor_props['pickradius'] = self.get_input('pickradius')


class MplYAxisProperties(MplAxisProperties):
    """None
    """
    _input_ports = [
              ("offset_position", "basic:String",
                {'optional': True}),
              ("view_interval", "basic:String",
                {'optional': True, 'docstring': 'If ignore is False, the order of vmin, vmax does not matter; the original axis orientation will be preserved. In addition, the view limits can be expanded, but will not be reduced.  This method is for mpl internal use; for normal use, see :meth:`~matplotlib.axes.Axes.set_ylim`.'}),
              ("ticks_position", "basic:String",
                {'entry_types': "['enum']", 'docstring': "Set the ticks position (left, right, both, default or none) 'both' sets the ticks to appear on both positions, but does not change the tick labels.  'default' resets the tick positions to the default: ticks on both positions, labels at left.  'none' can be used if you don't want any ticks. 'none' and 'both' affect only the ticks, not the labels.", 'values': "[['left', 'right', 'both', 'default', 'none']]", 'optional': True}),
              ("axes", "basic:String",
                {'optional': True}),
              ("label_position", "basic:String",
                {'entry_types': "['enum']", 'docstring': 'Set the label position (left or right)', 'values': "[['left', 'right']]", 'optional': True}),
              ("data_interval", "basic:String",
                {'optional': True, 'docstring': 'set the axis data limits'}),
              ("pickradius", "basic:Integer",
                {'optional': True, 'defaults': '[15]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplYAxisProperties)")]

    class Artist(MplAxisProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplAxisProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplYAxisProperties.Artist()
            self.set_output("value", artist)

        MplAxisProperties.compute(self, artist)
        if self.has_input('offset_position'):
            artist.props['offset_position'] = self.get_input('offset_position')
        if self.has_input('view_interval'):
            artist.props['view_interval'] = self.get_input('view_interval')
        if self.has_input('ticks_position'):
            artist.props['ticks_position'] = self.get_input('ticks_position')
        if self.has_input('axes'):
            artist.constructor_props['axes'] = self.get_input('axes')
        if self.has_input('label_position'):
            artist.props['label_position'] = self.get_input('label_position')
        if self.has_input('data_interval'):
            artist.props['data_interval'] = self.get_input('data_interval')
        if self.has_input('pickradius'):
            artist.constructor_props['pickradius'] = self.get_input('pickradius')


class MplEllipseCollectionProperties(MplCollectionProperties):
    """
    A collection of ellipses, drawn using splines.
    
    """
    _input_ports = [
              ("units", "basic:String",
                {'optional': True, 'defaults': "[u'points']"}),
              ("widths", "basic:String",
                {'optional': True}),
              ("angles", "basic:String",
                {'optional': True}),
              ("heights", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplEllipseCollectionProperties)")]

    class Artist(MplCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplEllipseCollectionProperties.Artist()
            self.set_output("value", artist)

        MplCollectionProperties.compute(self, artist)
        if self.has_input('units'):
            artist.constructor_props['units'] = self.get_input('units')
        if self.has_input('widths'):
            artist.constructor_props['widths'] = self.get_input('widths')
        if self.has_input('angles'):
            artist.constructor_props['angles'] = self.get_input('angles')
        if self.has_input('heights'):
            artist.constructor_props['heights'] = self.get_input('heights')


class MplLineCollectionProperties(MplCollectionProperties):
    """
    All parameters must be sequences or scalars; if scalars, they will
    be converted to sequences.  The property of the ith line
    segment is::

       prop[i % len(props)]

    i.e., the properties cycle if the ``len`` of props is less than the
    number of segments.
    
    """
    _input_ports = [
              ("paths", "basic:String",
                {'optional': True}),
              ("antialiaseds", "basic:String",
                {'optional': True}),
              ("linestyles", "basic:String",
                {'optional': True, 'defaults': "[u'solid']"}),
              ("offsets", "basic:String",
                {'optional': True}),
              ("color", "basic:Color",
                {'optional': True, 'docstring': 'Set the color(s) of the line collection.  c can be a matplotlib color arg (all patches have same color), or a sequence or rgba tuples; if it is a sequence the patches will cycle through the sequence.'}),
              ("segments", "basic:String",
                {'optional': True}),
              ("linewidths", "basic:String",
                {'optional': True}),
              ("colors", "basic:String",
                {'optional': True}),
              ("cmap", "basic:String",
                {'optional': True}),
              ("transOffset", "basic:String",
                {'optional': True}),
              ("verts", "basic:String",
                {'optional': True}),
              ("pickradius", "basic:Integer",
                {'optional': True, 'defaults': '[5]'}),
              ("zorder", "basic:Integer",
                {'optional': True, 'defaults': '[2]'}),
              ("norm", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplLineCollectionProperties)")]

    class Artist(MplCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplLineCollectionProperties.Artist()
            self.set_output("value", artist)

        MplCollectionProperties.compute(self, artist)
        if self.has_input('paths'):
            artist.props['paths'] = self.get_input('paths')
        if self.has_input('antialiaseds'):
            artist.constructor_props['antialiaseds'] = self.get_input('antialiaseds')
        if self.has_input('linestyles'):
            artist.constructor_props['linestyles'] = self.get_input('linestyles')
        if self.has_input('offsets'):
            artist.constructor_props['offsets'] = self.get_input('offsets')
        if self.has_input('color'):
            artist.props['color'] = self.get_input('color')
            artist.props['color'] = translate_color(artist.props['color'])
        if self.has_input('segments'):
            artist.props['segments'] = self.get_input('segments')
        if self.has_input('linewidths'):
            artist.constructor_props['linewidths'] = self.get_input('linewidths')
        if self.has_input('colors'):
            artist.constructor_props['colors'] = self.get_input('colors')
        if self.has_input('cmap'):
            artist.constructor_props['cmap'] = self.get_input('cmap')
        if self.has_input('transOffset'):
            artist.constructor_props['transOffset'] = self.get_input('transOffset')
        if self.has_input('verts'):
            artist.props['verts'] = self.get_input('verts')
        if self.has_input('pickradius'):
            artist.constructor_props['pickradius'] = self.get_input('pickradius')
        if self.has_input('zorder'):
            artist.constructor_props['zorder'] = self.get_input('zorder')
        if self.has_input('norm'):
            artist.constructor_props['norm'] = self.get_input('norm')


class MplPatchCollectionProperties(MplCollectionProperties):
    """
    A generic collection of patches.

    This makes it easier to assign a color map to a heterogeneous
    collection of patches.

    This also may improve plotting speed, since PatchCollection will
    draw faster than a large number of patches.
    
    """
    _input_ports = [
              ("paths", "basic:String",
                {'optional': True}),
              ("patches", "basic:String",
                {'optional': True}),
              ("match_original", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplPatchCollectionProperties)")]

    class Artist(MplCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplPatchCollectionProperties.Artist()
            self.set_output("value", artist)

        MplCollectionProperties.compute(self, artist)
        if self.has_input('paths'):
            artist.props['paths'] = self.get_input('paths')
        if self.has_input('patches'):
            artist.constructor_props['patches'] = self.get_input('patches')
        if self.has_input('match_original'):
            artist.constructor_props['match_original'] = self.get_input('match_original')


class MplQuadMeshProperties(MplCollectionProperties):
    """
    Class for the efficient drawing of a quadrilateral mesh.

    A quadrilateral mesh consists of a grid of vertices. The
    dimensions of this array are (*meshWidth* + 1, *meshHeight* +
    1). Each vertex in the mesh has a different set of "mesh
    coordinates" representing its position in the topology of the
    mesh. For any values (*m*, *n*) such that 0 <= *m* <= *meshWidth*
    and 0 <= *n* <= *meshHeight*, the vertices at mesh coordinates
    (*m*, *n*), (*m*, *n* + 1), (*m* + 1, *n* + 1), and (*m* + 1, *n*)
    form one of the quadrilaterals in the mesh. There are thus
    (*meshWidth* * *meshHeight*) quadrilaterals in the mesh.  The mesh
    need not be regular and the polygons need not be convex.

    A quadrilateral mesh is represented by a (2 x ((*meshWidth* + 1) *
    (*meshHeight* + 1))) numpy array *coordinates*, where each row is
    the *x* and *y* coordinates of one of the vertices.  To define the
    function that maps from a data point to its corresponding color,
    use the :meth:`set_cmap` method.  Each of these arrays is indexed in
    row-major order by the mesh coordinates of the vertex (or the mesh
    coordinates of the lower left vertex, in the case of the
    colors).

    For example, the first entry in *coordinates* is the
    coordinates of the vertex at mesh coordinates (0, 0), then the one
    at (0, 1), then at (0, 2) .. (0, meshWidth), (1, 0), (1, 1), and
    so on.

    *shading* may be 'flat', or 'gouraud'
    
    """
    _input_ports = [
              ("meshWidth", "basic:String",
                {'optional': True}),
              ("meshHeight", "basic:String",
                {'optional': True}),
              ("antialiased", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("coordinates", "basic:String",
                {'optional': True}),
              ("shading", "basic:String",
                {'optional': True, 'defaults': "[u'flat']"}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplQuadMeshProperties)")]

    class Artist(MplCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplQuadMeshProperties.Artist()
            self.set_output("value", artist)

        MplCollectionProperties.compute(self, artist)
        if self.has_input('meshWidth'):
            artist.constructor_props['meshWidth'] = self.get_input('meshWidth')
        if self.has_input('meshHeight'):
            artist.constructor_props['meshHeight'] = self.get_input('meshHeight')
        if self.has_input('antialiased'):
            artist.constructor_props['antialiased'] = self.get_input('antialiased')
        if self.has_input('coordinates'):
            artist.constructor_props['coordinates'] = self.get_input('coordinates')
        if self.has_input('shading'):
            artist.constructor_props['shading'] = self.get_input('shading')


class MplTriMeshProperties(MplCollectionProperties):
    """
    Class for the efficient drawing of a triangular mesh using
    Gouraud shading.

    A triangular mesh is a :class:`~matplotlib.tri.Triangulation`
    object.
    
    """
    _input_ports = [
              ("triangulation", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplTriMeshProperties)")]

    class Artist(MplCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplTriMeshProperties.Artist()
            self.set_output("value", artist)

        MplCollectionProperties.compute(self, artist)
        if self.has_input('triangulation'):
            artist.constructor_props['triangulation'] = self.get_input('triangulation')


class Mpl_CollectionWithSizesProperties(MplCollectionProperties):
    """
    Base class for collections that have an array of sizes.
    
    """
    _input_ports = [
              ("edgecolors", "basic:String",
                {'optional': True}),
              ("antialiaseds", "basic:String",
                {'optional': True}),
              ("pickradius", "basic:Float",
                {'optional': True, 'defaults': '[5.0]'}),
              ("linestyles", "basic:String",
                {'optional': True, 'defaults': "[u'solid']"}),
              ("offsets", "basic:String",
                {'optional': True}),
              ("sizes", "basic:String",
                {'optional': True, 'docstring': "\n        Set the sizes of each member of the collection.\n\n        Parameters\n        ----------\n        sizes : ndarray or None\n            The size to set for each element of the collection.  The\n            value is the 'area' of the element.\n\n        dpi : float\n            The dpi of the canvas. Defaults to 72.0.\n        "}),
              ("offset_position", "basic:String",
                {'optional': True, 'defaults': "[u'screen']"}),
              ("linewidths", "basic:String",
                {'optional': True}),
              ("cmap", "basic:String",
                {'optional': True}),
              ("transOffset", "basic:String",
                {'optional': True}),
              ("urls", "basic:String",
                {'optional': True}),
              ("hatch", "basic:String",
                {'optional': True}),
              ("zorder", "basic:Integer",
                {'optional': True, 'defaults': '[1]'}),
              ("facecolors", "basic:String",
                {'optional': True}),
              ("norm", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(Mpl_CollectionWithSizesProperties)")]

    class Artist(MplCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = Mpl_CollectionWithSizesProperties.Artist()
            self.set_output("value", artist)

        MplCollectionProperties.compute(self, artist)
        if self.has_input('edgecolors'):
            artist.constructor_props['edgecolors'] = self.get_input('edgecolors')
        if self.has_input('antialiaseds'):
            artist.constructor_props['antialiaseds'] = self.get_input('antialiaseds')
        if self.has_input('pickradius'):
            artist.constructor_props['pickradius'] = self.get_input('pickradius')
        if self.has_input('linestyles'):
            artist.constructor_props['linestyles'] = self.get_input('linestyles')
        if self.has_input('offsets'):
            artist.constructor_props['offsets'] = self.get_input('offsets')
        if self.has_input('sizes'):
            artist.props['sizes'] = self.get_input('sizes')
        if self.has_input('offset_position'):
            artist.constructor_props['offset_position'] = self.get_input('offset_position')
        if self.has_input('linewidths'):
            artist.constructor_props['linewidths'] = self.get_input('linewidths')
        if self.has_input('cmap'):
            artist.constructor_props['cmap'] = self.get_input('cmap')
        if self.has_input('transOffset'):
            artist.constructor_props['transOffset'] = self.get_input('transOffset')
        if self.has_input('urls'):
            artist.constructor_props['urls'] = self.get_input('urls')
        if self.has_input('hatch'):
            artist.constructor_props['hatch'] = self.get_input('hatch')
        if self.has_input('zorder'):
            artist.constructor_props['zorder'] = self.get_input('zorder')
        if self.has_input('facecolors'):
            artist.constructor_props['facecolors'] = self.get_input('facecolors')
        if self.has_input('norm'):
            artist.constructor_props['norm'] = self.get_input('norm')


class MplArrowProperties(MplPatchProperties):
    """
    An arrow patch.
    
    """
    _input_ports = [
              ("y", "basic:String",
                {'optional': True}),
              ("x", "basic:String",
                {'optional': True}),
              ("dy", "basic:String",
                {'optional': True}),
              ("dx", "basic:String",
                {'optional': True}),
              ("width", "basic:Float",
                {'optional': True, 'defaults': '[1.0]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplArrowProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplArrowProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('y'):
            artist.constructor_props['y'] = self.get_input('y')
        if self.has_input('x'):
            artist.constructor_props['x'] = self.get_input('x')
        if self.has_input('dy'):
            artist.constructor_props['dy'] = self.get_input('dy')
        if self.has_input('dx'):
            artist.constructor_props['dx'] = self.get_input('dx')
        if self.has_input('width'):
            artist.constructor_props['width'] = self.get_input('width')


class MplEllipseProperties(MplPatchProperties):
    """
    A scale-free ellipse.
    
    """
    _input_ports = [
              ("width", "basic:String",
                {'optional': True}),
              ("xy", "basic:String",
                {'optional': True}),
              ("angle", "basic:Float",
                {'optional': True, 'defaults': '[0.0]'}),
              ("height", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplEllipseProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplEllipseProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('width'):
            artist.constructor_props['width'] = self.get_input('width')
        if self.has_input('xy'):
            artist.constructor_props['xy'] = self.get_input('xy')
        if self.has_input('angle'):
            artist.constructor_props['angle'] = self.get_input('angle')
        if self.has_input('height'):
            artist.constructor_props['height'] = self.get_input('height')


class MplFancyArrowPatchProperties(MplPatchProperties):
    """
    A fancy arrow patch. It draws an arrow using the :class:ArrowStyle.
    
    """
    _input_ports = [
              ("connectionstyle", "basic:String",
                {'optional': True, 'docstring': 'Set the connection style.\n\nOld attrs simply are forgotten.\n\nWithout argument (or with connectionstyle=None), return available styles as a list of strings.'}),
              ("mutation_scale", "basic:Float",
                {'optional': True, 'docstring': 'Set the mutation scale.'}),
              ("arrowstyle", "basic:String",
                {'optional': True, 'docstring': 'Set the arrow style.\n\nOld attrs simply are forgotten.\n\nWithout argument (or with arrowstyle=None), return available box styles as a list of strings.'}),
              ("arrow_transmuter", "basic:String",
                {'optional': True}),
              ("positions", "basic:String",
                {'optional': True}),
              ("shrinkA", "basic:Float",
                {'optional': True, 'defaults': '[2.0]'}),
              ("posB", "basic:String",
                {'optional': True}),
              ("dpi_cor", "basic:String",
                {'optional': True, 'docstring': 'dpi_cor is currently used for linewidth-related things and shink factor. Mutation scale is not affected by this.'}),
              ("connector", "basic:String",
                {'optional': True}),
              ("path", "basic:String",
                {'optional': True}),
              ("shrinkB", "basic:Float",
                {'optional': True, 'defaults': '[2.0]'}),
              ("mutation_aspect", "basic:Float",
                {'optional': True, 'docstring': 'Set the aspect ratio of the bbox mutation.'}),
              ("patchA", "basic:String",
                {'optional': True, 'docstring': 'set the begin patch.'}),
              ("patchB", "basic:String",
                {'optional': True, 'docstring': 'set the begin patch'}),
              ("posA", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplFancyArrowPatchProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplFancyArrowPatchProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('connectionstyle'):
            artist.props['connectionstyle'] = self.get_input('connectionstyle')
        if self.has_input('mutation_scale'):
            artist.props['mutation_scale'] = self.get_input('mutation_scale')
        if self.has_input('arrowstyle'):
            artist.props['arrowstyle'] = self.get_input('arrowstyle')
        if self.has_input('arrow_transmuter'):
            artist.constructor_props['arrow_transmuter'] = self.get_input('arrow_transmuter')
        if self.has_input('positions'):
            artist.props['positions'] = self.get_input('positions')
        if self.has_input('shrinkA'):
            artist.constructor_props['shrinkA'] = self.get_input('shrinkA')
        if self.has_input('posB'):
            artist.constructor_props['posB'] = self.get_input('posB')
        if self.has_input('dpi_cor'):
            artist.props['dpi_cor'] = self.get_input('dpi_cor')
        if self.has_input('connector'):
            artist.constructor_props['connector'] = self.get_input('connector')
        if self.has_input('path'):
            artist.constructor_props['path'] = self.get_input('path')
        if self.has_input('shrinkB'):
            artist.constructor_props['shrinkB'] = self.get_input('shrinkB')
        if self.has_input('mutation_aspect'):
            artist.props['mutation_aspect'] = self.get_input('mutation_aspect')
        if self.has_input('patchA'):
            artist.props['patchA'] = self.get_input('patchA')
        if self.has_input('patchB'):
            artist.props['patchB'] = self.get_input('patchB')
        if self.has_input('posA'):
            artist.constructor_props['posA'] = self.get_input('posA')


class MplFancyBboxPatchProperties(MplPatchProperties):
    """
    Draw a fancy box around a rectangle with lower left at *xy*=(*x*,
    *y*) with specified width and height.

    :class:`FancyBboxPatch` class is similar to :class:`Rectangle`
    class, but it draws a fancy box around the rectangle. The
    transformation of the rectangle box to the fancy box is delegated
    to the :class:`BoxTransmuterBase` and its derived classes.

    
    """
    _input_ports = [
              ("mutation_scale", "basic:Float",
                {'optional': True, 'docstring': 'Set the mutation scale.'}),
              ("bbox_transmuter", "basic:String",
                {'optional': True}),
              ("height", "basic:Float",
                {'optional': True, 'docstring': 'Set the width rectangle'}),
              ("width", "basic:Float",
                {'optional': True, 'docstring': 'Set the width rectangle'}),
              ("xy", "basic:String",
                {'optional': True}),
              ("boxstyle", "basic:String",
                {'optional': True, 'docstring': 'Set the box style.\n\nboxstyle can be a string with boxstyle name with optional comma-separated attributes. Alternatively, the attrs can be provided as keywords:\n\nset_boxstyle("round,pad=0.2") set_boxstyle("round", pad=0.2)\n\nOld attrs simply are forgotten.\n\nWithout argument (or with boxstyle = None), it returns available box styles.'}),
              ("mutation_aspect", "basic:Float",
                {'optional': True, 'docstring': 'Set the aspect ratio of the bbox mutation.'}),
              ("y", "basic:Float",
                {'optional': True, 'docstring': 'Set the bottom coord of the rectangle'}),
              ("x", "basic:Float",
                {'optional': True, 'docstring': 'Set the left coord of the rectangle'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplFancyBboxPatchProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplFancyBboxPatchProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('mutation_scale'):
            artist.props['mutation_scale'] = self.get_input('mutation_scale')
        if self.has_input('bbox_transmuter'):
            artist.constructor_props['bbox_transmuter'] = self.get_input('bbox_transmuter')
        if self.has_input('height'):
            artist.props['height'] = self.get_input('height')
        if self.has_input('width'):
            artist.props['width'] = self.get_input('width')
        if self.has_input('xy'):
            artist.constructor_props['xy'] = self.get_input('xy')
        if self.has_input('boxstyle'):
            artist.props['boxstyle'] = self.get_input('boxstyle')
        if self.has_input('mutation_aspect'):
            artist.props['mutation_aspect'] = self.get_input('mutation_aspect')
        if self.has_input('y'):
            artist.props['y'] = self.get_input('y')
        if self.has_input('x'):
            artist.props['x'] = self.get_input('x')


class MplPathPatchProperties(MplPatchProperties):
    """
    A general polycurve path patch.
    
    """
    _input_ports = [
              ("path", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplPathPatchProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplPathPatchProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('path'):
            artist.constructor_props['path'] = self.get_input('path')


class MplPolygonProperties(MplPatchProperties):
    """
    A general polygon patch.
    
    """
    _input_ports = [
              ("xy", "basic:String",
                {'optional': True, 'docstring': '\n        Set the vertices of the polygon\n\n        Parameters\n        ----------\n        xy : numpy array or iterable of pairs\n            The coordinates of the vertices as a Nx2\n            ndarray or iterable of pairs.\n        '}),
              ("closed", "basic:String",
                {'optional': True, 'docstring': '\n        Set if the polygon is closed\n\n        Parameters\n        ----------\n        closed : bool\n           True if the polygon is closed\n        '}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplPolygonProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplPolygonProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('xy'):
            artist.props['xy'] = self.get_input('xy')
        if self.has_input('closed'):
            artist.props['closed'] = self.get_input('closed')


class MplRectangleProperties(MplPatchProperties):
    """
    Draw a rectangle with lower left at *xy* = (*x*, *y*) with
    specified *width* and *height*.
    
    """
    _input_ports = [
              ("angle", "basic:Float",
                {'optional': True, 'defaults': '[0.0]'}),
              ("height", "basic:Float",
                {'optional': True, 'docstring': 'Set the width rectangle'}),
              ("width", "basic:Float",
                {'optional': True, 'docstring': 'Set the width rectangle'}),
              ("xy", "basic:List",
                {'optional': True, 'docstring': 'Set the left and bottom coords of the rectangle'}),
              ("y", "basic:Float",
                {'optional': True, 'docstring': 'Set the bottom coord of the rectangle'}),
              ("x", "basic:Float",
                {'optional': True, 'docstring': 'Set the left coord of the rectangle'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplRectangleProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplRectangleProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('angle'):
            artist.constructor_props['angle'] = self.get_input('angle')
        if self.has_input('height'):
            artist.props['height'] = self.get_input('height')
        if self.has_input('width'):
            artist.props['width'] = self.get_input('width')
        if self.has_input('xy'):
            artist.props['xy'] = self.get_input('xy')
        if self.has_input('y'):
            artist.props['y'] = self.get_input('y')
        if self.has_input('x'):
            artist.props['x'] = self.get_input('x')


class MplRegularPolygonProperties(MplPatchProperties):
    """
    A regular polygon patch.
    
    """
    _input_ports = [
              ("xy", "basic:Float,basic:Float",
                {'optional': True, 'docstring': 'A length 2 tuple (x, y) of the center.'}),
              ("radius", "basic:Integer",
                {'optional': True, 'docstring': 'The distance from the center to each of the vertices.', 'defaults': '[5]'}),
              ("orientation", "basic:Integer",
                {'optional': True, 'docstring': 'rotates the polygon (in radians).', 'defaults': '[0]'}),
              ("numVertices", "basic:String",
                {'optional': True, 'docstring': 'the number of vertices.'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplRegularPolygonProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplRegularPolygonProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('xy'):
            artist.constructor_props['xy'] = self.get_input('xy')
        if self.has_input('radius'):
            artist.constructor_props['radius'] = self.get_input('radius')
        if self.has_input('orientation'):
            artist.constructor_props['orientation'] = self.get_input('orientation')
        if self.has_input('numVertices'):
            artist.constructor_props['numVertices'] = self.get_input('numVertices')


class MplShadowProperties(MplPatchProperties):
    """None
    """
    _input_ports = [
              ("patch", "basic:String",
                {'optional': True}),
              ("props", "basic:String",
                {'optional': True}),
              ("oy", "basic:String",
                {'optional': True}),
              ("ox", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplShadowProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplShadowProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('patch'):
            artist.constructor_props['patch'] = self.get_input('patch')
        if self.has_input('props'):
            artist.constructor_props['props'] = self.get_input('props')
        if self.has_input('oy'):
            artist.constructor_props['oy'] = self.get_input('oy')
        if self.has_input('ox'):
            artist.constructor_props['ox'] = self.get_input('ox')


class MplWedgeProperties(MplPatchProperties):
    """
    Wedge shaped patch.
    
    """
    _input_ports = [
              ("theta2", "basic:String",
                {'optional': True}),
              ("theta1", "basic:String",
                {'optional': True}),
              ("center", "basic:String",
                {'optional': True}),
              ("width", "basic:String",
                {'optional': True}),
              ("r", "basic:String",
                {'optional': True}),
              ("radius", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplWedgeProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplWedgeProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('theta2'):
            artist.props['theta2'] = self.get_input('theta2')
        if self.has_input('theta1'):
            artist.props['theta1'] = self.get_input('theta1')
        if self.has_input('center'):
            artist.props['center'] = self.get_input('center')
        if self.has_input('width'):
            artist.props['width'] = self.get_input('width')
        if self.has_input('r'):
            artist.constructor_props['r'] = self.get_input('r')
        if self.has_input('radius'):
            artist.props['radius'] = self.get_input('radius')


class MplYAArrowProperties(MplPatchProperties):
    """
    Yet another arrow class.

    This is an arrow that is defined in display space and has a tip at
    *x1*, *y1* and a base at *x2*, *y2*.
    
    """
    _input_ports = [
              ("xytip", "basic:Float,basic:Float",
                {'optional': True, 'docstring': '(x, y) location of arrow tip'}),
              ("headwidth", "basic:Integer",
                {'optional': True, 'docstring': 'The width of the base of the arrow head in points', 'defaults': '[12]'}),
              ("frac", "basic:Float",
                {'optional': True, 'docstring': 'The fraction of the arrow length occupied by the head', 'defaults': '[0.1]'}),
              ("figure", "basic:String",
                {'optional': True, 'docstring': 'The :class:`~matplotlib.figure.Figure` instance (fig.dpi)'}),
              ("xybase", "basic:Float,basic:Float",
                {'optional': True, 'docstring': '(x, y) location the arrow base mid point'}),
              ("width", "basic:Integer",
                {'optional': True, 'docstring': 'The width of the arrow in points', 'defaults': '[4]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplYAArrowProperties)")]

    class Artist(MplPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplYAArrowProperties.Artist()
            self.set_output("value", artist)

        MplPatchProperties.compute(self, artist)
        if self.has_input('xytip'):
            artist.constructor_props['xytip'] = self.get_input('xytip')
        if self.has_input('headwidth'):
            artist.constructor_props['headwidth'] = self.get_input('headwidth')
        if self.has_input('frac'):
            artist.constructor_props['frac'] = self.get_input('frac')
        if self.has_input('figure'):
            artist.constructor_props['figure'] = self.get_input('figure')
        if self.has_input('xybase'):
            artist.constructor_props['xybase'] = self.get_input('xybase')
        if self.has_input('width'):
            artist.constructor_props['width'] = self.get_input('width')


class MplAnnotationProperties(MplTextProperties):
    """
    A :class:`~matplotlib.text.Text` class to make annotating things
    in the figure, such as :class:`~matplotlib.figure.Figure`,
    :class:`~matplotlib.axes.Axes`,
    :class:`~matplotlib.patches.Rectangle`, etc., easier.

    Annotate the *x*, *y* point *xy* with text *s* at *x*, *y*
    location *xytext*.  (If *xytext* = *None*, defaults to *xy*,
    and if *textcoords* = *None*, defaults to *xycoords*).
    
    """
    _input_ports = [
              ("xycoords", "basic:String",
                {'entry_types': "['enum']", 'values': "[['figure points', 'figure pixels', 'figure fraction', 'axes points', 'axes pixels', 'axes fraction', 'data', 'offset points', 'polar']]", 'optional': True, 'defaults': "[u'data']"}),
              ("figure", "basic:String",
                {'optional': True}),
              ("annotation_clip", "basic:String",
                {'optional': True}),
              ("xytext", "basic:String",
                {'optional': True}),
              ("s", "basic:String",
                {'optional': True}),
              ("xy", "basic:String",
                {'optional': True}),
              ("textcoords", "basic:String",
                {'entry_types': "['enum']", 'values': "[['figure points', 'figure pixels', 'figure fraction', 'axes points', 'axes pixels', 'axes fraction', 'data', 'offset points', 'polar']]", 'optional': True}),
              ("arrowprops", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplAnnotationProperties)")]

    class Artist(MplTextProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplTextProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplAnnotationProperties.Artist()
            self.set_output("value", artist)

        MplTextProperties.compute(self, artist)
        if self.has_input('xycoords'):
            artist.constructor_props['xycoords'] = self.get_input('xycoords')
        if self.has_input('figure'):
            artist.props['figure'] = self.get_input('figure')
        if self.has_input('annotation_clip'):
            artist.constructor_props['annotation_clip'] = self.get_input('annotation_clip')
        if self.has_input('xytext'):
            artist.constructor_props['xytext'] = self.get_input('xytext')
        if self.has_input('s'):
            artist.constructor_props['s'] = self.get_input('s')
        if self.has_input('xy'):
            artist.constructor_props['xy'] = self.get_input('xy')
        if self.has_input('textcoords'):
            artist.constructor_props['textcoords'] = self.get_input('textcoords')
        if self.has_input('arrowprops'):
            artist.constructor_props['arrowprops'] = self.get_input('arrowprops')


class MplTextWithDashProperties(MplTextProperties):
    """
    This is basically a :class:`~matplotlib.text.Text` with a dash
    (drawn with a :class:`~matplotlib.lines.Line2D`) before/after
    it. It is intended to be a drop-in replacement for
    :class:`~matplotlib.text.Text`, and should behave identically to
    it when *dashlength* = 0.0.

    The dash always comes between the point specified by
    :meth:`~matplotlib.text.Text.set_position` and the text. When a
    dash exists, the text alignment arguments (*horizontalalignment*,
    *verticalalignment*) are ignored.

    *dashlength* is the length of the dash in canvas units.
    (default = 0.0).

    *dashdirection* is one of 0 or 1, where 0 draws the dash after the
    text and 1 before.  (default = 0).

    *dashrotation* specifies the rotation of the dash, and should
    generally stay *None*. In this case
    :meth:`~matplotlib.text.TextWithDash.get_dashrotation` returns
    :meth:`~matplotlib.text.Text.get_rotation`.  (i.e., the dash takes
    its rotation from the text's rotation). Because the text center is
    projected onto the dash, major deviations in the rotation cause
    what may be considered visually unappealing results.
    (default = *None*)

    *dashpad* is a padding length to add (or subtract) space
    between the text and the dash, in canvas units.
    (default = 3)

    *dashpush* "pushes" the dash and text away from the point
    specified by :meth:`~matplotlib.text.Text.set_position` by the
    amount in canvas units.  (default = 0)

    .. note::

        The alignment of the two objects is based on the bounding box
        of the :class:`~matplotlib.text.Text`, as obtained by
        :meth:`~matplotlib.artist.Artist.get_window_extent`.  This, in
        turn, appears to depend on the font metrics as given by the
        rendering backend. Hence the quality of the "centering" of the
        label text with respect to the dash varies depending on the
        backend used.

    .. note::

        I'm not sure that I got the
        :meth:`~matplotlib.text.TextWithDash.get_window_extent` right,
        or whether that's sufficient for providing the object bounding
        box.

    
    """
    _input_ports = [
              ("dashpush", "basic:Float",
                {'optional': True, 'docstring': 'Set the "push" of the TextWithDash, which is the extra spacing between the beginning of the dash and the specified position.'}),
              ("dashdirection", "basic:String",
                {'optional': True, 'docstring': "Set the direction of the dash following the text. 1 is before the text and 0 is after. The default is 0, which is what you'd want for the typical case of ticks below and on the left of the figure."}),
              ("linespacing", "basic:String",
                {'optional': True}),
              ("figure", "basic:String",
                {'optional': True, 'docstring': 'Set the figure instance the artist belong to.'}),
              ("color", "basic:String",
                {'optional': True}),
              ("text", "basic:String",
                {'optional': True, 'defaults': "[u'']"}),
              ("verticalalignment", "basic:String",
                {'optional': True, 'defaults': "[u'center']"}),
              ("dashpad", "basic:Float",
                {'optional': True, 'docstring': 'Set the "pad" of the TextWithDash, which is the extra spacing between the dash and the text, in canvas units.'}),
              ("dashrotation", "basic:Float",
                {'optional': True, 'docstring': 'Set the rotation of the dash, in degrees'}),
              ("transform", "basic:String",
                {'optional': True, 'docstring': 'Set the :class:`matplotlib.transforms.Transform` instance used by this artist.'}),
              ("fontproperties", "basic:String",
                {'optional': True}),
              ("multialignment", "basic:String",
                {'optional': True}),
              ("x", "basic:Float",
                {'optional': True, 'docstring': 'Set the x position of the :class:`TextWithDash`.'}),
              ("y", "basic:Float",
                {'optional': True, 'docstring': 'Set the y position of the :class:`TextWithDash`.'}),
              ("position", "basic:Float,basic:Float",
                {'optional': True, 'docstring': 'Set the (x, y) position of the :class:`TextWithDash`.'}),
              ("dashlength", "basic:Float",
                {'optional': True, 'docstring': 'Set the length of the dash.'}),
              ("rotation", "basic:String",
                {'optional': True}),
              ("horizontalalignment", "basic:String",
                {'optional': True, 'defaults': "[u'center']"}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplTextWithDashProperties)")]

    class Artist(MplTextProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplTextProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplTextWithDashProperties.Artist()
            self.set_output("value", artist)

        MplTextProperties.compute(self, artist)
        if self.has_input('dashpush'):
            artist.props['dashpush'] = self.get_input('dashpush')
        if self.has_input('dashdirection'):
            artist.props['dashdirection'] = self.get_input('dashdirection')
        if self.has_input('linespacing'):
            artist.constructor_props['linespacing'] = self.get_input('linespacing')
        if self.has_input('figure'):
            artist.props['figure'] = self.get_input('figure')
        if self.has_input('color'):
            artist.constructor_props['color'] = self.get_input('color')
        if self.has_input('text'):
            artist.constructor_props['text'] = self.get_input('text')
        if self.has_input('verticalalignment'):
            artist.constructor_props['verticalalignment'] = self.get_input('verticalalignment')
        if self.has_input('dashpad'):
            artist.props['dashpad'] = self.get_input('dashpad')
        if self.has_input('dashrotation'):
            artist.props['dashrotation'] = self.get_input('dashrotation')
        if self.has_input('transform'):
            artist.props['transform'] = self.get_input('transform')
        if self.has_input('fontproperties'):
            artist.constructor_props['fontproperties'] = self.get_input('fontproperties')
        if self.has_input('multialignment'):
            artist.constructor_props['multialignment'] = self.get_input('multialignment')
        if self.has_input('x'):
            artist.props['x'] = self.get_input('x')
        if self.has_input('y'):
            artist.props['y'] = self.get_input('y')
        if self.has_input('position'):
            artist.props['position'] = self.get_input('position')
        if self.has_input('dashlength'):
            artist.props['dashlength'] = self.get_input('dashlength')
        if self.has_input('rotation'):
            artist.constructor_props['rotation'] = self.get_input('rotation')
        if self.has_input('horizontalalignment'):
            artist.constructor_props['horizontalalignment'] = self.get_input('horizontalalignment')


class MplXTickProperties(MplTickProperties):
    """
    Contains all the Artists needed to make an x tick - the tick line,
    the label text and the grid line
    
    """
    _input_ports = [
              ("label1On", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("loc", "basic:String",
                {'optional': True}),
              ("major", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("label2On", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
              ("color", "basic:String",
                {'optional': True}),
              ("axes", "basic:String",
                {'optional': True}),
              ("label", "basic:String",
                {'optional': True}),
              ("labelcolor", "basic:String",
                {'optional': True}),
              ("tickdir", "basic:String",
                {'optional': True}),
              ("pad", "basic:String",
                {'optional': True}),
              ("gridOn", "basic:String",
                {'optional': True}),
              ("zorder", "basic:String",
                {'optional': True}),
              ("tick2On", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("labelsize", "basic:String",
                {'optional': True}),
              ("width", "basic:String",
                {'optional': True}),
              ("tick1On", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("size", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplXTickProperties)")]

    class Artist(MplTickProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplTickProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplXTickProperties.Artist()
            self.set_output("value", artist)

        MplTickProperties.compute(self, artist)
        if self.has_input('label1On'):
            artist.constructor_props['label1On'] = self.get_input('label1On')
        if self.has_input('loc'):
            artist.constructor_props['loc'] = self.get_input('loc')
        if self.has_input('major'):
            artist.constructor_props['major'] = self.get_input('major')
        if self.has_input('label2On'):
            artist.constructor_props['label2On'] = self.get_input('label2On')
        if self.has_input('color'):
            artist.constructor_props['color'] = self.get_input('color')
        if self.has_input('axes'):
            artist.constructor_props['axes'] = self.get_input('axes')
        if self.has_input('label'):
            artist.constructor_props['label'] = self.get_input('label')
        if self.has_input('labelcolor'):
            artist.constructor_props['labelcolor'] = self.get_input('labelcolor')
        if self.has_input('tickdir'):
            artist.constructor_props['tickdir'] = self.get_input('tickdir')
        if self.has_input('pad'):
            artist.constructor_props['pad'] = self.get_input('pad')
        if self.has_input('gridOn'):
            artist.constructor_props['gridOn'] = self.get_input('gridOn')
        if self.has_input('zorder'):
            artist.constructor_props['zorder'] = self.get_input('zorder')
        if self.has_input('tick2On'):
            artist.constructor_props['tick2On'] = self.get_input('tick2On')
        if self.has_input('labelsize'):
            artist.constructor_props['labelsize'] = self.get_input('labelsize')
        if self.has_input('width'):
            artist.constructor_props['width'] = self.get_input('width')
        if self.has_input('tick1On'):
            artist.constructor_props['tick1On'] = self.get_input('tick1On')
        if self.has_input('size'):
            artist.constructor_props['size'] = self.get_input('size')


class MplYTickProperties(MplTickProperties):
    """
    Contains all the Artists needed to make a Y tick - the tick line,
    the label text and the grid line
    
    """
    _input_ports = [
              ("label1On", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("loc", "basic:String",
                {'optional': True}),
              ("major", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("label2On", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
              ("color", "basic:String",
                {'optional': True}),
              ("axes", "basic:String",
                {'optional': True}),
              ("label", "basic:String",
                {'optional': True}),
              ("labelcolor", "basic:String",
                {'optional': True}),
              ("tickdir", "basic:String",
                {'optional': True}),
              ("pad", "basic:String",
                {'optional': True}),
              ("gridOn", "basic:String",
                {'optional': True}),
              ("zorder", "basic:String",
                {'optional': True}),
              ("tick2On", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("labelsize", "basic:String",
                {'optional': True}),
              ("width", "basic:String",
                {'optional': True}),
              ("tick1On", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("size", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplYTickProperties)")]

    class Artist(MplTickProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplTickProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplYTickProperties.Artist()
            self.set_output("value", artist)

        MplTickProperties.compute(self, artist)
        if self.has_input('label1On'):
            artist.constructor_props['label1On'] = self.get_input('label1On')
        if self.has_input('loc'):
            artist.constructor_props['loc'] = self.get_input('loc')
        if self.has_input('major'):
            artist.constructor_props['major'] = self.get_input('major')
        if self.has_input('label2On'):
            artist.constructor_props['label2On'] = self.get_input('label2On')
        if self.has_input('color'):
            artist.constructor_props['color'] = self.get_input('color')
        if self.has_input('axes'):
            artist.constructor_props['axes'] = self.get_input('axes')
        if self.has_input('label'):
            artist.constructor_props['label'] = self.get_input('label')
        if self.has_input('labelcolor'):
            artist.constructor_props['labelcolor'] = self.get_input('labelcolor')
        if self.has_input('tickdir'):
            artist.constructor_props['tickdir'] = self.get_input('tickdir')
        if self.has_input('pad'):
            artist.constructor_props['pad'] = self.get_input('pad')
        if self.has_input('gridOn'):
            artist.constructor_props['gridOn'] = self.get_input('gridOn')
        if self.has_input('zorder'):
            artist.constructor_props['zorder'] = self.get_input('zorder')
        if self.has_input('tick2On'):
            artist.constructor_props['tick2On'] = self.get_input('tick2On')
        if self.has_input('labelsize'):
            artist.constructor_props['labelsize'] = self.get_input('labelsize')
        if self.has_input('width'):
            artist.constructor_props['width'] = self.get_input('width')
        if self.has_input('tick1On'):
            artist.constructor_props['tick1On'] = self.get_input('tick1On')
        if self.has_input('size'):
            artist.constructor_props['size'] = self.get_input('size')


class MplAxesProperties(Mpl_AxesBaseProperties):
    """
    The :class:`Axes` contains most of the figure elements:
    :class:`~matplotlib.axis.Axis`, :class:`~matplotlib.axis.Tick`,
    :class:`~matplotlib.lines.Line2D`, :class:`~matplotlib.text.Text`,
    :class:`~matplotlib.patches.Polygon`, etc., and sets the
    coordinate system.

    The :class:`Axes` instance supports callbacks through a callbacks
    attribute which is a :class:`~matplotlib.cbook.CallbackRegistry`
    instance.  The events you can connect to are 'xlim_changed' and
    'ylim_changed' and the callback will be called with func(*ax*)
    where *ax* is the :class:`Axes` instance.
    
    """
    _input_ports = [
              ("sharey", "basic:String",
                {'optional': True}),
              ("sharex", "basic:String",
                {'optional': True}),
              ("yscale", "basic:String",
                {'optional': True}),
              ("title", "basic:String",
                {'optional': True, 'docstring': "Set a title for the axes.\n\nSet one of the three available axes titles. The available titles\nare positioned above the axes in the center, flush with the left\nedge, and flush with the right edge.\n\nParameters\n----------\nlabel : str\n    Text to use for the title\n\nfontdict : dict\n    A dictionary controlling the appearance of the title text,\n    the default `fontdict` is::\n\n       {'fontsize': rcParams['axes.titlesize'],\n        'fontweight' : rcParams['axes.titleweight'],\n        'verticalalignment': 'baseline',\n        'horizontalalignment': loc}\n\nloc : {'center', 'left', 'right'}, str, optional\n    Which title to set, defaults to 'center'\n\nReturns\n-------\ntext : :class:`~matplotlib.text.Text`\n    The matplotlib text instance representing the title\n\nOther parameters\n----------------\nkwargs : text properties\n    Other keyword arguments are text properties, see\n    :class:`~matplotlib.text.Text` for a list of valid text\n    properties."}),
              ("frameon", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("axisbg", "basic:String",
                {'optional': True}),
              ("xlabel", "basic:String",
                {'optional': True, 'docstring': 'Set the label for the xaxis.\n\nParameters\n----------\nxlabel : string\n    x label\n\nlabelpad : scalar, optional, default: None\n    spacing in points between the label and the x-axis\n\nOther parameters\n----------------\nkwargs : `~matplotlib.text.Text` properties\n\nSee also\n--------\ntext : for information on how override and the optional args work'}),
              ("fig", "basic:String",
                {'optional': True}),
              ("ylabel", "basic:String",
                {'optional': True, 'docstring': 'Set the label for the yaxis\n\nParameters\n----------\nylabel : string\n    y label\n\nlabelpad : scalar, optional, default: None\n    spacing in points between the label and the x-axis\n\nOther parameters\n----------------\nkwargs : `~matplotlib.text.Text` properties\n\nSee also\n--------\ntext : for information on how override and the optional args work'}),
              ("xscale", "basic:String",
                {'optional': True}),
              ("label", "basic:String",
                {'optional': True, 'defaults': "[u'']"}),
              ("rect", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplAxesProperties)")]

    class Artist(Mpl_AxesBaseProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            Mpl_AxesBaseProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplAxesProperties.Artist()
            self.set_output("value", artist)

        Mpl_AxesBaseProperties.compute(self, artist)
        if self.has_input('sharey'):
            artist.constructor_props['sharey'] = self.get_input('sharey')
        if self.has_input('sharex'):
            artist.constructor_props['sharex'] = self.get_input('sharex')
        if self.has_input('yscale'):
            artist.constructor_props['yscale'] = self.get_input('yscale')
        if self.has_input('title'):
            artist.props['title'] = self.get_input('title')
        if self.has_input('frameon'):
            artist.constructor_props['frameon'] = self.get_input('frameon')
        if self.has_input('axisbg'):
            artist.constructor_props['axisbg'] = self.get_input('axisbg')
        if self.has_input('xlabel'):
            artist.props['xlabel'] = self.get_input('xlabel')
        if self.has_input('fig'):
            artist.constructor_props['fig'] = self.get_input('fig')
        if self.has_input('ylabel'):
            artist.props['ylabel'] = self.get_input('ylabel')
        if self.has_input('xscale'):
            artist.constructor_props['xscale'] = self.get_input('xscale')
        if self.has_input('label'):
            artist.constructor_props['label'] = self.get_input('label')
        if self.has_input('rect'):
            artist.constructor_props['rect'] = self.get_input('rect')


class MplAxesImageProperties(Mpl_AxesImageBaseProperties):
    """None
    """
    _input_ports = [
              ("origin", "basic:String",
                {'optional': True}),
              ("resample", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
              ("norm", "basic:String",
                {'optional': True}),
              ("cmap", "basic:String",
                {'optional': True}),
              ("filterrad", "basic:Float",
                {'optional': True, 'defaults': '[4.0]'}),
              ("extent", "basic:String",
                {'optional': True, 'docstring': 'extent is data axes (left, right, bottom, top) for making image plots\n\nThis updates ax.dataLim, and, if autoscaling, sets viewLim to tightly fit the image, regardless of dataLim.  Autoscaling state is not changed, so following this with ax.autoscale_view will redo the autoscaling in accord with dataLim.'}),
              ("ax", "basic:String",
                {'optional': True}),
              ("filternorm", "basic:Integer",
                {'optional': True, 'defaults': '[1]'}),
              ("interpolation", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplAxesImageProperties)")]

    class Artist(Mpl_AxesImageBaseProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            Mpl_AxesImageBaseProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplAxesImageProperties.Artist()
            self.set_output("value", artist)

        Mpl_AxesImageBaseProperties.compute(self, artist)
        if self.has_input('origin'):
            artist.constructor_props['origin'] = self.get_input('origin')
        if self.has_input('resample'):
            artist.constructor_props['resample'] = self.get_input('resample')
        if self.has_input('norm'):
            artist.constructor_props['norm'] = self.get_input('norm')
        if self.has_input('cmap'):
            artist.constructor_props['cmap'] = self.get_input('cmap')
        if self.has_input('filterrad'):
            artist.constructor_props['filterrad'] = self.get_input('filterrad')
        if self.has_input('extent'):
            artist.props['extent'] = self.get_input('extent')
        if self.has_input('ax'):
            artist.constructor_props['ax'] = self.get_input('ax')
        if self.has_input('filternorm'):
            artist.constructor_props['filternorm'] = self.get_input('filternorm')
        if self.has_input('interpolation'):
            artist.constructor_props['interpolation'] = self.get_input('interpolation')


class MplBboxImageProperties(Mpl_AxesImageBaseProperties):
    """The Image class whose size is determined by the given bbox.
    """
    _input_ports = [
              ("origin", "basic:String",
                {'optional': True}),
              ("interp_at_native", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("resample", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
              ("cmap", "basic:String",
                {'optional': True}),
              ("filternorm", "basic:Integer",
                {'optional': True, 'defaults': '[1]'}),
              ("norm", "basic:String",
                {'optional': True}),
              ("interpolation", "basic:String",
                {'optional': True}),
              ("filterrad", "basic:Float",
                {'optional': True, 'defaults': '[4.0]'}),
              ("bbox", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplBboxImageProperties)")]

    class Artist(Mpl_AxesImageBaseProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            Mpl_AxesImageBaseProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplBboxImageProperties.Artist()
            self.set_output("value", artist)

        Mpl_AxesImageBaseProperties.compute(self, artist)
        if self.has_input('origin'):
            artist.constructor_props['origin'] = self.get_input('origin')
        if self.has_input('interp_at_native'):
            artist.constructor_props['interp_at_native'] = self.get_input('interp_at_native')
        if self.has_input('resample'):
            artist.constructor_props['resample'] = self.get_input('resample')
        if self.has_input('cmap'):
            artist.constructor_props['cmap'] = self.get_input('cmap')
        if self.has_input('filternorm'):
            artist.constructor_props['filternorm'] = self.get_input('filternorm')
        if self.has_input('norm'):
            artist.constructor_props['norm'] = self.get_input('norm')
        if self.has_input('interpolation'):
            artist.constructor_props['interpolation'] = self.get_input('interpolation')
        if self.has_input('filterrad'):
            artist.constructor_props['filterrad'] = self.get_input('filterrad')
        if self.has_input('bbox'):
            artist.constructor_props['bbox'] = self.get_input('bbox')


class MplEventCollectionProperties(MplLineCollectionProperties):
    """
    A collection of discrete events.

    An event is a 1-dimensional value, usually the position of something along
    an axis, such as time or length.  Events do not have an amplitude.  They
    are displayed as v
    
    """
    _input_ports = [
              ("linelength", "basic:String",
                {'optional': True, 'docstring': 'set the length of the lines used to mark each event'}),
              ("orientation", "basic:String",
                {'optional': True, 'docstring': "set the orientation of the event line [ 'horizontal' | 'vertical' | None ] defaults to 'horizontal' if not specified or None"}),
              ("color", "basic:String",
                {'optional': True}),
              ("positions", "basic:String",
                {'optional': True, 'docstring': 'set the positions of the events to the specified value'}),
              ("antialiased", "basic:String",
                {'optional': True}),
              ("lineoffset", "basic:String",
                {'optional': True, 'docstring': 'set the offset of the lines used to mark each event'}),
              ("linewidth", "basic:String",
                {'optional': True}),
              ("linestyle", "basic:String",
                {'optional': True, 'defaults': "[u'solid']"}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplEventCollectionProperties)")]

    class Artist(MplLineCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplLineCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplEventCollectionProperties.Artist()
            self.set_output("value", artist)

        MplLineCollectionProperties.compute(self, artist)
        if self.has_input('linelength'):
            artist.props['linelength'] = self.get_input('linelength')
        if self.has_input('orientation'):
            artist.props['orientation'] = self.get_input('orientation')
        if self.has_input('color'):
            artist.constructor_props['color'] = self.get_input('color')
        if self.has_input('positions'):
            artist.props['positions'] = self.get_input('positions')
        if self.has_input('antialiased'):
            artist.constructor_props['antialiased'] = self.get_input('antialiased')
        if self.has_input('lineoffset'):
            artist.props['lineoffset'] = self.get_input('lineoffset')
        if self.has_input('linewidth'):
            artist.constructor_props['linewidth'] = self.get_input('linewidth')
        if self.has_input('linestyle'):
            artist.constructor_props['linestyle'] = self.get_input('linestyle')


class MplCircleCollectionProperties(Mpl_CollectionWithSizesProperties):
    """
    A collection of circles, drawn using splines.
    
    """
    _input_ports = [
              ("sizes", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplCircleCollectionProperties)")]

    class Artist(Mpl_CollectionWithSizesProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            Mpl_CollectionWithSizesProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplCircleCollectionProperties.Artist()
            self.set_output("value", artist)

        Mpl_CollectionWithSizesProperties.compute(self, artist)
        if self.has_input('sizes'):
            artist.constructor_props['sizes'] = self.get_input('sizes')


class MplPathCollectionProperties(Mpl_CollectionWithSizesProperties):
    """
    This is the most basic :class:`Collection` subclass.
    
    """
    _input_ports = [
              ("paths", "basic:String",
                {'optional': True}),
              ("sizes", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplPathCollectionProperties)")]

    class Artist(Mpl_CollectionWithSizesProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            Mpl_CollectionWithSizesProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplPathCollectionProperties.Artist()
            self.set_output("value", artist)

        Mpl_CollectionWithSizesProperties.compute(self, artist)
        if self.has_input('paths'):
            artist.props['paths'] = self.get_input('paths')
        if self.has_input('sizes'):
            artist.constructor_props['sizes'] = self.get_input('sizes')


class MplPolyCollectionProperties(Mpl_CollectionWithSizesProperties):
    """None
    """
    _input_ports = [
              ("paths", "basic:String",
                {'optional': True, 'docstring': 'This allows one to delay initialization of the vertices.'}),
              ("verts", "basic:String",
                {'optional': True, 'docstring': 'This allows one to delay initialization of the vertices.'}),
              ("closed", "basic:Boolean",
                {'optional': True, 'defaults': '[True]'}),
              ("sizes", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplPolyCollectionProperties)")]

    class Artist(Mpl_CollectionWithSizesProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            Mpl_CollectionWithSizesProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplPolyCollectionProperties.Artist()
            self.set_output("value", artist)

        Mpl_CollectionWithSizesProperties.compute(self, artist)
        if self.has_input('paths'):
            artist.props['paths'] = self.get_input('paths')
        if self.has_input('verts'):
            artist.props['verts'] = self.get_input('verts')
        if self.has_input('closed'):
            artist.constructor_props['closed'] = self.get_input('closed')
        if self.has_input('sizes'):
            artist.constructor_props['sizes'] = self.get_input('sizes')


class MplRegularPolyCollectionProperties(Mpl_CollectionWithSizesProperties):
    """Draw a collection of regular polygons with *numsides*.
    """
    _input_ports = [
              ("numsides", "basic:String",
                {'optional': True}),
              ("rotation", "basic:Integer",
                {'optional': True, 'defaults': '[0]'}),
              ("sizes", "basic:String",
                {'optional': True, 'defaults': '[(1,)]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplRegularPolyCollectionProperties)")]

    class Artist(Mpl_CollectionWithSizesProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            Mpl_CollectionWithSizesProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplRegularPolyCollectionProperties.Artist()
            self.set_output("value", artist)

        Mpl_CollectionWithSizesProperties.compute(self, artist)
        if self.has_input('numsides'):
            artist.constructor_props['numsides'] = self.get_input('numsides')
        if self.has_input('rotation'):
            artist.constructor_props['rotation'] = self.get_input('rotation')
        if self.has_input('sizes'):
            artist.constructor_props['sizes'] = self.get_input('sizes')


class MplArcProperties(MplEllipseProperties):
    """
    An elliptical arc.  Because it performs various optimizations, it
    can not be filled.

    The arc must be used in an :class:`~matplotlib.axes.Axes`
    instance---it can not be added directly to a
    :class:`~matplotlib.figure.Figure`---because it is optimized to
    only render the segments that are inside the axes bounding box
    with high resolution.
    
    """
    _input_ports = [
              ("theta2", "basic:Float",
                {'optional': True, 'defaults': '[360.0]'}),
              ("theta1", "basic:Float",
                {'optional': True, 'defaults': '[0.0]'}),
              ("angle", "basic:Float",
                {'optional': True, 'defaults': '[0.0]'}),
              ("height", "basic:String",
                {'optional': True}),
              ("width", "basic:String",
                {'optional': True}),
              ("xy", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplArcProperties)")]

    class Artist(MplEllipseProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplEllipseProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplArcProperties.Artist()
            self.set_output("value", artist)

        MplEllipseProperties.compute(self, artist)
        if self.has_input('theta2'):
            artist.constructor_props['theta2'] = self.get_input('theta2')
        if self.has_input('theta1'):
            artist.constructor_props['theta1'] = self.get_input('theta1')
        if self.has_input('angle'):
            artist.constructor_props['angle'] = self.get_input('angle')
        if self.has_input('height'):
            artist.constructor_props['height'] = self.get_input('height')
        if self.has_input('width'):
            artist.constructor_props['width'] = self.get_input('width')
        if self.has_input('xy'):
            artist.constructor_props['xy'] = self.get_input('xy')


class MplCircleProperties(MplEllipseProperties):
    """
    A circle patch.
    
    """
    _input_ports = [
              ("xy", "basic:String",
                {'optional': True}),
              ("radius", "basic:Float",
                {'optional': True, 'docstring': 'Set the radius of the circle'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplCircleProperties)")]

    class Artist(MplEllipseProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplEllipseProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplCircleProperties.Artist()
            self.set_output("value", artist)

        MplEllipseProperties.compute(self, artist)
        if self.has_input('xy'):
            artist.constructor_props['xy'] = self.get_input('xy')
        if self.has_input('radius'):
            artist.props['radius'] = self.get_input('radius')


class MplConnectionPatchProperties(MplFancyArrowPatchProperties):
    """
    A :class:`~matplotlib.patches.ConnectionPatch` class is to make
    connecting lines between two points (possibly in different axes).
    
    """
    _input_ports = [
              ("connectionstyle", "basic:String",
                {'optional': True, 'docstring': 'the connection style', 'defaults': "[u'arc3']"}),
              ("coordsA", "basic:String",
                {'entry_types': "['enum']", 'values': "[['figure points', 'figure pixels', 'figure fraction', 'axes points', 'axes pixels', 'axes fraction', 'data', 'offset points', 'polar']]", 'optional': True}),
              ("arrowstyle", "basic:String",
                {'optional': True, 'docstring': 'the arrow style', 'defaults': "[u'-']"}),
              ("clip_on", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
              ("arrow_transmuter", "basic:String",
                {'optional': True}),
              ("axesA", "basic:String",
                {'optional': True}),
              ("axesB", "basic:String",
                {'optional': True}),
              ("annotation_clip", "basic:String",
                {'optional': True, 'docstring': 'set annotation_clip attribute.\n\nNone: the self.xy will be checked only if xycoords is "data"'}),
              ("dpi_cor", "basic:Float",
                {'optional': True, 'defaults': '[1.0]'}),
              ("connector", "basic:String",
                {'optional': True}),
              ("xyA", "basic:String",
                {'optional': True}),
              ("xyB", "basic:String",
                {'optional': True}),
              ("relpos", "basic:String",
                {'optional': True, 'docstring': 'default is (0.5, 0.5)', 'defaults': "['(0.5']"}),
              ("shrinkB", "basic:Float",
                {'optional': True, 'docstring': 'default is 2 points', 'defaults': '[0.0]'}),
              ("shrinkA", "basic:Float",
                {'optional': True, 'docstring': 'default is 2 points', 'defaults': '[0.0]'}),
              ("mutation_aspect", "basic:Integer",
                {'optional': True, 'docstring': 'default is 1.', 'defaults': '[1]'}),
              ("mutation_scale", "basic:String",
                {'optional': True, 'docstring': 'default is text size (in points)', 'defaults': '[10.0]'}),
              ("patchA", "basic:String",
                {'optional': True, 'docstring': 'default is bounding box of the text', 'defaults': "['bounding']"}),
              ("patchB", "basic:String",
                {'optional': True, 'docstring': 'default is None'}),
              ("coordsB", "basic:String",
                {'entry_types': "['enum']", 'values': "[['figure points', 'figure pixels', 'figure fraction', 'axes points', 'axes pixels', 'axes fraction', 'data', 'offset points', 'polar']]", 'optional': True}),
              ("?", "basic:String",
                {'optional': True, 'docstring': 'any key for :class:`matplotlib.patches.PathPatch`'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplConnectionPatchProperties)")]

    class Artist(MplFancyArrowPatchProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplFancyArrowPatchProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplConnectionPatchProperties.Artist()
            self.set_output("value", artist)

        MplFancyArrowPatchProperties.compute(self, artist)
        if self.has_input('connectionstyle'):
            artist.constructor_props['connectionstyle'] = self.get_input('connectionstyle')
        if self.has_input('coordsA'):
            artist.constructor_props['coordsA'] = self.get_input('coordsA')
        if self.has_input('arrowstyle'):
            artist.constructor_props['arrowstyle'] = self.get_input('arrowstyle')
        if self.has_input('clip_on'):
            artist.constructor_props['clip_on'] = self.get_input('clip_on')
        if self.has_input('arrow_transmuter'):
            artist.constructor_props['arrow_transmuter'] = self.get_input('arrow_transmuter')
        if self.has_input('axesA'):
            artist.constructor_props['axesA'] = self.get_input('axesA')
        if self.has_input('axesB'):
            artist.constructor_props['axesB'] = self.get_input('axesB')
        if self.has_input('annotation_clip'):
            artist.props['annotation_clip'] = self.get_input('annotation_clip')
        if self.has_input('dpi_cor'):
            artist.constructor_props['dpi_cor'] = self.get_input('dpi_cor')
        if self.has_input('connector'):
            artist.constructor_props['connector'] = self.get_input('connector')
        if self.has_input('xyA'):
            artist.constructor_props['xyA'] = self.get_input('xyA')
        if self.has_input('xyB'):
            artist.constructor_props['xyB'] = self.get_input('xyB')
        if self.has_input('relpos'):
            artist.constructor_props['relpos'] = self.get_input('relpos')
        if self.has_input('shrinkB'):
            artist.constructor_props['shrinkB'] = self.get_input('shrinkB')
        if self.has_input('shrinkA'):
            artist.constructor_props['shrinkA'] = self.get_input('shrinkA')
        if self.has_input('mutation_aspect'):
            artist.constructor_props['mutation_aspect'] = self.get_input('mutation_aspect')
        if self.has_input('mutation_scale'):
            artist.constructor_props['mutation_scale'] = self.get_input('mutation_scale')
        if self.has_input('patchA'):
            artist.constructor_props['patchA'] = self.get_input('patchA')
        if self.has_input('patchB'):
            artist.constructor_props['patchB'] = self.get_input('patchB')
        if self.has_input('coordsB'):
            artist.constructor_props['coordsB'] = self.get_input('coordsB')
        if self.has_input('?'):
            artist.constructor_props['?'] = self.get_input('?')


class MplFancyArrowProperties(MplPolygonProperties):
    """
    Like Arrow, but lets you set head width and head height independently.
    
    """
    _input_ports = [
              ("length_includes_head", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
              ("head_length", "basic:String",
                {'optional': True}),
              ("head_width", "basic:String",
                {'optional': True}),
              ("width", "basic:Float",
                {'optional': True, 'defaults': '[0.001]'}),
              ("shape", "basic:String",
                {'optional': True, 'defaults': "[u'full']"}),
              ("dx", "basic:String",
                {'optional': True}),
              ("dy", "basic:String",
                {'optional': True}),
              ("y", "basic:String",
                {'optional': True}),
              ("x", "basic:String",
                {'optional': True}),
              ("head_starts_at_zero", "basic:Boolean",
                {'optional': True, 'defaults': '[False]'}),
              ("overhang", "basic:Integer",
                {'optional': True, 'defaults': '[0]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplFancyArrowProperties)")]

    class Artist(MplPolygonProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPolygonProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplFancyArrowProperties.Artist()
            self.set_output("value", artist)

        MplPolygonProperties.compute(self, artist)
        if self.has_input('length_includes_head'):
            artist.constructor_props['length_includes_head'] = self.get_input('length_includes_head')
        if self.has_input('head_length'):
            artist.constructor_props['head_length'] = self.get_input('head_length')
        if self.has_input('head_width'):
            artist.constructor_props['head_width'] = self.get_input('head_width')
        if self.has_input('width'):
            artist.constructor_props['width'] = self.get_input('width')
        if self.has_input('shape'):
            artist.constructor_props['shape'] = self.get_input('shape')
        if self.has_input('dx'):
            artist.constructor_props['dx'] = self.get_input('dx')
        if self.has_input('dy'):
            artist.constructor_props['dy'] = self.get_input('dy')
        if self.has_input('y'):
            artist.constructor_props['y'] = self.get_input('y')
        if self.has_input('x'):
            artist.constructor_props['x'] = self.get_input('x')
        if self.has_input('head_starts_at_zero'):
            artist.constructor_props['head_starts_at_zero'] = self.get_input('head_starts_at_zero')
        if self.has_input('overhang'):
            artist.constructor_props['overhang'] = self.get_input('overhang')


class MplCirclePolygonProperties(MplRegularPolygonProperties):
    """
    A polygon-approximation of a circle patch.
    
    """
    _input_ports = [
              ("radius", "basic:Integer",
                {'optional': True, 'defaults': '[5]'}),
              ("xy", "basic:String",
                {'optional': True}),
              ("resolution", "basic:Integer",
                {'optional': True, 'defaults': '[20]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplCirclePolygonProperties)")]

    class Artist(MplRegularPolygonProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplRegularPolygonProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplCirclePolygonProperties.Artist()
            self.set_output("value", artist)

        MplRegularPolygonProperties.compute(self, artist)
        if self.has_input('radius'):
            artist.constructor_props['radius'] = self.get_input('radius')
        if self.has_input('xy'):
            artist.constructor_props['xy'] = self.get_input('xy')
        if self.has_input('resolution'):
            artist.constructor_props['resolution'] = self.get_input('resolution')


class MplNonUniformImageProperties(MplAxesImageProperties):
    """None
    """
    _input_ports = [
              ("cmap", "basic:String",
                {'optional': True}),
              ("filternorm", "basic:String",
                {'optional': True}),
              ("filterrad", "basic:String",
                {'optional': True}),
              ("ax", "basic:String",
                {'optional': True}),
              ("data", "basic:String",
                {'optional': True, 'docstring': 'Set the grid for the pixel centers, and the pixel values.'}),
              ("norm", "basic:String",
                {'optional': True}),
              ("interpolation", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplNonUniformImageProperties)")]

    class Artist(MplAxesImageProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplAxesImageProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplNonUniformImageProperties.Artist()
            self.set_output("value", artist)

        MplAxesImageProperties.compute(self, artist)
        if self.has_input('cmap'):
            artist.props['cmap'] = self.get_input('cmap')
        if self.has_input('filternorm'):
            artist.props['filternorm'] = self.get_input('filternorm')
        if self.has_input('filterrad'):
            artist.props['filterrad'] = self.get_input('filterrad')
        if self.has_input('ax'):
            artist.constructor_props['ax'] = self.get_input('ax')
        if self.has_input('data'):
            artist.props['data'] = self.get_input('data')
        if self.has_input('norm'):
            artist.props['norm'] = self.get_input('norm')
        if self.has_input('interpolation'):
            artist.props['interpolation'] = self.get_input('interpolation')


class MplBrokenBarHCollectionProperties(MplPolyCollectionProperties):
    """
    A collection of horizontal bars spanning *yrange* with a sequence of
    *xranges*.
    
    """
    _input_ports = [
              ("xranges", "basic:String",
                {'optional': True}),
              ("yrange", "basic:String",
                {'optional': True}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplBrokenBarHCollectionProperties)")]

    class Artist(MplPolyCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplPolyCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplBrokenBarHCollectionProperties.Artist()
            self.set_output("value", artist)

        MplPolyCollectionProperties.compute(self, artist)
        if self.has_input('xranges'):
            artist.constructor_props['xranges'] = self.get_input('xranges')
        if self.has_input('yrange'):
            artist.constructor_props['yrange'] = self.get_input('yrange')


class MplAsteriskPolygonCollectionProperties(MplRegularPolyCollectionProperties):
    """
    Draw a collection of regular asterisks with *numsides* points.
    """
    _input_ports = [
              ("numsides", "basic:String",
                {'optional': True}),
              ("rotation", "basic:Integer",
                {'optional': True, 'defaults': '[0]'}),
              ("sizes", "basic:String",
                {'optional': True, 'defaults': '[(1,)]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplAsteriskPolygonCollectionProperties)")]

    class Artist(MplRegularPolyCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplRegularPolyCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplAsteriskPolygonCollectionProperties.Artist()
            self.set_output("value", artist)

        MplRegularPolyCollectionProperties.compute(self, artist)
        if self.has_input('numsides'):
            artist.constructor_props['numsides'] = self.get_input('numsides')
        if self.has_input('rotation'):
            artist.constructor_props['rotation'] = self.get_input('rotation')
        if self.has_input('sizes'):
            artist.constructor_props['sizes'] = self.get_input('sizes')


class MplStarPolygonCollectionProperties(MplRegularPolyCollectionProperties):
    """
    Draw a collection of regular stars with *numsides* points.
    """
    _input_ports = [
              ("numsides", "basic:String",
                {'optional': True}),
              ("rotation", "basic:Integer",
                {'optional': True, 'defaults': '[0]'}),
              ("sizes", "basic:String",
                {'optional': True, 'defaults': '[(1,)]'}),
        ]

    # only one output port: 'value'
    _output_ports = [("value", "(MplStarPolygonCollectionProperties)")]

    class Artist(MplRegularPolyCollectionProperties.Artist):
        def __init__(self):
            self.props = {}
            self.constructor_props = {}
            self.not_setp_props = {}
            self.sub_props = {}

        def update_props(self, objs):
            matplotlib.artist.setp(objs, **self.props)
            if not matplotlib.cbook.iterable(objs):
                objs_iter = [objs]
            else:
                objs_iter = matplotlib.cbook.flatten(objs)
            for obj in objs_iter:
                for attr_name, attr_val in self.not_setp_props.iteritems():
                    setattr(obj, attr_name, attr_val)
            self.update_sub_props(objs)

        def update_sub_props(self, objs):
            MplRegularPolyCollectionProperties.Artist.update_sub_props(self, objs)

        def update_kwargs(self, kwargs):
            kwargs.update(self.constructor_props)
            kwargs.update(self.props)

    def compute(self, artist=None):
        if artist is None:
            artist = MplStarPolygonCollectionProperties.Artist()
            self.set_output("value", artist)

        MplRegularPolyCollectionProperties.compute(self, artist)
        if self.has_input('numsides'):
            artist.constructor_props['numsides'] = self.get_input('numsides')
        if self.has_input('rotation'):
            artist.constructor_props['rotation'] = self.get_input('rotation')
        if self.has_input('sizes'):
            artist.constructor_props['sizes'] = self.get_input('sizes')



_modules = [
            MplArtistProperties,
            MplAxisProperties,
            MplCollectionProperties,
            MplFigureImageProperties,
            MplFigureProperties,
            MplLegendProperties,
            MplLine2DProperties,
            MplPatchProperties,
            MplPcolorImageProperties,
            MplTextProperties,
            MplTickProperties,
            Mpl_AxesBaseProperties,
            Mpl_AxesImageBaseProperties,
            MplXAxisProperties,
            MplYAxisProperties,
            MplEllipseCollectionProperties,
            MplLineCollectionProperties,
            MplPatchCollectionProperties,
            MplQuadMeshProperties,
            MplTriMeshProperties,
            Mpl_CollectionWithSizesProperties,
            MplArrowProperties,
            MplEllipseProperties,
            MplFancyArrowPatchProperties,
            MplFancyBboxPatchProperties,
            MplPathPatchProperties,
            MplPolygonProperties,
            MplRectangleProperties,
            MplRegularPolygonProperties,
            MplShadowProperties,
            MplWedgeProperties,
            MplYAArrowProperties,
            MplAnnotationProperties,
            MplTextWithDashProperties,
            MplXTickProperties,
            MplYTickProperties,
            MplAxesProperties,
            MplAxesImageProperties,
            MplBboxImageProperties,
            MplEventCollectionProperties,
            MplCircleCollectionProperties,
            MplPathCollectionProperties,
            MplPolyCollectionProperties,
            MplRegularPolyCollectionProperties,
            MplArcProperties,
            MplCircleProperties,
            MplConnectionPatchProperties,
            MplFancyArrowProperties,
            MplCirclePolygonProperties,
            MplNonUniformImageProperties,
            MplBrokenBarHCollectionProperties,
            MplAsteriskPolygonCollectionProperties,
            MplStarPolygonCollectionProperties,
]
