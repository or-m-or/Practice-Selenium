from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time

from time import sleep  
import math


# Chrome WebDriver 실행 파일의 경로를 설정합니다.
webdriver_path = r'C:\Users\thheo\Documents\selenium_test\chromedriver.exe'

# Part 2. 셀레니움 크롬창 제어
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')  # 크롬 최대화

# Chrome WebDriver의 Service를 직접 생성합니다.
service = Service(webdriver_path)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.naver.com/")
driver.find_element(By.ID, 'query').click()
driver.find_element(By.ID, 'query').send_keys("빅데이터" + Keys.ENTER)
driver.find_element(By.LINK_TEXT, '뉴스').click()

# Part 3. BeautifulSoup4로 소스코드 추출
html = driver.page_source  # 현재 페이지의 전체 소스코드 추출
soup = BeautifulSoup(html, 'html.parser')

# Part 4. 반복문 활용 뉴스 제목 추출
contents = soup.select('a.news_tit')  # 뉴스 제목 경로['a'태그 - 'news_tit'클래스]
for index, element in enumerate(contents, 1):  # (반복문) & (enumerate 함수) 사용
    print('{} 번째 뉴스 제목: {}'.format(index, element.text))

# Selenium 사용 후 WebDriver를 종료합니다.
driver.quit()
