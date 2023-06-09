from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.action_chains import ActionChains 
from constants import globalConstants

class Test_Sauce:
    # def __init__(self):
    #     self.driver=webdriver.Chrome(ChromeDriverManager().install())
    #     self.driver.maximize_window()
    #     self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"user-name")))
       
        #maksımum 5 sn kadr duruyor ekran gorunur
        #en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        usernameInput=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"password")))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
     
        errorMessage=self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU:{testResult}")

    def test_valid_login(self):
        self.driver.get(globalConstants.URL)
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"user-name")))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.ID,"password")))
        passwordInput=self.driver.find_element(By.ID,"password")
        

        #action Chains-zincir nerede çağırırsak çağıralım zincir misalı ikiisi bir arada gelecek!
        actions=ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        #usernameInput.send_keys("standard_user")
        #passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(3)
        loginBtn.click()
        sleep(5)
        self.driver.execute_script("window.scrollTo(0,500)")#javascript ile sayfanın sonuna atmak istedim bu kod ile yaptım.
        sleep(3)

       

        
testClass=Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()

