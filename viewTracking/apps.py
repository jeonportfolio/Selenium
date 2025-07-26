import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller 

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

searchquery = ["opic", "toeic"]
target_play_links = ["https://tv.naver.com/v/77379162", "https://www.youtube.com/watch?v=z8dOXr-nRCA"]
nowRank = -1

for query, target_play_link in zip(searchquery, target_play_links):
    search_link = f"https://search.naver.com/search.naver?ssc=tab.video.all&where=video&sm=tab_jum&query={query}"
    driver.get(search_link)
    time.sleep(2)

    link_selector = f'a[href^="{target_play_link}"]'
    PLAY_FOUND = False
    for _ in range(7): # 최대 7번의 영상 순위 찾기 글을 불러온다.
        try:
            element = driver.find_element(By.CSS_SELECTOR, link_selector)
            while True:
                new_element = element.find_element(By.XPATH, "./..")
                nowRank = new_element.get_attribute("data-cr-rank")
                if nowRank != None: 
                         
                       #print("현재랭크 찾음", realRank)
                        PLAY_FOUND = True
                        break
                #print ("현재랭크 못찾음")
                element = new_element   
            if PLAY_FOUND: 
                break     
        except: 
            print("타겟 영상을 못찾았습니다 스크롤을 시작합니다.")
            driver.execute_script("window.scrollBy(0,10000);")
            time.sleep(3) #  로딩 대기 
    print(f"{query}/{nowRank} : 타겟 영상의 순위를 찾았습니다.")
input()