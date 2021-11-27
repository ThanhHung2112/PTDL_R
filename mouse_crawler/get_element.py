from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd



chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

df = pd.read_csv("mouse_link.csv")
n = 1

for link in df["m_link"]:

    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get(str(link))
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        name = WebDriverWait(browser,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"title"))
        )
    finally:
        print(n,name.text)
    print("link:", link)

    element_exist = False if len(browser.find_elements_by_class_name('product-price__current-price')) > 0 else True
    if element_exist == False:
        price = browser.find_element_by_class_name("product-price__current-price") #flash-sale-price
        sale = "Non"
    else:
        price = browser.find_element_by_class_name("flash-sale-price")
        sale = "sale"
    print("Price:   ",price.text)
    print("Sale:",sale)

    browser.execute_script("window.scrollTo(0, 2350)")

    element_exist = False if len(browser.find_elements_by_xpath('/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]')) > 0 else True
    if element_exist == False:
        sold = browser.find_element_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]")
        print(sold.text)
        try:
            rate = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "review-rating__point"))
            )
            review = browser.find_element_by_class_name('review-rating__total')
            star = browser.find_elements_by_class_name("review-rating__number")

        finally:
            print("Rate :", rate.text)
            print(review.text)
            star5 = star[0].text
            star4 = star[1].text
            star3 = star[2].text
            star2 = star[3].text
            star1 = star[4].text
    else:
        sold = 0
        print(sold)
        rate = 0
        print(rate)
        review = 0
        star5 = star4 = star3 = star2 = star1 = 0


    #rate = browser.find_element_by_class_name("review-rating__point")
    #print("Rate :", rate.text)

    def rate_star(star1, star2, star3, star4, star5):
        print("5 star :", star5, "\n"
                                 "4 star :", star4, "\n"
                                                    "3 star :", star3, "\n"
                                                                       "2 star :", star2, "\n"
                                                                                          "1 star :", star1, "\n")


    print(rate_star(star1, star2, star3, star4, star5))

    n = n+1
    browser.close()
