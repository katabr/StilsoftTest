# Тест проверяет все карточки товаров со страницы
# https://stilsoft.ru/products/kitsoz-synerget
# на предмет:
# • Наличие фотографии
# • Наличие заполненного поля «Назначенный срок службы»
# со значением больше 7 лет.
# Все карточки, у которых меньше срок или нет фото,
# помещаются в txt файл results.txt

from menu.cards import Cards

class TestStilSoft():
    def test_img_and_time_life_of_cards(self, browser):
        cds = Cards(browser)
        # формирует файл со списком всех карточек
        cds.list_of_cards()
        # формирует файл со списком карточек по заданию
        cds.result_list_of_cards()
