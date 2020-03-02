from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_login_to_jira():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://jira.hillel.it/secure/Dashboard.jspa')
    assert "System Dashboard" in driver.title

    driver.find_element_by_id("login-form-username").clear()
    driver.find_element_by_id("login-form-username").send_keys("adikalova")
    driver.find_element_by_id("login-form-password").clear()
    driver.find_element_by_id("login-form-password").send_keys("1234567")
    driver.find_element_by_id("login").submit()

    assert driver.page_source.find('Dashboard')
