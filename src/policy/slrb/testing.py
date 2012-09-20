from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicySlrb(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.slrb
        xmlconfig.file('configure.zcml',
                       policy.slrb,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.slrb:default')

POLICY_SLRB_FIXTURE = PolicySlrb()
POLICY_SLRB_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_SLRB_FIXTURE, ),
                       name="PolicySlrb:Integration")