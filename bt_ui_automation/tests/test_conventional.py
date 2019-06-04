

def test_level_one(pages):
    pages.home.navigate()
    pages.home.select_level('one')
    assert pages.level_one.has_success_message()


def test_level_two(pages):
    pages.home.navigate()
    pages.home.select_level('two')
    pages.level_two.click_for_victory()
    assert pages.level_two.has_success_message()


def test_level_three(pages):
    pages.home.navigate()
    pages.home.select_level('three')
    pages.level_three.destroy_dark_patterns()
    assert pages.level_three.has_success_message()
