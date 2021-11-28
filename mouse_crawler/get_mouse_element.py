from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#from ..get_mouse_link import page_up
from time import sleep
import random
import pandas as pd

df = pd.read_csv("mouse_link.csv",)
#df.rename({df"0":'links'}, axis=1)
df[["Name","Price","Shop","Brand","Sold","Rate","Comment","5","4","3","2","1"]] = None
print(df)

class Mouse_Tiki_Crawler(df,i):

    self.link = df["m_link"]
    self.i = i
    self.browser = webdriver.Chrome(executable_path="chromedriver.exe")

    def seting_options(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920x1080")
        return


    def star_url(self):
        url = "" + str(self.i)
        self.browser.maximize_window()\
        self.browser.get(url)
        pass

    def find_1ele_by_classname(self):
        pass

    def find_ele_by_xpath(self):
        pass

    def show_data(self):
        pass

    def Create_file(self):
        pass
