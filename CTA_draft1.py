# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:24:10 2020

@author: eacru
"""
#%%
import os
import os.path
from pathlib import Path, PureWindowsPath
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv
from datetime import datetime
#%%
CTA_test = pd.ExcelFile("C:/Users/eacru/OneDrive/Documents/Ferguson lab data/CTA/Scores (MNN).xlsx")
CTA_test.sheet_names
CTA_list=[]
for name in CTA_test.sheet_names:
    df = pd.read_excel(CTA_test, name)
#%%
#function to prep data by splitting into dataframe each sheet, selecting columns with all of the times for each box, renaming and parsing start and end times
def diffExtract(data):
    CTA_df = pd.DataFrame(data.iloc[:,3:9])
    CTA_df.rename(columns={'Box 1':'Box 1 Start', 'Box 2': 'Box 2 Start','Box 3': 'Box 3 Start', 'Box 4': 'Box 4 Start', 'Box 5': 'Box 5 Start', 'Box 6': 'Box 6 Start'}, inplace=True)
    return(CTA_df)
#%%
def timeSeparator(data,session, group, numbers, initials):
    for ind, columns in enumerate(data):
        sep_times = data['Box {} Start'.format(ind+1)], data['Box {} End'.format(ind+1)] = data['Box {} Start'.format(ind+1)].str.split('-',1).str
    sep_times.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s{session}_group{group}_{numbers}_{initials}.csv")
    return sep_times
#%%
#Batch generate csv files for future analyses

#%%
def getDiff(date_time_obj, date_time_obj_2):
    if(date_time_obj == None or date_time_obj_2 == None):
        return None
    difference = None
    if(date_time_obj_2.minute == 0):
        difference = date_time_obj_2.second - date_time_obj.second
    else:
        difference = (date_time_obj_2 - date_time_obj).seconds
        
    print(difference)
    return difference
#%%
def clean_datetime(uncleaned_datetime):
    date_time_obj = None
    #print(uncleaned_datetime)
    if(str(uncleaned_datetime) != 'nan'):
        date_time_obj = datetime.strptime(str(uncleaned_datetime),'%M:%S')
    #    print('Date:', date_time_obj.date())
    #    print('Time:', date_time_obj.time())    
    #    print('Date-time:', date_time_obj)
    return date_time_obj

start_times = []
for test_start_time in toy['Box 1 Start']:    
    start_times.append(clean_datetime(test_start_time))

print(len(start_times))

end_times = []
for test_end_time in toy['Box 1 End']:
    end_times.append(clean_datetime(test_end_time))
    
print(len(end_times))
differences = []
for i in range (0, len(start_times)):
    print(getDiff(start_times[i], end_times[i]))
    differences.append(getDiff(start_times[i], end_times[i]))