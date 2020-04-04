# -*- coding: utf-8 -*-
"""
CTA Analysis
Created on Thu Mar 26 08:50:07 2020

@author: eacru
"""
#%% 
#Import relevant packages (or potentially relevant)
import os
import os.path
from pathlib import Path, PureWindowsPath
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv

#%%
#Read in csv file
CTA11MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s1_group2_274-275, 282-285_MNN_TEST.csv")
CTA11EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s1_group2_274-275, 282-285_EAC_TEST.csv")
CTA12MNN = pd.read_csv("C:\\Users\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\CTA_s1_group2_276-281_MNN_TEST.csv")
CTA12EAC = pd.read_csv("C:\\Users\eacru\OneDrive\\Documents\\Ferguson lab data\\CTA\CTA_s1_group2_276-281_EAC_TEST.csv")
CTA21MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s2_group2_274-275, 282-285_MNN_TEST.csv")
CTA21EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s2_group2_274-275, 282-285_EAC_TEST.csv")
CTA22MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s2_group2_276-281_MNN_TEST.csv")
CTA22EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s2_group2_276-281_EAC_TEST.csv")
CTA31MNN= pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s3_group2_274-275, 282-285_MNN_TEST.csv")
CTA31EAC=pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s3_group2_274-275, 282-285_EAC_TEST.csv")
CTA32MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s3_group2_276-281_MNN_TEST.csv")
CTA32EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\Ferguson lab data\\CTA\\CTA_s3_group2_276-281_EAC_TEST.csv")
CTA41MNN = pd.read_csv("C:\\Users\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\CTA_s4_group2_274-275, 282-285_MNN_TEST.csv")
CTA41EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s4_group2_274-275, 282-285_EAC_TEST.csv")
CTA42MNN=pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s4_group2_276-281_MNN_TEST.csv")
CTA42EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s4_group2_276-281_EAC_TEST.csv")
#Convert to df
CTA_df = pd.DataFrame(CTA)
#Some last cleaning
CTA_df.drop(CTA_df.loc[CTA_df['Difference'] < 0].index, inplace=True)
CTA_df.dropna()

 
#%%
#Group 1 read in files
CTA11MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s1_group1_230-235_MNN_TEST.csv")
CTA12MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s1_group1_236-240_MNN_TEST.csv")
CTA21MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s2_group1_230-235_MNN_TEST.csv")
CTA22MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s2_group1_236-240_MNN_TEST.csv")
CTA31MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s3_group1_230-235_MNN_TEST.csv")
CTA32MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s3_group1_236-240_MNN_TEST.csv")
CTA41MNN = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s4_group1_230-235_MNN_TEST.csv")
CTA42MNN=pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s4_group1_236-240_MNN_TEST.csv")
#%%
#Group one EAC files
CTA11EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s1_group1_230-235_EAC_TEST.csv")
CTA12EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s1_group1_236-240_EAC_TEST.csv")
CTA21EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s2_group1_230-235_EAC_TEST.csv")
CTA22EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s2_group1_236-240_EAC_TEST.csv")
CTA31EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s3_group1_230-235_EAC_TEST.csv")
CTA32EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s3_group1_236-240_EAC_TEST.csv")
CTA41EAC = pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s4_group1_230-235_EAC_TEST.csv")
CTA42EAC=pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s4_group1_236-240_EAC_TEST.csv")
#%%
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
print(CTA_stats)
CTA_stats['Session']= 1
#%%
CTA_stats.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\Test.csv")
#%% 
#generate function using all of these fun things
def CTA_sessionAnalysis(data,session, group, numbers, initials):
    numbers_list = ['274-275, 282-285', '276-281','230-235','236-240']
    initials_list = ['MNN', 'EAC']
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
    CTA_stats.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s{session}_group{group}_{numbers_list[numbers]}_{initials_list[initials]}_Stats.csv")
    return(CTA_stats)
#%%
#numbers = ['274-275, 282-285', '276-281']
#initials = ['MNN', 'EAC']
CTA_sessionAnalysis(CTA11MNN,1,2,numbers[0],initials[0])
CTA_sessionAnalysis(CTA11EAC,1,2,0,1)
CTA_sessionAnalysis(CTA12MNN,1,2,numbers[1],initials[0])
CTA_sessionAnalysis(CTA12EAC,1,2,1,1)
CTA_sessionAnalysis(CTA21MNN,2,2,numbers[0],initials[0])
CTA_sessionAnalysis(CTA21EAC,2,2,numbers[0],initials[1])
CTA_sessionAnalysis(CTA22MNN,2,2,numbers[1],initials[0])
CTA_sessionAnalysis(CTA22EAC,2,2,numbers[1],initials[1])
CTA_sessionAnalysis(CTA31MNN,3,2,numbers[0],initials[0])
CTA_sessionAnalysis(CTA31EAC,3,2,numbers[0],initials[1])
CTA_sessionAnalysis(CTA32MNN,3,2,numbers[1],initials[0])
CTA_sessionAnalysis(CTA32EAC,3,2,numbers[1],initials[1])
CTA_sessionAnalysis(CTA41MNN,4,2,numbers[0],initials[0])
CTA_sessionAnalysis(CTA41EAC,4,2,0,1)
CTA_sessionAnalysis(CTA42MNN,4,2,1,0)
CTA_sessionAnalysis(CTA42EAC,4,2,1,1)
#%%
#Group 1
CTA_sessionAnalysis(CTA11MNN,1,1,2,0)
CTA_sessionAnalysis(CTA12MNN,1,1,3,0)
CTA_sessionAnalysis(CTA21MNN,2,1,2,0)
CTA_sessionAnalysis(CTA22MNN,2,1,3,0)
CTA_sessionAnalysis(CTA31MNN,3,1,2,0)
CTA_sessionAnalysis(CTA32MNN,3,1,3,0)
CTA_sessionAnalysis(CTA41MNN,4,1,2,0)
CTA_sessionAnalysis(CTA42MNN,4,1,3,0)
#%%
#Group 1 EAC
CTA_sessionAnalysis(CTA11EAC,1,1,2,1)
CTA_sessionAnalysis(CTA12EAC,1,1,3,1)
CTA_sessionAnalysis(CTA21EAC,2,1,2,1)
CTA_sessionAnalysis(CTA22EAC,2,1,3,1)
CTA_sessionAnalysis(CTA31EAC,3,1,2,1)
CTA_sessionAnalysis(CTA32EAC,3,1,3,1)
CTA_sessionAnalysis(CTA41EAC,4,1,2,1)
CTA_sessionAnalysis(CTA42EAC,4,1,3,1)
#%%
#Get percent change between s1 and s4

    
session_1_1 = CTA_sessionAnalysis(CTA11MNN,1,2,numbers_list[0],initials_list[0])
session_4_1 = CTA_sessionAnalysis(CTA41MNN,4,2,numbers_list[0],initials_list[0])

percentchange_2_1_bout = (session_4_1['Difference']['LickCounts'] - session_1_1['Difference']['LickCounts']) /session_1_1['Difference']['LickCounts'] * 100
percentchange_2_1_time = (session_4_1['Difference']['LickTime_total'] - session_1_1['Difference']['LickTime_total'] ) /session_1_1['Difference']['LickTime_total']  * 100
percentchange_2_1_avg = (session_4_1['Difference']['LickTime_mean'] - session_1_1['Difference']['LickTime_mean'] ) /session_1_1['Difference']['LickTime_mean']  * 100

dictionary = {'PercentChange_Bouts': percentchange_2_1_bout, 'PercentChange_Time':percentchange_2_1_time, 'PercentChange_Bouts/Time':percentchange_2_1_avg}
CTA_percentchange_MNN= pd.DataFrame(dictionary, columns =['PercentChange_Bouts', 'PercentChange_Time', 'PercentChange_Bouts/Time'])
CTA_percentchange_MNN.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_group{group}_{numbers}_{initials}_PercentChange.csv")
 #%%
 def percentChange(data1,data4, session1, session4, group, numbers, initials):
     numbers_list = ['274-275, 282-285', '276-281','230-235','236-240']
     initials_list = ['MNN', 'EAC']
     session_1 = CTA_sessionAnalysis(data1,session1,group,numbers, initials)
     session_4=  CTA_sessionAnalysis(data4,session4,group,numbers, initials)
     percentchange_bout = session_4['Difference']['LickCounts'] /session_1['Difference']['LickCounts'] * 100
     percentchange_time = session_4['Difference']['LickTime_total'] /session_1['Difference']['LickTime_total']  * 100
     percentchange_avg = session_4['Difference']['LickTime_mean'] /session_1['Difference']['LickTime_mean']  * 100
     dictionary = {'PercentChange_Bouts': percentchange_bout, 'PercentChange_Time':percentchange_time, 'PercentChange_Bouts/Time':percentchange_avg}
     CTA_percentchange_MNN= pd.DataFrame(dictionary, columns =['PercentChange_Bouts', 'PercentChange_Time', 'PercentChange_Bouts/Time'])
     CTA_percentchange_MNN.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_group{group}_{numbers_list[numbers]}_{initials_list[initials]}_PercentChange.csv")
     return CTA_percentchange_MNN
 #%%
 #CTA_change_2_2 = percentChange(CTA12MNN,CTA42MNN,1,4,2,1,0)
 CTA_change_1_1 = percentChange(CTA11EAC,CTA41EAC,1,4,1,0,1)
CTA_change_1_2 = percentChange(CTA12EAC,CTA42EAC,1,4,1,1,1)  