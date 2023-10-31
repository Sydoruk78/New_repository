from modules.ui.page_objects.start_page_postch import StartPagePoctCH
import pytest

@pytest.mark.uipostch
def test_open_login_page():
    start_page_postch = StartPagePoctCH()
    start_page_postch.go_to()
    start_page_postch.try_login()
    assert start_page_postch.check_title("Бізнес-кабінет - Нова пошта")
    start_page_postch.close()

@pytest.mark.uipostch
def test_cost_search():
    start_page_post = StartPagePoctCH()
    start_page_post.go_to()
    assert start_page_post.try_find_cost('Одеса',"Дніпро",3,100,10,10,10) == 'Разом: 100.00 ... 170.00грн *'
    start_page_post.close()

@pytest.mark.uipostch
def test_search_job():
    start_page_post = StartPagePoctCH()
    start_page_post.go_to()
    start_page_post.search_vakansii() 
    assert start_page_post.check_title('Вакансії – «Нова Пошта»| Доставка майбутнього')
    start_page_post.close()

@pytest.mark.uipostch
def test_too_short_phone_number():
    start_page_post = StartPagePoctCH()
    start_page_post.go_to()
    start_page_post.try_login()
    assert start_page_post.login('+380555') == True
    start_page_post.close()


