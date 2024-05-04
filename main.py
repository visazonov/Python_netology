import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
