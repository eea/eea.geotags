""" EEA Geotags Installer
"""
import os
from setuptools import setup, find_packages

NAME = 'eea.geotags'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description=(
          "EEA Geotags package redefines the location field in Plone. "
          "Right now in Plone location field is a free text field. "
          "EEA Geotags lets you easy define locations using a map picker "
          "and http://geonames.org geographical database."),
      long_description_content_type="text/x-rst",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Zope2",
          "Framework :: Plone",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Zope",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
      ],
      keywords='EEA Add-ons Plone Zope',
      author='European Environment Agency: IDM2 A-Team',
      author_email='eea-edw-a-team-alerts@googlegroups.com',
      url='https://github.com/eea/eea.geotags',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'eventlet',
          'archetypes.schemaextender',
          'eea.jquery',
          'eea.alchemy',
          'eea.geolocation',
          'collective.taxonomy',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """
      )
