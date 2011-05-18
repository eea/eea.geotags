""" Base test cases
"""
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup
import eea.geotags
import logging

#TODO: plone4
#product_globals = globals()
logger = logging.getLogger('eea.geotags.tests.base')

PloneTestCase.installProduct('ATVocabularyManager')

@onsetup
def setup_eea_geotags():
    """Set up the additional products.

    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer.
    """
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', eea.geotags)
    fiveconfigure.debug_mode = False

setup_eea_geotags()
ptc.setupPloneSite(extension_profiles=('eea.geotags:01-default', 'eea.geotags:03-demo'))

class EEAGeotagsTestCase(ptc.PloneTestCase):
    """ Base class for integration tests for the 'EEA Geotags' product.
    """

class EEAGeotagsFunctionalTestCase(ptc.FunctionalTestCase, EEAGeotagsTestCase):
    """ Base class for functional integration tests for the
        'EEA Geotags' product.
    """
