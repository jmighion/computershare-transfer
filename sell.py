# Sell all ESPP shares from Computershare
# Company name, login info, and an electronic payment already setup
# Currently, an EFT avoids all fees and charges
# Loading the previously mentioned info from a .env file in the same directory as this file

import os
import sys

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Load env variables from ".env" file in the same folder
load_dotenv()

# Your Computershare username
USERNAME = os.getenv("USERNAME")

# Your Computershare password
PASSWORD = os.getenv("PASSWORD")

# Your company name
COMPANY_NAME = os.getenv("COMPANY_NAME")

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

# Automatically get and cache the webdriver for Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Function to sell all shares from Computershare directly
def sell_shares():
    wait = WebDriverWait(driver, 10)
    driver.get("https://www-us.computershare.com/employee/login/selectcompany.aspx")
    try:
        print("Sign in")
        wait.until(expected_conditions.title_contains("Employee - Plans"))
        driver.find_element(By.ID, "SearchName").send_keys(str(COMPANY_NAME))
        driver.find_element(By.NAME, "submitform").click()

        print("Select Employee login")
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//a[contains(@href,"Employee/Login")]')))
        driver.find_element(By.XPATH, '//a[contains(@href,"Employee/Login")]').click()
        wait.until(expected_conditions.presence_of_element_located((By.ID, "loginIDType")))

        print("Choose Username login option")
        select = Select(driver.find_element(By.ID, "loginIDType"))
        select.select_by_visible_text("Username")

        print("Input credentials")
        driver.find_element(By.ID, "tempLoginID").send_keys(str(USERNAME))
        driver.find_element(By.ID, "employeePIN").send_keys(str(PASSWORD))
        print("Login")
        driver.find_element(By.NAME, "sbmtBtn").click()

        print("Click Transact")
        wait.until(expected_conditions.presence_of_element_located((By.ID, "ctl01_primaryNavigation")))
        driver.find_element(By.XPATH, '//a[contains(@href,"Transactions")]').click()
        print("Click Sell button")
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "DlgLnk")))
        driver.find_element(By.XPATH, '//a[contains(@title,"Sell Shares")]').click()

        print("Click Market order")
        wait.until(expected_conditions.presence_of_element_located((By.ID, "selectSellMethod2")))
        driver.find_element(By.ID, "selectSellMethod2").click()
        print("Click Accept")
        driver.find_element(By.ID, "acceptance5").click()
        print("Click Next")
        driver.find_element(By.XPATH, '//input[contains(@value,"Next")]').click()

        print("Click All shares")
        driver.find_element(By.XPATH, '//input[@value="all" and @name="sharePortion"]').click()
        print("Click Electronic payment")
        driver.find_element(By.XPATH, '//input[@value="D" and @name="proceedsDistributionMethod"]').click()
        print("Click Next")
        driver.find_element(By.XPATH, '//input[contains(@value,"Next")]').click()

        print("Input PIN again")
        wait.until(expected_conditions.presence_of_element_located((By.ID, "employeePIN")))
        driver.find_element(By.ID, "employeePIN").send_keys(str(PASSWORD))
        print("Click submit")
        driver.find_element(By.XPATH, '//input[@value="Submit" and @type="submit"]').click()
    except:
        # Need to add more specific exception catches
        print("Error?")
        print(sys.exc_info()[0])
        pass

    driver.quit()


try:
    sell_shares()
except:
    driver.quit
