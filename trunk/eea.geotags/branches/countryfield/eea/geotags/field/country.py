""" Country Field
"""
from eea.geotags.field.location import GeotagsFieldMixin


class CountryFieldMixin(GeotagsFieldMixin):
    """ Country Field Mixin
    """

    def getJSON(self, instance, **kwargs):
        """
        :param instance:
        :type instance:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        pass

    def setJSON(self, instance, value, **kwargs):
        """
        :param instance:
        :type instance:
        :param value:
        :type value:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        pass
