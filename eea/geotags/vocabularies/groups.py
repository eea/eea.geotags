""" Groups
"""
from zope.component import getUtility
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from plone.registry.interfaces import IRegistry
from eea.geotags.vocabularies.interfaces import IGeoGroups
from eea.geotags.controlpanel.interfaces import IGeoVocabularies


class Groups(object):
    """ Extract countries for group
    """
    implements(IGeoGroups)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        # return []
        from collective.taxonomy.interfaces import ITaxonomy
        from plone.i18n.normalizer.interfaces import IIDNormalizer
        from zope.component import queryUtility

        normalizer = getUtility(IIDNormalizer)
        name = 'eea.geolocation.geotags.taxonomy'
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
        # import pdb; pdb.set_trace()
        # term = SimpleTerm(identifier, identifier, value)

        # items.append({
            
        # })                
            # print identifier, value
            # items.append(term)
            # key = key.encode('ascii', 'ignore').decode('ascii')
            # term = SimpleTerm(key, key, val)

        # (Pdb) dece={u'eea32': {u'geo-146669': u'Cyprus', u'geo-2623032': u'Denmark', u'geo-3144096': u'Norway', u'geo-298795': u'Turkey'}}
        # (Pdb) dece
        # {u'eea32': {u'geo-146669': u'Cyprus', u'geo-2623032': u'Denmark', u'geo-298795': u'Turkey', u'geo-3144096': u'Norway'}}
        # (Pdb) dece.items()
        # [(u'eea32', {u'geo-146669': u'Cyprus', u'geo-2623032': u'Denmark', u'geo-298795': u'Turkey', u'geo-3144096': u'Norway'})]
        # (Pdb) for key, val in dece.items(): print key
        # eea32
        # (Pdb) for key, val in dece.items(): print val
        # {u'geo-146669': u'Cyprus', u'geo-2623032': u'Denmark', u'geo-298795': u'Turkey', u'geo-3144096': u'Norway'}

        # registry = getUtility(IRegistry).forInterface(IGeoVocabularies, False)
        # geotags = registry.geotags or dict()
        # items = [
        #     SimpleTerm(key, key, val['title'])
        #     for key, val in geotags.items()
        # ]
        return SimpleVocabulary(items)
