===========
EEA Geotags
===========
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.geotags/develop
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.geotags/job/develop/display/redirect
  :alt: develop
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.geotags/master
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.geotags/job/master/display/redirect
  :alt: Master

EEA Geotags package redefines the location field in Plone. Right now in Plone
location field is a free text field. EEA Geotags lets you easy define locations
using a map picker and http://geonames.org geographical database.


Contents
========

.. contents::


Introduction
============

EEA Geotags is an alternative for the default location field in Plone.


Main features
=============

EEA Geotags features:

1. User friendly search for locations
2. Map preview of selected locations
3. Suggest geographic entities based on http://geonames.org
4. Country/regions drill down selection, including several layers like
   biogeographical region, countries group, country, nuts region, city and natural feature
5. The widget can be used as single or multiple location picker

Also read README.txt under eea.alchemy.

More details about how to use this package can be found at the following link:

1. https://taskman.eionet.europa.eu/projects/zope/wiki/HowToGeotag


Installation
============

The easiest way to get eea.geotags support in Plone 4 using this
package is to work with installations based on `zc.buildout`_.
Other types of installations should also be possible, but might turn out
to be somewhat tricky.

To get started you will simply need to add the package to your "eggs" and
"zcml" sections, run buildout, restart your Plone instance and install the
"eea.geotags" package using the quick-installer or via the "Add-on
Products" section in "Site Setup".

.. _`zc.buildout`: https://pypi.python.org/pypi/zc.buildout/

You can download a sample buildout at:

* https://github.com/eea/eea.geotags/tree/master/buildouts/plone4


Dependecies
===========

1. Plone 4.x
3. archetypes.schemaextender
4. eea.jquery
5. eea.alchemy
6. eventlet


Source code
===========

Latest source code (Plone 4 compatible):
   https://github.com/eea/eea.geotags

Plone 2 and 3 compatible:
   https://github.com/eea/eea.geotags/tree/plone25


Copyright and license
=====================
The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Geotags (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

More details under docs/License.txt


Links
=====

1. EEA Geotags wiki page: https://taskman.eionet.europa.eu/projects/zope/wiki/HowToGeotag


Funding
=======

EEA_ - European Enviroment Agency (EU)

.. _EEA: https://www.eea.europa.eu/
