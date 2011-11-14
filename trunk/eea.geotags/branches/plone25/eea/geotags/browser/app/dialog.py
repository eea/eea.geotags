#from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView

class Dialog(BrowserView):
    """ Geotags popup sidebar
    """
    _fieldName = ''

    @property
    def fieldName(self):
        return self._fieldName

    def __call__(self, **kwargs):
        if self.request:
            kwargs.update(self.request.form)
        self._fieldName = kwargs.get('fieldName', '')
        return self.index()
