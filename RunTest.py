#encoding = utf-8

from testScript.TestTonelink import testTonelinkAPI
from util import SendEmail

# 测试数据&报告绝对路径
testData_Path = "D:\\tonelinkTestFrame\\apiTest\\testData\\ApiDatas_broker.xlsx"

if __name__ == "__main__":
    # 执行接口测试
    testTonelinkAPI()
    # 邮件发送最新的测试报告
    #SendEmail.emailSend(testData_Path)

