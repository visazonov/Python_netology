import os
from dotenv import load_dotenv

load_dotenv()

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import random

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(options=chrome_options)

from selenium.webdriver.support.ui import WebDriverWait


def test_authorization_yandex():
    login = os.getenv("login_ya")
    password = os.getenv("password_ya")

    driver.get("https://passport.yandex.ru/auth/")
    driver.maximize_window()

    driver.find_element(By.ID, "passp-field-login").send_keys(login)
    driver.find_element(By.ID, "passp:sign-in").click()

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, "passp-field-passwd")))

    driver.find_element(By.ID, "passp-field-passwd").send_keys(password)
    driver.find_element(By.ID, "passp:sign-in").click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "react-aria-13"))
        )
    except:
        print("error")

    assert driver.find_element(By.ID, "react-aria-13").text == "Владимир Сазонов"

    driver.close()
