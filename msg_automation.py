from selenium import webdriver
from keyboard import press
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd
import keyboard
import random

pause_pt =False # setpause value to false 


def pause_func():         #function to stop loop
    global pause_pt
    pause_pt = True #set pause value to true

data = pd.read_csv("ids.csv",names=['B']) #reading the csv file which contains the facebook ids(B column)
ids_targets= data.B.tolist() #alternatively you can  make a list of  targets = [18882121112,12232442423..]
print(ids_targets)
x = "facebook_email"
y = "facebook_password"
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

          ]  # list of ids to iterate
             # id of  message box in messanger changes over requests

number = 1
text = "your message"
for id_target in ids_targets:
    msg_url ='https://www.facebook.com/messages/t/' + id_target     

    keyboard.add_hotkey("ctrl+alt", lambda: pause_func()) #calling pause_func by clicking "ctrl+alt"
                                                     
    if pause_pt == True:   #it will break the loop 
        break 
    try:
        driver.get(msg_url)
        driver.implicitly_wait(5)
        msg = driver.find_element_by_css_selector('div._kmc._7kpg.navigationFocus') #finding css selector  of msg_box of class "_kmc _7kpg navigationFocus"

        for id_logic in id_dom: #iterating over ids of the msg_box since it changes everytime / most of the time
            try:
                msg_text = msg.find_element_by_id(id_logic) #finding the id in the msg
                for letters in text:
                    msg_text.send_keys(letters) #sending each letter of the target msg
                    time.sleep(random.uniform(0.1, 0.3)) #sending each letter at a time span to slow down the speed of typing
                                                          
                msg_text.send_keys(Keys.ENTER) 
                ids_targets.remove(id_target) #remove the id if msg is sent 
                print("msg sent to\t",id_target)
                break


            except:
                print("error with\t",id_logic)


    except:
        print("Skiping")
    print(number,"-----------------------------------------Msg_automate_kaux---------------------------------------------")
    number+=1
    time.sleep(random.uniform(3.2,4.5)) #sleeping after sending a msg
pd.DataFrame(ids_targets).to_csv("fish_query_assam12_towns_info.csv",mode='w') #saving the remaining facebook_ids








