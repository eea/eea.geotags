from zope.interface import provider
from zope.interface import implementer

from zope import schema

from Acquisition import ImplicitAcquisitionWrapper
from Acquisition import aq_self

from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider

from eea.geotags.behavior.widget import GeotagFieldWidget
from eea.geotags.config import _

from eea.geotags.field.location import json2string
from eea.geotags.field.location import json2list
from eea.geotags.field.location import set_json
from eea.geotags.field.location import get_tags


@provider(IFormFieldProvider)
class ISingleGeoTag(model.Schema):

    model.fieldset(
        'categorization',
        label=_(u'Categorization'),
        fields=('location', )
    )

    location = schema.Text(title=_(u'Location'), required=False)
    directives.widget('location', GeotagFieldWidget, multiline=0)


@provider(IFormFieldProvider)
class IMultiGeoTag(model.Schema):

    model.fieldset(
        'categorization',
        label=_(u'Categorization'),
        fields=('location', )
    )

    location = schema.Text(title=_(u'Location'), required=False)
    directives.widget('location', GeotagFieldWidget, multiline=1)


@implementer(ISingleGeoTag, IMultiGeoTag)
class GeoTag(object):

    def __init__(self, context):
        # dewrap context when a Dexterity object is added
        # taken from collective.geo.behaviour
        if isinstance(context, ImplicitAcquisitionWrapper):
            context = aq_self(context)
        self.context = context

    @property
    def location(self):
        return json2list(get_tags(self.context))

    @location.setter
    def location(self, value):
        set_json(self.context, value)
