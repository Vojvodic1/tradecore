from behave import *
# from program import *

@given("home page")
def step_impl(context):
    context.tester.load_first_page()

@when("page loaded")
def step_impl(context):
    print(context.tester.first_page_loaded())
    assert (context.tester.first_page_loaded() == True)

@then("first name tag exists")
def step_impl(context):
    print(context.tester.first_name_tag_exists())
    assert (context.tester.first_name_tag_exists() == True)


@given("page is loaded")
def step_impl(context):
    assert (context.tester.first_name_tag_exists() == True)

@when("first name tag found")
def step_impl(context):
    context.tester.get_first_name_tag()

@then("enter first name")
def step_impl(context):
    context.tester.fill_first_name()

@given("last name tag exists")
def step_impl(context):
    assert(context.tester.last_name_tag_exists() == True)

@when("last name tag found")
def step_impl(context):
    context.tester.get_last_name_tag()

@then("enter last name")
def step_impl(context):
    context.tester.fill_last_name()

@given("email field exists")
def step_impl(context):
    assert (context.tester.email_field_exists() == True)

@when("email field found")
def step_impl(context):
    context.tester.get_email_field()

@then("enter email")
def step_impl(context):
    context.tester.fill_email_field()

@given("password field exists")
def step_impl(context):
    assert (context.tester.password_field_exists() == True)

@when("password field found")
def step_impl(context):
    context.tester.get_password_field()

@then("enter password")
def step_impl(context):
    context.tester.fill_password_field()

@given("password confirmation field exists")
def step_impl(context):
    assert (context.tester.password_conf_field_exists() == True)

@when("password confirmation field found")
def step_impl(context):
    context.tester.get_password_conf_field()

@then("enter password confirmation")
def step_impl(context):
    context.tester.fill_password_conf_field()

@given("telephone tag exists")
def step_impl(context):
    assert (context.tester.telephone_tag_exists() == True)

@when("telephone tag found")
def step_impl(context):
    context.tester.get_telephone_tag()

@then("enter telephone")
def step_impl(context):
    context.tester.fill_telephone_tag()


@given("date of birth tag exists")
def step_impl(context):
    assert (context.tester.date_of_birth_tag_exists() == True)

@when("date of birth tag found")
def step_impl(context):
    context.tester.get_date_of_birth_tag()

@then("enter date of birth")
def step_impl(context):
    context.tester.fill_date_of_birth_tag()


@given("postcode tag exists")
def step_impl(context):
    assert (context.tester.postcode_tag_exists() == True)

@when("postcode tag found")
def step_impl(context):
    context.tester.get_postcode_tag()

@then("enter postcode")
def step_impl(context):
    context.tester.fill_postcode_tag()


@given("address tag exists")
def step_impl(context):
    assert(context.tester.address_tag_exists() == True)

@when("address tag found")
def step_impl(context):
    context.tester.get_address_tag()

@then("enter address")
def step_impl(context):
    context.tester.fill_address_tag()


@given("address 2 tag exists")
def step_impl(context):
    assert (context.tester.address_2_tag_exists() == True)

@when("address 2 tag found")
def step_impl(context):
    context.tester.get_address_2_tag()

@then("enter address 2")
def step_impl(context):
    context.tester.fill_address_2_tag()


@given("city tag exists")
def step_impl(context):
    assert (context.tester.city_tag_exists() == True)

@when("city tag found")
def step_impl(context):
    context.tester.get_city_tag()

@then("enter city name")
def step_impl(context):
    context.tester.fill_city_tag()


@given("first step complete button exists")
def step_impl(context):
    assert (context.tester.first_step_complete_button_exists() == True)

@then("click on first step complete button")
def step_impl(context):
    context.tester.click_on_first_step_complete_button()

@given("shares tag exists")
def step_impl(context):
    assert (context.tester.shares_tag_exists() == True)

@then("select shares tag value 1")
def step_impl(context):
    context.tester.select_shares_value_1()

@given("forex tag exists")
def step_impl(context):
    assert (context.tester.forex_tag_exists() == True)

@then("select forex tag value 2")
def step_impl(context):
    context.tester.select_forex_value_2()

@given("cfds tag exists")
def step_impl(context):
    assert (context.tester.cfds_tag_exists() == True)

@then("select cfds tag value 3")
def step_impl(context):
    context.tester.select_cfds_value_3()

@given("spread betting tag exists")
def step_impl(context):
    assert (context.tester.spread_betting_tag_exists() == True)

@then("select spread betting tag value 2")
def step_impl(context):
    context.tester.select_spread_betting_value_2()


@given("other relevant experience tag exists")
def step_impl(context):
    assert (context.tester.other_relevant_experience_tag_exists() == True)

@then("select other relevant experience tag value 1")
def step_impl(context):
    context.tester.select_other_relevant_experience_value_1()


@given("trading platform tag exists")
def step_impl(context):
    assert (context.tester.trading_platform_tag_exists() == True)

@then("select trading platform value")
def step_impl(context):
    context.tester.select_trading_platform_value()


@given("trading curency tag exists")
def step_impl(context):
    assert (context.tester.trading_curency_tag_exists() == True)

@then("select trading curency value")
def step_impl(context):
    context.tester.select_trading_curency_value()



@given("approximate income tag exists")
def step_impl(context):
    assert (context.tester.approximate_income_tag_exists() == True)

@then("select approximate income value")
def step_impl(context):
    context.tester.select_approximate_income_value()


@given("employment status tag exists")
def step_impl(context):
    assert (context.tester.employment_status_tag_exists() == True)

@then("select employment status value")
def step_impl(context):
    context.tester.select_employment_status_value()


@given("approximate value of assets tag exists")
def step_impl(context):
    assert (context.tester.approximate_value_of_assets_tag_exists() == True)

@then("select approximate value of assets amount")
def step_impl(context):
    context.tester.select_approximate_value_of_assets_amount()


@given("privacy policy button tag exists")
def step_impl(context):
    assert (context.tester.privacy_policy_button_tag_exists() == True)

@then("click on privacy policy button")
def step_impl(context):
    context.tester.privacy_policy_button_click()


@given("finish step button tag exists")
def step_impl(context):
    assert (context.tester.finish_step_button_tag_exists() == True)

@then("click on finish step button")
def step_impl(context):
    context.tester.click_on_finish_step_button()


@given("add new trading acc tag exists")
def step_impl(context):
    assert (context.tester.add_new_trading_acc_tag_exists() == True)

@then("click on add new trading acc button")
def step_impl(context):
    context.tester.click_on_add_new_trading_acc_button()


@given("create new trading acc tag exists")
def step_impl(context):
    assert (context.tester.create_new_trading_acc_tag_exists() == True)

@then("click on create new trading acc button")
def step_impl(context):
    context.tester.create_new_trading_acc.click()


@given("new currency tag exists")
def step_impl(context):
    assert (context.tester.new_currency_tag_exists() == True)

@then("select new currency value")
def step_impl(context):
    context.tester.select_new_currency_value()


@given("add new demo acc tag exists")
def step_impl(context):
    assert (context.tester.add_new_demo_acc_tag_exists() == True)

@then("click on add new demo acc button")
def step_impl(context):
    context.tester.click_on_add_new_demo_acc_button()


@given("demo currency tag exists")
def step_impl(context):
    assert (context.tester.demo_currency_tag_exists() == True)

@then("select demo currency value")
def step_impl(context):
    context.tester.select_demo_currency_value()


@given("create new demo acc tag exists")
def step_impl(context):
    assert (context.tester.create_new_demo_acc_tag_exists() == True)

@then("click on create new demo acc button")
def step_impl(context):
    context.tester.create_new_demo_acc.click()


@given("personal inf tag exists")
def step_impl(context):
    assert (context.tester.personal_inf_tag_exists() == True)

@then("click on personal inf button")
def step_impl(context):
    context.tester.personal_inf.click()


@given("update personal inf tag exists")
def step_impl(context):
    assert (context.tester.update_personal_inf_tag_exists() == True)

@then("click on update personal inf button")
def step_impl(context):
    context.tester.update_personal_inf.click()


@given("nationality tag exists")
def step_impl(context):
    assert (context.tester.nationality_tag_exists() == True)

@then("select nationality")
def step_impl(context):
    context.tester.select_nationality_name()


@given("save changes tag exists")
def step_impl(context):
    assert (context.tester.save_changes_tag_exists() == True)

@then("click on save changes button")
def step_impl(context):
    context.tester.save_changes.click()


@given("change password tag exists")
def step_impl(context):
    assert (context.tester.change_password_tag_exists() == True)

@then("click on change password button")
def step_impl(context):
    context.tester.change_password.click()


@given("current password tag exists")
def step_impl(context):
    assert (context.tester.current_password_tag_exists() == True)

@when("current password tag found")
def step_impl(context):
    context.tester.get_current_password()

@then("enter current password")
def step_impl(context):
    context.tester.fill_current_password()


@given("new password tag exists")
def step_impl(context):
    assert (context.tester.new_password_tag_exists() == True)

@when("new password tag found")
def step_impl(context):
    context.tester.get_new_password()

@then("enter new password")
def step_impl(context):
    context.tester.fill_new_password()


@given("confirm new password tag exists")
def step_impl(context):
    assert (context.tester.confirm_new_password_tag_exists() == True)

@when("confirm new password tag found")
def step_impl(context):
    context.tester.get_confirm_new_password()

@then("confirm new password")
def step_impl(context):
    context.tester.fill_confirm_new_password()


@given("logout tag exists")
def step_impl(context):
    assert (context.tester.logout_tag_exists() == True)

@then("click on logout button")
def step_impl(context):
    context.tester.click_on_logout_button()





