from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
class GmailInbox(BaseDriver):
    text_socialmails_css = "div[aria-label = 'Social']"
    text_mails_xpath = "//tr[@class = 'zA zE']/td[4]"
    text_markstar_xpath = "//tr[@class = 'zA zE']/td[3]"
    text_clickonm_xpath = "//tr[@class = 'zA zE']/td[4]"
    text_subject_css = "h2[class = 'hP']"
    text_maibody_xpath = "//div[@class='gs']/div[3]"
    text_mail_name = "me"
    text_subject_title = "Test Mail"
    text_mailbody_title = "Test Mail Body"
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    def mails(self):
        mails = self.findelements(By.XPATH,self.text_mails_xpath)
        return mails
    def markstar(self):
        ms = self.findelement(By.XPATH,self.text_markstar_xpath).click()
        return ms
    def clickonmail(self):
        ce = self.findelement(By.XPATH,self.text_clickonm_xpath).click()
        return ce
    def subject(self):
        se = self.findelement(By.CSS_SELECTOR,self.text_subject_css).text
        return se
    def mailbody(self):
        mb = self.findelement(By.XPATH,self.text_maibody_xpath).text
        return mb
    def clickonsocaillab(self):
        sc = self.findelement(By.CSS_SELECTOR,self.text_socialmails_css).click()
        return sc




