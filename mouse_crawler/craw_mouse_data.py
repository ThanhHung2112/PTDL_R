from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from time import sleep
from easygui import passwordbox
import pandas as pd

'''
    element_exist = 0

    while element_exist != True:
        element_exist = False if len(browser.find_elements_by_class_name('review-rating__point')) > 0 else True
        sleep(1)


   # wait = WebDriverWait(browser,10)
   # rate = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'review-rating__point')))


    while True:
        try:
            rate = browser.find_elements_by_class_name('review-rating__point')
            break
        except common.exceptions.NoSuchElementException:
            rate = 0
'''

# Lưu ý: Cần đặt file chromedriver chung bên cạnh để có thể chạy chương trình

    #  1.2 Giả lập chrome
browser = webdriver.Chrome(executable_path="chromedriver.exe")
'''
browser.get("https://shopee.vn/search?keyword=chu%E1%BB%99t%20m%C3%A1y%20t%C3%ADnh")
mouse_shoppe = browser.find_elements_by_class_name("_1N6I4W")
print('Mouse Shoppe')
x = 1
for mouse in mouse_list:
    #mouns_l = mouns.find_element_by_xpath("_10Wbs- _5SSWfi UjjMrh")
    #sleep(random.randint(2,5))
    print(x,mouse.text)
    x = x+1
sleep(random.randint(4,8))
browser.close()


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
'''
# Cào dữ liệu tiki
browser.get("https://tiki.vn/search?q=chu%E1%BB%99t+m%C3%A1y+t%C3%ADnh&sort=top_seller&page=1")

sleep(random.randint(2,5))

all_mouse = browser.find_elements_by_class_name("info")
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
'''
links = browser.find_elements_by_partial_link_text('')
#get the first one
x = 1
for i in links:
    print(x, i)
    x = x+1
'''
mouse_name = []
mouse_price = []
mouse_link = []
mouse_rate = []
review_rate = []
x = 1
a = 1
for mouse in all_mouse :
    #print(x, mouse.text)
    #Get Link
    links = browser.find_elements_by_class_name("product-item")
    for link in links:
        z = link.get_attribute("href")
        mouse_link.append(z)
        print(a,z)
        a = a+1
    # Get Name
    mouse_name_tiki = mouse.find_element_by_class_name("name")
    mouse_name.append(mouse_name_tiki)
    #rating_tiki = mouse.find_element_by_class_name("full-rating")
    #rt = rating_tiki.get_attribute('href')
    #sold.append(mouse.find_element_by_class_name('styles__StyledRatingQtySold-sc-732h27-0 uDeVr'))
    #print(sold[x-1].text)
    # Get Price
    price_tiki = mouse.find_element_by_class_name("price-discount__price")
    mouse_price.append(price_tiki)
    #print(x,' Name :', mouse_name_tiki.text,'_Rating :rt','\n'
     #     'price :',price_tiki.text,'link:', mouse_link[x-1],'Sold :', 'sold_tiki.text')

    x = x+1

browser.close()
print('len name:',len(mouse_name),'len price:',len(mouse_price),'len link:',len(mouse_link))
df = pd.DataFrame(mouse_name,mouse_price,mouse_link[:len(mouse_name)-1])
print(df)


