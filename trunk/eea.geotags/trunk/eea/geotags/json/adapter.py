""" JSON adapters
"""
from zope.interface import implements
from eea.geotags.json.interfaces import IJsonProviderSearchMutator


class JSONProviderSearchMutator(object):
    """ Abstract adapter to mutate JSONProvider search results
    """
    implements(IJsonProviderSearchMutator)

    def __init__(self, context):
        self.context = context

    def __call__(self, template):
        """ Return a dict of geonames search results
        """
        return template


class EEAJSONProviderSearchMutator(object):
    """ Abstract adapter to mutate JSONProvider search results
    """
    implements(IJsonProviderSearchMutator)

    def __init__(self, context):
        self.context = context
        self.country_mapping = {
            "Czechia": "Czech Republic",
            "Macedonia": "Macedonia (FYR)",
            "Kosovo": "Kosovo (UNSCR 1244/99)"
        }

    def __call__(self, template):
        """ Return a dict of geonames search with mutated results
        """
        features = template.get('features')
        if features:
            first_result = features[0]
            match = self.country_mapping.get(
                first_result['properties'].get('title'))

            # check also description for country matching as some matches
            # might be triggered while checking for description
            if not match:
                match = self.country_mapping.get(
                    first_result['properties'].get('description'))
            if match:
                first_result['properties']['title'] = match
                first_result['properties']['description'] = match
        return template

