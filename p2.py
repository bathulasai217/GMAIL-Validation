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
driver.find_element(By.CSS_SELECTOR,"div[aria-label = 'Social']").click()
#driver.find_element(By.CSS_SELECTOR,"td[class = 'apU xY']").click()
mails = driver.find_elements(By.XPATH,"//tr[@class = 'zA zE']/td[4]")
for m in mails:
    if m.text == "me":
        driver.find_element(By.XPATH, "//tr[@class = 'zA zE']/td[3]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//tr[@class = 'zA zE']/td[4]").click()
        time.sleep(2)
        subject = driver.find_element(By.CSS_SELECTOR,"h2[class = 'hP']")
        print(subject.text)
        if subject.text == "Test Mail":
            print("passed")
            assert True
        else:
            assert False
        body = driver.find_element(By.XPATH,"//div[@class='gs']/div[3]")
        print(body.text)
        if body.text == "Test Mail Body":
            print("true")
            assert True
        else:
            assert False




time.sleep(10)