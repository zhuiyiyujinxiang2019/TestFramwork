#- * - coding:UTF-8 - * -
import logging
import logging.config
from config.VarConfig import parentDirPath

#读取日志配置文件
logging.config.fileConfig(parentDirPath + u'\\config\\Logger.conf')
#logging.config.fileConfig("D:/MyPytest/DataDrivenFrameWork/config/Logger.conf")
#选择一个日志格式
logger = logging.getLogger('example01') #或者01

def debug(message):
    #定义debug级别日志打印方法
    logger.debug(message)

def info(message):
    # 定义info级别日志打印方法
    logger.info(message)

def warning(message):
    # 定义warning级别日志打印方法
    logger.warning(message)


#调试输出代码
# logger.debug('这是01')
# logger.info('这是01')
# logger.warning('这是01')
# logging.debug('杀得快放假啊速度快放假爱丽丝的看法')
# logging.info('就打卡机了贷款')