from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time
import pickle
from password import password, number
user_agent = UserAgent()
options = webdriver.ChromeOptions()
# options.add_argument(f"user-agent={user_agent['google chrome']}")

# webdriver mode disable
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)

try:
    print(number)
    driver.get("https://vk.com/")
    time.sleep(10)
    numberBox = driver.find_element(By.ID, 'index_email')
    numberBox.clear()
    saveLogIn = driver.find_element(By.ID, 'index_save_user_checkbox')
    saveLogIn.click()
    numberBox.send_keys(number)
    time.sleep(15)
    butToLogIn = driver.find_element(By.CLASS_NAME, 'VkIdForm__signInButton')
    butToLogIn.click()
    time.sleep(10)
    butToSkipSMS = driver.find_element(By.CSS_SELECTOR, '.vkc__Bottom__switchToPassword')
    butToSkipSMS.click()
    time.sleep(10)

    passwordBox = driver.find_element(By.NAME, 'password')
    passwordBox.clear()
    passwordBox.send_keys(password)
    driver.find_element(By.CLASS_NAME, 'vkc__Password__ViewIcon').click()
    time.sleep(5)
    passwordBox.send_keys(Keys.ENTER)
    time.sleep(15)
    # cookies
    # pickle.dump(driver.get_cookie(), open(f'{number}_cookies', 'wb'))

    messengerA = driver.find_element(By.ID, 'l_msg')
    messengerA.click()
    time.sleep(15)
    defaultDialog = driver.find_element(By.CSS_SELECTOR, '._im_dialog_200625992')
    defaultDialog.click()
    time.sleep(15)

    lastMesseges = driver.find_elements(By.CLASS_NAME, "im-mess-stack")

    # for check in lastMesseges:
    #     print(check.get_attribute('data-peer'))
    while True:
        time.sleep(5)
        lastMesseges = driver.find_elements(By.CLASS_NAME, "im-mess-stack")
        if lastMesseges[-1].get_attribute('data-peer')=='200625992':
            driver.find_element(By.CLASS_NAME, 'im-chat-input--text').send_keys('чел ты', Keys.ENTER)
            print('отвечаю долбоебу')


except Exception as ex:
    print(ex)

driver.quit()