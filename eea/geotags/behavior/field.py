from zope.interface import implementer

from zope import schema

from zope.schema.interfaces import IField

from eea.geotags.field.location import GeotagsFieldMixin


class IGeotagsStringField(IField):
    """ """


@implementer(IGeotagsStringField)
class GeotagsStringField(GeotagsFieldMixin, schema.Text):
    """ zope.schema field implementation
    """

    multiline = 0
