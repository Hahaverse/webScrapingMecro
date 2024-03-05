from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#크롬 드라이버 자동 설치->최신 버전 설치->Service에 저장
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#파일 생성
with open("resume.txt", 'a') as writeResume:
    bookNum = 400650

    while bookNum <= 400669:
        url = f'https://joara.com/book/{bookNum}'
        driver.get(url)

        #웹 페이지 로딩 대기
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'span')))
        sleep(0.1)


        page_title = driver.title

        #title 말꼬리 제거
        if " - 조아라 : 스토리 본능을 깨우다" in page_title:
            title = page_title.split(" - 조아라 : 스토리 본능을 깨우다")[0]
        else:
            title = "작품 정보가 존재하지 않습니다."

        #파일에 저장
        resume = f"Book Code: {bookNum}, Title: {title}\n"
        writeResume.write(resume)

        bookNum += 1

driver.quit()
