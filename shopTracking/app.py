import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller 

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()


queries = ["아디다스"] 
target_codes = ["87741572945"]

for query, target_code in zip(queries, target_codes):
    real_rank = -1
    rank = -1
    for pageIndex in range(1,15):
        # URL로 1페이지 방문

        product_link = f"https://msearch.shopping.naver.com/search/all?adQuery=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4&origQuery=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4&pagingIndex={pageIndex}&pagingSize=40&personalized=true&productSet=total&query={query}&sort=foryou&viewType=list"

        driver.get(product_link)
        time.sleep(3)

        # 페이지를 밑으로 내리기 
        for _ in range(5):
            driver.execute_script("window.scrollBy(0,10000);")
            time.sleep(0.5)
            

        # 타겟 상품이 페이지에 노출되고 있는지 확인하기 
        try:
            target_selector = f"a[data-i='{target_code}']"
            target_element = driver.find_element(By.CSS_SELECTOR, target_selector)
            data = target_element.get_attribute('data-nclick')
            print(data.split(f"{target_code}","r:"))
            print(data.split(f"{target_code}","r:")[-1])
            real_rank = data.split(f"{target_code}","r:")[-1].split(",")[0]
        
            rank = int(real_rank) - (int(pageIndex) -1) * 40
            break
            
        except:
            print(f"{pageIndex} 페이지에서 타겟 상품을 찾지 못함")
            
            # 없다면 다음 페이지 방문  
    print("찾는 상품의 등수는", real_rank, " 등입니다.")
    print(f"찾는 상품은 {pageIndex} 페이지의 {rank}등에 노출되고 있습니다.")
input()