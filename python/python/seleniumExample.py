from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By 

driver= webdriver.Chrome()
driver.maximize_window()#tam ekran yapmak için
driver.get("https://www.google.com/")
#sleep(10)
input=driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")#yazı yazmak için kullanıyoruz
searchButton=driver.find_element(By.NAME,"btnK")#google arama butonuna tıkladık
sleep(10)
searchButton.click()
firstResult=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var.")


while True:
    continue
#HTML LOCATORS

#copy/fullXpath 
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a
#copy/xpath
#//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a

#web scraping
#data scraping