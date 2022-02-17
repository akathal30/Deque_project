from axe_selenium_python_dev import Axe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import json


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://dequeuniversity.com/demo/mars")
wait = WebDriverWait(driver, 10)
axe = Axe(driver)
axe.inject()

def test_1():
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main-nav")))
    print('main nav loaded')

def test_2():
    radio_buttons = driver.find_elements(By.XPATH, "//div/h3[text()='Let the Adventure Begin!']/../form/fieldset/div/input[@type='radio']")
    assert(len(radio_buttons))==5, "test failed as radio buttons are not 5"
    print(len(radio_buttons))

def test_3():
    #//div[@id='passengers']/div[@class='dynamic']/div[@class='passenger added-passenger'] - xpath of new [assenger
    #//div[@id='passengers']/div[@id='passenger0']  - xpath of original passenger
    first_passenger = driver.find_element(By.XPATH, "//div[@id='passengers']/div[@id='passenger0']")
    no_of_added_passsengers_before_add_traveller = driver.find_elements(By.XPATH, "//div[@id='passengers']/div[@class='dynamic']/div[@class='passenger added-passenger']")
    assert len(no_of_added_passsengers_before_add_traveller)==0
    print(len(no_of_added_passsengers_before_add_traveller))
    # check for no of passengers
    driver.find_element(By.XPATH, "//div[@id='add-traveler']/a").click()
    new_no_ofadded_traveller = driver.find_elements(By.XPATH, "//div[@id='passengers']/div[@class='dynamic']/div[@class='passenger added-passenger']")
    assert len(new_no_ofadded_traveller)==1, "test failed"
    print('new no. of addded passengers = '+str(len(new_no_ofadded_traveller)))

def test_4():
    video_header = driver.find_element(By.XPATH, "//div[@id='video-box']/div[@class='interior-container']/h3").text
    print(video_header)
    driver.find_element(By.XPATH, "//div[@id='video-box']/div[@class='interior-container']/div[@class='vid-arrows nextvid']/i").click()
    new_video_header = driver.find_element(By.XPATH, "//div[@id='video-box']/div[@class='interior-container']/h3").text
    print(new_video_header)
    assert video_header != new_video_header, "test failed as headers are same"
    print('passed')

def test_5():
    results = axe.run()
    axe.write_results(results, 'a11y.json')

    with open(r'''E:\Ankit\Python\Learning\deque_project\a11y.json''', encoding='utf-8', errors='ignore') as json_data:
        jsondict = json.load(json_data, strict=False)
    print(type(jsondict))
    print(jsondict)
    violations_list = jsondict['violations']
    print(len(violations_list))
    no_of_violation = len(violations_list)
    print(violations_list)
    for violation in violations_list:
        print(violation['description'])
    assert no_of_violation == 0, "violations found hence test failed"









