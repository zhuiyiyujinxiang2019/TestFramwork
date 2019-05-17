#coding:utf-8
#author:ppliang
#=======================

from action import *
from util.ParseExcel import ParseExcel
from config.VarConfig import *
import time
import traceback

#设置此次测试的环境编码为utf-8
import sys
from imp import reload
reload(sys)
sys.setdefaultencoding = 'utf-8'

#创建解析Excel对象
excelObj = ParseExcel()
#将Excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)


