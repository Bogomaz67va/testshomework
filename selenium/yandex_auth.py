from selenium import webdriver
import time


def auth_yandex(login: str, password: str):
    driver = webdriver.Chrome()
    driver.get("https://passport.yandex.ru/auth/")
    input_login = driver.find_elements_by_class_name("Textinput-Control")
    input_login[0].send_keys(login)
    button_auth = driver.find_elements_by_class_name(
        "Button2.Button2_size_l.Button2_view_action.Button2_width_max.Button2_type_submit")
    button_auth[0].click()
    time.sleep(1)
    input_password = driver.find_elements_by_class_name("Textinput-Control")
    input_password[0].send_keys(password)
    button_auth = driver.find_elements_by_class_name(
        "Button2.Button2_size_l.Button2_view_action.Button2_width_max.Button2_type_submit")
    button_auth[0].click()
    time.sleep(3)
    driver.close()


if __name__ == '__main__':
    auth_yandex('login', 'password')
