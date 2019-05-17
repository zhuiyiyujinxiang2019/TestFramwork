#coding:utf-8
#author:ppliang
#=======================
# 小程序登陆API
from testScript import *
from testScript.WriteTestResult import writeTestResult
from testScript.WriteExcel import writeContent
import requests
from util.Log import *

# 调登录接口
def login_api(url,payload):
    #因为数据表中的 payload 变量类型是str 需要用eval函数转换成dict
    jsoninfo = eval(payload)
    # 执行请求
    response = requests.post(url, data=jsoninfo)
    message = response.json()
    #print(message)
    return message

# 接口测试脚本
def testLoginApi(dataSourceSheetObj):
    try:
        # 获取数据源表（注册）中是否执行审核列对象
        dataIsExcuteColumn = excelObj.getColumn(
            dataSourceSheetObj,
            apiData_isExecute)  #============改============
        # 记录成功执行的数据条数
        successDatas = 0
        # 记录被设置为执行的数据条数
        requiredDatas = 0
        for idx, data in enumerate(dataIsExcuteColumn[1:]):
            # 遍历数据源表，进行数据驱动测试
            # 因为第一行是标题行，因此从第二行开始遍历
            # idx从0开始记录
            if data.value == "y":
                requiredDatas += 1
                logging.info('开始执行【登录API】测试用例')
                # =================================改================
                url = excelObj.getCellOfValue(dataSourceSheetObj,rowNo=idx+2,colsNo=apiData_url)
                # 接口参数
                payload = excelObj.getCellOfValue(dataSourceSheetObj,rowNo=idx+2,colsNo=apiData_payload)
                # 断言返回消息值
                assertMessage = excelObj.getCellOfValue(dataSourceSheetObj,rowNo=idx+2,colsNo=apiData_assertMessage)
                try:
                    # 注册============改======
                    #print("开始执行注册接口")
                    returnMessage = str(login_api(url,payload))
                except Exception as e:
                    logging.debug("执行【登录API】发生异常",traceback.format_exc())
                    # 写入失败信息
                    writeTestResult(sheetObj=dataSourceSheetObj,
                                    rowNo=idx + 2, colsNo="apiData_datasheet",
                                    testResult="faild")
                else:
                    writeContent(sheetObj=dataSourceSheetObj,returnMessage=returnMessage,
                                 rowNo=idx + 2,colsNo="return_Message")
                    # 进行断言对比
                    if assertMessage in returnMessage:
                        successDatas+=1
                        writeTestResult(sheetObj=dataSourceSheetObj,
                                        rowNo=idx + 2, colsNo="apiData_datasheet",
                                        testResult="pass")
                    else:
                        writeTestResult(sheetObj=dataSourceSheetObj,
                                        rowNo=idx + 2, colsNo="apiData_datasheet",
                                        testResult="faild")
            else:
                # 将不需要执的数据的行的执行时间和结果清空
                writeTestResult(sheetObj=dataSourceSheetObj,
                                rowNo=idx + 2, colsNo="apiData_datasheet",
                                testResult="")
        if requiredDatas == successDatas:
            # 只要当成功执行的数据条数等于被设置为需要执行的数
            # 据条数，才表示调用数据驱动的测试用例执行通过
            return 1
            # 表示调用数据驱动的测试用例执行失败
        return 0
    except Exception as e:
        raise e
