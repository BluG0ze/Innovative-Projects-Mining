#coding=UTF-8
#############################################
#File name: kmeans.py
#Author: LiteA
#Mail: vshionagisa@gmail.com
#Function: Kmeans Cluster
##############################################
#calculate TF-IDF valuses，use Kmeans to cluster
import os
import codecs
import MySQLdb
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn import metrics

def calculate_result(actual, pred):
    m_precision = metrics.precision_score(actual, pred)
    m_recall = metrics.recall_score(actual, pred)
    print 'predict info:'
    print 'precision:{0:.3f}'.format(m_precision)
    print 'recall:{0:0.3f}'.format(m_recall)
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual, pred))

#connect database
conn = MySQLdb.connect (
        host = '',
        port = 3306,
        user = '',
        passwd = '',
        db = '',
        charset = 'utf8'
)
cur = conn.cursor()

corpus = []

#put text data into corpus
for i in range (22, 1862):
    sqlComm1 = 'SELECT `tag` FROM `BUPTcreate` WHERE `id` =' + '%d' %i
    cur.execute(sqlComm1)

    data = cur.fetchone()
    if data :
        s = ''.join(tuple(data))
        corpus.append(s)

#transfer text data into tf-idf matrix
vectorizer = CountVectorizer()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
word = vectorizer.get_feature_names()
weight = tfidf.toarray()

print 'Totally i text:',len(weight)
print 'Totally j terms:',len(word)

print '*************\nK-Means\n*************'

#K-Means cluster
path = '~/python/'
if not os.path.isfile('tmp_info.txt'):
    os.mknod("tmp_info.txt")
fp = codecs.open("tmp_info.txt","w","utf-8")

#K is 2 to 11，write into file
for l in range(2, 11):
    #cluster
    pred = KMeans(n_clusters = l)
    pred.fit(weight)

    #cluster results
    Centers = pred.cluster_centers_

    Labels = pred.labels_

    Labels = Labels.tolist()

    #write into file
    str = u'一共%d类时：\n'%l
    fp.write(str)

    for i in range (0,l):
        centers_temp = Centers[i]
        centers_sub = range (0,len(word))
        for j in range (0,10):
            for k in range (0,len(word)-j-1):
                if centers_temp[k] > centers_temp[k+1]:
                    (centers_temp[k], centers_temp[k+1]) = (centers_temp[k+1], centers_temp[k])
                    (centers_sub[k], centers_sub[k+1]) = (centers_sub[k+1], centers_sub[k])

        num_i_labels = 0
        num_i_labels = Labels.count(i)

        str = u'    第%d类共有%d个项目，标签为：\n' %(i, num_i_labels)
        fp.write(str)
        #print str
        for j in range (0,10):
            str = u'        %s  %f  %d\n' %(word[centers_sub[len(word)-j-1]], centers_temp[len(word)-j-1], centers_sub[len(word)-j-1])
            fp.write(str)
            #print str
    fp.write(u'\n')

fp.close()

cur.close()
conn.commit()
conn.close()
