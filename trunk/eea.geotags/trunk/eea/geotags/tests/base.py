""" Base test cases
"""
from Products.Five import zcml
from Products.Five import fiveconfigure
product_globals = globals()

# Import PloneTestCase - this registers more products with Zope as a side effect
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
import logging
logger = logging.getLogger('eea.geotags.tests.base')

@onsetup
def setup_eea_geotags():
    """Set up the additional products.

    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """
    fiveconfigure.debug_mode = True
    import Products.Five
    zcml.load_config('meta.zcml', Products.Five)

    import eea.geotags
    zcml.load_config('configure.zcml', eea.geotags)
    fiveconfigure.debug_mode = False

    try:
        ptc.installPackage('eea.geotags')
    except AttributeError, err:
        #BBB Plone 2.5
        logger.info(err)

    #from zope.component import provideUtility
    ptc.installProduct('ATVocabularyManager')
    ptc.installProduct('Five')

    #BBB Plone 2.5
    try: 
        import Products.FiveSite
        Products.FiveSite
    except ImportError: pass
    else: ptc.installProduct('FiveSite')

setup_eea_geotags()
ptc.setupPloneSite(extension_profiles=('eea.geotags:01-default', 'eea.geotags:03-demo'))

class EEAGeotagsTestCase(ptc.PloneTestCase):
    """Base class for integration tests for the 'EEA Geotags' product.
    """

class EEAGeotagsFunctionalTestCase(ptc.FunctionalTestCase, EEAGeotagsTestCase):
    """Base class for functional integration tests for the 'EEA Geotags' product.
    """
