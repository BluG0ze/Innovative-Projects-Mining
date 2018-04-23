#coding=UTF-8
#############################################
#File name: Spider4pros.py
#Author: LiteA
#Mail: vshionagisa@gmail.com
#Function: spider all pages
##############################################

import first_dev
import MySQLdb
import string
import re
import time
URLbase = 'http://lcin.scs.bupt.cn/innovation/projectinfo.aspx?id='

conn = MySQLdb.connect (
        host = '',
        port = 3306,
        user = '',
        passwd = '',
        db = 'dataMiningDB',
        charset = 'utf8'
        )
cur = conn.cursor()

for i in range(1,4452):
    URL = URLbase + '%d' %i
    SigleWeb = first_dev.Sigle_Spider(URL,False,{})
    SigleWeb.getInfoDic()
    #print SigleWeb.projectInfo['Name'].encode('UTF-8')
    if SigleWeb.isEmpty :
        del SigleWeb
        time.sleep(3)
        continue
    else:
        Intro = SigleWeb.projectInfo['Intro'].encode('UTF-8')
        Intro = re.sub('&nbsp', ' ', Intro)
        sqli = '''INSERT INTO `dataMiningDB`.`BUPTcreate` (`id`, `name`, `level`, `school`, `year`, `teacher`, `members`, `intro`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
        cur.execute(sqli, ('',
                           SigleWeb.projectInfo['Name'].encode('UTF-8'),
                           SigleWeb.projectInfo['Level'].encode('UTF-8'),
                           SigleWeb.projectInfo['School'].encode('UTF-8'),
                           SigleWeb.projectInfo['Year'].encode('UTF-8'),
                           SigleWeb.projectInfo['Teacher'].encode('UTF-8'),
                           SigleWeb.projectInfo['Members'].encode('UTF-8'),
                           Intro
                           ))
        del SigleWeb
        time.sleep(3)
cur.close()
conn.commit()
conn.close()
