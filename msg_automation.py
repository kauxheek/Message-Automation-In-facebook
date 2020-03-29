from selenium import webdriver
from keyboard import press
from selenium.webdriver.common.keys import Keys
import id_info
import time
import pandas as pd
import keyboard
import random

pause_pt =False


def func1():
    global pause_pt
    pause_pt = True
data = pd.read_csv("fish_query_assam12_towns_info.csv",names=['B'])

ids_targets= data.B.tolist()
print(ids_targets)
x = id_info.email
y = id_info.password
driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
email = driver.find_element_by_css_selector("input[name=email]")
email.send_keys(x)
password = driver.find_element_by_css_selector("input[name=pass]")
password.send_keys(y)
login_button = driver.find_element_by_css_selector("input[type=submit]")
login_button.click()


id_dom = ["js_f","js_g","js_h","js_i",
           "js_j", "js_k","js_l","js_m","js_n","js_o","js_p","js_q","js_r",
           "js_s","js_t","js_u","js_v","js_w","js_x","js_y","js_z","js_a","js_b","js_c","js_d","js_e","js_1","js_2","js_3",
           "js_4","js_5","js_6","js_7","js_8","js_9","js_10","js_0",

          ]

number = 1
text = "CIL AGROTECH LIMITED,Assam is engaged in commercial  BIOFLOC FISH farming.CoCoPL group of Assam and Delhi is engaged in manufacturing BIOFLOC FISH TANK and also helps to set up entire fish tanks and also assist in procuring Fish Seedlings.We also provide  practical training for BIOFLOC FISH farming. Contact our whatsapp no 9531102021  for  more information or send message to our email assamplastic@gmail.com. Visit our Facebook page  https://www.facebook.com/BioFloc-Fish-Farming-NE-107026507571390 for more information.CIL AGROTECH LIMITED &CONTEMPORARY CONSULTANTS PRIVATE LIMITED (visit : https://www.cocopl.com)"
for id_target in ids_targets:
    msg_url ='https://www.facebook.com/messages/t/' + id_target

    keyboard.add_hotkey("ctrl+alt", lambda: func1())
    if pause_pt == True:
        break
    try:
        driver.get(msg_url)
        driver.implicitly_wait(5)
        msg = driver.find_element_by_css_selector('div._kmc._7kpg.navigationFocus')

        for id_logic in id_dom:
            try:
                msg_text = msg.find_element_by_id(id_logic)
                for letters in text:
                    msg_text.send_keys(letters)
                    time.sleep(random.uniform(0.1, 0.3))
                msg_text.send_keys(Keys.ENTER)
                ids_targets.remove(id_target)
                print("msg sent to\t",id_target)
                break


            except:
                print("error with\t",id_logic)


    except:
        print("Skiping")
    print(number,"-----------------------------------------Msg_automate_kaux---------------------------------------------")
    number+=1
    time.sleep(random.uniform(3.2,4.5))
pd.DataFrame(ids_targets).to_csv("fish_query_assam12_towns_info.csv",mode='w')








