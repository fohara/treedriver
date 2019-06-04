import py_trees
from selenium import webdriver

from bt_ui_automation.tests.page_objects.pages import Pages

IMPLICIT_WAIT = 2

class Driver(py_trees.behaviour.Behaviour):

    def __init__(self, name="Driver"):
        super(Driver, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        existing_driver = self.blackboard.get('driver')
        stale_driver = False

        if existing_driver:
            try:
                existing_driver.title
            except Exception as e:
                self.logger.info('Stale driver detected')
                stale_driver = True

        if not existing_driver or stale_driver:
            driver = webdriver.Firefox()
            driver.implicitly_wait(IMPLICIT_WAIT)
            self.blackboard.set('driver', driver)
        return py_trees.common.Status.SUCCESS


class CloseDriver(py_trees.behaviour.Behaviour):

    def __init__(self, name="CloseDriver"):
        super(CloseDriver, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):

        existing_driver = self.blackboard.get('driver')

        if existing_driver:
            try:
                existing_driver.quit()
                self.logger.info('Successfully closed the driver')
            except Exception as e:
                self.logger.info('Stale driver detected, assuming already closed')

        return py_trees.common.Status.SUCCESS


class NavigateToHome(py_trees.behaviour.Behaviour):

    def __init__(self, name="NavigateToHome"):
        super(NavigateToHome, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        pages = Pages(self.blackboard.get('driver'))
        pages.home.navigate()
        return py_trees.common.Status.SUCCESS


class CheckForSuccess(py_trees.behaviour.Behaviour):

    def __init__(self, name="CheckForSuccess"):
        super(CheckForSuccess, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        pages = Pages(self.blackboard.get('driver'))

        try:
            assert pages.home.has_success_message()
            self.logger.info('Found the success message!')
        except Exception as e:
            self.logger.info("Could not find the success message:\n{}".format(e))
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.SUCCESS