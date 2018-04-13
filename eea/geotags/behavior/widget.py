import json

from zope.component import adapter
from zope.component import getUtility
from zope.interface import implementer

from zope.schema.interfaces import IField

from plone.registry.interfaces import IRegistry

from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget

from eea.geotags.field.location import get_tags
from eea.geotags.widget.location import IGeotagSingleField
from eea.geotags.controlpanel.interfaces import IGeotagsSettings

STR_PF = 'portal_factory'

URL_DIALOG = '@@eea.geotags.dialog'
URL_SIDEBAR = '@@eea.geotags.sidebar'
URL_BASKET = '@@eea.geotags.basket'
URL_JSON = '@@eea.geotags.json'
URL_SUGGESTIONS = '@@eea.geotags.suggestions'
URL_COUNTRY_MAPPING = '@@eea.geotags.mapping'


def _base_url(request):
    url1 = request.URL1
    portal_factory = STR_PF in url1
    return url1.split(STR_PF)[0] if portal_factory else url1 + '/'


@implementer(IGeotagSingleField)
class GeolocationWidget(TextAreaWidget):

    klass = u'eea.geolocation.widget'
    multiline = 0

    @property
    def base_url(self):
        return _base_url(self.request)

    @property
    def dialog(self):
        from eea.geotags.interfaces import IGeoTaggable
        from eea.geotags.storage.interfaces import IGeoTags
        return self.base_url + URL_DIALOG

    @property
    def sidebar(self):
        return self.base_url + URL_SIDEBAR

    @property
    def basket(self):
        return self.base_url + URL_BASKET

    @property
    def json(self):
        return self.base_url + URL_JSON

    @property
    def suggestions(self):
        return self.base_url + URL_SUGGESTIONS

    @property
    def country_mapping(self):
        return self.base_url + URL_COUNTRY_MAPPING

    @property
    def geojson(self):
        data = self.extract(dict())
        return data.get(self.name, self.field.getJSON(self.context))

    @property
    def api_key(self):
        try:
            settings = getUtility(IRegistry).forInterface(IGeotagsSettings)
            return settings.maps_api_key
        except KeyError:
            return ''

    @property
    def js_props(self):
        return json.dumps(dict(
            id=self.id,
            name=self.name.replace('.', '\\.'),
            basket=self.basket,
            sidebar=self.sidebar,
            dialog=self.dialog,
            json=self.json,
            geojson=get_tags(self.context),
            multiline=self.multiline,
            suggestions=self.suggestions,
            country_mapping=self.country_mapping,
        ))


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def geotag_single_field_widget(field, request):
    return FieldWidget(field, GeolocationWidget(request))


GeotagSingleFieldWidget = geotag_single_field_widget
