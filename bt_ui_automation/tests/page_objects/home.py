import os
from bt_ui_automation.tests.page_objects.base import Base

port = os.environ.get('BT_HOST_PORT', 5000)

class Home(Base):

    def navigate(self):
        self.driver.get('http://localhost:{}'.format(port))

    def select_level(self, level='one'):
        self.driver.find_element_by_id("level-{}".format(level)).click()