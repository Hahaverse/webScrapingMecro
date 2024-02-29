from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
bookNum = 1728348

while bookNum <= 1728349:
    url = f'https://joara.com/book/{bookNum}'
    driver.get(url)

    #웹 페이지 로딩 대기
    sleep(1.3)

    #title을 저장하고 출력
    page_title = driver.title

    print(f"Book {bookNum} Title: {page_title}")
    bookNum += 1