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

df = pd.read_csv("mouse24link.csv")

#df[["Name","Price","Shop","Brand","Sold","Rate","Comment","5","4","3","2","1"]] = None
#print(df)

class Mouse_Tiki_Crawler():

    def __init__(self,df,i,n):
        self.df = df

        self.n = n
        self.link = df["m_link"]
        self.i = i
        self.browser = webdriver.Chrome(executable_path="chromedriver.exe")

    def seting_options(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1920x1080")
        return

    def script_page(self):
        return self.browser.execute_script("window.scrollTo(0, 2350)")

    def start_url(self):
        url = str(self.i)
        self.browser.maximize_window()

        return self.browser.get(url)

    def find_1ele_by_classname(self,classname,classname2):

        try:
            element = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, str(classname))).text
            )
        except:
            if classname2 != "Non":
                try:
                    element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, str(classname2))).text
                    )
                except:
                    element = "Non"
            else: element  = "Non"

        finally:
            print(element)

        return element

    def find_ele_by_xpath(self,el_xpath):

        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, str(el_xpath))).text
            )
        except:
            element = 0
        finally:
            print(element)
        return element

    def get_rate_star(self,string):

        self.browser.execute_script("window.scrollTo(0, 2350)")
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC. presence_of_all_elements_located((By.CLASS_NAME, str(string))).text
            )
        except:
            element = [0,0,0,0,0]
        finally:
            star5 = star[0]
            star4 = star[1]
            star3 = star[2]
            star2 = star[3]
            star1 = star[4]
        return star5,star4,star3,star2,star1

    def fill_data(self,col,val):
        self.df[str(col)][self.n] = val
        return

    def Create_file(self):

        f_name = input("file name:")
        path = "C:\\Users\\Admin\\Desktop\\Web Scrapy\\mouse_crawler\\" + str(f_name) + ".csv"
        self.df.to_csv(path)

        return print("Your file has been saved in", path)

