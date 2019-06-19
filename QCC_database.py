# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:02:05 2019
"""


import sqlite3
import QCC_Files as Files

def sqlwrite(data, table):    
    conn = sqlite3.connect(Files.db_path + 'QCC.db')
    cursor = conn.cursor()
    try:
        if table == 'vendor':
            cursor.execute('''create table if not exists table_''' + 
                           table + 
                           '''(
                           id varchar(5) primary key,
                           KeyNo varchar(5),
                           Name varchar(5),
                           OperName varchar(5),
                           No varchar(5), 
                           Status varchar(5), 
                           BelongOrg varchar(5), 
                           Province varchar(5), 
                           UpdatedDate varchar(5), 
                           StartDate varchar(5),
                           EndDate varchar(5),
                           CreditCode varchar(5),
                           RegistCapi varchar(5),
                           EconKind varchar(5),
                           Address varchar(5),
                           
                           Industry varchar(5),
                           IndustryCode varchar(5),                           
                           SubIndustry varchar(5),
                           SubIndustryCode varchar(5),
                           ThirdIndustry varchar(5),
                           ThirdIndustryCode varchar(5),
                           ForthIndustry varchar(5),
                           ForthIndustryCode varchar(5),
                           
                           OriginalName varchar(5),
                           Scope varchar(20),
                           ContactNumber varchar(5),
                           Email varchar(5),
                           WebSite varchar(5),
                           ImageUrl varchar(5),
                           OrgNo varchar(5),
                           StartDateYear varchar(5),
                           EnglishName varchar(5),
                           RelativeDistance varchar(3),
                           X varchar(3),
                           Y varchar(3),
                           Type varchar(3),
                           Tag varchar(3),
                           TelList varchar(3),
                           Financing varchar(3),
                           AreaCode varchar(3),
                           HitReason varchar(3),
                           Flag varchar(3),
                           InsuredCount varchar(3),
                           CoyType varchar(3),
                           ShortStatus varchar(3),
                           lat_lng_dis varchar(10),
                           page charvar(3),
                           count charvar(3)
                           )''') 
            cursor.execute('''insert into table_''' + 
                           table + 
                           '''(id,
                           KeyNo,
                           Name,
                           OperName,
                           No, 
                           Status, 
                           BelongOrg, 
                           Province, 
                           UpdatedDate, 
                           StartDate,
                           EndDate,
                           CreditCode,
                           RegistCapi,
                           EconKind,
                           Address,
                           
                           Industry,
                           IndustryCode,                           
                           SubIndustry,
                           SubIndustryCode,
                           ThirdIndustry,
                           ThirdIndustryCode,
                           ForthIndustry,
                           ForthIndustryCode,
                           
                           OriginalName,
                           Scope,
                           ContactNumber,
                           Email,
                           WebSite,
                           ImageUrl,
                           OrgNo,
                           StartDateYear,
                           EnglishName,
                           RelativeDistance,
                           X,
                           Y,
                           Type,
                           Tag,
                           TelList,
                           Financing,
                           AreaCode,
                           HitReason,
                           Flag,
                           InsuredCount,
                           CoyType,
                           ShortStatus,
                           lat_lng_dis,
                           page,
                           count) 
                           values (?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,? )''', 
                           (data))
        elif table == 'map': 
            cursor.execute('''create table if not exists table_''' + 
                           table + 
                           '''(
                           Id varchar(8) primary key,
                           radius varchar(2),
                           lat varchar(2), 
                           lng varchar(2),
                           COA varchar(2),
                           COF varchar(2),
                           page varchar(2),
                           NY varcar(2)
                           )''') 
            cursor.execute('''insert into table_''' + 
                           table + 
                           '''(
                           Id, 
                           radius,
                           lat,
                           lng,
                           CoA,
                           CoF,
                           page,
                           NY) 
                           values (?,?,?,?,?, ?,?,?)''', 
                           (data)) 
    except sqlite3.IntegrityError:
        pass
    cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()

def sqlselect(table, **args):    
    conn = sqlite3.connect(Files.db_path + 'QCC.db')
    cursor = conn.cursor()
    if table == 'map' :
        cursor.execute('''create table if not exists table_''' + 
                       table + 
                       '''(Id varchar(50) primary key,
                           radius varchar(20),
                           lat varchar(30), 
                           lng varchar(2),
                           COA varchar(2),
                           COF varchar(2),
                           page varchar(2),
                           NY varcar(2)
                       )''') 
        cursor.execute('SELECT * FROM table_' + table + ' WHERE NY = 0')    
    res =cursor.fetchall()
    suc = res
    cursor.close()
    conn.commit()
    conn.close() 
    return suc
    

def sqlupdate(count, dl, table, record):    
    conn = sqlite3.connect(Files.db_path + 'QCC.db')
    cursor = conn.cursor()
    if table == 'map':
        if record == 'COA':
            cursor.execute('UPDATE table_' + table + ' SET COA = ?  WHERE Id = ?',(count, dl,))
        elif record == 'COF':    
            cursor.execute('UPDATE table_' + table + ' SET COF = ?  WHERE Id = ?',(count, dl,))
        elif record == 'NY':    
            cursor.execute('UPDATE table_' + table + ' SET NY = ?  WHERE Id = ?',(count, dl,))
        elif record == 'page':    
            cursor.execute('UPDATE table_' + table + ' SET page = ?  WHERE Id = ?',(count, dl,))
    cursor.close()
    conn.commit()
    conn.close() 

def sqlcheck(dl, table):
    conn = sqlite3.connect(Files.db_path + 'QCC.db')
    cursor = conn.cursor()
    if table == 'vendor':
            cursor.execute('''create table if not exists table_''' + 
                           table + 
                           '''(
                           id varchar(5) primary key,
                           KeyNo varchar(5),
                           Name varchar(5),
                           OperName varchar(5),
                           No varchar(5), 
                           Status varchar(5), 
                           BelongOrg varchar(5), 
                           Province varchar(5), 
                           UpdatedDate varchar(5), 
                           StartDate varchar(5),
                           EndDate varchar(5),
                           CreditCode varchar(5),
                           RegistCapi varchar(5),
                           EconKind varchar(5),
                           Address varchar(5),
                           
                           Industry varchar(5),
                           IndustryCode varchar(5),                           
                           SubIndustry varchar(5),
                           SubIndustryCode varchar(5),
                           ThirdIndustry varchar(5),
                           ThirdIndustryCode varchar(5),
                           ForthIndustry varchar(5),
                           ForthIndustryCode varchar(5),
                           
                           OriginalName varchar(5),
                           Scope varchar(20),
                           ContactNumber varchar(5),
                           Email varchar(5),
                           WebSite varchar(5),
                           ImageUrl varchar(5),
                           OrgNo varchar(5),
                           StartDateYear varchar(5),
                           EnglishName varchar(5),
                           RelativeDistance varchar(3),
                           X varchar(3),
                           Y varchar(3),
                           Type varchar(3),
                           Tag varchar(3),
                           TelList varchar(3),
                           Financing varchar(3),
                           AreaCode varchar(3),
                           HitReason varchar(3),
                           Flag varchar(3),
                           InsuredCount varchar(3),
                           CoyType varchar(3),
                           ShortStatus varchar(3),
                           lat_lng_dis varchar(10),
                           page charvar(3),
                           count charvar(3)
                           )''') 
            cursor.execute('SELECT * FROM table_' + table + ' WHERE lat_lng_dis = ?',(dl,))    
    res =cursor.fetchall()
    suc = len(res)
    cursor.close()
    conn.commit()
    conn.close() 
    return suc      


