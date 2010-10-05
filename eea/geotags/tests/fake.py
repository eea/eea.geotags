from zope.interface import implements
from eea.geotags.discover.AlchemyAPI import AlchemyAPI
from eea.geotags.interfaces import IAlchemyAPI

class FakeAlchemyAPI(AlchemyAPI):
    """ Fake API to be used within tests
    """
    implements(IAlchemyAPI)

    def PostRequest(self, apiCall, apiPrefix, paramObject):
        template = {
            'entities': [],
            'language': 'english',
            'status': 'FAKE',
            'url': '',
            'usage': ('By accessing AlchemyAPI or using information generated '
                      'by AlchemyAPI, you are agreeing to be bound by the '
                      'AlchemyAPI Terms of Use: '
                      'http://www.alchemyapi.com/company/terms.html')
        }
        text = paramObject.getText()
        if 'Spain' in text:
            template['entities'].append({
                'count': '1',
                'relevance': '0.33',
                'text': 'Spain',
                'type': 'Country'
            })

        if 'Valencia' in text:
            template['entities'].append({
                'count': '1',
                'relevance': '0.33',
                'text': 'Valencia',
                'type': 'City'
            })

        if 'Venice' in text:
            template['entities'].append({
                'count': '1',
                'relevance': '0.33',
                'text': 'Venice',
                'type': 'StateOrCounty'})

        return template.copy()

    GetRequest = PostRequest
