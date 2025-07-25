# python -m virtualenv venv => 가상환경 설치 
# venv/Scripts/activate - 가상환경 활성화, deactivate 가상환경 비활성화 
# pip install selenium chromedriver_autoinstaller
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller 

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
# 웹 브라우저 주소창 컨트롤
driver.get("https://www.naver.com")
time.sleep(3)
# 요소를 찾아서 copy
css_selector = "#shortcutArea > ul > li:nth-child(8) > a"
# 찾아온 요소를 find_element로 가져오기
group_navigation = driver.find_element(By.CSS_SELECTOR, css_selector)
#데이터 가져오기
print(group_navigation.text)
# 요소 클릭
group_navigation.click() 
input()

