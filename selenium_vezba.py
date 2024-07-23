from selenium import webdriver
from concurrent.futures import wait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys



def positive_testing():
    driver = webdriver.Chrome()

    navigationPage = driver.get("https://elearn.smartinit.net/login/index.php")

    username = driver.find_element("id", "username").send_keys("ljubojevich.z@gmail.com")
    driver.implicitly_wait(10)
    password = driver.find_element("id", "password").send_keys("klasikaK1-")

    login = driver.find_element("id", "loginbtn").click()

    homePage = driver.find_element("xpath", "//*[contains(text(), 'Automatsko testiranje softvera 2/24')]")
    assert homePage.is_displayed

def negative_testing():
    driver = webdriver.Chrome()

    navigationPage = driver.get("https://elearn.smartinit.net/login/index.php")

    username = driver.find_element("id", "username").send_keys("ljubojevich.z@gmail.com")
    driver.implicitly_wait(10)
    password = driver.find_element("id", "password").send_keys("123")

    login = driver.find_element("id", "loginbtn").click()    

    validationError = driver.find_element("xpath", "//*[contains(text(), 'Pogrešno korisničko ime ili lozinka. Molimo pokušajte ponovo.')]")
    assert validationError.is_displayed
    

if __name__ == '__main__':
    positive_testing()
    negative_testing()