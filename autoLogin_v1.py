from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time


def autoSubMcGillGymSession():
    secretNum = 410645
    usernameStr = "436015CZhou"
    pwStr = "zslong0627"
    url = "https://hnd-p-ols.spectrumng.net/mcgill/Login.aspx"
    usernameInputID = "ctl00_pageContentHolder_loginControl_UserName"
    pwInputID = "ctl00_pageContentHolder_loginControl_Password"
    signInInputID = "ctl00_pageContentHolder_loginControl_Login"

    part2_BookYourWorkOutDivID = "menu_GRX"

    browser = webdriver.Firefox(executable_path='/Users/joe/Downloads/geckodriver')
    browser.get(url)

    #Sign in page
    username = browser.find_element_by_id(usernameInputID)
    username.send_keys(usernameStr)

    pw = browser.find_element_by_id(pwInputID)
    pw.send_keys(pwStr)

    signInButton = browser.find_element_by_id(signInInputID)
    signInButton.click()


    # Book your work out selection page


    BookYourWorkOutBtn = WebDriverWait(browser, 1000).until(
        EC.presence_of_element_located((By.ID, part2_BookYourWorkOutDivID)))
    BookYourWorkOutBtn.click()





    # click "next page" Optional
    enrollBtn = WebDriverWait(browser, 1000).until(
        EC.presence_of_element_located((By.CLASS_NAME, "clsNextWeek")))
    enrollBtn.click()

    # Book work out table page

    chosenWorkOutPeriod = WebDriverWait(browser, 1000).until(
        EC.presence_of_element_located((By.ID, secretNum)))
    chosenWorkOutPeriod.click()





    # click "enroll"
    enrollBtn = WebDriverWait(browser, 1000).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btnselectschedule")))
    enrollBtn.click()


    # click "I agree"

    agreeBtn = WebDriverWait(browser, 2000).until(
        EC.presence_of_element_located((By.ID, "btnWaiverAgree")))
    agreeBtn.click()


    # click register btn

    registerBtn = WebDriverWait(browser, 3000).until(
        EC.presence_of_element_located((By.ID, "ctl00_pageContentHolder_btnContinueCart")))
    registerBtn.click()


schedule.every().day.at("00:01").do(autoSubMcGillGymSession)

while True:
    schedule.run_pending()
    time.sleep(10) # wait one minute
