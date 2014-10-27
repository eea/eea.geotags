""" Widget
"""
from Products.Archetypes.Registry import registerWidget
from eea.geotags.widget.location import GeotagsWidget
from eea.geotags.widget.country import CountriesWidget

registerWidget(GeotagsWidget,
    title='Geotags Widget',
    description='Geotags widget',
    used_for=(
        'eea.geotags.field.GeotagsStringField',
        'eea.geotags.field.GeotagsLinesField',
    )
)

registerWidget(CountriesWidget,
               title='Countries Widget',
               description='Countries widget',
               used_for=(
                   'eea.geotags.field.GeotagsStringField',
                   'eea.geotags.field.GeotagsLinesField',
               )
)
