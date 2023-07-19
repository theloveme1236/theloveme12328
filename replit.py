import os
os.system('pip install selenium')
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome, ChromeOptions
import pickle
#from keep_alive import keep_alive

#keep_alive()
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.maximize_window()
con = 0
errrrroo = 0
def cookis_like():
    for cookie in cookies:
        
        fields = cookie.strip().split('\t')
        if len(fields) >= 7:
            cookie_dict = {'name': fields[5],'value': fields[6],'domain': fields[0],'path': fields[2],'expires': int(fields[4]),'secure': bool(fields[3])}
            driver.add_cookie(cookie_dict)
    driver.refresh()

def like3like_login():
    
    for cookies_totel in os.listdir(os.getcwd()):
        cookies_totel_1 = cookies_totel.split('_cookies')[0]
        if cookies_totel_1=='like':
            print(cookies_totel)
            driver.get("https://www.like4like.org/#social-media-platform-list")
            cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except Exception as ss:
                    print(ss)
                    continue
for cookies_totel in os.listdir(os.getcwd()):
    cookies_totel_1 = cookies_totel.split('_cookies')[0]
    if cookies_totel_1=='like':
        print(cookies_totel)
        driver.get("https://www.like4like.org/#social-media-platform-list")
        cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
            except Exception as ss:
                print(ss)
                continue
    if cookies_totel_1=='youtube':
        driver.get("https://www.youtube.com/")
        print(cookies_totel)
        with open(cookies_totel, 'r') as file:
            cookies = file.readlines()
        cookis_like()

def Subscribe():

    for s in range(40004000):
        try:
             
            driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")
            driver.maximize_window()
            driver.implicitly_wait(15)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

            driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[3]/div/div').click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)
            driver.find_element(By.ID, 'subscribe-button').click()
            
            time.sleep(5)
            #driver.save_screenshot('{}.png'.format(s))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
            time.sleep(5)

            print('succeed_Subscribe')
        except Exception as s2:
            #print(s2)
            try:
                current_url = driver.current_url
                if current_url=='https://www.like4like.org/login/':
                    print('https://www.like4like.org/login/')
                    like3like_login()
                
                all_windows = driver.window_handles
                if len(all_windows) > 1:
                    for window in all_windows[1:]:
                        driver.switch_to.window(window)
                        driver.close()

                driver.switch_to.window(driver.window_handles[0])
                #errrrroo += 1
                errrrroo='errrrt1'
                driver.save_screenshot('{}.png'.format(errrrroo))
                #print('false'+int(errrrroo))
                
                like()
            except Exception as s4:
                print(s4)
                continue
def like():
    for s in range(40004000):
        try:
            driver.get("https://www.like4like.org/earn-credits.php?feature=youtube")
            driver.maximize_window()
            driver.implicitly_wait(15)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

            time.sleep(5)
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[3]/div/div/a').click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)
            driver.find_element(By.ID, 'segmented-like-button').click()
            time.sleep(5)
            driver.save_screenshot('{}.png'.format(s))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
            time.sleep(5)
            print('succeed_like')
        except Exception as s:
            print(s)
            try:
                current_url = driver.current_url
                if current_url=='https://www.like4like.org/login/':
                    print('https://www.like4like.org/login/')
                    like3like_login()

                all_windows = driver.window_handles
                if len(all_windows) > 1:
                    for window in all_windows[1:]:
                        driver.switch_to.window(window)
                        driver.close()
                #errrrroo += 1
                #print('false'+int(errrrroo))
                errrrroo='erro'
                #driver.save_screenshot('{}.png'.format(errrrroo))
                Subscribe()
            except Exception as s3:
                print(s3)
                continue
Subscribe()
