#encoding = utf-8

import os

firefoxDriverFilePath = 'D:\Python36\geckodriver'
ieDriverFilePath = 'c:\IEDriverServer'
chromeDriverFilePath = 'c:\chromedriver'

#获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
screenPicturesDir = parentDirPath + '\\exceptionpictures\\'
# print(parentDirPath)

#测试数据文件存放绝对路径
dataFilePath = parentDirPath + "\\testData\\ApiDatas_broker.xlsx"
#print(dataFilePath)
#测试数据文件中，测试用例表中部分对应的数字序号
testCase_testCaseName = 1
testCase_frameWorkName = 3
testCase_dataSourdeSheetName = 4
testCase_isExecute = 5
testCase_runTime = 6
testCase_testResult = 7

#账号数据源表中，通用列数字编号
#数据源表中，对应的数字编号

apiData_url = 3
apiData_payload = 5
apiData_message = 7
apiData_assertMessage = 8
apiData_isExecute = 9
apiData_runTime = 10
apiData_result = 11
