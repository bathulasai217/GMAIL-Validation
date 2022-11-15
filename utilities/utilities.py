import time

from pages.gmailinbox import GmailInbox
from base.base_driver import BaseDriver


class Utils(BaseDriver):

    def mailverfication(self):
        gi = GmailInbox(self.driver)
        gi.clickonsocaillab()
        for m in gi.mails():
            if m.text == gi.text_mail_name:
                gi.markstar()
                time.sleep(2)
                gi.clickonmail()
                time.sleep(2)
                if gi.subject() == gi.text_subject_title:
                    print("passed")
                    assert True
                else:
                    gi.save_screenshot(".\\screenshots\\" + "subject.png")
                    assert False
                if gi.mailbody() == gi.text_mailbody_title:
                    print("true")
                    assert True
                else:
                    gi.save_screenshot(".\\screenshots\\" + "mailbody.png")
                    assert False
