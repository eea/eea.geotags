""" Widget
"""
from Products.Archetypes.atapi import StringWidget

class GeotagsWidget(StringWidget):
    """ Geotags
    """
    _properties = StringWidget._properties.copy()
    _properties.update({
        'macro': "eea.geotags",
        'dialog': '@@eea.geotags.dialog',
        'sidebar': '@@eea.geotags.sidebar',
        'basket': '@@eea.geotags.basket',
        'json': '@@eea.geotags.json',
    })
