""" Country Field
"""
import logging
from Products.Archetypes import atapi
from zope.component import queryAdapter
from eea.geotags.field.location import GeotagsFieldMixin
from eea.geotags.storage.interfaces import ICountryTags

logger = logging.getLogger(__name__)


class CountryFieldMixin(GeotagsFieldMixin):
    """ Country Field Mixin
    """

    def get_adapter(self, instance):
        """
        :param instance: field instance
        :type instance: object
        :return: adapted object
        :rtype:  object
        """
        return queryAdapter(instance, ICountryTags)

    def remove_interface(self, instance, value):
        """ There is no interface to remove for the CountryField
        """
        pass


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

