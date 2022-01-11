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
#chrome_options.add_argument("--window-size=1920x1080")


def star_url(i):
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.maximize_window()
    #url = "https://tiki.vn/search?q=chu%E1%BB%99t+m%C3%A1y+t%C3%ADnh&sort=top_seller&page="
    url2_1 = "https://www.lazada.vn/catalog/?_keyori=ss&from=input&page="
    url2_2 = "&q=Chu%E1%BB%99t%20m%C3%A1y%20t%C3%ADnh&spm=a2o4n.searchlist.search.go.41bd4aefRlNGWT"
    browser.get(url2_1+str(i)+url2_2)
    return

'''
chrome_options.add_argument("--start-maximized")
browser = c
browser = ChromeDriver(options)
'''
page_number = int(input("Write page number to craw: "))

while  page_number > 10 :
    print("page_number p must be smaller than 10    ")
    page_number = int(input("Write page number to craw:"))
def page_up():
    html = browser.find_element_by_tag_name('html')
    for i in range(5):
        html.send_keys(Keys.PAGE_UP)
    sleep(2)
    return

mouse_link = []

#all_mouse = browser.find_elements_by_class_name("info")
x = a = 1
for i in range(page_number):
    url = 'https://tiki.vn/search?q=chu%E1%BB%99t+m%C3%A1y+t%C3%ADnh&sort=top_seller&page='
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.maximize_window()
    browser.get(url + str(i+1))

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        links = WebDriverWait(browser,10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME,"product-item")))

    finally:
        print("page:",i + 1)

        for link in links:
            print(link)
            z = link.get_attribute("href")
            mouse_link.append(z)
            print(a,z)
            a = a+1
    print(page_up())
    browser.close()

'''    element_wait = False if len(browser.find_elements_by_xpath(
        '/html/body/div[1]/div[1]/main/div[2]/div/div[2]/div[1]/div[3]/ul/li[6]/a/i')) > 0 else True
    while element_wait == True:
        element_wait = False if len(browser.find_elements_by_xpath(
            '/html/body/div[1]/div[1]/main/div[2]/div/div[2]/div[1]/div[3]/ul/li[6]/a/i')) > 0 else True
    arrow = browser.find_element_by_xpath("/html/body/div[1]/div[1]/main/div[2]/div/div[2]/div[1]/div[3]/ul/li[6]/a/i")
    arrow.click()
    sleep(random.randint(1,4))'''

df = pd.DataFrame(mouse_link)
print(df)
print(".....Đã craw hoàn tất",a - 1,"link..........")
print("Press s to stop program","\n"
      "Press c to countinute craw data","\n"
      "Press df to show dataframe")
countinute = input("Press to countinute: ")
check = ["s","c","df"]

def which_next(check,countinute):
    while len(set(check) & set(countinute)) < 1:
        countinute = input("choose the next program :")
    return countinute

def checkrequest(countinute):
    if countinute == "df":
        print(df)
        print(which_next(check,countinute))
    elif countinute == "c":
        os.system('get_element.py')
    else: print("The program ends")
    return

def create_file(df):
    ask = input("Wanna create a csv file with this dataframe ?(y/n)")
    if ask == "y":
        f_name = input("file name:")
        path = "C:\\Users\\Admin\\Desktop\\Web Scrapy\\mouse_crawler\\"+str(f_name)+".csv"
        df.to_csv(path)
        print("Your file has been saved in",path)
    return

print(which_next(check,countinute))
print(checkrequest(countinute))
print(create_file(df))