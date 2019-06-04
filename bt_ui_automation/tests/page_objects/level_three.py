from bt_ui_automation.tests.page_objects.base import Base

class LevelThree(Base):

    def navigate(self):
        self.driver.get('http://localhost:5000/level_three')

    def destroy_dark_patterns(self):
        self.driver.find_element_by_css_selector('button.is-dark').click()

    def dismiss_modal(self):
        self.driver.find_element_by_css_selector('button.delete').click()
