from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import logging
import random


def isimOlusturucu():
    isim = ["İrem","Ali", "Veli", "Elif", "Veli", "Hamit", "Elif", "Zehra"]
    soyisim = ["Keskin","Beyaz", "Doruk", "Kır", "Yerli", "Kaya", "Yıldız", "Yurttaş"]
    return "{} {}".format(random.choice(isim), random.choice(soyisim))
 
for i in range(1):
    print(isimOlusturucu())

def kadıOlusturucu():
  kadı=["iremmmk","jalemahsuuu","özlenm98a","telamhel55","351qametsah1","mahmutjule872","yasanbuhara159","veliiii","ahmmettt","782harun98","bela234z"]
  kadı1=["samiiii","sametu34","mahmet2892","zen8720","piton965","mahmutkeskin872","zx1234","haso000x","benjaminüzeyir","oraldoj5754","samet234xxa","uzeyir_","usta32_4_"]
  return "{} {}".format(random.choice(kadı), random.choice(kadı1))
for i in range(1):
    a=(kadıOlusturucu().replace(" ",""))
print(a)








PROXY = "169.0.237.181:8080" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

driver = webdriver.Chrome(options=chrome_options,executable_path="chromedriver")











driver2=webdriver.Chrome()
driver = webdriver.Chrome()
driver2.get("https://tr.emailfake.com/")
copy=driver2.find_element_by_id("copbtn")
copy.click()
driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(3)
epostagir=driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
epostagir.send_keys(Keys.CONTROL, 'v')
adgir=driver.find_element_by_name("fullName")
adgir.send_keys(isimOlusturucu())
kadıgir=driver.find_element_by_name("username")
kadıgir.send_keys(a)
sifregir=driver.find_element_by_name("password")
sifregir.send_keys("lqm33washere")
kayıt=driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[7]/div/button")
kayıt.click()
logging.basicConfig(filename='kullaniciler.txt',level=logging.DEBUG)
logging.debug(a)

