#coding=UTF-8
#############################################
#File name: graph_draw.py
#Author: LiteA
#Mail: vshionagisa@gmail.com
#Created Time: 2015-8-10 18:39:40
#Function: Use PCA to reduce dimensionality
#          and draw the results of K-means and NB
##############################################
import os
import codecs
import MySQLdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from numpy import *
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def importdata(corpus = []):
    for i in range (22,1862):
        sqlComm1 = 'SELECT `tag` FROM `BUPTcreate` WHERE `id` =' + '%d' %i
        cur.execute(sqlComm1)
        data = cur.fetchone()
        if data :
            s = ''.join(tuple(data))
            corpus.append(s)
    return corpus

def data2mat(corpus = []):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    return mat(weight)

#def pca(dataMat, topNfeat):
#    meanVals = mean(dataMat, axis = 0)
#    meanRemoved = dataMat - meanVals #remove mean
#    covMat = cov(meanRemoved, rowvar = 0)
#    eigVals,eigVects = linalg.eig(mat(covMat))
#    eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest
#    n_eigValInd = eigValInd[-1:-(topNfeat+1):-1]  #cut off unwanted dimensions
#    n_EigVects = eigVects[:,n_eigValInd]       #reorganize eig vects largest to
#    lowDDataMat = meanRemoved * n_EigVects#transform data into new dimensions
#    reconMat = (lowDDataMat * n_EigVects.T) + meanVals
#    return (lowDDataMat, reconMat)

def pca(dataMat, topNfeat):
    pca = PCA(n_components = topNfeat)
    pca.fit(dataMat)
    lowDDataMat = pca.transform(dataMat)
    return lowDDataMat

def writeIntoFile(lowDDataMat, reconMat):
    path = '~/python/'
    if not os.path.isfile('Mat_info.txt'):
        os.mknod('Mat_info.txt')
    fp = codecs.open('Mat_info.txt', 'w', 'utf-8')
    fp.write(u'lowDDataMat is :\n')
    fp.write(lowDDataMat)
    fp.write(u'\nreconMat is :\n')
    fp.write(reconMat)

def kmeans(data, n_cl):
    pred = KMeans(n_clusters = n_cl)
    pred.fit(data)
    Labels = pred.labels_
    centers = pred.cluster_centers_
    return (Labels, centers)

def plotBestFit(dataSet1, Labels, centers):#, dataSet2):
    dataArr1 = array(dataSet1)
    #dataArr2 = array(dataSet2)
    n = shape(dataArr1)[0]
    xcord0 = []; ycord0 = []
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    xcord3 = []; ycord3 = []
    xcord4 = []; ycord4 = []
    xcord5 = []; ycord5 = []
    xcord6 = []; ycord6 = []
    for i in range(n):
        if Labels[i] == 0:
            xcord0.append(dataArr1[i,0]); ycord0.append(dataArr1[i,1])
        if Labels[i] == 1:
            xcord1.append(dataArr1[i,0]); ycord1.append(dataArr1[i,1])
        if Labels[i] == 2:
            xcord2.append(dataArr1[i,0]); ycord2.append(dataArr1[i,1])
        if Labels[i] == 3:
            xcord3.append(dataArr1[i,0]); ycord3.append(dataArr1[i,1])
        if Labels[i] == 4:
            xcord4.append(dataArr1[i,0]); ycord4.append(dataArr1[i,1])
        if Labels[i] == 5:
            xcord5.append(dataArr1[i,0]); ycord5.append(dataArr1[i,1])
        if Labels[i] == 6:
            xcord6.append(dataArr1[i,0]); ycord6.append(dataArr1[i,1])
    xcenters = centers[:,0]; ycenters = centers[:,1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord0, ycord0, s=30, c='Blue')
    ax.scatter(xcord1, ycord1, s=30, c='Orange')
    ax.scatter(xcord2, ycord2, s=30, c='Green')
    ax.scatter(xcord3, ycord3, s=30, c='Red')
    ax.scatter(xcord4, ycord4, s=30, c='Purple')
    ax.scatter(xcord5, ycord5, s=30, c='Brown')
    ax.scatter(xcord6, ycord6, s=30, c='Pink')
    ax.scatter(xcenters, ycenters, s=90, c='Black', marker='x')
    plt.xlabel('X'); plt.ylabel('Y');
    plt.savefig('myfig')

def catch_cl_result(cl_name):
    sqlComm2 = "SELECT  `%s` FROM  `BUPTcreate` ORDER BY  `id` "%cl_name
    cur.execute(sqlComm2)
    cl_result = []
    data = cur.fetchall()
    if data:
        for temp in data:
            cl_result = cl_result + list(temp)
    return cl_result

def draw_classify(dataSet1, Labels, draw_name):
    dataArr1 = array(dataSet1)
    n = shape(dataArr1)[0]
    xcord0 = []; ycord0 = []
    xcord1 = []; ycord1 = []
    for i in range(n):
        if Labels[i] == 0:
            xcord0.append(dataArr1[i,0]); ycord0.append(dataArr1[i,1])
        if Labels[i] == 1:
            xcord1.append(dataArr1[i,0]); ycord1.append(dataArr1[i,1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord0, ycord0, s=30, c='Yellow')
    ax.scatter(xcord1, ycord1, s=30, c='White')
    plt.xlabel('X'); plt.ylabel('Y');
    plt.savefig(draw_name)


if __name__ == '__main__':
    conn = MySQLdb.connect (
            host = '',
            port = 3306,
            user = '',
            passwd = '',
            db = '',
            charset = 'utf8'
    )
    cur = conn.cursor()

    corpus = importdata([])

    matA = data2mat(corpus)

    print repr(matA.shape)

    lowDDataMat = pca(matA, 2)

    #########writeIntoFile(lowDDataMat)

    (Labels, centers) = kmeans(lowDDataMat, 7)

    plotBestFit(lowDDataMat, Labels, centers)

    #cl_names = ['intelligent device', 'social sciences', 'life']

    #for cl_name in cl_names:
    #    cl_result = catch_cl_result(cl_name)
    #    draw_classify(lowDDataMat, cl_result, cl_name)
