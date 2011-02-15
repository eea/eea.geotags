""" Field
"""
import logging
import simplejson as json
from zope.component import queryAdapter
from Products.Archetypes import atapi
from eea.geotags.interfaces import IGeoTags

logger = logging.getLogger('eea.geotags.field')

class GeotagsFieldMixin(object):
    """ Add methods to get/set json tags
    """
    @property
    def multiline(self):
        return isinstance(self, atapi.LinesField)

    def getJSON(self, instance, **kwargs):
        """ Get GeoJSON tags from instance annotations using IGeoTags adapter
        """
        geo = queryAdapter(instance, IGeoTags)
        if not geo:
            return ''
        return json.dumps(geo.tags)

    def setJSON(self, instance, value, **kwargs):
        """ Set GeoJSON tags to instance annotations using IGeoTags adapter
        """
        geo = queryAdapter(instance, IGeoTags)
        if not geo:
            return

        if not isinstance(value, dict):
            try:
                value = json.loads(value)
            except Exception, err:
                logger.exception(err)
                return

        geo.tags = value

    def json2list(self, geojson, attr='description'):
        """ Util method to extract human readable geo tags from geojson struct
        """
        if not geojson:
            return

        try:
            value = json.loads(geojson)
        except Exception, err:
            logger.exception(err)
            return

        features = value.get('features', [])
        if not features:
            return

        for feature in features:
            properties = feature.get('properties', {})
            yield properties.get(attr, properties.get('title', ''))

    def json2string(self, geojson, attr='description'):
        """ Util method to extract human readable geo tag from geojson struct
        """
        items = self.json2list(geojson, attr)
        for item in items:
            return item
        return ''

class GeotagsStringField(atapi.StringField, GeotagsFieldMixin):
    """ Single geotag field
    """
    def set(self, instance, value, **kwargs):
        self.setJSON(instance, value, **kwargs)
        tag = self.json2string(value)
        return atapi.StringField.set(self, instance, tag, **kwargs)

class GeotagsLinesField(atapi.LinesField, GeotagsFieldMixin):
    """ Multiple geotags field
    """
    def set(self, instance, value, **kwargs):
        self.setJSON(instance, value, **kwargs)
        tags = [tag for tag in self.json2list(value)]
        return atapi.LinesField.set(self, instance, tags, **kwargs)

