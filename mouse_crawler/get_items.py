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

        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")

        self.browser = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options = chrome_options)



    def script_page(self):
        return self.browser.execute_script("window.scrollTo(0, 2350)")

    def start_url(self):
        url = str(self.i)
        self.browser.maximize_window()

        return self.browser.get(url)

    def find_1ele_by_classname(self,classname,classname2):

        try:
            element = WebDriverWait(self.browser, 12).until(
                EC.presence_of_element_located((By.CLASS_NAME, str(classname)))
            ).text

        except:

            if classname2 != "Non":
                try:
                    element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, str(classname2)))
                    ).text
                except:
                    element = "Non"
            else: element  = "Non"

        finally:
            print(element)

        return element

    def find_ele_by_xpath(self,el_xpath):

        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, str(el_xpath)))
            ).text
        except:
            element = 0
        finally:
            print(element)
        return element

    def get_rate_star(self,string):

        star_list1 = []
        self.browser.execute_script("window.scrollTo(0, 2350)")
        try:
            star = WebDriverWait(self.browser, 10).until(
                EC. presence_of_all_elements_located((By.CLASS_NAME, str(string)))
            )
            def rate_star_list(star):
                if len(star) > 0:
                    for i in star:
                        star_list1.append(i.text)
                return star_list1
            #print("done Try")
            rate_star_list(star)
            #print(star_list1)
            #star = self.browser.find_elements_by_class_name(str(string)).text
        except:
            star_list1 = [0,0,0,0,0]
        finally:
            def last_star_list(star_list = []):
                #print("len", len(star_list1))
                if len(star_list1) == 5:
                    star_list = star_list1
                elif (len(star_list1) == 4) :
                    star_list = star_list1
                elif len(star_list1) < 4 :
                    for i in range(4 - len(star_list1)):
                        star_list.append(0)
                    for i in star_list1:
                        star_list.append(i)

                return star_list
            #last_star_list()
            def show_rate_star(star_list):
                #print("list ")
                for i in star_list:
                    print(i)
                return

            show_rate_star(last_star_list())

        return last_star_list()

    def fill_data(self,col,val):
        self.df[str(col)][self.n] = val
        return



