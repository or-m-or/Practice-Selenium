"""
봇 탐지를 우회하는 코드 : 디버거 크롬 사용

자바스크립트를 안쓰고 로그인 하는 방법은 쉽게 말하면 element 의 click(), send_keys() 와 같은 메소드를 피하는 것 -> 복사해서 붙여넣기 혹은 크롬에 아이디,비번 저장
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

# try:
#     shutil.rmtree(r"c:\chrometemp")  # 쿠키 / 캐쉬파일 수동 삭제 : 그냥 셀레니움 드라이버를 구동하면 쿠키와 캐시 저장 X
# except FileNotFoundError:
#     pass


# 1. 크롬 브라우저 수동 실행
# --remote-debugging-port=9222    : 크롬 포트
# --user-data-dir="C:\chrometemp" : 크롬을 사용하여 웹상을 돌아다녔을 때 생기는 쿠키와 캐쉬파일을 저장하는 곳
subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동



# debuggerAddress 옵션 설정
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
"""
# 2. 크롬 브라우저의 버전을 가져와서 해당 버전에서 호환되는 ChromeDriver의 메이저 버전을 추출
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
#-----------------------------------------------------------------------------------------------
# ChromeDriver 실행
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

#-----------------------------------------------------------------------------------------------
"""
#-----------------------------------------------------------------------------------------------
# Chrome WebDriver 실행 파일의 경로를 설정.
webdriver_path = r'C:\Users\thheo\Documents\selenium_test\chromedriver.exe'

# # Part 2. 셀레니움 크롬창 제어
# options = webdriver.ChromeOptions()
# options.add_argument('start-maximized')  # 크롬 최대화

# Chrome WebDriver의 Service를 직접 생성합니다.
service = Service(webdriver_path)

driver = webdriver.Chrome(service=service, options=option)
#-----------------------------------------------------------------------------------------------


driver.implicitly_wait(20)


# 뉴욕타임스 접속
# driver.get("https://www.nytimes.com/")
driver.get(r'https://myaccount.nytimes.com/auth/login?response_type=cookie&client_id=vi&redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Fsubscription%2Fonboarding-offer%3FcampaignId%3D7JFJX%26EXIT_URI%3Dhttps%253A%252F%252Fwww.nytimes.com%252F&asset=masthead')
time.sleep(5) #혹시 모를 에러 방지를 위한 적절한 wait 넣어주기

id = 'dev-admin@rbrain.co.kr'
pw = 'Fpdlsqhdn2023!'

pyperclip.copy(id)

driver.find_element_by_id('id').send_keys(Keys.CONTROL + 'v')
# pyperclip.copy(pw)

# driver.find_element_by_id('pw').send_keys(Keys.CONTROL + 'v')
# time.sleep(0.7)

# driver.find_element_by_id('log.login').click()
# time.sleep(1)


# driver.find_element(By.ID, 'query').click()
# driver.find_element(By.ID, 'query').send_keys("빅데이터" + Keys.ENTER)
# driver.find_element(By.LINK_TEXT, '뉴스').click()


print("exit")
driver.quit()