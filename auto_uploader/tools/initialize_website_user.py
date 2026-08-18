from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class Website():
    def __init__(self, url, browser):
        self.url     = url
        self.browser = browser
        global driver
        global wait

        #currently chrome is the only option
        if self.browser == "Chrome":
            driver = webdriver.Chrome()
        else:
            pass

        driver.get(str(self.url))
        wait = WebDriverWait(driver, 10)

    def login_nm911(self, user):
        wait.until(EC.element_to_be_clickable((By.ID, "provider_id"))).send_keys(user.username)
        wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(user.password)
        wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
        time.sleep(1)

    def upload_nm911(self, path_to_file):
        driver.find_element(by=By.ID, value="file").send_keys(path_to_file)
        # wait.until(EC.element_to_be_clickable((By.ID, "uploadbutton"))).click()
        time.sleep(1)

    def logout(self):
        driver.close()

        

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_login(self):
        print(f"my username is {self.username}, my password is {self.password}")



if __name__ == "__main__":
    ######can be safely deleted upon download, just for testing purposes###############
    try:
        import sys
        sys.path.append("E:/save/")
        from secret import secret
    except:
        pass
    ##################################################################################

    chrome = Website("https://portal.nm911.org/", "Chrome")
    user_me_nm911 = User(secret.username, secret.password)

    chrome.login_nm911(user_me_nm911)
    chrome.upload_nm911("C:/Users/GIS/Desktop/thing/GIS_upload.zip")

    time.sleep(5)
    driver.close()