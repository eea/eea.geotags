""" JSON Components
"""
import logging
import urllib, urllib2
import simplejson
import operator
from zope.component import queryAdapter
from zope.interface import implements

from eea.geotags.config import WEBSERVICE

from eea.geotags.interfaces import IGeoGroups
from eea.geotags.interfaces import IGeoCountries
from interfaces import IJsonProvider

logger = logging.getLogger('eea.geotags.json')

class GeoNamesJsonProvider(object):
    """ get json from http://geonames.org and convert it to geojson
    """
    def __init__(self, context):
        self.context = context

    def groups(self, **kwargs):
        voc = queryAdapter(self.context, IGeoGroups)
        json = {
            'type': 'FeatureCollection',
            'features': []
        }
        json['features'] = []

        terms = [term for term in voc()]
        terms.sort(key=operator.attrgetter('title'))

        for term in terms:
            feature = {
                'type': 'Feature',
                'bbox': [],
                'geometry': {
                    'type': 'Point',
                    'coordinates': [],
                    },
                'properties': {
                    'name': '',
                    'title': '',
                    'description': '',
                    'tags': '',
                    'center': [],
                    'country': '',
                    'adminCode1': '',
                    'adminName1': '',
                    'other': {}
                }
            }

            feature['geometry']['type'] = 'Polygon'
            feature['properties']['name'] = term.value
            feature['properties']['title'] = term.title
            json['features'].append(feature)
        return json

    def countries(self, **kwargs):
        group = kwargs.get('group', '')
        filters = []
        if group:
            voc = queryAdapter(self.context, IGeoCountries)
            filters = [term.value.replace('geo-', '') for
                       term in voc(group=group)]

        continentCode = kwargs.get('continentCode', 'EU')
        json = self.search(continentCode=continentCode,
                           featureClass='A',
                           featureCode='PCLI')

        if filters:
            features = json['features']
            json['features'] = [feature for feature in features
                                if feature['properties']['name'] in filters]
        return json

    def nuts(self, **kwargs):
        query = kwargs.copy()
        query['featureClass'] = 'A'
        query['featureCode'] = 'ADM1'
        return self.search(**query)

    def cities(self, **kwargs):
        query = kwargs.copy()
        query['featureClass'] = 'P'
        return self.search(**query)

    def natural_features(self, **kwargs):
        query = kwargs.copy()
        query['featureClass'] = ['H', 'T']
        return self.search(**query)

    def search(self, **kwargs):
        """ Search using geonames webservice
        """
        template = GEOJSON = {
            'type': 'FeatureCollection',
            'features': []
        }

        template['features'] = []

        query = kwargs.copy()
        query.setdefault('lang', 'en')
        query = urllib.urlencode(query, doseq=1)
        try:
            conn = urllib2.urlopen(WEBSERVICE, query)
            json = conn.read()
        except Exception, err:
            logger.exception(err)
            return template

        try:
            json = simplejson.loads(json)
            json = json.get('geonames', []) or []
        except Exception, err:
            logger.exception(err)
            return template

        json.sort(key=operator.itemgetter('name'))

        for item in json:
            feature = {
                'type': 'Feature',
                'bbox': [],
                'geometry': {
                    'type': 'Point',
                    'coordinates': [],
                    },
                'properties': {
                    'name': '',
                    'title': '',
                    'description': '',
                    'tags': '',
                    'center': [],
                    'country': '',
                    'adminCode1': '',
                    'adminName1': '',
                    'other': {}
                }
            }

            feature['geometry']['coordinates'] = [
                item.get('lat'), item.get('lng')]

            feature['properties']['center'] = [
                item.get('lat'), item.get('lng')]

            feature['properties']['name'] = str(item.get('geonameId'))
            feature['properties']['title'] = item.get('name')
            feature['properties']['tags'] = item.get('fclName')
            feature['properties']['country'] = item.get('countryCode')
            feature['properties']['adminCode1'] = item.get('adminCode1')
            feature['properties']['adminName1'] = item.get('adminName1')

            feature['properties']['other'] = item.copy()
            template['features'].append(feature)
        return template
