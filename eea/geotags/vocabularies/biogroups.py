""" Groups
"""
from zope.component import getUtility
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from plone.registry.interfaces import IRegistry

from eea.geotags.vocabularies.interfaces import IBioGroups
from eea.geotags.controlpanel.interfaces import IGeoVocabularies


class BioGroups(object):
    """ Biogeographical regions
    """
    implements(IBioGroups)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        from collective.taxonomy.interfaces import ITaxonomy
        from plone.i18n.normalizer.interfaces import IIDNormalizer
        from zope.component import queryUtility

        normalizer = getUtility(IIDNormalizer)
        name = 'eea.geolocation.biotags.taxonomy'
        normalized_name = normalizer.normalize(name).replace("-", "")
        utility_name = "collective.taxonomy." + normalized_name
        taxonomy = queryUtility(ITaxonomy, name=utility_name)

        # data = taxonomy.data['en']
        vocabulary = taxonomy(self)
        identifier_data = {}
        data = {}
        identifier = 'placeholderidentifier'
        for value, key in vocabulary.iterEntries():
            value = value.encode('ascii', 'ignore').decode('ascii')
            key = key.split('||')[-1]

            if identifier not in value:
                data.update({'title': identifier})
                identifier_data.update({identifier: data})
                identifier = value
                data = {}
            else:
                data.update({key: value.split(identifier)[-1]})
        data.update({'title': identifier})
        identifier_data.update({identifier: data})
        del identifier_data['placeholderidentifier']

        items = [
            SimpleTerm(key, key, val['title'])
            for key, val in identifier_data.items()
        ]
        # registry = getUtility(IRegistry).forInterface(IGeoVocabularies, False)
        # biotags = registry.biotags or dict()
        # items = [
        #     SimpleTerm(key, key, val['title'])
        #     for key, val in biotags.items()
        # ]
        return SimpleVocabulary(items)
