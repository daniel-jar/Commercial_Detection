from pickle import TRUE
import time
import selenium as se
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
    #     # if "ist nicht in einem aktiven Spiel" in html:
from datetime import datetime
DOWNLOADPATH = "C:/Users/Daniel/Downloads"
import glob
import os



chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080");
chrome_options.add_argument("--no-sandbox");
#chrome_options.add_argument("--headless");
chrome_options.add_argument("--disable-gpu");
chrome_options.add_argument("--disable-crash-reporter");
chrome_options.add_argument("--disable-extensions");
chrome_options.add_argument("--disable-in-process-stack-traces");
chrome_options.add_argument("--disable-logging");
chrome_options.add_argument("--disable-dev-shm-usage");
chrome_options.add_argument("--log-level=3");
chrome_options.add_argument("--output=/dev/null");



chrome_options.add_experimental_option("prefs", {
  "download.default_directory": DOWNLOADPATH,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
#url = "https://euw.op.gg/summoners/euw/darkmoon008/ingame"
#url = "https://euw.op.gg/summoners/euw/Hashtag%20Swag/ingame"
url = "https://euw.op.gg/summoners/euw/papatabachi/ingame"
#url = "https://euw.op.gg/summoners/euw/cr4yzed/ingame"
#while TRUE:

browser.get(url)
time.sleep(10)
dateTimeObj = datetime.now()
curTime = dateTimeObj.strftime("%H:%M:%S.%f")
date = dateTimeObj.strftime("%d.%m.%Y")

if len(browser.find_elements(By.XPATH,"//*[ text() = 'ZUSTIMMEN']"))>0:
    browser.find_element(By.XPATH,"//*[ text() = 'ZUSTIMMEN']").click()

if len(browser.find_elements(By.XPATH,"//*[ text() = 'Aufnehmen']"))>0:
#print(elem.is_displayed)
#html = browser.page_source
    print(curTime)
    print(url+" ist in einem aktiven Spiel")
    browser.find_element(By.XPATH,"//*[ text() = 'Zuschauen']").click()
    
    list_of_files = glob.glob(DOWNLOADPATH+"/*") # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    time.sleep(10)
    os.startfile(latest_file)
else:
    print(curTime)
    print(url+" ist in keinem aktiven Spiel")
    # try:
    #     elem = len(browser.find_element(By.XPATH,"//*[ text() = 'Aufnehmen']"))
    #     #print(elem.is_displayed)
    #     #html = browser.page_source
    #     print(url+" ist in einem aktiven Spiel")
    #     # if "ist nicht in einem aktiven Spiel" in html:
    #     #     print(url+" ist nicht in einem aktiven Spiel")
    #     # else:
    #     #     print(url+" ist in einem aktiven Spiel")
    # except:
    #         print(url+" ist in keinem aktiven Spiel")