from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

PATH = os.environ.get('CHROME_WEBDRIVER_PATH')
driver = webdriver.Chrome(PATH)
driver.get(r"https://linkus-chat-app.herokuapp.com/")

# create room
room = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "room"))
)
room.send_keys('test_room')
room.send_keys(Keys.RETURN)

# enter user
name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "name"))
)
name.send_keys('Selenium_testing')

button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "modal-button"))
)
button.click()

# send message
message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "message-container"))
)
message.send_keys("this is an automated message by selenium!")

button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "send-button"))
)
button.click()
