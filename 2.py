from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new chrome browser instance
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get('https://survey.usk.ac.id/')

login_link = driver.find_element(By.XPATH, '//a[@data-toggle="modal" and @data-target="#exampleModal"]')
login_link.click()


time.sleep(3)
# locate the username field and enter the username
username = driver.find_element(By.NAME,'username')
nim = input("Masukkan NIM Anda: ")
username.send_keys(nim)

# locate the password field and enter the password
password = driver.find_element(By.NAME,'password')
passwordUser = input("Masukkan Password Anda: ")
password.send_keys(passwordUser)
print(sep='\n') 


# locate the login button and click it
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

#check url
new_url = driver.current_url
# print(new_url)

#Print Table for data 
tbody_elements = driver.find_elements(By.CSS_SELECTOR, 'div.col-sm-12')
for tbody in tbody_elements:
   tr_elements = tbody.find_elements(By.TAG_NAME, 'tr')
   for tr in tr_elements:
       td_elements = tr.find_elements(By.TAG_NAME, 'td')
       if len(td_elements) >= 4:
           print(td_elements[0].text, td_elements[1].text, td_elements[2].text) # Second td
           print(td_elements[3].text) 
           print(td_elements[4].text)
           print('=====================================')
           print(sep='\n') 

#Print data from input user
print("**Input angka sesuai dengan angka sebelum kode mata kuliah**")
userInput = input("Masukkan Angka: ")
tbody_elements = driver.find_elements(By.CSS_SELECTOR, 'div.col-sm-12')
for tbody in tbody_elements:
   tr_elements = tbody.find_elements(By.TAG_NAME, 'tr')
   for tr in tr_elements:
       td_elements = tr.find_elements(By.TAG_NAME, 'td')
       if len(td_elements) >= 4:
           for td in td_elements:
               if td.text == userInput:
                  # print(td.text)
                  print(sep='\n') 
                  print("Pilih dosen yang ingin anda isi: ")
                  print(sep='\n') 
                  kodeKelas = td_elements[1].text
                  # print("Kode Kelas", td_elements[1].text)
                  print("Kelas", td_elements[2].text) # Second td
                  print("1",td_elements[3].text)
                  print("2",td_elements[4].text)
                  print('=====================================')
                  print(sep='\n') 


#check kode kelas
# print(kodeKelas)
userInput = input("Masukkan Angka Sesuai dengan dosen yang ingin di isi: (Enter 1 or 2)\n")

infElement = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{kodeKelas}')]")))
if userInput == "1":
    next_element = infElement.find_element(By.XPATH, 'following-sibling::*[2]')
    # print(next_element.text)
    next_element.click()
    time.sleep(5)
elif userInput == "2":
    next_element = infElement.find_element(By.XPATH, 'following-sibling::*[3]')
    next_element.click()
    time.sleep(5)
else:
    print("Not Found")    
    exit()

#Check new url
new_url = driver.current_url
# print(new_url)

# Assuming driver is already initialized
radio_button = driver.find_element(By.XPATH,"//input[@value='5']") # Find the radio button
              # Click the radio button
radio_button.click()
              
if radio_button.is_selected():
   print("Radio button is already selected.")
else:
   # Click the radio button if it's not already selected
   radio_button.click()
   print("Radio button clicked.")

button = driver.find_element(By.XPATH, '//button[@type="submit"]')
if button.is_displayed():
   button.click()
   print("Button is clicked")
   print("Anda telah berhasil mengisi survey")
else:
   print("Button is not displayed")



driver.quit()