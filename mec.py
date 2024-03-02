from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#크롬 드라이버 자동 설치->최신 버전 설치->Service에 저장
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#파일 생성
with open("resume.txt", 'a') as writeResume:
    bookNum = 1728348

    while bookNum <= 1728349:
        url = f'https://joara.com/book/{bookNum}'
        driver.get(url)

        #웹 페이지 로딩 대기
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'span')))

        page_title = driver.title

        #파일에 저장
        resume = f"Book Code: {bookNum}, Title: {page_title}\n"
        writeResume.write(resume)

        bookNum += 1

driver.quit()
