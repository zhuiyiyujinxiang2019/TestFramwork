#encoding = utf-8

from selenium import webdriver
from config.VarConfig import firefoxDriverFilePath
from config.VarConfig import ieDriverFilePath
from config.VarConfig import chromeDriverFilePath
from util.ObjectMap import getElement
from util.ClipboardUtil import Clipboard
from util.KeyBoardUtil import KeyboardKeys
from util.DirAndTime import *
from util.WaitUtil import WaitUtil
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#定义全局driver变量
driver = None
#全局的等待类实例对象
waitUtil = None

def open_browser(browserName,*agr):
    #打开浏览器
    global driver,waitUtil
    try:
        if browserName.lower() == 'ie':
            driver = webdriver.Ie(executable_path=ieDriverFilePath)
        elif browserName.lower() == 'chrome':
            #创建chrome浏览器的一个options实例对象
            chrome_options = Options()
            #添加屏蔽--ignore-certificate-errors提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitcher",
                ["ignore-certificate-error"]
            )
            driver = webdriver.Chrome(
                executable_path=chromeDriverFilePath,
                chrome_options = chrome_options
            )
        else:
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
        #driver对象创建成功后，创建等待类实例对象
        waitUtil = WaitUtil(driver)

    except Exception as e:
        raise e

def visit_url(url,*arg):
    #访问某个网站
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e
def close_browser(*arg):
    #关闭浏览器
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise e

def refresh_page(*arg):
    #刷新页面
    try:
        driver.refresh()
    except Exception as e:
        raise e

def sleep(sleepSeconds,*arg):
    #强制等待
    try:
        time.sleep(int(sleepSeconds))
    except Exception as e:
        raise e

def clear(locationType,locatorExpression,*arg):
    #清除输入框默认内容
    global driver
    try:
        getElement(driver,locationType,locatorExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType,locatorExpression,inputContent):
    #在页面输入框中输入数据
    global driver
    try:
        getElement(driver,locationType,locatorExpression).send_keys(inputContent)
    except Exception as e:
        raise e

def click(locationType,locatorExpression,*arg):
    # 单击页面元素
    global driver
    try:
        getElement(driver, locationType, locatorExpression).click()
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString,*arg):
    #断言页面源码是否存在某关键字或关键字符串
    global driver
    try:
        assert assertString in driver.page_source,\
                "%s not found in page source!" % assertString
    except AssertionError as e:
        raise AssertionError
    except Exception as e:
        raise e

def assert_title(titleStr,*arg):
    # 断言页面标题是否存在给定的关键字符串
    global driver
    try:
        assert titleStr in driver.title, \
            "%s not found in title!" % titleStr
    except AssertionError as e:
        raise AssertionError
    except Exception as e:
        raise e

def getTitle(*arg):
    #获取页面标题
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

def getTitle_new_window(*arg):
    #获取页面标题
    global driver
    try:
        title = driver.switch_to.window(driver.window_handles[1])
        return title
    except Exception as e:
        raise e

# 返回到第一个窗口
def switch_tab(*arg):
    global driver
    handles = driver.window_handles           # 获取当前窗口句柄集合（列表类型）
    driver.switch_to.window(handles[0])   # 跳转到第1个窗口

# 聚焦元素
def scroll_js(locationType,locatorExpression,*arg):
    global driver
    target = getElement(driver,locationType,locatorExpression)
    driver.execute_script("arguments[0].scrollIntoView();", target)

def getPageSource(*arg):
    #获取页面源码
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise e

def get_text(locationType,locatorExpression,*arg):
    # 获取页面文本
    global driver
    try:
        mytext = getElement(driver,locationType,locatorExpression).text
        return  mytext
    except Exception as e:
        raise e

def execute_script_js(*arg):
    #变更js文件
    try:
        #js = 'document.getElementById("dietime").removeAttribute("readonly")'
        driver.execute_script(*arg)
    except Exception as e:
        raise e
def execute_script_txt(text,*arg):
    #变更js文件，创建项目描述
    try:
        #js = 'document.getElementById("dietime").removeAttribute("readonly")'
        driver.execute_script('document.getElementById("ke-edit-iframe").contentWindow.document.body.innerHTML="%s"'% text)
    except Exception as e:
        raise e

def execute_script_menu_js(locationType,locatorExpression,*arg):
    try:
        js = """ var evObj = document.createEvent('MouseEvents');
                          evObj.initMouseEvent(\"mouseover\",true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                          arguments[0].dispatchEvent(evObj);
                          """
        more_menu = WebDriverWait(driver=driver, timeout=15).until(
                     EC.visibility_of_element_located((locationType, locatorExpression)))

        driver.execute_script(js, more_menu)
    except Exception as e:
        raise e


def switch_to_frame(locationType,locatorExpression,*arg):
    #切换进入frame
    global driver
    try:
        driver.switch_to.frame(getElement(driver,locationType,locatorExpression))
    except Exception as e:
        raise e

def switch_to_default_content(*arg):
    #切出fram
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

# def switch_to_window(*arg):
#     try:
#         driver.switch_to.window(driver.window_handles[1])
#     except Exception as e:
#         raise e

def paste_string(pasteString,*arg):
    #模拟ctrl+v操作
    try:
        Clipboard.setText(pasteString)
        #等待2秒，防止代码执行的太快，而未成功粘贴内容
        time.sleep(2)
        KeyboardKeys.twoKeys("ctrl","v")
    except Exception as e:
        raise e

def press_tab_key(*arg):
    #模拟tab键
    try:
        KeyboardKeys.oneKey("tab")
    except Exception as e:
        raise e

def press_enter_key(*arg):
    #模拟enter键
    try:
        KeyboardKeys.oneKey("enter")
    except Exception as e:
        raise e

def maximize_browser():
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e
def capture_screen(*args):
    #截取屏幕图片
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(createCurrentDateDir()) + "\\" +str(currTime) + ".png"
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\',r'\\'))
    except Exception as e:
        raise e
    else:
        return picNameAndPath

def waitPresenceOfElementLocated(locationType,locatorExpression,*arg):
    '''显示等待页面元素出现在DOM中，但并不一定可见，
    存在则返回该页面元素对象'''
    global driver
    try:
        waitUtil.presenceOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitFrameToBeAvailableAndSwitchToIt(locationType,locatorExpression,*arg):
    '''检查frame是否存在，存在则切换进入frame控件中'''
    global driver
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType,locatorExpression)
    except Exception as e:
        raise e

def waitVisibilityOfElementLocated(locationType,locatorExpression,*arg):
    '''显示等待页面元素出现在DOM中，并且可见，存在则返回该页面元素对象'''
    global driver
    try:
        waitUtil.visibilityOfElementLocated(locationType,locatorExpression)
    except Exception as e:
        raise e

