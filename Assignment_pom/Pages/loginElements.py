class loginElements():

    def __init__(self,driver):
        self.driver = driver

        self.webUrl = "https://www.farfetch.com/in/shopping/women/items.aspx"
        self.signin_xpath = '//*[@id="slice-header"]/div[1]/nav/div[2]/button[2]'
        self.username_xpath = '//*[@id="tabpanel-0"]/form/div[1]/div/div/input'
        self.password_xpath = '//*[@id="tabpanel-0"]/form/div[2]/div/div/input'
        self.signin_btn_xpath = '//*[@id="tabpanel-0"]/form/button'

