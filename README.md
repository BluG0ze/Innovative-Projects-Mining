# Innovative-Projects-Mining
Multidimensional Analysis System of University Students 
Innovative Project Based on Data Mining
=========================================
File Name          Description
-----------------------------------------
first_dev.py:      Custom web crawlers based on the Goose framework crawl
                   information on a single innovation project page
Spider4pros.py:    Call first_dev.py, crawl all items, stored in the database

fenci.py:          Use jieba segmentation library, store the project name, 
                   profile segmentation, stop words, the results in the database
kmeans.py:         Call scikit-learn to calculate tf-idf values for all features
                   of all items and implement KMeans clustering
naive_bayes.py:    Call scikit-learn, use tf-idf word bag model to achieve naive
                   bayesian classification
graph_draw.py:     Call scikit-learn, use PCA for dimensionality reduction, and
                   use Matplotlib to draw a two-dimensional scatter plot of 
                   clustering results and classfing results

=========================================
Program Language：python2.6
OS：CentOS6.4

Contact information：vshionagisa@gmail.com







Developed By
LiteA






--------------------プロダクトの説明「日本語」-----------------------------


プロダクトの名前：
データマイニングに使って大学生のイノベーションプロジェクトの多次元分析

データの取得方法：
私はクローラソフトウェアを書いて、学校のイノベーションプロジェクトウェブサイトからデータをクロールしまして、mysqlに保存しました。

データ前処理:
Mysqlに保存しましたら、データクリーニングしました。そして、中国語の単語分割フレームワークJiebaを使って、ソースデータを単語に分割しました。分割の結果もmysqlに保存しました。

クラスタリング：
Mysqlから分割した単語をとりだして、tfidfアルゴリズムを使って、単語から数字に変換しました。変換した数字は特徴にとして、Kmeansアルゴリズムを使ってクラスタリングしました。

分類：
部分のデータをラベル付けりましたら、tfidfアルゴリズム変換した数字は特徴にとして、ナイーブベイズアルゴリズムを使って分類しました。更に、分類した結果とクラスタリングした結果も比較しました。

結果展示：
クラスタリングと分類後の結果はPCAを使って、2次元に下がって、matplotを使って結果を展示しました。
