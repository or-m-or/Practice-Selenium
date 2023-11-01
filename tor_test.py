from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

"""
# 그냥 크롬 브라우저 열었을 때, ip 주소 조회
# 115.90.231.116
driver = webdriver.Chrome()
driver.get('http://icanhazip.com/')
print(driver.page_source)
driver.quit()
"""


# Tor 프록시 설정
# 118.0.5993.118
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "127.0.0.1:9150"
proxy.socks_proxy = "127.0.0.1:9150"
proxy.ssl_proxy = "127.0.0.1:9150"

# 프록시를 Chrome 옵션에 추가
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)

# Chrome 드라이버 시작
driver = webdriver.Chrome(options=chrome_options)

# 웹사이트 열기
driver.get('http://icanhazip.com/')

# 페이지 소스 출력
print(driver.page_source)

# 브라우저 종료
driver.quit()
