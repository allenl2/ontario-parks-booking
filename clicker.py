from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging


def retriveTableData():
    # set up the browser
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get('https://reservations.ontarioparks.com/')
    browser.implicitly_wait(10)

    # navigate the site to for the selected campground
    navigateSite(browser)

    time.sleep(3)

    table = browser.find_element_by_id("grid-table")
    logging.info('Found table')

    print(table)

    data = table.get_attribute('innerHTML')
    logging.info("Data retrived")

    return data

# Navigates to the calendar screen for the specified park and dates
# Inputs: park_id, date_arrive, date_depart
# Outputs: n/a


month = 'Jun 2023'


def navigateSite(browser):
    # navigate to correct tab
    waitUntilLoaded(browser, "mat-tab-label-0-3")
    browser.find_element_by_id("mat-tab-label-0-3").click()
    logging.info("Click - Roofed Accomodations")

    # input location details
    browser.find_element_by_id("park-field").click()
    logging.info("Click - Park dropdown")

    browser.find_element_by_id("mat-option-104").click()  # change to argument
    logging.info("Click - Algonquin Mew Lake")

    # input search date details
    browser.find_element_by_id("mat-date-range-input-1").click()
    logging.info("Clicked - Open calendar")
    browser.find_element_by_id("monthDropdownPicker").click()
    logging.info("Clicked - Open months")
    browser.find_element_by_css_selector(f"button[aria-label='{month}']").click()
    logging.info("Clicked - Click Month")
    browser.find_elements_by_css_selector("td[data-mat-col='5']")[1].click()
    logging.info("Clicked - Click Start Date")
    browser.find_elements_by_css_selector("td[data-mat-col='5']")[2].click()
    logging.info("Clicked - Click End Date")

    # start search
    browser.find_element_by_id("actionSearch").click()
    logging.info("Searching")

    time.sleep(3)

    # browser.find_element_by_id("consentButton").click()
    # logging.info("Clicked - Consent")

    # select campground
    browser.find_element_by_id("list-view-button").click()
    # browser.find_element_by_id("grid-view-button").click()
    logging.info("Clicked - List View")
    browser.find_element_by_id("mat-checkbox-1").click()
    logging.info("Clicked - Filter Unselect")
    browser.find_element_by_id("resource-name-0").click()
    logging.info("Clicked - Hydro Campground")

    # get the dates
    browser.find_element_by_id("grid-view-button").click()
    logging.info("Clicked - Calendar View")


# pauses run until the specified element is loaded


def waitUntilLoaded(browser, id):
    element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, id))
    )

# for selecting by CSS selector
# element[attribute = 'attribute-value']
# td[aria-label = 'September 2021']
