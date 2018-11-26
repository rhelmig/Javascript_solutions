import pyautogui
from pytest import mark
from selenium.webdriver import ActionChains
# pytest -v -s --html=report.html --tb=short


@mark.js
def test_javascript_alert(driver):
    driver.get('http://the-internet.herokuapp.com/javascript_alerts')
    driver.find_element_by_css_selector("[onclick='jsAlert\(\)']").click()
    alert = driver.switch_to_alert()
    msg = alert.text
    print(msg)
    alert.accept()


@mark.js
def test_javascript_confirm(driver):
    driver.get('http://the-internet.herokuapp.com/javascript_alerts')
    driver.find_element_by_css_selector("[onclick='jsConfirm\(\)']").click()
    alert = driver.switch_to_alert()
    msg = alert.text
    print(msg)
    alert.accept()


@mark.jst
def test_javascript_prompt(driver):
    driver.get('http://the-internet.herokuapp.com/javascript_alerts')
    driver.find_element_by_css_selector("[onclick='jsPrompt\(\)']").click()
    alert = driver.switch_to_alert()
    alert.send_keys('TEST')
    # Note: send_keys has a bug where the text is entered but is NOT always visible.
    alert.accept()
    result = driver.find_element_by_css_selector('#result')
    assert result.text == 'You entered: TEST'


@mark.js_execute
def test_execute_javascript(driver):
    driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_intro_inner_html')
    driver.execute_script('document.getElementById("demo")')


#########################################################
# Drag and Drop using pyautogui

@mark.dd
def test_get_position(driver):
    driver.get("http://the-internet.herokuapp.com/drag_and_drop")
    pos = driver.find_element_by_xpath("/html//div[@id='column-b']")
    location = pos.location
    print(location)


@mark.dd
def test_drag_and_drop(driver):
    # location of the grab
    pyautogui.moveTo(800, 250, 1)
    # drag to
    pyautogui.dragTo(550, 240, 1)
    # check that it made it
    moved = driver.find_element_by_xpath("//div[@id='column-a']/header[.='B']")
    if moved:
        print('Success')


@mark.scroll
def test_scroll_to(driver):
    driver.get('https://stackoverflow.com/questions/34562095/scrollintoview-vs-movetoelement')
    element = driver.find_element_by_link_text('Blog')
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()


#################################################################
# ACTION CHAINS review
@mark.action
# clicks a sub pop up menu
def test_chain(driver):
    driver.get('https://www.imdb.com/')
    showtime = driver.find_element_by_id("navTitleMenu")
    action_chains = ActionChains(driver)
    action_chains.move_to_element(showtime)
    action_chains.click(driver.find_element_by_link_text("Coming Soon"))
    action_chains.perform()


@mark.drag
def test_drag_by_action_chain(driver):
    driver.get('http://the-internet.herokuapp.com/drag_and_drop')
    action_chains = ActionChains(driver)
    source = driver.find_element_by_id('column-b')
    target = driver.find_element_by_id('column-a')
#    action_chains.move_to_element(source)
    action_chains.drag_and_drop(source, target).perform()
