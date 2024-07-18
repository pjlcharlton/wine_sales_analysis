# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

archive_df = pd.read_csv('wine_sales_archive_anonymous.csv').drop(['Unnamed: 0'],axis=1)

'''
archive_df['WINE PURCHASED'] = archive_df['WINE PURCHASED'].str.strip()

#Want to strip product line info into its own column
product_lines_dict = { 'ec':'eclipse'}

#Want to strip country info into it's own column
country_tag_replacements = {'itl.':'italy'}


#Customer additions are usually labelled by ' + ' or ' - ', handle these here
archive_df['WINE PURCHASED'].str.split('+',expand=True)

wine_str_replacements = {' no oak, no so2':'', ' aging + so2': ''
                         ,' age': ' aging', ' aging':''
                         , ' 1/2 so2': '' , ' 1/4 tsp so2':'', ' 1/2 so2':'', ' 1/2 s02':'', ' 1/4 so2':'', ' no so2':'', ' no xtra so2':'', ' so2':'', ' s02':''
                         , '2 level tbsp of black pepper':'', '1 tbsp of blk pep' : '', '1.5 tbsp of blk pep' : '', '1.5 tbsp blk pep' : '', '2 tbsp of blk pep.' : '', '2 tbsp of blk pep' : '', '2 tbsp blk pep.' : '', '2 tsp blk pep' : '', '2 tsp of blk pep' : ''
                         , ' res. pak': '' , ' res pak': ''
                         , '100ml cc': '', '125ml cc':'', '150ml cc':'',' 200ml cc': '', '250 ml cc': '', '675ml cc':'', '700ml cc':'', '50ml cc': ''
                         , ' -dry': '', ' dry': ''
                         , '8gr pot. bicarb. @ stab.':''
                         , 'no oak': '', '2x oak': '', '2 x oak':'', 'unoaked': '', 'oaked':'', '+1/2 oak only':'', '120gr oak':'', '1/2 oak':''
                         , ' 45gr oak cubes':'', ' extra dark oak':'', ' 40gr dark oak':''
                         , ' 1/2 sulfites':''
                         , '1/2 f pak':'', '2/3 f pak': '', '2/3 f pak':'', '3/4 f pak only':'', 'no f pak':''
                         , ' 6.5gr global yeast energizer' :'', ' 6.4gr yst erg':'', ' 6.4gr yst eng':'', '6.4gr yst enrg':'', ' 6.5 gr yst energ':'', ' 6.5gr yst energ':'', ' 6.5gr global yst energ':''
                         , ' no skins': '', ' skins' : ''
                         , ' no ban': '', ' bann.':''
                         , ' 5gr eno blk':'', ' 10gr eno blk':'', ' 12gr eno blk':''
                         , ' 1/2 batch': '', 'half batch':''
                         , ' 6 weeks':'',' 8 weeks': ''
                         , ' lighten @ racking': ''
                         , ' 10gr granucol @ stab' :''
                         , ' 25gr bianco neve @ stab.':''
                         , ' in own barrel':''
                         , ' flav': ''
                         , 'discontinued & cancelled':''
                         , '-replacement for ec':''
                         , 'lighten colour': '', 'iighten @ stab.':'' , 'iighten @ stab':''
                         , 'less sweet':'', ' 1/2 sweet':''
                         , 'sample taken 4/25/19':''
                         , '*use new barrel':'', 'in new barrel':''
                         , ' -' : '' , ' +':'', '+':'', ' ?':'', ' only':''
                         , '1/4':'', '2/3':'', ' 23l':''}

for key, value in wine_str_replacements.items():
  archive_df['WINE PURCHASED'] = archive_df['WINE PURCHASED'].str.replace(key, value)
'''


