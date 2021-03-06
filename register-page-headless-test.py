import unittest
from selenium import webdriver
import StringIO
from PIL import Image

class TestGoogleGhostDriver(unittest.TestCase):
    def setUp(self):
        # The phantomjs executable is assumed to be in your PATH:
        self.driver = webdriver.PhantomJS('phantomjs')
        self.driver.set_window_size(1366, 728)  # optional
        #self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()

    # Simple test that performs a google Signup
    def testGoogleSearch(self):
        self.driver.get("https://accounts.google.com/SignUp?")
        self.assertEqual(u'Create your Google Account', self.driver.title)
        # Enter text field FirstName
        self.driver.find_element_by_name("FirstName").send_keys("Lorem123Lorem123")
        # Enter text field LastName
        self.driver.find_element_by_name("LastName").send_keys("Lorem123Lorem123")
        # Enter text field Gmail Address
        self.driver.find_element_by_name("GmailAddress").send_keys("Lorem123Lorem123")
        # Enter text field Password
        self.driver.find_element_by_name("Passwd").send_keys("Lorem123Lorem123")
        # Enter text field Password Again
        self.driver.find_element_by_name("PasswdAgain").send_keys("Lorem123Lorem123")
        # Enter text field birthday month
        self.driver.find_element_by_xpath("//div[@role='listbox']").send_keys("June")
        # Enter text field birthday date
        self.driver.find_element_by_name("BirthDay").send_keys("24")
        # Enter text field birthday year
        self.driver.find_element_by_name("BirthYear").send_keys("1994")
        # Enter text field Gender
        self.driver.find_element_by_xpath("//div[@id='Gender']/div").send_keys("Male")
        # Enter text field Recovery Phone Number
        self.driver.find_element_by_name("RecoveryPhoneNumber").send_keys("123456789")
        # Enter text field Recovery Email Address
        self.driver.find_element_by_name("RecoveryEmailAddress").send_keys("test@gmail.com")
        # Click submit button
        self.driver.find_element_by_name("submitbutton").click()
        print("Current page '%s'" % (self.driver.current_url))
        self.driver.save_screenshot('google_form.png')
        screen = self.driver.get_screenshot_as_png()

        # Crop it back to the window size (it may be taller)
        box = (0, 0, 1366, 728)
        im = Image.open(StringIO.StringIO(screen))
        region = im.crop(box)
        region.save('screen_lores.jpg', 'JPEG', optimize=True, quality=95)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
