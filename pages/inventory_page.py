from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")

    def is_opened(self):
        self.wait_for_element(self.INVENTORY_CONTAINER)
        return "inventory.html" in self.driver.current_url
