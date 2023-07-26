import os
os.system('sudo apt update -y')
os.system('! sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('! sudo apt install ./google-chrome-stable_current_amd64.deb')
os.system('! sudo pip install selenium')
os.system('! sudo pip install pymongo')
os.system('! sudo pip install undetected_chromedriver')

import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome, ChromeOptions
import undetected_chromedriver as uc
from pymongo import MongoClient
import requests
import pickle
from datetime import datetime, timedelta
import base64
cluster = MongoClient('mongodb+srv://theloveme1238:zx5LtPcgLpcpIh7D@cluster0.pzuhxov.mongodb.net/?retryWrites=true&w=majority')
db = cluster["my_database"]
collection = db["users"]        
options = uc.ChromeOptions()
options.add_argument('--headless')
driver = uc.Chrome(options=options)

driver.implicitly_wait(10)
            
driver.maximize_window()
con = 0
errrrroo = 0
Subscribe_erro_stop_time= str('start')
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
            email = cookies_totel.split('like_cookies_')[-1].split('.pkl')[0]
            print(email)
            password = '1234thelove'
            driver.get("https://www.like4like.org/login/")
            time.sleep(2)
            driver.find_element(By.ID, 'username').send_keys(email)
            time.sleep(2)
            driver.find_element(By.ID, 'password').send_keys(password)
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, '/html/body/div[6]/form/fieldset/table/tbody/tr[8]/td/span').click()
            except:
                pass
            time.sleep(10)
            driver.get("https://www.like4like.org/user/")
            time.sleep(10)
            current_url = driver.current_url
            if current_url=='https://www.like4like.org/user/':
                print(current_url)
                print('login_usearname_passowrd')
                driver.get("https://www.like4like.org/#social-media-platform-list")
                time.sleep(5)
                cookies_add = "like_cookies_{}.pkl".format(email)
                pickle.dump(driver.get_cookies(), open("like_cookies_{}.pkl".format(email), "wb"))
                email_to_find = email
                user_data = collection.find_one({"email": email_to_find})
                new_login_like = 'true_login'
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"login_like": new_login_like}}
                )
                print('login_usearname_passowrd_true')
                
            else:
                print('first_logon_cookies')
                driver.get("https://www.like4like.org/#social-media-platform-list")
                cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
                for cookie in cookies:
                    try:
                        driver.add_cookie(cookie)
                    except Exception as ss:
                        print(ss)
                        continue
                driver.get("https://www.like4like.org/user/")
                time.sleep(15)
                current_url = driver.current_url
                if current_url=='https://www.like4like.org/user/':
                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_like = 'true'
                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_like": new_login_like}}
                    )
                    print('first_logon_cookies_true')
                else:
                    print('first_logon_cookies_flase')
                    email_to_find = email
                    user_data = collection.find_one({"email": email_to_find})
                    new_login_like = 'false'

                    collection.update_one(
                        {"email": email_to_find},
                        {"$set": {"login_like": new_login_like}}
                    )
                    driver.quit()
                
for cookies_totel in os.listdir(os.getcwd()):
    cookies_totel_1 = cookies_totel.split('_cookies')[0]
    if cookies_totel_1=='like':
        email = cookies_totel.split('like_cookies_')[-1].split('.pkl')[0]
        print(email)
        password = '1234thelove'
        driver.get("https://www.like4like.org/login/")
        time.sleep(2)
        driver.find_element(By.ID, 'username').send_keys(email)
        time.sleep(2)
        driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, '/html/body/div[6]/form/fieldset/table/tbody/tr[8]/td/span').click()
        except:
            pass
        time.sleep(10)
        driver.get("https://www.like4like.org/user/")
        time.sleep(10)

        current_url = driver.current_url
        if current_url=='https://www.like4like.org/user/':
            print(current_url)
            driver.get("https://www.like4like.org/#social-media-platform-list")
            time.sleep(5)
            cookies_add = "like_cookies_{}.pkl".format(email)
            pickle.dump(driver.get_cookies(), open("like_cookies_{}.pkl".format(email), "wb"))

        else:
            print('else')
            driver.get("https://www.like4like.org/#social-media-platform-list")
            cookies = pickle.load(open('{}'.format(cookies_totel), "rb"))
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except Exception as ss:
                    print(ss)
                    continue
            driver.get("https://www.like4like.org/user/")
            time.sleep(15)
            current_url = driver.current_url
            if current_url=='https://www.like4like.org/user/':
                email_to_find = email
                user_data = collection.find_one({"email": email_to_find})
                new_login_like = 'true'
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"login_like": new_login_like}}
                )
            else:
                email_to_find = email
                user_data = collection.find_one({"email": email_to_find})
                new_login_like = 'false'

                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"login_like": new_login_like}}
                )
                driver.quit()
                
    if cookies_totel_1=='youtube':
        driver.get("https://www.youtube.com/")
        print(cookies_totel)
        with open(cookies_totel, 'r') as file:
            cookies = file.readlines()
        cookis_like()

def failed_success_minutes():
    try:
        erro_minutes=driver.find_element(By.ID, 'error-text').text
        You_have_failed  = erro_minutes.split(' success rate validation')[0]
        if You_have_failed == str('You have failed our'):
            print('You have failed our')
            minutes_to_add =  erro_minutes.split('next ')[-1].split(' minutes.')[0]
            print(minutes_to_add)
            current_time = datetime.utcnow()
            time_delta = timedelta(minutes=int(minutes_to_add))
            new_time = current_time + time_delta
            new_date = new_time.date()
            formatted_time = new_time.strftime('%H:%M')
            failed_success= "date:" + str(new_date) + "time:"+ str(formatted_time)
            print(failed_success)
            email_to_find = email
            print('____________')
            print(email_to_find)
            print('____________')
            user_data = collection.find_one({"email": email_to_find})
            collection.update_one(
            {"email": email_to_find},
            {"$set": {"limit": failed_success}})
            print('minutes_to_add_eroooooo')
            Subscribe_erro_stop_time = str('stop')
        if erro_minutes == 'No tasks are currently available, please try again later...':
            print('No tasks are currently available')
        #driver.quit()
    except Exception as ssssd2:
        
        print('failed_success_minutes:  ',ssssd2)
        
def Subscribe():

    for s in range(40004000):
        try:
             
            driver.get("https://www.like4like.org/earn-credits.php?feature=youtubes")
            driver.maximize_window()
            driver.implicitly_wait(15)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")

            driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[3]/div/div').click()
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            driver.find_element(By.ID, 'subscribe-button').click()
            
            time.sleep(3)
            
            #driver.save_screenshot('{}.png'.format(s))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR, '[alt="Click On The Button To Confirm Interaction!"]').click()
            time.sleep(5)
            print('succeed_Subscribe')
            email_to_find = email

            # البحث عن المستخدم باستخدام البريد الإلكتروني
            user_data = collection.find_one({"email": email_to_find})

            if user_data:
                print(user_data)
                # القيمة الحالية لـ sub وتحويلها إلى رقم صحيح
                current_sub_value = int(user_data.get("sub", 0))

                # تعديل القيمة وإضافة +1
                new_sub_value = current_sub_value + 1
                print('sub', int(new_sub_value))
                # تحديث الوثيقة بالقيمة الجديدة لـ sub
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"sub": new_sub_value}}
                )

            else:
                
                pass
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
                errrrroo='erro_sub_{}'.format(s)
                driver.save_screenshot('{}.png'.format(errrrroo))
                failed_success_minutes()
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
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight/1);")

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
            print('like')
            email_to_find = email
            # البحث عن المستخدم باستخدام البريد الإلكتروني
            user_data = collection.find_one({"email": email_to_find})
            
            if user_data:
                print(user_data)
                # القيمة الحالية لـ sub وتحويلها إلى رقم صحيح
                current_sub_value = int(user_data.get("like", 0))

                # تعديل القيمة وإضافة +1
                new_sub_value = current_sub_value + 1
                print('like', int(new_sub_value))
                # تحديث الوثيقة بالقيمة الجديدة لـ sub
                collection.update_one(
                    {"email": email_to_find},
                    {"$set": {"like": new_sub_value}}
                    )

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
                errrrroo='erro_like_{}'.format(s)
                driver.save_screenshot('{}.png'.format(errrrroo))
                failed_success_minutes()
                if Subscribe_erro_stop_time == str('stop'):
                    print('Subscribe_erro_stop_time')
                else:
                    print('runnnnn   Subscribe')
                    Subscribe()
            except Exception as s3:
                print(s3)
                continue
Subscribe()
