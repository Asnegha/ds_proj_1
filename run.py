# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:06:47 2022

@author: snegh
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/snegh/Desktop/Data_science/ds_proj_1/chromedriver"

df = gs.get_jobs('data scientist', 5, False , path, 10)