# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:10:39 2020

@author: eacru
"""

import os
import os.path
from pathlib import Path, PureWindowsPath
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv
from datetime import datetime

def clean_datetime(uncleaned_datetime):
    date_time_obj = None
    #print(uncleaned_datetime)
    if(str(uncleaned_datetime) != 'nan'):
        if(len(str(uncleaned_datetime).split(':',1)) == 2):
            date_time_obj = datetime.strptime(str(uncleaned_datetime),'%M:%S')
        else:
            date_time_obj = datetime.strptime(str(uncleaned_datetime),'%S')
    #    print('Date:', date_time_obj.date())
    #    print('Time:', date_time_obj.time())    
    #    print('Date-time:', date_time_obj)
    return date_time_obj


#analysis_data = pd.read_excel()
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

def timeSeparator(data,session, group, numbers, initials):
    df = pd.DataFrame(columns=[ 'Box Number', 'Box Start', 'Box End', 'Difference'])
    i = 0
    for ind, columns in enumerate(data):
        #print(data['Box {} Start'.format(ind+1)])
        #print(data['Box {} End'.format(ind+1)])
        
        times = data['Box {} Start'.format(ind+1)].str.split('-',1)
       
        #print(data['Box {} Start'.format(ind+1)].str.split('-',1))
        for j in range(0, len(times)):
            if(str(times[j]) == 'nan'):     
                df.loc[i] = [str(ind + 1), times[j], times[j], times[j]]
                i = i + 1
            else:
                print(times[j])
                df.loc[i] = [str(ind + 1), times[j][0], times[j][1], getDiff(clean_datetime(times[j][0]), clean_datetime(times[j][1]))]
                i = i + 1
        #sep_times = data['Box {} Start'.format(ind+1)], data['Box {} End'.format(ind+1)] = data['Box {} Start'.format(ind+1)].str.split('-',1).str
        #print(sep_times)  
    df.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s{session}_group{group}_{numbers}_{initials}_TEST.csv")
    return df

#%%
#function to prep data by splitting into dataframe each sheet, selecting columns with all of the times for each box, renaming and parsing start and end times
def diffExtract(data):
    CTA_df = pd.DataFrame(data.iloc[:,3:9])
    CTA_df.rename(columns={'Box 1':'Box 1 Start', 'Box 2': 'Box 2 Start','Box 3': 'Box 3 Start', 'Box 4': 'Box 4 Start', 'Box 5': 'Box 5 Start', 'Box 6': 'Box 6 Start'}, inplace=True)
    return(CTA_df)
#%%
#function for getting stats on bouts, time, and bouts/time
def CTA_sessionAnalysis(data,session, group, numbers, initials):
    CTA_df = pd.DataFrame(data)
#Some last cleaning
    CTA_df.drop(data.loc[CTA_df['Difference'] < 0].index, inplace=True)
    CTA_df.dropna()
    aggregations = {
    # work on the "duration" column
        'Difference': { 
        # get the sum, and call this result 'total_duration'
        'LickTime_total': 'sum',  
        # get mean, call result 'average_duration'
        'LickTime_mean': 'mean', 
        'LickCounts': 'count',
        'LickTime_median' : 'median'
        },
    }
    CTA_stats=CTA_df.groupby('Box Number').agg(aggregations)
    CTA_stats['Session']= session
    CTA_stats.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s{session}_group{group}_{numbers}_{initials}_Stats.csv")
    return(CTA_stats)
#%%
#function for percent change
 def percentChange(data1,data4, session1, session4, group, numbers, initials):
     numbers_list = ['274-275, 282-285', '276-281', '230-235','236-240']
     initials_list = ['MNN', 'EAC']
     session_1 = CTA_sessionAnalysis(data1,session1,group,numbers_list[numbers], initials_list[initials])
     session_4=  CTA_sessionAnalysis(data4,session4,group,numbers_list[numbers], initials_list[initials])
     percentchange_bout = session_4['Difference']['LickCounts'] /session_1['Difference']['LickCounts'] * 100
     percentchange_time = session_4['Difference']['LickTime_total'] /session_1['Difference']['LickTime_total']  * 100
     percentchange_avg = session_4['Difference']['LickTime_mean'] /session_1['Difference']['LickTime_mean']  * 100
     dictionary = {'PercentChange_Bouts': percentchange_bout, 'PercentChange_Time':percentchange_time, 'PercentChange_Bouts/Time':percentchange_avg}
     CTA_percentchange_MNN= pd.DataFrame(dictionary, columns =['PercentChange_Bouts', 'PercentChange_Time', 'PercentChange_Bouts/Time'])
     CTA_percentchange_MNN.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_group{group}_{numbers_list[numbers]}_{initials_list[initials]}_PercentChange.csv")
     return CTA_percentchange_MNN    