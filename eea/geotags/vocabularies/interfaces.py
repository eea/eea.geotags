""" Interfaces
"""
from zope.interface import Interface
from plone.registry import field

from eea.geotags.config import _


class IGeoGroups(Interface):
    """ Provide an adapter for this interface in order to get Geotags Groups
    """
    def __call__(self):
        """ Returns a SimpleVocabulary instance of geo groups
        """


class IBioGroups(Interface):
    """ Provide an adapter for this interface in order to
        get Biogeographical regions
    """
    def __call__(self):
        """ Returns a SimpleVocabulary instance of biogeographical regions
        """


class IGeoCountries(Interface):
    """ Provide an adapter for this in order to get geotags countries for a
        specified group
    """
    def __call__(group):
        """ Returns a SimpleVocabulary instance of geo countries
            for given group
        """


class IGeoCountriesMapping(Interface):
    """ Provide an adapter for this in order to get geotags countries with
        custom name and description mapping
    """
    def __call__(self):
        """ Returns a SimpleVocabulary instance of geo countries with custom
            name
        """


class IGeoVocabularies(Interface):
    geotags = field.Dict(
        title=_(u'Geotags tree'),
        key_type=field.TextLine(),
        value_type=field.Dict(
            key_type=field.TextLine(),
            value_type=field.TextLine(),
        ),
    )

    biotags = field.Dict(
        title=_(u'Biogeographical regions'),
        key_type=field.TextLine(),
        value_type=field.Dict(
            key_type=field.TextLine(),
            value_type=field.TextLine(),
        ),
    )

    countries_mapping = field.Dict(
        title=_(u'EEA Custom Country Name Mappings'),
        key_type=field.TextLine(),
        value_type=field.TextLine(),
    )
