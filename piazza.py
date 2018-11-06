from selenium import webdriver
import cmd, getpass




class Piazza:
    def __init__(self, link):
        self.driver = webdriver.Chrome("driver/chromedriver")
        self.link = link
    def login(self, username, password):
        self.driver.get(self.link)
        username_input = self.driver.find_element_by_id("email")
        password_input = self.driver.find_element_by_id("password")
        submit_button = self.driver.find_element_by_id("submit")
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.submit()
    def read_posts(self):
        self.driver.get(self.driver.current_url)
        try:
            self.driver.switch_to.alert.accept()
        except:
            pass
        posts = self.driver.find_elements_by_class_name("feed_item")
        count = 0
        while count < len(posts):
            post = posts[count]
            try:
                post.click()
            except Exception as error:
                print(error)
            self.driver.get(self.driver.current_url)
            try:
                self.driver.switch_to.alert.accept()
            except:
                pass
            posts = self.driver.find_elements_by_class_name("feed_item")
            count += 1



username = input("Enter username:")
password = getpass.getpass("Enter password:")

piazza = Piazza("https://piazza.com/account/login")
piazza.login(username, password)
piazza.read_posts()


