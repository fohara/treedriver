import py_trees

from bt_ui_automation.tests.page_objects.pages import Pages

class SelectLevelThree(py_trees.behaviour.Behaviour):

    def __init__(self, name="SelectLevelThree"):
        super(SelectLevelThree, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        pages = Pages(self.blackboard.get('driver'))
        try:
            pages.home.select_level('three')
        except Exception as e:
            self.logger.info("Failed to select level three:\n{}".format(e))
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.SUCCESS


class DestroyDarkPatterns(py_trees.behaviour.Behaviour):

    def __init__(self, name="DestroyDarkPatterns"):
        super(DestroyDarkPatterns, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        pages = Pages(self.blackboard.get('driver'))
        try:
            pages.level_three.destroy_dark_patterns()
            self.logger.info('Destroyed Dark Patterns!')
        except Exception as e:
            self.logger.info("Failed to destroy dark patterns:\n{}".format(e))
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.SUCCESS


class DismissModal(py_trees.behaviour.Behaviour):

    def __init__(self, name="DismissModal"):
        super(DismissModal, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        pages = Pages(self.blackboard.get('driver'))
        try:
            pages.level_three.dismiss_modal()
            self.logger.info('Dismissed Modal!')
        except Exception as e:
            self.logger.info("Failed to dismiss modal:\n{}".format(e))
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.SUCCESS