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
Program Language��python2.6
OS��CentOS6.4

Contact information��vshionagisa@gmail.com







Developed By
 LiteA���� ���⣩






--------------------�ץ�����Ȥ��h�����ձ��Z��-----------------------------


�ץ�����Ȥ���ǰ��
�ǩ`���ޥ��˥󥰤�ʹ�äƴ�ѧ���Υ��Υ٩`�����ץ������Ȥζ��Ԫ����

�ǩ`����ȡ�÷�����
˽�ϥ���`�饽�եȥ�����������ơ�ѧУ�Υ��Υ٩`�����ץ������ȥ����֥����Ȥ���ǩ`���򥯥�`�뤷�ޤ��ơ�mysql�˱��椷�ޤ�����

�ǩ`��ǰ�I��:
Mysql�˱��椷�ޤ����顢�ǩ`������`�˥󥰤��ޤ����������ơ��й��Z�΅g�Z�ָ�ե�`���`��Jieba��ʹ�äơ����`���ǩ`����g�Z�˷ָ�ޤ������ָ�νY����mysql�˱��椷�ޤ�����

���饹����󥰣�
Mysql����ָ���g�Z��Ȥ�����ơ�tfidf���르�ꥺ���ʹ�äơ��g�Z�������֤ˉ�Q���ޤ�������Q�������֤��؏դˤȤ��ơ�Kmeans���르�ꥺ���ʹ�äƥ��饹����󥰤��ޤ�����

���
���֤Υǩ`�����٥븶����ޤ����顢tfidf���르�ꥺ����Q�������֤��؏դˤȤ��ơ��ʥ��`�֥٥������르�ꥺ���ʹ�äƷ���ޤ��������ˡ�������Y���ȥ��饹����󥰤����Y������^���ޤ�����

�Y��չʾ��
���饹����󥰤ȷ����νY����PCA��ʹ�äơ�2��Ԫ���¤��äơ�matplot��ʹ�äƽY����չʾ���ޤ�����