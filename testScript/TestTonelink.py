#ecoding:utf-8
#author:ppliang
#=======================
from testScript import *
from testScript import apiRegister
from testScript import apiLogin
from testScript import apiResetPw
from testScript import apiGetBrokerInfo
from testScript.WriteTestResult import writeTestResult
from util.Log import *

def testTonelinkAPI():
    try:
        #根据Excel文件中的sheet名获取sheet对象
        caseSheet = excelObj.getSheetByName("API测试用例")
        #获取测试用例sheet中是否执行列对象
        isExecuteColumn = excelObj.getColumn(caseSheet,testCase_isExecute)
        #记录执行成功的测试用例个数
        successfulCase = 0
        #记录需要执行的用例个数
        requiredCase = 0

        for idx,i in enumerate(isExecuteColumn[1:]):
            #因为用例sheet中第一行为标题行，无需执行
            #用例名
            caseName = excelObj.getCellOfValue(
                caseSheet,rowNo=idx+2,
                colsNo=testCase_testCaseName)

            #循环遍历“测试用例”表中的测试用例，执行被设置为执行的用例
            if i.value == 'y':
                requiredCase += 1
                #获取测试用例表中，第idx+1行中
                #用例执行时所使用的框架类型
                useFrameWorkName = excelObj.getCellOfValue(
                    caseSheet,rowNo = idx+2,
                    colsNo = testCase_frameWorkName)
                logging.info("-----执行测试用例'%s'---------" % caseName)
                if useFrameWorkName == u"数据":
                    logging.info("*********调用数据驱动************")
                    #获取测试用例表中第idx+1行，执行框架为
                    #数据驱动的用例所使用的数据sheet名
                    dataSheetName = excelObj.getCellOfValue(
                        caseSheet,rowNo=idx+2,
                        colsNo=testCase_dataSourdeSheetName
                    )
                    # 获取第idx+1行测试用例使用的数据sheet对象
                    dataSheetObj = excelObj.getSheetByName(dataSheetName)
                    # 执行注册接口测试用例
                    if dataSheetName=='注册':
                        # 通过数据驱动框架执行注册接口测试
                        result = apiRegister.testRegisterApi(dataSheetObj)
                        if result:
                            logging.info("用例 %s 执行完成啦啦啦" % caseName)
                            successfulCase += 1
                            writeTestResult(
                                caseSheet,rowNo=idx+2,
                                colsNo="testCase",testResult="pass"
                            )
                        else:
                            #logging.debug("用例%s执行失败" % caseName,traceback.format_exc())
                            writeTestResult(
                                caseSheet,rowNo=idx+2,
                                colsNo="testCase",testResult="faild"
                            )
                    # 执行登录&获取用户信息接口测试用例
                    if dataSheetName=='登录&获取用户信息':
                        # 通过数据驱动框架执行接口测试
                        result = apiLogin.testLoginApi(dataSheetObj)
                        if result:
                            logging.info("用例 %s 执行完成啦啦啦" % caseName)
                            successfulCase += 1
                            writeTestResult(
                                caseSheet,rowNo=idx+2,
                                colsNo="testCase",testResult="pass"
                            )
                        else:
                            #logging.debug("用例%s执行失败" % caseName,traceback.format_exc())
                            writeTestResult(
                                caseSheet,rowNo=idx+2,
                                colsNo="testCase",testResult="faild"
                            )
                    # 执行忘记密码接口测试用例
                    if dataSheetName == '忘记密码':
                        # 通过数据驱动框架执行接口测试
                        result = apiResetPw.testResetPwApi(dataSheetObj)
                        if result:
                            logging.info("用例 %s 执行完成啦啦啦" % caseName)
                            successfulCase += 1
                            writeTestResult(
                                caseSheet, rowNo=idx + 2,
                                colsNo="testCase", testResult="pass"
                            )
                        else:
                            # logging.debug("用例%s执行失败" % caseName,traceback.format_exc())
                            writeTestResult(
                                caseSheet, rowNo=idx + 2,
                                colsNo="testCase", testResult="faild"
                            )
                    # 执行获取经纪人信息接口测试用例
                    if dataSheetName == '获取经纪人信息':
                        # 通过数据驱动框架执行接口测试
                        result = apiGetBrokerInfo.testGetBrokerInfoApi(dataSheetObj)
                        if result:
                            logging.info("用例 %s 执行完成啦啦啦" % caseName)
                            successfulCase += 1
                            writeTestResult(
                                caseSheet, rowNo=idx + 2,
                                colsNo="testCase", testResult="pass"
                            )
                        else:
                            # logging.debug("用例%s执行失败" % caseName,traceback.format_exc())
                            writeTestResult(
                                caseSheet, rowNo=idx + 2,
                                colsNo="testCase", testResult="faild"
                            )

            else:
                #清空不需要执行用例的执行时间和执行结果，
                #异常信息，异常图片单元格
                writeTestResult(caseSheet,rowNo=idx+2,
                                colsNo="testCase",testResult="")
        logging.info("共%d条用例，%d 条需要被执行，成功执行%d条" % (len(isExecuteColumn)-1,
                          requiredCase,successfulCase))

    except Exception as e:
        logging.debug("程序本身发生异常\n %s" % traceback.format_exc())
