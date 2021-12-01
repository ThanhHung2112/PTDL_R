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
        self.df[["Name", "Price","Product_price","Discount", "Shop", "Brand", "Sold", "Warranty",
                 "Warranty_way", "Warranty_place", "From", "Rate", "Comment", "5", "4", "3", "2", "1"]] = None
        print(self.df)
        return self.df

    def craw(self):
        n = 0
        self.df = SC.get_link()
        cls2 = "Non"
        for i in df["m_link"]:

            MTC = Mouse_Tiki_Crawler(df, i, n)
            #print(MTC.setting_options())
            MTC.start_url()
            print(n+1,i)
            self.df["Name"][n] = MTC.find_1ele_by_classname("title",cls2)
            self.df["Price"][n] = MTC.find_1ele_by_classname("product-price__current-price","flash-sale-price")
            self.df["Product_price"][n] = MTC.find_1ele_by_classname("product-price__list-price",cls2)
            self.df["Discount"][n] = MTC.find_1ele_by_classname("product-price__discount-rate",cls2)
            self.df["Shop"][n] = MTC.find_1ele_by_classname("seller-name",cls2)
            self.df["Brand"][n] =  MTC.find_1ele_by_classname("brand-and-author",cls2)
            warranty = MTC.get_rate_star("itemRight")
            print(len(warranty))
            self.df["Warranty"][n] = warranty[0]
            self.df["Warranty_way"][n] = warranty[1]
            self.df["Warranty_place"][n] = warranty[2]
            self.df["Sold"][n] = MTC.find_ele_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]")
            MTC.script_page()
            self.df["From"][n] = MTC.find_ele_by_xpath("/html/body/div[1]/div[1]/main/div[3]/div[3]/div[1]/div[1]/div/table/tbody/tr[3]/td[2]")
            self.df["Rate"][n] = MTC.find_1ele_by_classname("review-rating__point",cls2)
            self.df["Comment"][n] = MTC.find_1ele_by_classname("review-rating__total",cls2)
            star = MTC.get_rate_star("review-rating__number")
            self.df["5"][n] = star[0]
            self.df["4"][n] = star[1]
            self.df["3"][n] = star[2]
            self.df["2"][n] = star[3]
            self.df["1"][n] = star[4]

            MTC.browser.close()
            #df.loc[n] =  [name,price,seller,brand,sold,warranty,come_from,rate,review,star5,star4,start3,star2,star1]

            #print(df.loc[n])
            n += 1

        Create_file(self.df)
        return

    def Create_file(data):

        f_name = input("file name:")
        path = "C:\\Users\\Admin\\Desktop\\Web Scrapy\\mouse_crawler\\" + str(f_name) + ".csv"
        data.to_csv(path)

        return print("Your file has been saved in", path)



SC = start_craw(df)
SC.craw()







