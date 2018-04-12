from zope.interface import provider
from zope.interface import implementer

from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider

from eea.geotags.behavior.widget import GeotagSingleFieldWidget
from eea.geotags.behavior.field import GeotagsStringField
from eea.geotags.config import _

from eea.geotags.field.location import json2string
from eea.geotags.field.location import set_json


@provider(IFormFieldProvider)
class ISingleGeoTag(model.Schema):

    model.fieldset(
        'categorization',
        label=_(u'Categorization'),
        fields=('location', )
    )

    directives.widget('location', GeotagSingleFieldWidget)
    location = GeotagsStringField(
        title=_(u'Location'),
        required=False,
    )


@implementer(ISingleGeoTag)
class SingleGeoTag(object):

    def __init__(self, context):
        self.context = context

    @property
    def location(self):
        return getattr(self.context, 'location', '')

    @location.setter
    def location(self, value):
        set_json(self.context, value)
        setattr(self.context, 'location', json2string(value))