from selenium import webdriver
import unittest



class NewVisitortest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()
        
    def test_new_visitors_website_title(self):
        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn("To-Do",self.browser.title) 
        self.fail("to do is not in title")


if __name__ == "__main__":
    unittest.main()
