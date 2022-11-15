import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.service import Service
serv_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=serv_obj)
wait = WebDriverWait(driver,1)
driver.implicitly_wait(20)
driver.get("https://www.gmail.com/")
driver.maximize_window()
usernmae = driver.find_element(By.ID,"identifierId")
usernmae.clear()
usernmae.send_keys("bathulasairkishna9133@gmail.com")
wait.until(EC.element_to_be_clickable((By.ID,"identifierNext"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name = 'Passwd']"))).send_keys("Kalyani@#9133")
driver.find_element(By.ID,"passwordNext").click()
try:
    driver.switch_to.frame("callout")
    driver.find_element(By.XPATH,"//button[@class = 'M6CB1c rr4y5c']").click()
    driver.switch_to.parent_frame()
except:
    print("no such element")
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class = 'T-I T-I-KE L3']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@role='combobox']"))).send_keys("bathulasairkishna9133@gmail.com")
wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class = 'agM agG']/div"))).click()
sb = driver.find_element(By.XPATH,"//input[@name = 'subjectbox']")
sb.click()
sb.send_keys("Test Mail")
mb = driver.find_element(By.XPATH,"//div[@aria-label = 'Message Body']")
mb.click()
mb.send_keys("Test Mail Body")
driver.find_element(By.XPATH,"//div[@class = 'J-JN-M-I J-J5-Ji Xv L3 T-I-ax7 T-I']").click()
driver.find_element(By.XPATH,"//span[@class = 'J-Ph-hFsbo']").click()
driver.find_element(By.XPATH,"//div[@title='Social']").click()
driver.find_element(By.XPATH,"//div[@class = 'dC']").click()


time.sleep(5)

