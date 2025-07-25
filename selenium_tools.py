# python -m virtualenv venv => 가상환경 설치 
# folder/Scripts/activate - 가상환경 활성화, deactivate 가상환경 비활성화 
# pip install selenium chromedriver_autoinstaller
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import chromedriver_autoinstaller 

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
#  네비게이션 관련 툴 
# driver.get("https://www.naver.com")
# time.sleep(1)
# driver.get("http://google.com")

# #뒤로가기
# driver.back()
# time.sleep(2)

# #앞으로 가기 
# driver.forward()
# time.sleep(2)
# print("동작끝")
# input()



# 브라우저 정보 가져오기 

# 타이틀 정보 가져오기 

# driver.get("https://www.naver.com")
# time.sleep(1)

# name = driver.title
# print(name, "브라우저 타이틀") 

# # current_url 주소창을 가지고옴

# url = driver.current_url
# print(url, "현재 주소")

# if "nid.naver.com" in url:
#     print("로그인 로직 필요")
# else: 
#     print("그대로 실행")

# input()


# Driver Wait 
# 3초 후 로딩이 끝나서 element가 찾아짐 -> 30초까지는 기다리는데 그 이상이면 에러를 던짐 

driver.get("https://www.naver.com")

try:
    selector = "#special-input-logo > a.link_naver.type_motion_n.is_fadein > span.ico_n_logo_svg > svg" 
    WebDriverWait(driver,10).until(EC.presence_of_element_located(
        By.CSS_SELECTOR, selector
))
except: 
    print("예외 발생")
print("다음 코드 실행")
input()

