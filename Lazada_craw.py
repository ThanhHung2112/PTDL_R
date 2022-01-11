from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Options

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

page_number = int(input("Write page number to craw: "))

while  page_number > 20 :
    print("page_number p must be smaller than 10    ")
    page_number = int(input("Write page number to craw:"))
def page_up():
    html = browser.find_element_by_tag_name('html')
    for i in range(5):
        html.send_keys(Keys.PAGE_UP)
        sleep(random.randint(1,3))
    return

mouse_link = []
x = a = 1
for i in range(page_number):
    url2_1 = "https://www.lazada.vn/catalog/?_keyori=ss&from=input&page="
    url2_2 = "&q=Chu%E1%BB%99t%20m%C3%A1y%20t%C3%ADnh&spm=a2o4n.searchlist.search.go.41bd4aefRlNGWT"
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.maximize_window()
    browser.get(url2_1 + str(i+1) + url2_2)
    sleep(random.randint(2,5))
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        #links = WebDriverWait(browser,10).until(
        #        EC.presence_of_all_elements_located((By.CLASS_NAME,"_95X4G")))
        links = browser.find_elements_by_xpath('//*[@class="RfADt"]/a')
    finally:
        print("page:",i + 1)
        for link in links:
            #print(link)
            z = link.get_attribute("href")
            mouse_link.append(z)
            print(a,z)
            a = a+1
    sleep(random.randint(1,5))
    page_up()
    browser.close()
print('Craw', a,'link in lazada')
df = pd.DataFrame(mouse_link)
def create_file(df):
    ask = input("Wanna create a csv file with this dataframe ?(y/n)")
    if ask == "y":
        f_name = input("file name:")
        path = "C:\\Users\\Admin\\Desktop\\PTDL_R\\mouse_crawler\\"+str(f_name)+".csv"
        df.to_csv(path)
        print("Your file has been saved in",path)
    return
create_file(df)