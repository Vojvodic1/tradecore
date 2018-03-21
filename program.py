from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class TradeCoreTester(object):
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver")
        self.first_page = None

    def close(self):
        self.driver.close()

        #opening home page
    def load_first_page(self):
        self.first_page = self.driver.get("https://demo-biq.dev.tradecore.io/#/")
        self.driver.maximize_window()

    def first_page_loaded(self):
        print("2")
        if self.driver.find_element_by_id("button-step"):
            return True
        return False

        #first name input
    def first_name_tag_exists(self):
        first_name_tag = self.driver.find_element_by_id("form-first_name")
        if first_name_tag:
            return True
        return False

    def get_first_name_tag(self):
        self.first_name_tag = self.driver.find_element_by_id("form-first_name")

    def fill_first_name(self):
        self.first_name_tag.send_keys("Adam")

        #last name input
    def last_name_tag_exists(self):
        last_name_tag = self.driver.find_element_by_id("form-last_name")
        if last_name_tag:
            return True
        return False

    def get_last_name_tag(self):
        self.last_name_tag = self.driver.find_element_by_id("form-last_name")

    def fill_last_name(self):
        self.last_name_tag.send_keys("Sandler")

        #email field input
    def email_field_exists(self):
        email_field = self.driver.find_element_by_id("form-email")
        if email_field:
            return True
        return False

    def get_email_field(self):
         self.email_field = self.driver.find_element_by_id("form-email")

    def fill_email_field(self):
        self.email_field.send_keys("adamsendler{}@tradecore.com".format(randint(10000, 99999)))

        #password input
    def password_field_exists(self):
        password_field = self.driver.find_element_by_id("form-password")
        if password_field:
            return True
        return False

    def get_password_field(self):
        self.password_field = self.driver.find_element_by_id("form-password")

    def fill_password_field(self):
        self.password_field.send_keys("AdamSandler12!")

        #confirmation password input
    def password_conf_field_exists(self):
        password_conf_field = self.driver.find_element_by_id("form-password2")
        if password_conf_field:
            return True
        return False

    def get_password_conf_field(self):
        self.password_conf_field = self.driver.find_element_by_id("form-password2")

    def fill_password_conf_field(self):
        self.password_conf_field.send_keys("AdamSandler12!")

        #telephone number input
    def telephone_tag_exists(self):
        telephone_tag = self.driver.find_element_by_id("form-telephone")
        if telephone_tag:
            return True
        return False

    def get_telephone_tag(self):
        self.telephone_tag = self.driver.find_element_by_id("form-telephone")

    def fill_telephone_tag(self):
        self.telephone_tag.send_keys("+381638858288")

        #date of birth input
    def date_of_birth_tag_exists(self):
        date_of_birth_tag = self.driver.find_element_by_id("form-date_of_birth")
        if date_of_birth_tag:
            return True
        return False

    def get_date_of_birth_tag(self):
        self.date_of_birth_tag = self.driver.find_element_by_id("form-date_of_birth")

    def fill_date_of_birth_tag(self):
        self.date_of_birth_tag.send_keys("09/09/1966/")

        #postcode input
    def postcode_tag_exists(self):
        postcode_tag = self.driver.find_element_by_id("form-addr_zip")
        if postcode_tag:
            return True
        return False

    def get_postcode_tag(self):
        self.postcode_tag = self.driver.find_element_by_id("form-addr_zip")

    def fill_postcode_tag(self):
        self.postcode_tag.send_keys("11073")

        #adress input
    def address_tag_exists(self):
        address_tag = self.driver.find_element_by_id("form-addr_street")
        if address_tag:
            return True
        return False

    def get_address_tag(self):
        self.address_tag = self.driver.find_element_by_id("form-addr_street")

    def fill_address_tag(self):
        self.address_tag.send_keys("Mileve Maric Ajnstajn 104")

        #adress 2 input
    def address_2_tag_exists(self):
        address_2_tag = self.driver.find_element_by_id("form-addr_line_2")
        if address_2_tag:
            return True
        return False

    def get_address_2_tag(self):
        self.address_2_tag = self.driver.find_element_by_id("form-addr_line_2")

    def fill_address_2_tag(self):
        self.address_2_tag.send_keys("random")

        #city input
    def city_tag_exists(self):
        city_tag =  self.driver.find_element_by_id("form-addr_city")
        if city_tag:
            return True
        return False

    def get_city_tag(self):
        self.city_tag = self.driver.find_element_by_id("form-addr_city")

    def fill_city_tag(self):
        self.city_tag.send_keys("Novi Beograd")

        #first step registration submit
    def first_step_complete_button_exists(self):
        first_step_complete_button = self.driver.find_element_by_id("button-step")
        if first_step_complete_button:
            return True
        return False

    def click_on_first_step_complete_button(self):
        first_step_complete_button = self.driver.find_element_by_id("button-step")

        first_step_complete_button.click()

        sleep(5)

        #shares select option
    def shares_tag_exists(self):
        shares = self.driver.find_element_by_id("form-shares")
        if shares:
            return True
        return False


    def select_shares_value_1(self):

        self.shares = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[2]/div/div/div/div/div/a/span')))
        self.shares.click()


        shares_option1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[2]/div/div/div/div/div/div/ul/li[1]')))
        shares_option1.click()

        #forex select option
    def forex_tag_exists(self):
        forex = self.driver.find_element_by_id("form-forex")
        if forex:
            return True
        return False

    def select_forex_value_2(self):
        self.forex = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[3]/div/div/div/div/div/a/span')))
        self.forex.click()

        forex_option2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[3]/div/div/div/div/div/div/ul/li[2]')))
        forex_option2.click()

        #cfds select option
    def cfds_tag_exists(self):
        cfds = self.driver.find_element_by_id("form-cfds")
        if cfds:
            return True
        return False

    def select_cfds_value_3(self):
        self.cfds = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[4]/div/div/div/div/div/a/span')))
        self.cfds.click()

        cfds_option3 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="steps"]/form/div[4]/div/div/div/div/div/div/ul/li[3]')))
        cfds_option3.click()

        #spread betting select option
    def spread_betting_tag_exists(self):
        spread_betting = self.driver.find_element_by_id("form-spread_betting")
        if spread_betting:
            return True
        return False

    def select_spread_betting_value_2(self):
        self.spread_betting = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[5]/div/div/div/div/div/a/span')))
        self.spread_betting.click()

        spread_betting_option2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="steps"]/form/div[5]/div/div/div/div/div/div/ul/li[2]')))
        spread_betting_option2.click()

        #other relevan exp select option
    def other_relevant_experience_tag_exists(self):
        other_relevant_experience = self.driver.find_element_by_id("form-relevant_experience")
        if other_relevant_experience:
            return True
        return False

    def select_other_relevant_experience_value_1(self):
        self.other_relevant_experience = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[7]/div/div/div/div/div/a/span')))
        print (self.other_relevant_experience.click())
        self.other_relevant_experience.click()

        other_relevant_experience_option_1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="steps"]/form/div[7]/div/div/div/div/div/div/ul/li[2]')))
        other_relevant_experience_option_1.click()

        #select trading platform
    def trading_platform_tag_exists(self):
        trading_platform = self.driver.find_element_by_id("form-trading_accounts")
        if trading_platform:
            return True
        return False

    def select_trading_platform_value(self):
        self.trading_platform = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[9]/div/div/div/div/div/a/span')))
        self.trading_platform.click()

        trading_platform_value_option_1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="steps"]/form/div[9]/div/div/div/div/div/div/ul/li[1]')))

        trading_platform_value_option_1.click()

        #select trading currency
    def trading_curency_tag_exists(self):
        trading_curency = self.driver.find_element_by_id("form-currency")
        if trading_curency:
            return True
        return False

    def select_trading_curency_value(self):
        self.trading_curency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[10]/div/div/div/div/div/a/span')))
        self.trading_curency.click()


        trading_curency_value_option_1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@field-id="currency"]/div/div/div/ul/li[1]')))
        trading_curency_value_option_1.click()

        #select approximate income
    def approximate_income_tag_exists(self):
        approximate_income = self.driver.find_element_by_id("form-currency")
        if approximate_income:
            return True
        return False

    def select_approximate_income_value(self):
        self.approximate_income = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[11]/div/div/div/div/div/a/span')))
        self.approximate_income.click()

        approximate_income_value_option_4 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="steps"]/form/div[11]/div/div/div/div/div/div/ul/li[4]')))
        approximate_income_value_option_4.click()

        #select empployment option
    def employment_status_tag_exists(self):
        employment_status = self.driver.find_element_by_id("form-employment_status")
        if employment_status:
            return True
        return False

    def select_employment_status_value(self):
        self.employment_status = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[12]/div/div/div/div/div/a/span')))
        self.employment_status.click()

        employment_status_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="steps"]/form/div[12]/div/div/div/div/div/div/ul/li[1]')))
        employment_status_option.click()

        #select approximate value of assets
    def approximate_value_of_assets_tag_exists(self):
        approximate_value_of_assets = self.driver.find_element_by_id("form-liquid_savings")
        if approximate_value_of_assets:
            return True
        return False

    def select_approximate_value_of_assets_amount(self):
        self.approximate_value_of_assets = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="steps"]/form/div[13]/div/div/div/div/div/a/span')))
        self.approximate_value_of_assets.click()

        approximate_value_of_assets_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="steps"]/form/div[13]/div/div/div/div/div/div/ul/li[2]')))
        approximate_value_of_assets_option.click()

        #accept terms and conditions
    def privacy_policy_button_tag_exists(self):
        self.privacy_policy_button = self.driver.find_element_by_xpath("//*[@id='steps']/form/div[15]/div/div/div/label")
        if self.privacy_policy_button:
            return True
        return False

    def privacy_policy_button_click(self):
        self.privacy_policy_button.click()

        #finish registration
    def finish_step_button_tag_exists(self):
        self.finish_step_button = self.driver.find_element_by_id("button-step")
        if self.finish_step_button:
            return True
        return False

    def click_on_finish_step_button(self):
        self.finish_step_button.click()

        sleep(8)


        #add new trading account
    def add_new_trading_acc_tag_exists(self):
        self.add_new_trading_acc = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "base.portal.account-add")))
        if self.add_new_trading_acc:
            return True
        return False

    def click_on_add_new_trading_acc_button(self):
        sleep(2)
        self.add_new_trading_acc.click()

        #select currency for new trading account
    def new_currency_tag_exists(self):
        self.new_currency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="form___fieldId___chosen"]/a/span')))
        if self.new_currency:
            return True
        return False

    def select_new_currency_value(self):
        self.new_currency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="form___fieldId___chosen"]/a/span')))
        self.new_currency.click()

        new_currency_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="form___fieldId___chosen"]/div/ul/li')))
        new_currency_option.click()

        #save new trading account
    def create_new_trading_acc_tag_exists(self):
        self.create_new_trading_acc = self.driver.find_element_by_id("portal-button-account-add")
        if self.create_new_trading_acc:
            return True
        return False

    def click_on_create_new_trading_acc_button(self):
        self.create_new_trading_acc.click()


        #add new demo account
    def add_new_demo_acc_tag_exists(self):
        self.add_new_demo_acc = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "base.portal.account-add-demo")))
        if self.add_new_demo_acc:
            return True
        return False

    def click_on_add_new_demo_acc_button(self):
        sleep(2)
        self.add_new_demo_acc.click()

        #select currency for new demo account
    def demo_currency_tag_exists(self):
        self.demo_currency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="form___fieldId___chosen"]/a/span')))
        if self.demo_currency:
            return True
        return False

    def select_demo_currency_value(self):
        self.demo_currency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="form___fieldId___chosen"]/a/span')))
        self.demo_currency.click()

        demo_currency_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="form___fieldId___chosen"]/div/ul/li')))
        demo_currency_option.click()

        #save new demo account
    def create_new_demo_acc_tag_exists(self):
        self.create_new_demo_acc = self.driver.find_element_by_id("portal-button-account-add-demo")
        if self.create_new_demo_acc:
            return True
        return False

    def click_on_create_new_demo_acc_button(self):
        self.create_new_demo_acc.click()


        #enter personal information
    def personal_inf_tag_exists(self):
        self.personal_inf = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "base.portal.personal")))
        if self.personal_inf:
            return True
        return False

    def click_on_personal_inf_button(self):
        self.personal_inf.click()



        #upadate personal information
    def update_personal_inf_tag_exists(self):
        self.update_personal_inf = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "portal-button-personal-update")))
        if self.update_personal_inf:
            return True
        return False

    def click_on_update_personal_inf_button(self):
        self.update_personal_inf.click()


        #add nationality
    def nationality_tag_exists(self):
        self.nationality = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@field-id="nationality"]/div/div/a/span')))
        if self.nationality:
            return True
        return False

    def select_nationality_name(self):
        self.nationality.click()
        self.nationality.click()

        nationality_name_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@field-id="nationality"]/div/div/div/ul/li[197]')))

        nationality_name_option.click()


        #save personal option
    def save_changes_tag_exists(self):
        self.save_changes = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "portal-button-personal")))
        if self.save_changes:
            return True
        return False

    def click_on_save_changes_button(self):
        self.save_changes.click()

        #change password
    def change_password_tag_exists(self):
        self.change_password = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "base.portal.change-password")))
        if self.change_password:
            return True
        return False

    def click_on_change_password_button(self):
        self.change_password.click()

        #enter current password
    def current_password_tag_exists(self):
        current_password = self.driver.find_element_by_id("form-current_pass")
        if current_password:
            return True
        return False

    def get_current_password(self):
        self.current_password = self.driver.find_element_by_id("form-current_pass")

    def fill_current_password(self):
        self.current_password.send_keys("AdamSandler12!")

        #enter new password
    def new_password_tag_exists(self):
        new_password = self.driver.find_element_by_id("form-new_pass")
        if new_password:
            return True
        return False

    def get_new_password(self):
        self.new_password = self.driver.find_element_by_id("form-new_pass")

    def fill_new_password(self):
        self.new_password.send_keys("Sandler334??")

        #confirm new password
    def confirm_new_password_tag_exists(self):
        confirm_new_password = self.driver.find_element_by_id("form-new_pass_confirm")
        if confirm_new_password:
            return True
        return False

    def get_confirm_new_password(self):
        self.confirm_new_password = self.driver.find_element_by_id("form-new_pass_confirm")

    def fill_confirm_new_password(self):
        self.confirm_new_password.send_keys("Sandler334??")

        #logout
    def logout_tag_exists(self):
        self.logout = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logout")))
        if self.logout:
            return True
        return False

    def click_on_logout_button(self):
        self.logout.click()

































