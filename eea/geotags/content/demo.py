""" Demonstrates the use of EEA Geotags widget """

from Products.Archetypes import atapi
from Products.ATContentTypes.content.folder import ATFolder
from eea.geotags.field import GeotagsField
from eea.geotags.widget import GeotagsWidget

SCHEMA = ATFolder.schema.copy() + atapi.Schema((
    GeotagsField('location',
        schemata='default',
        widget=GeotagsWidget(
            label='Location',
            description='Geographical location'
        )
    ),
))

class EEAGeotagsDemo(ATFolder):
    """ Demo from EEA Geotags Widget
    """
    archetypes_name = meta_type = portal_type = 'EEATagsDemo'
    _at_rename_after_creation = True
    schema = SCHEMA
