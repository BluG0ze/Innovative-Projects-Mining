#coding=utf8
#############################################
#File name: fenci.py
#Author: LiteA
#Mail: vshionagisa@gmail.com
#Function: cut up words of each project's intro
##############################################

import MySQLdb
import jieba
import re

conn = MySQLdb.connect (
        host = '',
        port = 3306,
        user = '',
        passwd = '',
        db = '',
        charset = 'utf8'
)
cur = conn.cursor()

for i in range (22, 1862):
    sqlComm1 = 'SELECT `name`, `intro` FROM `BUPTcreate` WHERE `id` =' + '%d' %i
    cur.execute(sqlComm1)

    data = cur.fetchone()
    if data :
        s = ''.join(tuple(data))

        s = re.sub('&nbsp', '', s)

        token = ["'","`","，","。","！","？","：","；","、","/","\n","\\"
                 ,"(",")","[","]","{","}","【","】","（","）","“","”",'"',
                 '"',".","1","2","3","4","5","6","7","8","9","0","?","<",
                 ">","《","》","①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","-",
                 "_","——","—","的","我们","要","自己","之","将","后","应","到",
                 "某","个","是","中","或","基于","其","使","在","被","对","与",
                 "和","它","并"," ",","]

        for j in range(0,len(token)):
            token[j] = token[j].decode('utf-8')

        result = []

        seg_list = jieba.cut(s, cut_all = False)
        for seg in seg_list :
            seg = ''.join(seg.split())
            if (seg not in token):
                result.append(seg)
        resultStr = ' '.join(result)

        sqlComm2 = "UPDATE  `BUPTcreate` SET  `tag` =  '"+ resultStr + "'WHERE  `id` =" + '%d' %i

        cur.execute(sqlComm2)

        #print resultStr
        print "%d Updates sucessfully" %i
    else:
        print "%d is empty" %i
cur.close()
conn.commit()
conn.close()
