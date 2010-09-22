""" Interfaces
"""
from zope.interface import Interface

class IGeoGroups(Interface):
    """
    Provide an adapter for this interface in order to
    get Geotags Groups
    """
    def __call__():
        """
        Returns a SimpleVocabulary instance of geo groups
        """

class IGeoCountries(Interface):
    """
    Provide an adapter for this in order to get geotags countries for a
    specified group
    """
    def __call__(group):
        """
        Returns a SimpleVocabulary instance of
        geo countries for given group
        """
