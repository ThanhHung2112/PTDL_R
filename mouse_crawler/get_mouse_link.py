from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random
import os

from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

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
df = pd.DataFrame(mouse_link)
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
        df.to_csv("C:\Users\Admin\Desktop\Web Scrapy\mouse_crawler\mouse_link.csv)
    return

print(which_next(check,countinute))
print(checkrequest(countinute))
print(create_file(df))