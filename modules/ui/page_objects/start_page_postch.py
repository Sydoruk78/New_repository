from selenium.webdriver.support.select import Select
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class StartPagePoctCH(BasePage):
    URL = 'https://novaposhta.ua'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(self.URL)

    def try_login(self):
        
        login_elem = self.driver.find_element(By.CLASS_NAME,'logo_in')
        login_elem.click()

    def try_find_cost(self, punkt1, punkt2, weight, cost, height, len, width):
        cost_elem = self.driver.find_element(By.CLASS_NAME, 'cost')
        cost_elem.click()

        weight_elem = self.driver.find_element(By.CLASS_NAME,'short.allowed-char.weight')
        weight_elem.send_keys(weight)
        cost_packet=self.driver.find_element(By.CLASS_NAME,'short.allowed-char.cost')
        cost_packet.send_keys(cost)
        len_packet=self.driver.find_element(By.CLASS_NAME,'allowed-char.volumetricLength')
        len_packet.send_keys(len)
        height_packet=self.driver.find_element(By.CLASS_NAME,'allowed-char.volumetricHeight')
        height_packet.send_keys(height)
        width_packet=self.driver.find_element(By.CLASS_NAME,'allowed-char.volumetricWidth')
        width_packet.send_keys(width)
        sender_elem = self.driver.find_element(By.ID,'DeliveryForm_senderCity')
        sender_elem.click()
        sender = self.driver.find_element(By.CLASS_NAME,'cdb5c88d0-391c-11dd-90d9-001a92567626')
        sender.click()
        reciever_elem = self.driver.find_element(By.ID,'DeliveryForm_recipientCity')
        reciever_elem.click()
        ul = self.driver.find_element(By.ID,'delivery_recipient_cities')
        reciever = ul.find_element(By.CLASS_NAME,'cdb5c88f0-391c-11dd-90d9-001a92567626')
        reciever.click()                                   

        btn_elem = self.driver.find_element(By.NAME, 'yt0')
        btn_elem.click()
        final_elem = self.driver.find_element(By.CLASS_NAME, 'final')
        return final_elem.text
    


    def search_vakansii(self):
        head_elem = self.driver.find_element(By.LINK_TEXT,'Про компанію')
        head_elem.click()
        WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.LINK_TEXT,'Робота в компанії')))
        list_elem = self.driver.find_element(By.LINK_TEXT,'Робота в компанії')
        list_elem.click()
        btn_job = self.driver.find_element(By.LINK_TEXT,'Вакансії')
        btn_job.click()
        print(self.driver.title)



    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def login(self, number):
        btn_elem = self.driver.find_element(By.CLASS_NAME,'mat-focus-indicator.mat-menu-trigger.mat-stroked-button.mat-button-base.mat-accent')
        btn_elem.click()
        menu_item = self.driver.find_element(By.LINK_TEXT,'як приватна')
        menu_item.click()
        tel_input = self.driver.find_element(By.ID,'mat-input-0')
        tel_input.send_keys(number)
        btn_elem2 = self.driver.find_element(By.CLASS_NAME,'mat-focus-indicator.continue-button.mat-raised-button.mat-button-base.mat-primary')
        btn_elem2.click()
        error_elem = self.driver.find_element(By.ID,'mat-error-0')
        return error_elem.is_displayed()


