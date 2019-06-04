from bt_ui_automation.tests.page_objects.base import Base

class LevelTwo(Base):

    def navigate(self):
        self.driver.get('http://localhost:5000/level_two')

    def click_for_victory(self):
        self.driver.find_element_by_tag_name('button').click()
