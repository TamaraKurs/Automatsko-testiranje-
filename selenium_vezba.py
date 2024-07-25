from concurrent.futures import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def positive_testing():
 
 driver = webdriver.Chrome()
 navigationPage = driver.get("https://elearn.smartinit.net/login/index.php")

 username = driver.find_element("id", "username").send_keys("deana.jerkovic13@gmail.com")
 driver.implicitly_wait(10)
 password = driver.find_element("id", "password").send_keys("klasikaK1-")
 login = driver.find_element("id", "loginbtn").click()

#potvrdjivanje uspesnog testa lociranjem elementa na pocetnoj strani

 homePage = driver.find_element("xpath","//*[contains(text(), 'Automatsko testiranje softvera 2/24')]")

 assert homePage.is_displayed



def negative_testing():
   driver = webdriver.Chrome()
   navigationPage = driver.get("https://elearn.smartinit.net/login/index.php")

   username = driver.find_element("id", "username").send_keys("tamara.mitrovic")
   #driver.implicitly_wait(10)
   #element = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
   password = driver.find_element("id", "password").send_keys("123")
   login = driver.find_element("id", "loginbtn").click()

#potvrdjivanje uspesnog testa lociranjem validacione poruke 

   validacionaPoruka = driver.find_element("xpath","//*[contains(text(), 'Pogrešno korisničko ime ili lozinka. Molimo pokušajte ponovo.')]")

   assert validacionaPoruka.is_displayed

def negative_testing2():
   driver = webdriver.Chrome()
   navigationPage = driver.get("https://elearn.smartinit.net/login/index.php")
   
   username = driver.find_element("id", "username").send_keys("tamara.mitrovic")
   #driver.implicitly_wait(10)
   #element = wait.until(EC.visibility_of_element_located((By.ID, 'password')))
   password = driver.find_element("id", "password").send_keys("123")
   login = driver.find_element("id", "loginbtn").click()

#potvrdjivanje uspesnog testa lociranjem validacione poruke 

   validacionaPoruka = driver.find_element("xpath","//*[contains(text(), 'Pogrešno korisničko ime ili lozinka. Molimo pokušajte ponovo.')]")

   assert validacionaPoruka.is_displayed







# konstrukcija if __name__ == '__main__': se koristi za kontrolu izvršavanja koda. Ovaj blok se izvrsava samo ako se datoteka pokrene direktno. Tada ce biti pozvana funkcija positive_testing
if __name__ == '__main__':
    positive_testing()
    negative_testing()
