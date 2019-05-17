from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import os
import time

#=========================================
#格式化email的头部信息，不然会出错，当做垃圾邮件
#=========================================
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 查找测试目录，找到最新生成的测试报告文件
def new_report(test_report_path): #测试报告存放文件夹位置：D:\\ppStudy\\tonelink\\AutoTest\\Test_Result\\Test_Report\\
    lists = os.listdir(test_report_path)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report_path + "/" + fn)) #linux
    file_new = os.path.join(test_report_path, lists[-1])  # 获取最新的文件保存到file_new
    #print(file_new) # 打印最新文件的绝对路径
    return file_new # 返回最新的测试报告文件的绝对路径

def emailSend(filename):  #filename为发送邮件的文件名
    # 发件人和收件人信息
    from_addr = "ppliang@tonelink.com"
    password = "1q2w3e4r_"
    to_addr = "857186493@qq.com"
    smtp_server = "smtp.tonelink.com"

    #======================================================
    #带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
    #所以，可以构造一个MIMEMultipart对象代表邮件本身，
    #然后往里面加上一个MIMEText作为邮件正文，
    #再继续往里面加上表示附件的MIMEBase对象即可。
    #=====================================================
    # 创建邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr('测试经理 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('小程序接口测试报告', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('测试报告请查收附件！', 'plain', 'utf-8'))
    # # 测试报告名称
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = '小程序API自动化测试报告' + now + '.xlsx'

    # 添加附件就是加上一个MIMEBase，从本地读取一个文件:
    with open(filename, 'rb') as f:
        # 设置附件的MIME和文件名，这里是xlsx类型:
        mime = MIMEBase('file', 'xlsx', filename=filename)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename="经纪人API测试报告.xlsx")  #filename是附件文件名
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    try:
        server = smtplib.SMTP(smtp_server, 25)
        #打印与服务器的交互信息
        #server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        raise e
