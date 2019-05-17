#encoding = utf-8
from testScript import *
from config import VarConfig

#用例或用例步骤执行结束后，想Excel中写执行结果信息
def writeTestResult(sheetObj,rowNo,colsNo,testResult):
    colorDict = {"pass":"green","faild":"red","":None}
    #因为测试用例工作表和用例步骤sheet表中都有测试执行时间和测试结果列，定义此字典对象是为了区分具体该写入哪个表
    colsDict ={
        "testCase":[testCase_runTime,testCase_testResult],
        "apiData_datasheet":[apiData_runTime,apiData_result],
    }
    try:
        #在测试步骤sheet中，写入测试结果
        excelObj.writeCell(sheetObj,content=testResult,rowNo=rowNo,colsNo=colsDict[colsNo][1],style=colorDict[testResult])
        if testResult == "":
            #清空时间单元格内容
            excelObj.writeCell(sheetObj,content="",rowNo=rowNo,colsNo=colsDict[colsNo][0])
        else:
            #在测试步骤sheet中，写入测试时间
            excelObj.writeCellCurrentTime(sheetObj,rowNo=rowNo,colsNo=colsDict[colsNo][0])

    except Exception as e:
        print("写入Excel时发生异常")
        print(traceback.print_exc())

