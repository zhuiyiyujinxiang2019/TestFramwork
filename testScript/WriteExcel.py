#encoding = utf-8
from testScript import *
from config import VarConfig

#用例或用例步骤执行结束后，想Excel中获取【项目编号】【项目投标地址】信息
def writeContent(sheetObj,rowNo,colsNo,returnMessage):
    #因为测试用例工作表和用例步骤sheet表中都有测试执行时间和测试结果列，定义此字典对象是为了区分具体该写入哪个表
    colsDict ={
        "return_Message":[apiData_message],
    }
    try:
        #在测试步骤sheet中，写入测试内容
        #excelObj.writeCell(sheetObj,content=content,rowNo=rowNo,colsNo=colsDict[colsNo][0])
        if returnMessage == "":
            #清空项目编号和项目投标地址单元格内容
            excelObj.writeCell(sheetObj,content="",rowNo=rowNo,colsNo=colsDict[colsNo][0])
            #excelObj.writeCell(sheetObj, content="", rowNo=rowNo, colsNo=colsDict[colsNo][1])
            #excelObj.writeCell(sheetObj, content="", rowNo=rowNo, colsNo=colsDict[colsNo][2])
        else:
            #在测试步骤sheet中，写入项目编号和项目投标地址内容
            excelObj.writeCell(sheetObj,content=returnMessage,rowNo=rowNo,colsNo=colsDict[colsNo][0])
            #excelObj.writeCell(sheetObj, content=content_taskUrl, rowNo=rowNo, colsNo=colsDict[colsNo][1])
            #excelObj.writeCell(sheetObj, content=content_company, rowNo=rowNo, colsNo=colsDict[colsNo][2])

    except Exception as e:
        print("写入Excel时发生异常")
        print(traceback.print_exc())

