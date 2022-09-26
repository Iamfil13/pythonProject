import time

import allure
from selenium.webdriver import Keys
from faker import Faker
from pages.base_page import BasePage
from locators.form_pages_locators import FormPageLocators as Locators

faker_en = Faker('En')


@allure.suite("Form page")
class FormPage(BasePage):

    @allure.title("Filling in the fields")
    def fill_fields_and_submit(self):

        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(faker_en.first_name())
        self.element_is_visible(Locators.LAST_NAME).send_keys(faker_en.last_name())
        self.element_is_visible(Locators.EMAIL).send_keys(faker_en.email())
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(faker_en.msisdn())
        subject = self.element_is_visible(Locators.SUBJECTS)
        subject.send_keys('English')
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(
            '/Users/maccube/PycharmProjects/pythonProject/requirements.txt')
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(faker_en.address())
        self.element_is_visible(Locators.SUBMIT).click()
        time.sleep(5)

    @allure.title("Result")
    def from_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        # for i in result_list:
        #    result_text.append(i.text)
        return result_text

