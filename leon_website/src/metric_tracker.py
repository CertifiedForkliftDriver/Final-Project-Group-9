import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from popUsers import user52 as user


# Initialize browser
driver = webdriver.Chrome()

# Navigate to your website 
driver.get("http://localhost:3000/")

user.userAction(driver)

# Close the browser
driver.quit()