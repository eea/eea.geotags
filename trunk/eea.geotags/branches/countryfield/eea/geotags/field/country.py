""" Country Field
"""
import json
import logging
from Products.Archetypes import atapi
from zope.component import queryAdapter
from eea.geotags.field.location import GeotagsFieldMixin
from eea.geotags.storage.interfaces import ICountryTags

logger = logging.getLogger(__name__)


class CountryFieldMixin(GeotagsFieldMixin):
    """ Country Field Mixin
    """

    def getJSON(self, instance, **kwargs):
        """
        :param instance: context object
        :type instance: object
        :return: json string dump
        :rtype: string
        """
        geo = queryAdapter(instance, ICountryTags)
        if not geo:
            return ''
        return json.dumps(geo.tags)

    def setJSON(self, instance, value, **kwargs):
        """
        :param instance:
        :type instance:
        :param value:
        :type value:
        :return:
        :rtype:
        """
        geo = queryAdapter(instance, ICountryTags)
        if not geo:
            return

        if not isinstance(value, dict) and value:
            try:
                value = json.loads(value)
            except Exception, err:
                logger.exception(err)
                return

        if not value:
            return
        geo.tags = value


class CountriesLinesField(CountryFieldMixin, atapi.LinesField):
    """ Multiple countries field
    """
    def set(self, instance, value, **kwargs):
        """ Set
        """
        new_value = self.setTranslationJSON(instance, value, **kwargs)
        if new_value is None:
            new_value = self.setCanonicalJSON(instance, value, **kwargs)
        if not new_value:
            return
        tags = [tag for tag in self.json2list(new_value)]
        return atapi.LinesField.set(self, instance, tags, **kwargs)
