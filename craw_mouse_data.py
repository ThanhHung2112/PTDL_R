from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from time import sleep
#from easygui import passwordbox

# Lưu ý: Cần đặt file chromedriver chung bên cạnh để có thể chạy chương trình

    #  1.2 Giả lập chrome
browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://shopee.vn/search?keyword=chu%E1%BB%99t%20m%C3%A1y%20t%C3%ADnh")
#Cào dữ liệu từ shoppe
#(Hiện tại link shoppe đang lỗi k thể truy cập)
mouse_shoppe = browser.find_elements_by_class_name("_1N6I4W")
print('Mouse Shoppe')
x = 1
for mouse in mouse_list:
    #mouns_l = mouns.find_element_by_xpath("_10Wbs- _5SSWfi UjjMrh")
    #sleep(random.randint(2,5))
    print(x,mouse.text)
    x = x+1
browser.close()
sleep(random.randint(4,8))
# Cào dữ liệu từ lazada
browser.get("https://www.lazada.vn/catalog/?spm=a2o4n.home.search.1.19056afef7Vf6H&q=Chu%E1%BB%99t%20m%C3%A1y%20t%C3%ADnh&_keyori=ss&from=search_history&sugg=Chu%E1%BB%99t%20m%C3%A1y%20t%C3%ADnh_0_1")

mouse_lazada = browser.find_elements_by_class_name("_3PztA")
x = 1
print('Mouse Lazada ')
for mouse in mouse_lazada:
    #mouns_l = mouns.find_element_by_xpath("_10Wbs- _5SSWfi UjjMrh")
    #sleep(random.randint(2,5))
    print(x,mouse.text)
    x = x+1

browser.close()