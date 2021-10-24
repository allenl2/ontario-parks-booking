from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


def retriveTableData():
    # set up the browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://reservations.ontarioparks.com/')
    browser.implicitly_wait(20)

    # wait for loading
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "mat-tab-label-0-1"))
    )
    print("Going to sleep")
    time.sleep(25)

    # input search type details
    browser.find_element_by_id("mat-tab-label-0-1").click()
    print("Clicked")
    browser.find_element_by_id("mat-tab-label-0-2").click()
    print("Clicked - Backcountry")

    # wait for loading
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "mat-label-1"))
    )

    browser.find_element_by_id("mat-label-1").click()
    print("Clicked - Hiking")
    browser.find_element_by_id("mat-select-8").click()
    print("Clicked - Park DD")
    browser.find_element_by_id("mat-option-126").click()
    print("Clicked - Algonquin Backcountry")

    # input search site details
    browser.find_element_by_id("mat-select-10").click()
    print("Clicked - Access Point DD")
    browser.find_element_by_id("mat-option-146").click()
    print("Clicked - Access Point West Gate")

    # input search date details
    browser.find_element_by_id("mat-input-6").click()
    print("Clicked - Open calendar")
    browser.find_element_by_id("monthDropdownPicker").click()
    print("Clicked - Open months")
    browser.find_element_by_css_selector(
        "td[aria-label='September 2021']").click()
    print("Clicked - Click Sept")
    browser.find_element_by_css_selector(
        "td[aria-label='September 4, 2021']").click()
    print("Clicked - Click 4")

    time.sleep(10)

    # actual search
    browser.find_element_by_id("actionSearch").click()
    print("SEARCH")

    time.sleep(10)

    browser.find_element_by_id("consentButton").click()
    print("Clicked - Consent")
    browser.find_element_by_id("grid-view-button").click()
    print("Clicked - Calendar View")

    table = browser.find_element_by_id("grid-table")
    print("Found Table")
    data = table.get_attribute('innerHTML')
    print("DATA RETRIEVED!")

    return data


# for selecting by CSS selector
# element[attribute = 'attribute-value']
# td[aria-label = 'September 2021']
