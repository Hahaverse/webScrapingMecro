from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#파일 생성
with open("resume.txt", 'a') as writeResume:
    driver = webdriver.Chrome()
    bookNum = 400664

    while bookNum <= 400669:
        url = f'https://joara.com/book/{bookNum}'
        driver.get(url)

        #웹 페이지 로딩 대기
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'span')))

        page_title = driver.title

        #파일에 저장
        resume = f"Book Code: {bookNum}, Title: {page_title}\n"
        writeResume.write(resume)

        #print(f'Book Code: {bookNum}, Title: {page_title}')

        bookNum += 1

driver.quit()