import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class GMAILINBOX(BaseDriver):
    text_compose_xpath = "//div[@class = 'T-I T-I-KE L3']"
    text_to_mail_xpath = "//input[@role='combobox']"
    text_popup_xpath = "//button[@class = 'M6CB1c rr4y5c']"
    text_to_click_xpath = "//div[@class = 'agM agG']/div"
    text_frame_id = "callout"
    text_subject_xpath = "//input[@name = 'subjectbox']"
    text_messagebody_xpath = "//div[@aria-label = 'Message Body']"

    text_moreoptions_xpath = "//div[@class = 'J-JN-M-I J-J5-Ji Xv L3 T-I-ax7 T-I']"
    text_label_xpath = "//span[@class = 'J-Ph-hFsbo']"
    text_sociallabel_xpath = "//div[@title='Social']"

    text_sendbutton_xpath = "//div[@class = 'dC']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_composemail(self):
        cp = self.findelement(By.XPATH, self.text_compose_xpath).click()
        return cp

    def enter_to_email(self, emailid):
        et = self.findelement(By.XPATH, self.text_to_mail_xpath).send_keys(emailid)
        self.wait_presence_of_element(By.XPATH, self.text_to_click_xpath).click()
        return et

    def popuphandle(self):
        try:
            self.switch_to_frame(self.text_frame_id)
            self.findelement(By.XPATH,self.text_popup_xpath).click()
            self.switch_to_parent()

        except:
            print("no such element")
    def subject(self,Text):
        sb = self.findelement(By.XPATH, self.text_subject_xpath)
        sb.click()
        sb.send_keys(Text)
    def messagebody(self,Text):
        mb = self.findelement(By.XPATH,self.text_messagebody_xpath)
        mb.click()
        mb.send_keys(Text)
    def label_social(self):
        self.findelement(By.XPATH,self.text_moreoptions_xpath).click()
        self.findelement(By.XPATH,self.text_label_xpath).click()
        self.findelement(By.XPATH,self.text_sociallabel_xpath).click()
    def click_on_send(self):
        send =self.findelement(By.XPATH,self.text_sendbutton_xpath).click()
        time.sleep(5)
        return send


