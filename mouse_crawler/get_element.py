from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

df = pd.read_csv("mouse_link.csv")
n = 1
for link in df[0]:

    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get(str(link))
    sleep(random.randint(1, 4))
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.execute_script("window.scrollTo(0, 2350)")
    sleep(random.randint(4, 5))

    name = browser.find_element_by_class_name("title")
    print(n,name.text)
    print("link:", link)
    price = browser.find_element_by_class_name("product-price__current-price") #flash-sale-price
    print(price.text)
    if len(browser.find_elements_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]")) > 0:
        sold = browser.find_element_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]")
    else: sold = 0
    print(sold.text)

    rate = browser.find_element_by_class_name("review-rating__point")
    print("Rate :", rate.text)
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
