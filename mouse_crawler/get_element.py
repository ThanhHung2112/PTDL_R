from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://tiki.vn/chuot-may-tinh-co-day-g5-es-chuot-gaming-dpi-4-cap-do-hieu-ung-den-nen-7-mau-hang-nhap-khau-p75614175.html?spid=91088172")
sleep(random.randint(4,6))
rate = browser.find_element_by_class_name('review-rating__point')
print(rate.text)
sleep(random.randint(1,3))

review = browser.find_element_by_class_name('review-rating__total')
print(review.text)


    #click vào đánh giá mới nhất
new_rate = browser.find_element_by_xpath('/html/body/div[1]/div[1]/main/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]')
new_rate.click()


