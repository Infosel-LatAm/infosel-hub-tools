#! /sbin/bash python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



CHROMEDRIVER_PATH = './chromedriver'

chrome_options = Options()

chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("detach", True)

LOGIN_PAGE = 'https://hub.infosel.com/'
USERNAME = 'YOUR_USER@dominio.com'
PASSWORD = 'YOUR_PASSWORD'

global driver

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
wait = WebDriverWait(driver, 30)
driver.get(LOGIN_PAGE)
wait.until(EC.element_to_be_clickable((By.ID, "mui-1"))).send_keys(USERNAME)
wait.until(EC.element_to_be_clickable((By.ID, "mui-2"))).send_keys(PASSWORD)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Ingresar']"))).click()


