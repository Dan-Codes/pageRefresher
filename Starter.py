import time
import random
from selenium import webdriver
#from AutoLogin import AutoLogin
from AutoLogin import AutoLogin


class PagePoller:
    def __init__(self, url):
        self.url = url
        self.createBrowser()

    def checkAvailable(self):
        time.sleep(5)
        addToCartButton = addButton = self.driver.find_element_by_class_name("add-to-cart-button")
        if ("btn-disabled" in addToCartButton.get_attribute("class")):
            return False
        else:
            time.sleep(2)
            addToCartButton.click()
            return True

    def addToCart(self):
        self.driver.implicitly_wait(30)
        time.sleep(3)
        addToCartButton = addButton = self.driver.find_element_by_partial_link_text("Go to Cart")
        addToCartButton.click()



    def createBrowser(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def refreshPage(self):
        self.driver.close()
        self.driver.quit()
        self.createBrowser()


textFile = open("bestbuy.txt", "r")
lines = textFile.readlines()
print(lines)

pages = []
for u in lines:
    pages.append(PagePoller(u))

while True:
    toRemove = []
    for p in pages:
        if p.checkAvailable():
            login = (AutoLogin("https://www.messenger.com/", p.url))
            toRemove.append(p)
            # p.addToCart()
        else:
            p.refreshPage()

    for p in toRemove:
        pages.remove(p)

    time.sleep(random.uniform(1, 3))


#
# #driver = webdriver.Firefox()
#
# # happy case - item is available
# #driver.get("https://www.bestbuy.com/site/nvidia-titan-rtx-24gb-gddr6-pci-express-3-0-graphics-card/6320585.p?skuId=6320585")
#
#
# #driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
#


# good
# <button class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type="button" style="padding:0 8px">
# </button>


# bad
# <button class="btn btn-disabled btn-lg btn-block add-to-cart-button" disabled="" type="button" style="padding: 0px 8px;">Sold Out</button>