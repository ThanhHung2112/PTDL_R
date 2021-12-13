from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from get_items import Mouse_Tiki_Crawler
from time import sleep
import random
import pandas as pd

df = pd.read_csv("mouse_crawler\\mouse24link.csv")

class start_craw:
    def __init__(self,df):
        self.df = df

    def get_link(self):
        self.df[["Name", "Price","Product_price","Discount", "Shop", "Brand", "Sold", "Warranty_time",
                 "Warranty_way", "Warranty_place", "Rate", "Comment", "5", "4", "3", "2", "1","More_inf"]] = None
        print(self.df)
        return self.df

    def craw(self):
        n = 0
        self.df = SC.get_link()
        cls2 = "Non"
        
        for i in df["m_link"]:

            MTC = Mouse_Tiki_Crawler(df, i, n)
            MTC.start_url()
            self.df["Name"][n] = MTC.find_1ele_by_classname(10,"title",cls2)
            self.df["Price"][n] = MTC.find_1ele_by_classname(10,"product-price__current-price","flash-sale-price")
            pro_p = MTC.find_1ele_by_classname(0,"product-price__list-price",cls2)
            if pro_p == 0:
                self.df["Product_price"][n] = self.df["Price"][n]
            else: self.df["Product_price"][n] = pro_p
            self.df["Discount"][n] = MTC.find_1ele_by_classname(0,"product-price__discount-rate",cls2)
            self.df["Shop"][n] = MTC.find_1ele_by_classname(10,"seller-name",cls2)
            self.df["Brand"][n] =  MTC.find_1ele_by_classname(0,"brand-and-author",cls2)
            warranty = MTC.get_rate_star(2,"itemRight")
            self.df["Warranty_time"][n] = warranty[0]
            self.df["Warranty_way"][n] = warranty[1]
            self.df["Warranty_place"][n] = warranty[2]
            self.df["Sold"][n] = MTC.find_ele_by_xpath(2,"/html/body/div[1]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[2]/div[2]")
            MTC.script_page()
            self.df["More_inf"][n] = MTC.find_1ele_by_classname(2,"content has-table",cls2)
            self.df["Rate"][n] = MTC.find_1ele_by_classname(2,"review-rating__point",cls2)
            self.df["Comment"][n] = MTC.find_1ele_by_classname(2,"review-rating__total",cls2)
            star = MTC.get_rate_star(2,"review-rating__number")
            self.df["5"][n] = star[0]
            self.df["4"][n] = star[1]
            self.df["3"][n] = star[2]
            self.df["2"][n] = star[3]
            self.df["1"][n] = star[4]
             
            MTC.browser.close()
            #print(df.loc[n])
            #if n == 4 : break
            n += 1

        def Create_file(data):
            f_name = input("file name:")
            path = "C:\\Users\\Admin\\Desktop\\PTDL_R\\mouse_crawler\\" + str(f_name) + ".csv"
            data.to_csv(path)

            return print("Your file has been saved in", path)

        Create_file(self.df)
        return

SC = start_craw(df)
SC.craw()







