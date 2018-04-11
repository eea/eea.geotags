from zope.component import adapter
from zope.interface import implementer

from zope.schema.interfaces import IField

from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget

from eea.geotags.widget.location import IGeotagSingleField

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


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def geotag_single_field_widget(field, request):
    return FieldWidget(field, GeolocationWidget(request))


GeotagSingleFieldWidget = geotag_single_field_widget
