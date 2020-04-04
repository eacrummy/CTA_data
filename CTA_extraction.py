# -*- coding: utf-8 -*-
"""
CTA Extraction 

Created on Tue Mar 24 06:35:09 2020

@author: eacru
"""

#%% import potential relevant packages

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
# import excel spreadsheet
test = pd.read_excel("C:/Users/eacru/OneDrive/Documents/Ferguson lab data/CTA/testCTA.xlsx")
print(test)

#convert to dataframe
test.df = pd.DataFrame
#split time start and ends into two columns
test['Start'], test['End'] = test['Start'].str.split('-',1).str
print(test)
#%%
CTA_test = pd.ExcelFile("C:/Users/eacru/OneDrive/Documents/Ferguson lab data/CTA/Scores (MNN).xlsx")

CTA_test.sheet_names
CTA_test_1.sheet_names
CTA_temp = pd.read_excel(CTA_test,CTA_test.sheet_names[5])
print(CTA_temp.iloc[:,3])
#CTA_s1_group2_1_EAC = pd.DataFrame(CTA_temp.iloc[:,3:9])
#CTA_s1_group2_1_EAC.rename(columns={'Box 1':'Box 1 Start', 'Box 2': 'Box 2 Start','Box 3': 'Box 3 Start', 'Box 4': 'Box 4 Start', 'Box 5': 'Box 5 Start', 'Box 6': 'Box 6 Start'}, inplace=True)

#%%
CTA_test_1 = pd.ExcelFile("C:/Users/eacru/OneDrive/Documents/Ferguson lab data/CTA/Scores(EAC)_reformatted.xlsx")

#%%
#loop through each column and do column separation
for ind, columns in enumerate(CTA_s1_group2_1_EAC.columns):
    CTA_s1_group2_1_EAC['Box {} Start'.format(ind+1)], CTA_s1_group2_1_EAC['Box {} End'.format(ind+1)] = CTA_s1_group2_1_EAC['Box {} Start'.format(ind+1)].str.split('-',1).str
#%%
#function to prep data by splitting into dataframe each sheet, selecting columns with all of the times for each box, renaming and parsing start and end times
    def diffExtract(data):
        CTA_df = pd.DataFrame(data.iloc[:,3:9])
        CTA_df.rename(columns={'Box 1':'Box 1 Start', 'Box 2': 'Box 2 Start','Box 3': 'Box 3 Start', 'Box 4': 'Box 4 Start', 'Box 5': 'Box 5 Start', 'Box 6': 'Box 6 Start'}, inplace=True)
        return(CTA_df)
#%%

#%% 
test = pd.read_excel(CTA_test,'Session 1 274, 275, 282-285')
newtest = diffExtract(test)


timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[0])),1,2,'274-275, 282-285','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[1])),1,2,'274-275, 282-285','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[2])),1,2,'276-281','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[3])),1,2,'276-281','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[4])),2,2,'274-275, 282-285','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[5])),2,2,'274-275, 282-285','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[6])),2,2,'276-281','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[7])),2,2,'276-281','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[8])),3,2,'274-275, 282-285','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[9])),3,2,'274-275, 282-285','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[10])),3,2,'276-281','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[11])),3,2,'276-281','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[12])),4,2,'274-275, 282-285','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[13])),4,2,'274-275, 282-285','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[14])),4,2,'276-281','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[15])),4,2,'276-281','EAC')
#%%
analysisfile= pd.read_csv("C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s1_group2_1_EAC.csv")
toy = pd.DataFrame(analysisfile)
toy_string = toy.to_string()
print(toy['Box 1 Start'].to_string())

    #%%
    date_time_obj = datetime.strptime(test_start_time.to_string(),'%M:%S')



date_time_obj = datetime.strptime(toy['Box 1 Start'].to_string(),'%M:%S')
print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)

date_time_obj_2 = datetime.strptime(toy['Box 1 End'], '%M:%S')
print('Date:', date_time_obj_2.date())
print('Time:', date_time_obj_2.time())
print('Date-time:', date_time_obj_2)
#%%
toy = pd.to_datetime(analysisfile.iloc[:,1:13], format = '%M:%S')
toy
#toy = pd.to_datetime(toy.iloc[:,1:13], format='%M:%S')
#%%
from datetime import datetime
from CTA_functions import getDiff, clean_datetime, timeSeparator, diffExtract
#analysis_data = pd.read_excel()


getDiff(datetime.strptime('4:33','%M:%S'), datetime.strptime('5:43','%M:%S'))

#%%
for ind, columns in enumerate(analysisfile):
    differences = getDiff(analysisfile['Box {} Start'.format(str(columns+1))], analysisfile['Box {} End'.format(str(columns+1))])
return differences
#%%

#%%


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
    #%%
    #put differences into a new dataframe
session_differences = pd.DataFrame()
session_differences['Box 1 Differences'] = pd.Series(differences)

#%%   

#%%

#%%
    
    #sep_times.to_csv(f"C:\\Users\\eacru\\OneDrive\\Documents\\Ferguson lab data\\CTA\\CTA_s{session}_group{group}_{numbers}_{initials}.csv")
    #return sep_times
import pandas as pd
myDataFrame=diffExtract(pd.read_excel(CTA_test,CTA_test.sheet_names[0]))

#myDataFrame.head()
blah = timeSeparator(myDataFrame,1,2,'274-275, 282-285','MNN')


#%%
#MNN group 1
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[0])),1,1,'230-235','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[1])),1,1,'236-240','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[2])),2,1,'230-235','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[3])),2,1,'236-240','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[4])),3,1,'230-235','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[5])),3,1,'236-240','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[6])),4,1,'230-235','MNN')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[7])),4,1,'236-240','MNN')
#%%
#EAC Group 1
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[0])),1,1,'230-235','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[1])),1,1,'236-240','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[2])),2,1,'230-235','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[3])),2,1,'236-240','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[4])),3,1,'230-235','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[5])),3,1,'236-240','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[6])),4,1,'230-235','EAC')
timeSeparator(diffExtract(pd.read_excel(CTA_test_1,CTA_test_1.sheet_names[7])),4,1,'236-240','EAC')
