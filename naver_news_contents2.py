from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 직접 tag 내용 추출
def get_tag_element(tag_name):
    element = None
    status = False
    try:
        element = driver.find_element_by_css_selector(tag_name)
        status = True
    except:
        print("요소가 존재하지 않습니다.",tag_name)
    finally:
        return element, status

#  화면 로딩 대기 후 tag 항목 추출 : 태그가 화면에 나타날 때까지 기다린 뒤 해당 요소를 반환
def get_tag_element_wait(tag_name, wait_time=10):
    element = None
    status = False
    try:
        wait = WebDriverWait(driver, wait_time)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, tag_name)))
        status = True
    except:
        print("요소가 존재하지 않습니다.",tag_name)
    finally:
        return element, status

####################################################
# 웹 드라이버 로드
driver = webdriver.Chrome()

# 경제 - 헤드라인
news_url="https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101"
tag_first_article = "#main_content > div > div._persist > div:nth-child(1) > div:nth-child(1) > div.cluster_body > ul > li:nth-child(1) > div.cluster_text > a"
tag_title = "#title_area"
tag_contents = "#contents"



# 첫 번째 기사 클릭하여 뉴스 본문으로 이동하여  제목과 내용을 추출 한다.

# (1) 페이지 접속
driver.get(news_url)
driver.implicitly_wait(5) # 10초 대기

# (2) 특정 영역을 포함한 부모 요소를 찾아서 링크를 클릭한다.
(first_article, status) = get_tag_element(tag_first_article)
if first_article != None:
    first_article.click()
else:
    print(" article not found")
    exit(1)

# (3) 기사 본문 페이지 로딩을 위해 명시적으로 대기 한다.
driver.implicitly_wait(3) # 10초 대기


# (4) 기사 본문의 제목과 내용을 수집한다.
(title, status ) = get_tag_element(tag_title)
print(title, status, tag_title )

(content, status ) = get_tag_element(tag_contents)
print(content, status, tag_contents )



# (5) 기사 본문의 제목과 내용을 저장한다.
with open('article.txt', 'w', encoding='utf-8') as f:
    f.write(f"제목 : {title}\n\n")
    f.write(content)

# (6) 브라우저 닫고 종료한다.
driver.quit()