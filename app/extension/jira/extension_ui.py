import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS


def app_specific_action(webdriver):
    page = BasePage(webdriver)

    @print_timing("selenium_app_custom_action")
    def measure():
        @print_timing("selenium_app_custom_action:open_course")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/jira/plugins/servlet/ac/atlassian-jira-training/app")
            page.wait_until_visible((By.ID, "app-root-atlassian-jira-training"))
        sub_measure()
    measure()

    def measure():
        @print_timing("selenium_app_custom_action:open_course_with_filters")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/jira/plugins/servlet/ac/atlassian-jira-training/app")
        sub_measure()
    measure()
