from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

navigationPage = driver.get("https://elearn.smartinit.net/login/index.php")
username = driver.find_element("id", "username").send_keys("tamara.mitrovic")
driver.implicitly_wait(10)
password = driver.find_element("id", "password").send_keys("123")
login = driver.find_element("id", "loginbtn").click()


fjalfjawlkds 