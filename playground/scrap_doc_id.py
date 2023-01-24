import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Enable Performance Logging of Chrome.
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

# Create the webdriver object and pass the arguments
options = webdriver.ChromeOptions()

# Chrome will start in Headless mode
options.add_argument('headless')

# Ignores any certificate errors if there is any
options.add_argument("--ignore-certificate-errors")

# Startup the chrome webdriver with executable path and
# pass the chrome options and desired capabilities as
# parameters.
driver = webdriver.Chrome(service=Service(f"../chromedriver/stable/chromedriver"),
                          options=options,
                          desired_capabilities=desired_capabilities)

# Send a request to the website and let it load
driver.get(f'https://eproc.esdm.go.id/eproc4/lelang')
 
# find id of option
input = Select(driver.find_element(By.NAME, 'tbllelang_length'))
input.select_by_visible_text("Semua")

time.sleep(30)

page_source = driver.page_source

# Quiting Selenium
driver.quit()

soup = BeautifulSoup(page_source, "html.parser")
td_ids = soup.find_all('td', attrs = {'class':'sorting_1'})

id = [ele.text.strip() for ele in td_ids]

print(id)
print(len(id))