import time, random
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
# 고유 ID 기반으로 찾는다. 
time.sleep(3)
place_id = 1294390363
place_selector = f"a[href='{place_id}?entry=pll']"
place_elements = driver.find_elements(By.CSS_SELECTOR, place_selector)

for _ in range(5):
    place_element = random.choice(place_elements)
    target_element = place_element.find_element(By.XPATH, './..')
    tag_name = target_element.get_attribute("tagName")

    if tag_name == "LI": 
            print("li태그를 찾았습니다.")
            break
    place_element = target_element

list_selector = "#place-main-section-root > div > div.rdX0R > ul > li"
list_element = driver.find_elements(By.CSS_SELECTOR, list_selector)
rank = 1 
for part_element in list_element:
   try: 
     part_element.find_element(By.CSS_SELECTOR, "svg.dPXjn")
     continue 
   except:  
     pass
   if part_element == target_element: 
        break
   rank += 1
print(f"{query}는 현재{rank}순위 입니다.")

input()