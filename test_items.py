import time
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)

    btn = len(browser.find_elements_by_css_selector("#add_to_basket_form button[type='submit']"))

    assert btn > 0, "Кнопка не найдена!"
