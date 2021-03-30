import unittest
from selenium import webdriver


class AbTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://www.agroprombank.com/')
        self.assertIn('Главная страница ЗАО "Агропромбанк"', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)
