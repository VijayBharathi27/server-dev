#import spacy
#import en_core_web_lg
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import request


def scraping():
    DRIVER_PATH = '/home/vijay/chromedriver/chromedriver'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.maximize_window()
    driver.delete_all_cookies()
    # opening indeed website
    # Inputs = request.get_json()  # Enter the name and location key in json
    Inputs = {}
    Inputs['job'] = request.form.get('job')
    Inputs['location'] = request.form.get('location')
    driver.get('https://indeed.com')
    jobName = Inputs['job']
    location = Inputs['location']

    search_job = driver.find_element_by_xpath('//*[@id=\"text-input-what\"]')
    search_job.send_keys([jobName])
    search_location = driver.find_element_by_xpath(
        '//*[@id=\"text-input-where\"]')
    search_location.send_keys([location])

    import time
    time.sleep(1)
    try:
        initial_search_button = driver.find_element_by_xpath(
            '/html/body/div/div[2]/span/div[3]/div[1]/div/div/div/form/div[3]/button')
    except:
        initial_search_button = driver.find_element_by_xpath(
            '/html/body/div/div[2]/span/div[3]/div[1]/div/div/form/button')
    initial_search_button.click()
    # initial search button click
    # initial_search_button = driver.find_element_by_class_name(
    #     'icl-Button icl-Button--primary icl-Button--md icl-WhatWhere-button')
    # full xpath
    # initial_search_button = driver.find_element_by_xpath(
    #    '/html/body/div/div[2]/span/div[3]/div[1]/div/div/div/form/button')
    # initial_search_button = driver.find_element_by_xpath(
    #     '//*[@id="whatWhereFormId"]/div[3]/button')
    # driver.implicitly_wait(3)
    # advanced search button
    advanced_search = driver.find_element_by_xpath(
        "//a[contains(text(),'Advanced Job Search')]")
    advanced_search.click()
    # display limit to 10
    display_limit = driver.find_element_by_xpath(
        '//select[@id="limit"]//option[@value="10"]')
    display_limit.click()
    # sort by date
    sort_option = driver.find_element_by_xpath(
        '//select[@id="sort"]//option[@value="date"]')
    sort_option.click()
    search_button = driver.find_element_by_xpath('//*[@id="fj"]')
    search_button.click()

    import time
    time.sleep(1)
    close_popup = driver.find_element_by_xpath('//*[@id=\"popover-x\"]/button')
    close_popup.click()

    data_list = []
    job_card = driver.find_elements_by_xpath(
        '//div[contains(@class,"job_seen_beacon")]')
    for job in job_card:
        try:
            review = job.find_element_by_xpath(
                './/span[@class="ratingNumber"]').text
        except:
            review = "None"
        try:
            salary = job.find_element_by_xpath(
                './/span[@class="salary-snippet"]').text
        except:
            salary = "Not disclosed"

        try:
            location = job.find_element_by_xpath(
                './/div[contains(@class,"companyLocation")]').text
        except:
            location = job.find_element_by_xpath(
                './/div[@class,"companyLocation"]').text

        try:
            title = job.find_element_by_class_name('jobTitle').text
        except:
            title = job.find_element_by_xpath(
                './/h2[@class="jobTitle"]').get_attribute(name="span")

        company = job.find_element_by_xpath(
            './/span[@class="companyName"]').text

        data = {'title': title, 'company': company,
                'salary': salary, 'location': location, 'review': review}
        data_list.append(data)
    # next_page = driver.find_element_by_xpath('//a[@aria-label="{}"]//span[@class="pn"]'.format(i+2))
    # try:
    #   next_page = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/table/tbody/tr/td[1]/nav/div/ul/li[7]/a/span')
    #   next_page.click();
    # except:
    #   break
    result_data_indeed = data_list
    return result_data_indeed

    #!pip install -U spacy[cuda92]
    #!python -m spacy download en_core_web_lg;

    #nlp = en_core_web_lg.load()

    # def check_concat(a, b, index_a):
    #     clone = 0
    #     job_a = a[index_a]
    #     for index_b in range(0, len(b)):
    #         job_b = b[index_b]
    #         comp_a = job_a.get('company')
    #         comp_a = ' '.join(comp_a.lower().split())
    #         comp_b = job_b.get('company')
    #         comp_b = ' '.join(comp_b.lower().split())
    #         if comp_a != comp_b:
    #             break
    #         disc_a = job_a.get('title')
    #         disc_b = job_b.get('title')
    #         disc_a = ' '.join(disc_a.lower().split())
    #         disc_b = ' '.join(disc_b.lower().split())
    #         doc1 = nlp(disc_a)
    #         doc2 = nlp(disc_b)
    #         similar = doc1.similarity(doc2)
    #         print(doc1.similarity(doc2))
    #         if similar > 0.9:
    #             print('Clone Found: '+str(similar))
    #             clone = 1
    #             break
    #     if clone == 0:
    #         b = b.append(job_a)

    # def filter_fn(a):
    #     b = []
    #     for index_a in range(0, len(a)):
    #         check_concat(a, b, index_a)
    #     return b

    # pure_data = filter_fn(result_data_indeed)
    # return pure_data
