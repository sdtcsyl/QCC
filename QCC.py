# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:23:13 2019
"""
class QCC:
    def __init__(self):
        #The cookie part should be changed since it varies in differrent PC
        self.cookie = {
                'QCCSESSID':'2fkgvm3pehil78236eku47lfh7', 
                'UM_distinctid':'16b6580731d557-043ea8da44a0d3-3b654406-e1000-16b6580731e4c2',
                'CNZZDATA1254842228':'1232614891-1560773264-%7C1560773264',
                'zg_did':'%7B%22did%22%3A%20%2216b658073e436a-0da4538c7bb324-3b654406-e1000-16b658073e5744%22%7D',
                'hasShow':'1',
                'Hm_lvt_3456bee468c83cc63fb5147f119f1075':'1560776046',
                '_uab_collina':'156077604564474956606763',
                'acw_tc':'701dc8ce15607760433774907e24ef816f1ef03ca2bc3c8a45d30fa2ae',        
                'Hm_lpvt_3456bee468c83cc63fb5147f119f1075':'1560776190',  
                'acw_sc__v3':'5d0792faed04b77595fed427c078638496952010',
                'acw_sc__v2':'5d0792f7410b8da59a86353fe1f0a235d4666f70',
                # the below item will change every time. the above items still stay the same when they are set at the first time.
                'zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f':'%7B%22sid%22%3A%201560867253543%2C%22updated%22%3A%201560867265043%2C%22info%22%3A%201560776045549%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%224c2c67fe8492e168ff683117aedcc767%22%7D'
                }
        
        self.header = {
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                  'Referer':'https://www.qichacha.com/map',
                  'Origin':'https://www.qichacha.com',
                  'Host': 'www.qichacha.com',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9',
                  'Connection': 'keep-alive',
                  'Content-Length': '347',
                  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                  'X-Requested-With': 'XMLHttpRequest'          
                  } 
        
        self.url = 'https://www.qichacha.com/map_searchByLocation'
    
    def dict_from_data(self, log, lat, dis, page):
        from_data = {
            'searchType': 'multiple',
            'longitude': log, #116.324847,
            'latitude': lat, #40.015998,
            'searchKey': None,
            'pageSize': 10,
            'pageIndex': page, #2,
            'distance': dis, #0.774,
            'startDateBegin': None,
            'startDateEnd': None,
            'registCapiBegin':None, 
            'registCapiEnd': None,
            'industryCode': None,
            'subIndustryCode': 0,
            'statusCode': None,
            'isSortAsc': None,
            'sortField': None,
            'orgType': None,
            'coyType': None,
            'flagT': None,
            'flagMN': None,
            'flagE': None,
            'flagGW': None,
            'flagM': None,
            'flagP': None,
            'flagF': None,
            'flagK': None,
            'flagS': None,
            'flagC': None,
            'flagSC': None,
            'insuredCnt': None
            }
        return from_data
    
    
