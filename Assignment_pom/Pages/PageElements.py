class pageElements():

    def __init__(self,driver):
        self.driver = driver

        #Selecting menswear and shoes other actions
        self.menswear_xpath = '//a[text()="Menswear"]'
        self.shoes_xpath = '//*[@id="slice-header"]/div[2]/div/div[1]/nav/ul/li[4]'
        self.boots_xpath = '//*[@id="meganav"]/div/div[1]/div[1]/ul/li[2]/a/span'

        self.filter_btn_xpath = '//*[@id="slice-container"]/div[3]/div/div[1]/button'
        self.size_xpath = '//*[@id="listing-filters-drawer-content"]/ul/li[2]/p'
        self.country_drp_xpath = '//*[@id="collapsed-panel-size"]/div/ul/div/button/span'
        self.brazil = "//span[text()='Brazil']"  #select uk
        self.sizechart_xpath = '//*[@id="collapsed-panel-size"]/div/ul/ul/li[3]' #Select 3
        self.show_result_xpath = '//*[@id="root"]/div[3]/div[2]/div[4]/div/div[3]/div/button[2]'
        self.sort_xpath = '//label[@data-testid="sortDropdownLabel"]' #selectByVisibleText
        self.ourpicks_xpath = '//a[text()="Our Picks"]'
        self.select_shoe_xpath = '//*[@id="slice-container"]/div[5]/div[2]/div/div[1]/ul/li[1]/div/a/div[2]/div[1]/p[1]'
        self.size_guidexpath = "//button[text()='Size guide']"
        self.forty_xpath = '//*[@id="panelInner-0"]/div/div/table/tbody/tr[3]/td[1]'

        self.addToBag_xpath = '//button[text()="Add To Bag"]' #try double click
        self.price_xpath = '//*[@id="content"]/div[1]/div/aside/div/div/div[1]/div/p[3]'




