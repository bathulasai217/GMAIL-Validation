import time

import pytest
from pages.loginpage import LoginPage
from pages.gmailcompose import GMAILINBOX
from utilities.utilities import Utils
from pages.gmailinbox import GmailInbox


@pytest.mark.usefixtures("setup")
class TestEMAIL:
    def test_login(self):
        lp = LoginPage(self.driver)
        gp = GMAILINBOX(self.driver)
        ut = Utils(self.driver)
        lp.username("bathulasairkishna9133@gmail.com")
        lp.click_on_next()
        lp.password("Kalyani@#9133")
        lp.click_on_nextpassword()
        gp.popuphandle()
        gp.click_on_composemail()
        gp.enter_to_email("bathulasairkishna9133@gmail.com")
        gp.subject("Test Mail")
        gp.messagebody("Test Mail Body")
        gp.label_social()
        gp.click_on_send()
        ut.mailverfication()


