import py_trees

def run_tree(tree):
    while tree.status != py_trees.common.Status.SUCCESS:
        tree.tick_once()


def diagram_tree(tree):
    print(py_trees.display.ascii_tree(tree))
    py_trees.display.render_dot_tree(tree, target_directory='./diagrams')
