import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import browser, driver_version
from dotenv import load_dotenv
load_dotenv()

def setup_driver(browser, driver_version):
    if browser == "chrome":
        from webdriver_manager.chrome import ChromeDriverManager
        
        driver = webdriver.Chrome(ChromeDriverManager(driver_version).install())
    elif browser == "firefox":
        from webdriver_manager.firefox import GeckoDriverManager

        driver = webdriver.Firefox(executable_path=GeckoDriverManager(driver_version).install())
    elif browser == "edge":
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        driver = webdriver.Edge(EdgeChromiumDriverManager(driver_version).install())
    elif browser == "opera":
        from webdriver_manager.opera import OperaDriverManager

        driver = webdriver.Opera(executable_path=OperaDriverManager(driver_version).install())
    elif browser == "chromium":
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.utils import ChromeType

        driver = webdriver.Chrome(ChromeDriverManager(driver_version, chrome_type=ChromeType.CHROMIUM).install())
    elif browser == "ie":
        from webdriver_manager.microsoft import IEDriverManager

        driver = webdriver.Ie(IEDriverManager(driver_version,).install())
    else:
        raise "Browser not recognizable, please check the supported browser and the browser spelling in settings file"

    return driver

def setup_timeout(timeout):
    driver.wait = WebDriverWait(driver, timeout)

def wait_until(By, selector):
    driver.wait.until(
        EC.presence_of_element_located((By, selector))
    )

def click(selector, By):
    driver.wait.until(
        EC.element_to_be_clickable((By, selector))
    ).click()

def send_keys(keys, selector, By):
    driver.wait.until(
        EC.element_to_be_clickable((By, selector))
    ).send_keys(keys)

def login(username, password):
    '''
    Login to apps.unnes, only accept using Google auth.

    please fill username and password in setting file
    '''    

    driver.get("https://apps.unnes.ac.id/")
    window_before = driver.window_handles[0]
    click("g-signin2", By.CLASS_NAME)

    #switch to login window
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    send_keys(username, '//input[@type="email"]', By.XPATH)
    click('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div', By.XPATH)

    # time.sleep(10)
    # isi password
    send_keys(password, "//input[@type='password']", By.XPATH)

    # next
    click("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div", By.XPATH)
    driver.switch_to.window(window_before)

# go to elena dashboard
def elena():
    """
    go to active semester
    """
    click("//a[contains(@href, 'https://apps.unnes.ac.id/30')]", By.XPATH)
    wait_until(By.CLASS_NAME, "xcomponent-outlet")
    # print(driver.find_element_by_tag_name("body").text)
    # time.sleep(5)
    driver.switch_to.frame(driver.find_element_by_class_name("xcomponent-component-frame"))
    # print(driver.find_element_by_tag_name("body").text)
    wait_until(By.CLASS_NAME, "authfy-login")
    click("//input[contains(@class, 'btn btn-lg btn-primary')]", By.XPATH)

if __name__ == "__main__":
    USERNAME = os.getenv("EMAIL_ELENA")
    PASSWORD = os.getenv("PASSWORD_ELENA")

    driver = setup_driver(browser, driver_version)
    setup_timeout(60)
    login(USERNAME, PASSWORD)
    elena()

