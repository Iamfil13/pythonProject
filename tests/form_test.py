from pages.form_page import FormPage


class TestFormPage:
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.from_result()

        # assert '' == result[0], 'the form has not been filled'
        # assert '' == result[1], 'the form has not been filled'


