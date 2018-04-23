#coding=UTF-8
#############################################
#File name: naive_bayes.py
#Author: LiteA
#Mail: vshionagisa@gmail.com
#Function: Naive Bayes Classifier
##############################################
#calculate TF-IDF value of training set and testing set，use Naive Bayes to classify
import numpy as np
import MySQLdb
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

def calculate_result(actual, pred):
    m_precision = metrics.precision_score(actual, pred)
    m_recall = metrics.recall_score(actual, pred)
    print 'predict info:'
    print 'precision:{0:.3f}'.format(m_precision)
    print 'recall:{0:0.3f}'.format(m_recall)
    print 'f1-score:{0:.3f}'.format(metrics.f1_score(actual, pred))

def trainNtest_set(classifyName):
    #-----------------------------------all-----------------------------------------
    corpus_all = []

    for i in range (22, 1862):
        sqlComm1 = 'SELECT `tag` FROM `BUPTcreate` WHERE `id` =' + '%d' %i
        cur.execute(sqlComm1)

        data = cur.fetchone()
        if data :
            s = ''.join(tuple(data))
            corpus_all.append(s)

    vectorizer = TfidfVectorizer()
    tfidf_all = vectorizer.fit_transform(corpus_all)
    print "the shape of all sets is "+repr(tfidf_all.shape)

    #-----------------------------------train----------------------------------------
    corpus_train = []

    sqlComm1 = "SELECT  `tag`  FROM  `BUPTcreate`  WHERE  `year`  IN ( '2008',  '2011',  '2012', '2013')  ORDER BY  `id` "
    cur.execute(sqlComm1)

    data = cur.fetchall()
    if data :
        for temp in data:
            s = ''.join(temp)
            corpus_train.append(s)

    tfidf_train = vectorizer.transform(corpus_train)
    print "the shape of train set is "+repr(tfidf_train.shape)


    target_train = []

    sqlComm2 = "SELECT  `%s`  FROM  `BUPTcreate`  WHERE  `year`  IN ( '2008', '2011',  '2012', '2013')  ORDER BY  `id` " %classifyName
    cur.execute(sqlComm2)

    data = cur.fetchall()
    if data :
        for temp in data:
            target_train = target_train + list(temp)

    #------------------------------------test-----------------------------------------

    corpus_test = []

    sqlComm1 = "SELECT  `tag`  FROM  `BUPTcreate`  WHERE  `year`  IN ( '2009',  '2010')  ORDER BY  `id` "
    cur.execute(sqlComm1)

    data = cur.fetchall()
    if data :
        for temp in data:
            s = ''.join(temp)
            corpus_test.append(s)

    tfidf_test = vectorizer.transform(corpus_test)

    print "the shape of test set is "+repr(tfidf_test.shape)


    target_test = []

    sqlComm2 = "SELECT  `%s`  FROM  `BUPTcreate`  WHERE  `year`  IN ( '2009', '2010')  ORDER BY  `id` " %classifyName
    cur.execute(sqlComm2)

    data = cur.fetchall()
    if data :
        for temp in data:
            target_test = target_test + list(temp)

    return (tfidf_train.toarray(), np.array(target_train), tfidf_test.toarray(), np.array(target_test), vectorizer)

def findBestAlpha(tfidf_train, target_train, tfidf_test, target_test):
    #------------------------------------naive_bayes----------------------------------

    print '*************************\nNaive Bayes\n*************************'

    ans = 0;
    fl = 0.01
    for i in range(1, 1000):
        fl = fl + 0.01
        clf = MultinomialNB(alpha = fl, class_prior=None, fit_prior=True)
        clf.fit(tfidf_train, target_train)
        pred = clf.predict(tfidf_test)
        m_precision = metrics.precision_score(target_test, pred)
        m_recall = metrics.recall_score(target_test, pred)
        m_f1_score = metrics.f1_score(target_test, pred)
        f_temp = (m_f1_score + m_precision + m_recall)
        if f_temp > ans:
            ans = f_temp
            fl_temp = fl
            (a,b,c) = (m_precision, m_recall, m_f1_score)

    print a
    print b
    print c
    print fl_temp

    return fl_temp

def predictTest(BestAlpha, tfidf_train, target_train, tfidf_test, target_test):
    clf = MultinomialNB(alpha = BestAlpha)#GaussianNB()
    clf.fit(tfidf_train, target_train)
    pred = clf.predict(tfidf_test)

    calculate_result(target_test, pred)

    #print pred

    print "Multinomial Naive Bayes has set up successfully!\n"

    #print np.array(target_test)

    return clf

def ClassifyRest(vectorizer, clf, classifyName):
    #---------------------------------classify the rest of data-------------------------
    sqlComm5 = "SELECT `id` FROM `BUPTcreate` WHERE `year` in ('2014','2015') order by `id`"
    cur.execute(sqlComm5)
    data = cur.fetchall()

    restId = []

    if data:
        for temp in data:
            restId = restId + list(temp)
    print restId

    #idtemp = [1145, 1147, 1150, 1151, 1152, 1153, 1154, 1155, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170,
    #          1171, 1172, 1173, 1175, 1176, 1177, 1178, 1179]

    for i in restId:
        sqlComm3 = "SELECT `tag` FROM `BUPTcreate` WHERE `id` = %d" %i
        cur.execute(sqlComm3)
        data = cur.fetchall()

        corpus_rest = []
        if data:
            for temp in data:
                s = ''.join(temp)
                corpus_rest.append(s)

            tfidf_rest = vectorizer.transform(corpus_rest)
            pred = clf.predict(tfidf_rest.toarray())

            print pred

            sqlComm4 = "UPDATE  `BUPTcreate` SET  `%s` =%d WHERE  `id` = %d" %(classifyName, pred[0], i)
            cur.execute(sqlComm4)

if __name__ == '__main__':
    conn = MySQLdb.connect (
            host = '',
            port = 3306,
            user = '',
            passwd = '',
            db = 'dataMiningDB',
            charset = 'utf8'
    )
    cur = conn.cursor()

    classifyNames = ['social sciences', 'intelligent device', 'service platform', 'social sciences', 'life', 'algorithm', 'campus improvement']
    for clname in classifyNames:
        (tfidf_train, target_train, tfidf_test, target_test, vectorizer) = trainNtest_set(clname)
        BestAlpha = findBestAlpha(tfidf_train, target_train, tfidf_test, target_test)
        #if clname == 'life':
        #    BestAlpha = 0.04
        #else:
        #    BestAlpha = 0.02
        #BestAlpha = 0.02
        clf = predictTest(BestAlpha, tfidf_train, target_train, tfidf_test, target_test)
        ClassifyRest(vectorizer, clf, clname)

    cur.close()
    conn.commit()
    conn.close()
