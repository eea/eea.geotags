""" EEA Geotags interfaces
"""
# Vocabulary adapters
from eea.geotags.vocabularies.interfaces import IGeoGroups
from eea.geotags.vocabularies.interfaces import IBioGroups
from eea.geotags.vocabularies.interfaces import IGeoCountries
from eea.geotags.json.interfaces import IJsonProvider
IGeoGroups, IBioGroups, IGeoCountries, IJsonProvider
# GeoTags storage
from eea.geotags.storage.interfaces import IGeoTaggable
from eea.geotags.storage.interfaces import IGeoTags
IGeoTaggable, IGeoTags
