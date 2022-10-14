import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from .general import General


class Cards(General):
    def count_number_of_cards(self):
        list = self.browser.find_elements(By.CSS_SELECTOR, 'div.boxImage')
        numberOfCards = len(list)
        print(numberOfCards)
        return numberOfCards

    def go_to_card(self, n):
        list = self.browser.find_elements(By.CSS_SELECTOR, 'div.boxImage')
        element = WDW(self.browser, 10).until(EC.element_to_be_clickable((list[n])))
        element.click()

    def get_name_of_card(self):
        photo = self.browser.find_elements(By.CSS_SELECTOR,'div.col-lg-12.breadcrumb_box>a')
        cardNameFull = photo[-1].get_attribute('textContent')
        cardName = re.sub("^\s+|\n|\r|\s+$", '', cardNameFull)
        print(cardName)
        return cardName

    def check_exists_photo(self):
        try:
            photo = WDW(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.imgCont')))
        except TimeoutError:
            return False
        return True

    def check_life_time(self):
        timel = self.browser.find_element(By.XPATH, '//*[contains(text(), "срок службы")]')
        life_time =timel.get_attribute('textContent')
        string = life_time.split(" ")
        print(string)
        time = int(string[-2])
        print(time)
        if time > 7 :
            return True
        else:
            return False



    def get_life_time(self):
        time = self.browser.find_element(By.XPATH, '//*[contains(text(), "срок службы")]')
        life_time = time.get_attribute('textContent')
        print(life_time)
        return life_time

    def list_of_cards(self):
        numberOfCards = self.count_number_of_cards()
        result_file = open('list_of_cards.txt', 'w')
        result_file.write("Список карточек" + '\n')
        n = 0
        i = 1
        while n < numberOfCards:
            self.go_to_card(n)
            cardName = self.get_name_of_card()
            lifeTime = self.get_life_time()
            result_file = open('list_of_cards.txt', 'a')
            k = str(int(i))
            result_file.write(k + ". " + cardName + " - " + lifeTime + '\n')
            self.browser.back()
            i = i+1
            n = n+2
        result_file.close()

    def result_list_of_cards(self):
        numberOfCards = self.count_number_of_cards()
        result_file = open('results.txt', 'w')
        result_file.write("Список карточек без фото, либо со сроком службы менее 7 лет" + '\n')
        n = 0
        i = 0
        while n < numberOfCards:
            self.go_to_card(n)
            self.check_exists_photo()
            self.check_life_time()
            if ((self.check_exists_photo() != True) or (self.check_life_time() != True)):
                cardName = self.get_name_of_card()
                lifeTime = self.get_life_time()
                result_file = open('results.txt', 'a')
                k = str(int(i+1))
                result_file.write(k + ". " + cardName + " - " + lifeTime + '\n')
                i = i+1
            self.browser.back()
            n = n+2
        result_file.close()
