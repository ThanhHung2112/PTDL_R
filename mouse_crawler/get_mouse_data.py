from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd

#Chạy ngầm
chrome_options = Options()
chrome_options.add_argument()

browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://tiki.vn/search?q=chu%E1%BB%99t+m%C3%A1y+t%C3%ADnh&sort=top_seller&page=1")
sleep(random.randint(2,5))

html = browser.find_element_by_tag_name('html')
for i in range(5):
    html.send_keys(Keys.PAGE_DOWN)

mouse_link = []

all_mouse = browser.find_elements_by_class_name("info")
x = a = 1
for mouse in all_mouse :
    #print(x, mouse.text)
    #Get Link
    links = browser.find_elements_by_class_name("product-item")
    for link in links:
        z = link.get_attribute("href")
        mouse_link.append(z)
        print(a,z)
        a = a+1
    x = x+1
browser.close()
print(".....Đã craw hoàn tất",a - 1,"link..........")
start = input("Press any to countinute :")
n = 1
for link in mouse_link:

    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get(str(link))
    sleep(random.randint(1, 4))
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.execute_script("window.scrollTo(0, 2350)")
    sleep(random.randint(4, 5))

    name = browser.find_element_by_class_name("title")
    print(n,name.text)
    print("link:", link)
    price = browser.find_element_by_class_name("product-price__current-price")
    print(price.text)
    if len(browser.find_elements_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]")) > 0:
        sold = browser.find_element_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]")
    else: sold = 0
    print(sold.text)
'''
    element_exist = 0
    while element_exist == True:
        element_exist = False if len(browser.find_elements_by_class_name('review-rating__point')) > 0 else True
        sleep(1)

'''
   # wait = WebDriverWait(browser,10)
   # rate = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'review-rating__point')))
    #rate = browser.find_element_by_class_name('review-rating__point')

    while True:
        try:
            rate = browser.find_elements_by_class_name('review-rating__point')
            break
        except common.exceptions.NoSuchElementException:
            rate = 0

    print("Rate :",rate.text)
    review = browser.find_element_by_class_name('review-rating__total')
    print(review.text)

    star = browser.find_elements_by_class_name("review-rating__number")
    star5 = star[0].text
    star4 = star[1].text
    star3 = star[2].text
    star2 = star[3].text
    star1 = star[4].text


    def rate_star(star1, star2, star3, star4, star5):
        print("5 star :", star5, "\n"
                                 "4 star :", star4, "\n"
                                                    "3 star :", star3, "\n"
                                                                       "2 star :", star2, "\n"
                                                                                          "1 star :", star1, "\n")


    print(rate_star(star1, star2, star3, star4, star5))
    n = n+1
    browser.close()