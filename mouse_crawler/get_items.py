from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from time import sleep
import random
import pandas as pd

class Mouse_Tiki_Crawler():

    def __init__(self,df,i,n):
        self.df = df

        self.n = n
        self.i = i

        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")

        self.browser = webdriver.Chrome(executable_path="mouse_crawler\\chromedriver.exe",chrome_options = chrome_options)

    '''
        Enter the class of variables
            i : product link  
            n : number
        Use chrome_options to add incognito,headless to run underground and windowsize
    '''

    def script_page(self):
        # scrip page to a place where ever you want (fix impurity)
        return self.browser.execute_script("window.scrollTo(0, 2350)")

    def start_url(self):
        url = str(self.i)
        self.browser.maximize_window()

        #start brower with a url
        return self.browser.get(url)

    def find_1ele_by_classname(self,time,classname,classname2):
        
        '''
        fill in time need to wait, classname of the element 
        and classname2 if that element may have another natural
        '''
        try:
            element = WebDriverWait(self.browser, time).until(
                EC.presence_of_element_located((By.CLASS_NAME, str(classname)))
            ).text
        
        except:

            '''
            I try to find that element with classname 1, if i can't find it with classname1
            then i will try to find it with classname2, even that, I still not see it that will be return Non
            '''

            if classname2 != "Non":
                try:
                    element = WebDriverWait(self.browser, time).until(
                    EC.presence_of_element_located((By.CLASS_NAME, str(classname2)))
                    ).text
                except:
                    element = "Non"
            else: element  = "Non"

        finally: return element

    def find_ele_by_xpath(self,time,el_xpath):

        '''
        It just the same with find_1ele_by_classname but this time i find it with xpath
        '''
        
        try:
            element = WebDriverWait(self.browser, time).until(
                EC.presence_of_element_located((By.XPATH, str(el_xpath)))
            ).text
        except:
            element = 0
        finally:
            #print(element)
            return element

    def get_rate_star(self,time,string):

        '''
        I create a list(star_list1) to check what i get after try to find all element with that classname
        If I can't find anything that mean nobody had been rated is yet or that shop don't give anywway to warranty so it will be [0,0,0,0,0].
        if i find 4 element or lower with that classname , it must be warranty.
        '''

        star_list1 = []
        self.browser.execute_script("window.scrollTo(0, 2350)")
        try:
            star = WebDriverWait(self.browser, time).until(
                EC. presence_of_all_elements_located((By.CLASS_NAME, str(string)))
            )

            # Add all a found to list
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
                    # this mean that i was found rate star
                    star_list = star_list1
                elif (len(star_list1) == 4) :
                    # this mean that i was found warranty 
                    star_list = star_list1
                elif len(star_list1) < 4 :
                    '''
                    This mean that shop given warranty information less than i want
                    But it will alwway have warranty time so i push it right the fist  
                    '''
                    for i in star_list1:
                        star_list.append(i)
                    for i in range(4 - len(star_list1)):
                        star_list.append(0)

                return star_list
            #last_star_list()
            def show_rate_star(star_list):
                #print("list ")
                for i in star_list:     
                    print(i)
                return

            #show_rate_star(last_star_list())

        return last_star_list()

    def fill_data(self,col,val):
        self.df[str(col)][self.n] = val
        return



