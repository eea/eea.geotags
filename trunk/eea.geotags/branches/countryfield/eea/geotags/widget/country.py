""" Widget
"""
from Products.Archetypes.atapi import StringWidget

class CountriesWidget(StringWidget):
    """ Countries Geotags
    """
    _properties = StringWidget._properties.copy()
    _properties.update({
        'macro': "country_widget",
        'dialog': '@@eea.geotags.dialog',
        'sidebar': '@@eea.geotags.sidebar',
        'basket': '@@eea.geotags.basket',
        'json': '@@eea.geotags.json',
        'suggestions': '@@eea.geotags.suggestions',
        })
