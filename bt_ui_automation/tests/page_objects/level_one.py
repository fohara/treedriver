from bt_ui_automation.tests.page_objects.base import Base

class LevelOne(Base):

    def navigate(self):
        self.driver.get('http://localhost:5000/level_one')
