from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from scrapy.utils.project import get_project_settings
from mouse_crawler.get_items import Mouse_Tiki_Crawler
from time import sleep
import random
import pandas as pd

df = pd.read_csv("mouse_link.csv")

class start_craw:
    def __init__(self,df):
        self.df = df

    def get_link(self):
        self.df[["Name", "Price", "Shop", "Brand", "Sold", "Warranty", "From", "Rate", "Comment", "5", "4", "3", "2", "1"]] = None
        print(self.df)
        return self.df

    def craw(self):
        n = 0
        df = SC.get_link()

        for i in df["m_link"]:

            MTC = Mouse_Tiki_Crawler(df, i, n)
            print(MTC.seting_options())
            MTC.start_url()
            print(i)
            df["Name"][n] = MTC.find_1ele_by_classname("title","Non")
            df["Price"][n] = MTC.find_1ele_by_classname("product-price__current-price","flash-sale-price")
            df["Shop"][n] = MTC.find_1ele_by_classname("seller-name","Non")
            df["Brand"][n] =  MTC.find_1ele_by_classname("brand-and-author","Non")
            df["Warranty"][n] = MTC.find_1ele_by_classname("itemRight","Non")
            df["Sold"][n] = MTC.find_ele_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]")
            MTC.script_page()
            df["From"][n] = MTC.find_ele_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[3]/div[1]/div[1]/div/table/tbody/tr[3]/td[2]")
            df["Rate"][n] = MTC.find_1ele_by_classname("review-rating__point","Non")
            df["Comment"][n] = MTC.find_1ele_by_classname("review-rating__total","Non")
            star = MTC.get_rate_star("review-rating__number")
            df["5"][n] = star[0]
            df["4"][n] = star[1]
            df["3"][n] = star[2]
            df["2"][n] = star[3]
            df["1"][n] = star[4]

            MTC.browser.close()
            #df.loc[n] =  [name,price,seller,brand,sold,warranty,come_from,rate,review,star5,star4,start3,star2,star1]

            #print(df.loc[n])
            n += 1

SC = start_craw(df)
print(SC.craw())







