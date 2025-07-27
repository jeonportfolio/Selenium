from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller 

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 네이버 검색창 + 키워드로 드라이버 get
query = "서울 맛집"
search_link = f"https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query={query}"
driver.get(search_link) 
input()

# place 더보기 탭을 클릭하고 없으면 에러 
try:
    more_selector = "a.FtXwJ"
    more_element = driver.find_element(By.CSS_SELECTOR, more_selector)
    print(more_element.text)
    more_selector.click()
except: 
    print(f"{query} 검색어로 장소 순위를 알 수 없습니다." )

    input()