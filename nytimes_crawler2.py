"""
봇 탐지를 우회하는 코드 : 디버거 크롬 사용
크롬을 debug 모드로 열어서 debugging port 를 열어두고, debugging port 를 통해 크롬을 제어한다.
이렇게 하면 실제 일반 크롬 브라우저가 열린 것이기 때문에 서버에서는 매크로 프로그램인 것을 알아차리기가 쉽지 않다.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import subprocess
import shutil
import time
import pyperclip
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType


try:
    shutil.rmtree(r"c:\chrometemp")  # 쿠키 / 캐쉬파일 수동 삭제 : 그냥 셀레니움 드라이버를 구동하면 쿠키와 캐시 저장 X
except FileNotFoundError:
    pass


# 1. 크롬 브라우저 실행 (디버거 모드로 구동)
# --remote-debugging-port=9222    : 크롬 포트
# --user-data-dir="C:\chrometemp" : 크롬을 사용하여 웹상을 돌아다녔을 때 생기는 쿠키와 캐쉬파일을 저장하는 곳
subprocess.Popen(
    r'C:\Program Files\Google\Chrome\Application\chrome.exe ' 
    r'--remote-debugging-port=9222 '
    r'--user-data-dir="C:\chrometemp"'
    ) 



# 2. 셀레니움 크롬창 제어
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--no-sandbox')
chrome_option.add_argument('--disable-dev-shm-usage')
chrome_option.add_argument('--ignore-certificate-errors')
chrome_option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


webdriver_path = r'C:\Users\thheo\Documents\selenium_test\chromedriver.exe' # 크롬 웹드라이버 실행 파일 경로 설정
service = Service(webdriver_path)                                           # 크롬 웹드라이버 Service 설정
driver = webdriver.Chrome(service=service, options=chrome_option)           # 웹 드라이버 생성


driver.implicitly_wait(5)


# 뉴욕타임스 Root페이지 접속
# driver.get("https://www.nytimes.com/") 

# 뉴욕타임스 로그인페이지 접속
driver.get(r'https://myaccount.nytimes.com/auth/login?response_type=cookie&client_id=vi&redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Fsubscription%2Fonboarding-offer%3FcampaignId%3D7JFJX%26EXIT_URI%3Dhttps%253A%252F%252Fwww.nytimes.com%252F&asset=masthead')






time.sleep(15)
print("exit")
driver.quit()







#------------------------------------------------------------------------------------------
# id = 'dev-admin@rbrain.co.kr'
# pw = 'Fpdlsqhdn2023!'

# pyperclip.copy(id)


# driver.find_element(By.ID, 'id').send_keys(Keys.CONTROL + 'v')
# pyperclip.copy(pw)

# driver.find_element_by_id('pw').send_keys(Keys.CONTROL + 'v')
# time.sleep(0.7)

# driver.find_element_by_id('log.login').click()
# time.sleep(1)


# driver.find_element(By.ID, 'query').click()
# driver.find_element(By.ID, 'query').send_keys("빅데이터" + Keys.ENTER)
# driver.find_element(By.LINK_TEXT, '뉴스').click()


