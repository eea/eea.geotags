from zope.interface import provider

from plone.supermodel import model
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider

from eea.geotags.interfaces import IGeoTaggable

from eea.geotags.behavior.widget import GeotagSingleFieldWidget
from eea.geotags.behavior.field import GeotagsStringField
from eea.geotags.config import _


@provider(IFormFieldProvider)
class ISingleGeoTag(model.Schema, IGeoTaggable):

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

