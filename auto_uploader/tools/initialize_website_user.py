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

        #Currently chrome is the only option. If chrome is not installed on the machine this will not work.
        if self.browser == "Chrome":
            driver = webdriver.Chrome()
        else:
            pass

        driver.get(str(self.url))
        wait = WebDriverWait(driver, 10)

    #This function is specific for each website since the ID can be different from site to site. I'm planning on being able to
    # make this a user input where you click on the field during the initial setup so that the average user won't have to
    # identify the correct code, ID, name etc. for a given field.
    def login_nm911(self, user):
        wait.until(EC.element_to_be_clickable((By.ID, "provider_id"))).send_keys(user.username)
        wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(user.password)
        wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
        time.sleep(1)

    #This function is specific for each website since the ID can be different from site to site.
    #Currently not clicking the upload function since we are still in the testing phase. Just uncomment the line to upload.
    def upload_nm911(self, path_to_file):
        driver.find_element(by=By.ID, value="file").send_keys(path_to_file)
        # wait.until(EC.element_to_be_clickable((By.ID, "uploadbutton"))).click()
        time.sleep(1)

    #It is important to close the driver between websites.
    def logout(self):
        driver.close()

        

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #It's imporant to remember we can do f string manipulation for whatever reason- I'll leave it in during development.
    def get_login(self):
        print(f"my username is {self.username}, my password is {self.password}")



if __name__ == "__main__":
    ######can be safely deleted upon download, just for testing purposes###############
    try:
        import sys
        sys.path.append("E:/save/")
        from secret_module import secret_info
    except:
        pass
    ##################################################################################

    chrome = Website("https://portal.nm911.org/", "Chrome")
    user_me_nm911 = User(secret_info.username, secret_info.password)

    chrome.login_nm911(user_me_nm911)
    chrome.upload_nm911("C:/Users/GIS/Desktop/thing/GIS_upload.zip")

    time.sleep(5)
    driver.close()