# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:55:57 2019
"""

from QCC import QCC
import QCC_Files as Files
import QCC_database as DB
import json
import requests
import math
import pandas as pd
import time
from random import randint
from datetime import datetime

def save_json(log, lat, dis, page , data_json):
    with open(Files.js_path + str(log) + '_' + str(lat) + '_' + str(dis) + '_' + str(page) + '.json', 'w') as outfile:
         json.dump(data_json['list'], outfile)

def timestamp2time(tstamp):
    try:
        if tstamp < 10**11:
            dt_object = datetime.fromtimestamp(tstamp) 
            timestamp = dt_object.strftime("%Y-%m-%d")
        else:
            dt_object = datetime.fromtimestamp(tstamp/1000)
            timestamp = dt_object.strftime("%Y-%m-%d %H:%M:%S")
    except TypeError:
        timestamp = ''
    return timestamp

def list_data(el):
    data=[el['KeyNo'],
               el['Name'],
               el['OperName'],
               el['No'],
               el['Status'],
               el['BelongOrg'], 
               el['Province'], 
               timestamp2time(el['UpdatedDate']),
               timestamp2time(el['StartDate']),
               el['EndDate'],
               el['CreditCode'],
               el['RegistCapi'],
               el['EconKind'],
               el['Address'],
               
#               '',#industry
#               '',#IndustryCode              
#               '',#SubIndustry
#               '',#SubIndustryCode
#               '',#ThirdIndustry
#               '',#ThirdIndustryCode
#               '',#ForthIndustry
#               '',#ForthIndustryCode
#               
#               '',#original name
               el['Scope'],
               el['ContactNumber'],
               el['Email'],
               el['WebSite'],
               el['ImageUrl'],
               el['OrgNo'],
               el['StartDateYear'],
               el['EnglishName'],
               el['RelativeDistance'],
               el['X'],
               el['Y'],
               el['Type'],
               el['Tag'],
               el['TelList'],
               el['Financing'],
               el['AreaCode'],
#               '',  #hit reason
               el['Flag'],
               el['InsuredCount'],
               el['CoyType'],
               el['ShortStatus']]
    return data

qcc = QCC()
url = qcc.url
header = qcc.header
cookie = qcc.cookie

xl = pd.read_excel(Files.source_path  + '20190624 ZGC_CID 17 GRIDS.xlsx',sheet_name='Sheet1',header=0)

for i in range(len(xl)):
    xl_data = tuple(xl.loc[i,:])
    xl_data = (str(xl_data[1])+'_'+str(xl_data[2])+'_'+str(xl_data[0]),)+xl_data+('0','0','1','0')
    DB.sqlwrite(xl_data,'map')

info = DB.sqlselect('map')
#info.reverse()

for inf in info:
    id_inf = inf[0]
    lat = inf[2]
    log = inf[3]
    dis = inf[1]
    page_start = int(inf[6])
    
    from_data = qcc.dict_from_data(log, lat, dis, 1)
    req = requests.post(url, headers=header, data=from_data, cookies = cookie, timeout=300)
    data_json = req.json()
    
    totalcounts = data_json['listCount']
    DB.sqlupdate(totalcounts, id_inf, 'map', 'COA')
    
    #try:
    pages = math.ceil(totalcounts/20)+1
    count = 1
    
    for page in range(page_start,pages,1):        
        from_data = qcc.dict_from_data(log, lat, dis, page)
        req = requests.post(url, headers=header, data=from_data, cookies = cookie, timeout=300)
        data_json = req.json()
        save_json(log, lat, dis, page, data_json)
        
        for i, el in enumerate(data_json['list']):
           data = list_data(el) #list(el.values())
           try:
               industry = list(el['Industry'].values())
           except:
               industry = []
           finally:
               industry = industry+(['' for _ in range(8-len(industry))])
               temp = industry[1]
               industry[1] = industry[0]
               industry[0] = temp               
           
#           try:
#               Industry  = el['Industry']['Industry']
#               IndustryCode  = el['Industry']['IndustryCode']
#           except (KeyError, TypeError):
#               Industry = IndustryCode = ''
#           try:
#               SubIndustry  = el['Industry']['SubIndustry']
#               SubIndustryCode  = el['Industry']['SubIndustryCode']
#           except (KeyError, TypeError):
#               SubIndustry = SubIndustryCode = ''
#           try:
#               ThirdIndustry  = el['Industry']['ThirdIndustry']
#               ThirdIndustryCode  = el['Industry']['ThirdIndustryCode']
#           except (KeyError, TypeError):
#               ThirdIndustry = ThirdIndustryCode = ''
#           try:
#               ForthIndustry  = el['Industry']['ForthIndustry']
#               ForthIndustryCode  = el['Industry']['ForthIndustryCode']
#           except (KeyError, TypeError):
#               ForthIndustry = ForthIndustryCode = ''

           try:    
               hitreason = el['HitReason']['Field']+'@'+el['HitReason']['Value']
           except KeyError:
               hitreason = '@'
               
           try:
               originalName = str(el['OriginalName'])
           except KeyError:
               originalName = ''
               
           data_tuple = (str(log)+'_'+str(lat)+'_'+data[0]+'_'+data[10],) + tuple(data[0:14]) + \
           tuple(industry) + (originalName,) +\
           tuple(data[14:32])+ (hitreason,) + tuple(data[32:37])+(id_inf, str(page), str(count),)
           DB.sqlwrite(data_tuple, 'vendor') 
           count = count + 1
        
        DB.sqlupdate(page, id_inf, 'map', 'page')   
        time.sleep(randint(40,90))   

    count_db = DB.sqlcheck(id_inf, 'vendor')
    DB.sqlupdate(count_db, id_inf, 'map', 'COF')
    if count_db == totalcounts:
        DB.sqlupdate('1', id_inf, 'map', 'NY')
    #except TypeError:
    #    DB.sqlupdate('2', id_inf, 'map', 'NY')  # 2 means no data
    
#step 4, output control sheet
file = pd.ExcelWriter(Files.db_path + '_QCC.xlsx')
output = DB.sqloutput('vendor')
output_excel = pd.DataFrame(output,columns = ['Id','KeyNo','Name','OperName','No', 'Status', 'BelongOrg', 'Province', 'UpdatedDate', 'StartDate','EndDate','CreditCode','RegistCapi','EconKind','Address','Industry','IndustryCode','SubIndustry','SubIndustryCode','ThirdIndustry','ThirdIndustryCode','ForthIndustry','ForthIndustryCode','OriginalName','Scope','ContactNumber','Email','WebSite','ImageUrl','OrgNo','StartDateYear','EnglishName','RelativeDistance','X','Y','Type','Tag','TelList','Financing','AreaCode','HitReason','Flag','InsuredCount','CoyType','ShortStatus','lat_lng_dis','page','count'])
output_excel.to_excel(file,sheet_name='vendor',index=False)
output = DB.sqloutput('map')
output_excel = pd.DataFrame(output,columns = ['Id', 'radius','lat','lng','CoA','CoF','page','NY'])
output_excel.to_excel(file,sheet_name='Control',index=False)
file.save()
    