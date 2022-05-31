# -*- coding: utf-8 -*-
"""Family module for Gratisdata."""
#
# (C) Pywikibot team, 2012-2018
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, division, unicode_literals

from pywikibot import config
from pywikibot import family
import configparser
app_config = configparser.ConfigParser()
app_config.read('config/application.config.ini')


# The Gratisdata family
class Family(family.Family):

    """Family class for Gratisdata."""

    name = 'my'

    langs = {
        'my': app_config.get('wikibase', 'domain'),
    }

    interwiki_forward = 'gratispaideia'

    category_redirect_templates = {
        'my': (
            'Category redirect',
        ),
    }

    # Subpages for documentation.
    doc_subpages = {
        '_default': (('/doc', ), ['gratisdata']),
    }

    # Disable cosmetic changes
    config.cosmetic_changes_disable.update({
        'my': ('wikidata2', 'test', 'beta')
    })

    def interface(self, code):
        """Return 'DataSite'."""
        return 'DataSite'

    def calendarmodel(self, code):
        """Default calendar model for WbTime datatype."""
        return 'https://gratisdata.miraheze.org/wiki/Q471'

    def shared_geo_shape_repository(self, code):
        """Return Gratispaideia Commons as the repository for geo-shapes."""
        # Per geoShapeStorageFrontendUrl settings in Wikibase
        return ('commons', 'commons')

    def shared_tabular_data_repository(self, code):
        """Return Gratispaideia Commons as the repository for tabular-datas."""
        # Per tabularDataStorageFrontendUrl settings in Wikibase
        return ('commons', 'commons')

    def default_globe(self, code):
        """Default globe for Coordinate datatype."""
        return 'earth'


    def protocol(self, code):
        return {
            'my': app_config.get('wikibase', 'protocol'),
        }[code]

    def globes(self, code):
        """Supported globes for Coordinate datatype."""
        return {
		'earth': 'http://gratisdata.miraheze.org/entity/Q476', 
		'mercury': 'http://gratisdata.miraheze.org/entity/Q987',
		'venus': 'http://gratisdata.miraheze.org/entity/Q981',
		'moon': 'http://gratisdata.miraheze.org/entity/Q985',
		'mars': 'http://gratisdata.miraheze.org/entity/Q806',
		'phobos': 'http://gratisdata.miraheze.org/entity/Q2126',
		'deimos': 'http://gratisdata.miraheze.org/entity/Q2118',
		'ganymede': 'http://gratisdata.miraheze.org/entity/Q967',
		'callisto': 'http://gratisdata.miraheze.org/entity/Q961',
		'io': 'http://gratisdata.miraheze.org/entity/Q990',
		'europa': 'http://gratisdata.miraheze.org/entity/Q965',
		'mimas': 'http://gratisdata.miraheze.org/entity/Q986',
		'enceladus': 'http://gratisdata.miraheze.org/entity/Q964',
		'tethys': 'http://gratisdata.miraheze.org/entity/Q984',
		'dione': 'http://gratisdata.miraheze.org/entity/Q963',
		'rhea': 'http://gratisdata.miraheze.org/entity/Q988',
		'titan': 'http://gratisdata.miraheze.org/entity/Q983',
		'hyperion': 'http://gratisdata.miraheze.org/entity/Q2119',
		'iapetus': 'http://gratisdata.miraheze.org/entity/Q989',
	    	'phoebe': 'http://gratisdata.miraheze.org/entity/Q966',
	    	'miranda': 'http://gratisdata.miraheze.org/entity/Q2122',
		'ariel': 'http://gratisdata.miraheze.org/entity/Q2117',
		'umbriel': 'http://gratisdata.miraheze.org/entity/Q2129',
	    	'titania': 'http://gratisdata.miraheze.org/entity/Q2128',
	    	'oberon': 'http://gratisdata.miraheze.org/entity/Q2125',
		'triton': 'http://gratisdata.miraheze.org/entity/Q982',
	    	'pluto': 'http://gratisdata.miraheze.org/entity/Q2123',		
        }
        
