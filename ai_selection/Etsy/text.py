from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

options = Options()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        'permissions.default.stylesheet': 2,
        'javascript': 2
    }
}
options.add_experimental_option('prefs', prefs)
options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.add_experimental_option("useAutomationExtension",'False')

browser = webdriver.Chrome(options=options)
url='https://www.etsy.com/listing/1520504265'
browser.get(url)
inputTag = browser.find_element(By.XPATH, '/html/body/script[4]')
print(inputTag.tag_name)