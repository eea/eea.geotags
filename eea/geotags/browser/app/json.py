""" JSON Service
"""
from pprint import pformat
import logging
import simplejson
from zope.component import queryAdapter
from Products.Five.browser import BrowserView
from eea.geotags.interfaces import IJsonProvider
from eea.geotags.cache import ramcache, cacheGeoJsonKey

logger = logging.getLogger('eea.geotags.browser.json')

class JSON(BrowserView):
    """ JSON service
    """
    @ramcache(cacheGeoJsonKey, dependencies=['eea.geotags'])
    def __call__(self, **kwargs):
        if self.request:
            kwargs.update(self.request.form)

        service = queryAdapter(self.context, IJsonProvider)
        json = kwargs.pop('type', 'search')
        if json == 'groups':
            res = service.groups(**kwargs)
        elif json == 'biogroups':
            res = service.biogroups(**kwargs)
        elif json == 'countries':
            res = service.countries(**kwargs)
        elif json == 'nuts':
            res = service.nuts(**kwargs)
        elif json == 'cities':
            res = service.cities(**kwargs)
        elif json == 'natural':
            res = service.natural_features(**kwargs)
        else:
            res = service.search(**kwargs)

        if kwargs.get('print', None):
            return pformat(res)
        return simplejson.dumps(res)
