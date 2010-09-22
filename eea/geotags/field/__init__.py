from Products.Archetypes.Registry import registerField
from location import GeotagsField

registerField(
    GeotagsField,
    title="Geotags Field",
    description=("Geotags field.")
)
