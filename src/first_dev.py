#coding=UTF-8
#############################################
#File name: first_dev.py
#Author: LiteA
#Mail: vshionagisa@gmail.com
#Function: spider one page
##############################################

from goose import Goose
from goose.text import StopWordsChinese
import re

class Sigle_Spider:

    def __init__(self, webURL, isEmpty, projectInfo):
        self.webURL = webURL
        self.isEmpty = isEmpty
        self.projectInfo = projectInfo

    def getInfoDic(self):
        #url = 'http://lcin.scs.bupt.cn/innovation/projectinfo.aspx?id=3842'
        #urlinput = raw_input('请输入项目网址\n')
        g = Goose({'stopwords_class': StopWordsChinese})
        article = g.extract(url=self.webURL)
        line0 = u'项目名称：'
        line1 = u'项目级别：'
        line2 = u'项目依托学院：'
        line3 = u'项目年度：'
        line3h = u'负责人：'
        line4 = u'指导老师：'
        line5 = u'参与人数：'
        line6 = u'项目简介： '

        matchObj = re.search(line0 + r'(.*?)' + line1, article.cleaned_text)
        if matchObj is None:
            projectName = u'无标题'
        else:
            projectName = ''.join(matchObj.group(1))

        matchObj = re.search(line1 + r'(.*?)' + line2, article.cleaned_text)
        if matchObj is None:
            projectLevel = u'无级别'
        else:
            projectLevel = ''.join(matchObj.group(1))

        matchObj = re.search(line2 + r'(.*?)' + line3, article.cleaned_text)
        if matchObj is None:
            projectSchool = u'无学院'
        else:
            projectSchool = ''.join(matchObj.group(1))

        matchObj = re.search(line3 + r'(.*?)' + line3h, article.cleaned_text)
        if matchObj is None:
            projectYear = u'无年度'
        else:
            projectYear = ''.join(matchObj.group(1))

        matchObj = re.search(line4 + r'(.*?)' + line5, article.cleaned_text)
        if matchObj is None:
            projectTeacher = u'老师A'
        else:
            projectTeacher = ''.join(matchObj.group(1))

        matchObj = re.search(line5 + r'(.*?)' + line6, article.cleaned_text)
        if matchObj is None:
            projectMembers = u'0'
        else:
            projectMembers = ''.join(matchObj.group(1))

        matchObj = re.search(line6 + r'(.*?)' + line0, article.cleaned_text)
        if matchObj is None:
            projectIntro = u'无简介'
        else:
            projectIntro = ''.join(matchObj.group(1))

        if (projectName == u'无标题'):
            self.isEmpty = True
        else:
            self.projectInfo = {'Name':projectName, 'Level':projectLevel, 'School':projectSchool,
                           'Year':projectYear, 'Teacher':projectTeacher,
                           'Members':projectMembers, 'Intro':projectIntro}
