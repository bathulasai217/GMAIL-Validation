from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from base.base_driver import BaseDriver
class LoginPage(BaseDriver):
    text_username_id = "identifierId"
    text_nextemail_id = "identifierNext"
    text_password_id = "input[name = 'Passwd']"
    text_nextpass_id = "passwordNext"
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def username(self,emailid):
        username = self.findelement(By.ID,self.text_username_id)
        username.clear()
        username.send_keys(emailid)
        return username
    def password(self,password):
        passw = self.findelement(By.CSS_SELECTOR,self.text_password_id).send_keys(password)
        return passw
    def click_on_next(self):
        nextemail = self.wait_for_element_to_be_clickable(By.ID,self.text_nextemail_id).click()
        return nextemail
    def click_on_nextpassword(self):
        nextp = self.findelement(By.ID,self.text_nextpass_id).click()
        return nextp


