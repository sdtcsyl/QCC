# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:57:25 2019

"""

import os
import sys


filepath = os.path.abspath(os.path.dirname(sys.argv[0]))
#return the 'scripts' folder path
parpath = os.path.dirname(filepath)
#return the parent folder of the 'scripts' folder


def createfolder(folder_path):
    directory = folder_path
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


db_path = createfolder(parpath + '\\Data\\DB') + '\\'
html_path = createfolder(parpath + '\\Data\\Html') + '\\'
files_path = parpath+'\\' #createfolder(parpath + '\\Files') + '\\'
js_path = createfolder(parpath + '\\Data\\Json') + '\\'
log_path = createfolder(parpath + '\\Data\\Logging') + '\\'
source_path = createfolder(parpath + '\\Source') + '\\'