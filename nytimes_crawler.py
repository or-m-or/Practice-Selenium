from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import random 

"""
nytimes의 봇 탐지에 걸려서 차단 당함.

"""


# 웹 드라이버 로드
driver = webdriver.Chrome()

# 페이지 접속
driver.get("https://www.nytimes.com/")
time.sleep(3)

# 비즈니스 섹션 클릭
first_article = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div:nth-child(4) > div.NYTAppHideMasthead.css-1r6wvpq.e1m0pzr40 > header > div.css-umysuv > nav > ul > li:nth-child(3) > a"))
)
first_article.click()

time.sleep(random.uniform(2, 5))  # 클릭 후 무작위로 2에서 5초간 대기



# 첫 번째 뉴스 제목 클릭
first_article = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#collection-highlights-container > div.css-17lldrv.eb97p611 > ol > li:nth-child(1) > article > div > h3 > a"))
)
first_article.click()

time.sleep(random.uniform(2, 5))  # 클릭 후 무작위로 2에서 5초간 대기



# 기사 제목과 내용 추출
title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#headline")) # data-testid
).text

print(title)
# content = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "#articleBodyContents"))
# ).text

# # 추출한 데이터 저장
# with open('article.txt', 'w', encoding='utf-8') as f:
#     f.write(f"제목 : {title}\n\n")
#     f.write(content)

# 브라우저 닫기
driver.quit()