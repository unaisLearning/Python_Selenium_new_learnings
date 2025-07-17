class BaseTest:
    def open_browser(self):
        print("opening Browser")

    def screen_short(self):
        print("screenshort save")

    def closing_browser(self):
        print("closing Browser")

class TestCase1(BaseTest):
    def test_1(self):
        self.open_browser()
        print("TC 1")
        self.closing_browser()

class Testcase2(BaseTest):
    def positive_test(self):
        self.open_browser()
        print("TC 2")
        self.closing_browser()

