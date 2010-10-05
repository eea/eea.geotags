""" EEA Geotags interfaces
"""
# Vocabulary adapters
from vocabularies.interfaces import IGeoGroups
from vocabularies.interfaces import IBioGroups
from vocabularies.interfaces import IGeoCountries
from json.interfaces import IJsonProvider

# GeoTags storage
from storage.interfaces import IGeoTaggable
from storage.interfaces import IGeoTags

# AlchemyAPI
from discover.interfaces import IAlchemyAPI

# Auto-discover geotags
from discover.interfaces import IDiscoverGeoTags
