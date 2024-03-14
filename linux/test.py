from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import schedule
import time
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def login(username, password):
    driver = None
    try:
        driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
        driver.get("https://hdu.huitu.zhishulib.com/Content/Index/startUp#!/User/Index/login?forward=%2FStation%2FStation%2Flist")

        username_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='学号/工号/账号/手机号']"))
        )
        username_input.send_keys(username)

        password_input = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='请输入密码']"))
        )
        password_input.send_keys(password)

        login_button = driver.find_element(By.XPATH, "//div[.//span[text()='登录']]")
        login_button.click()

        print("登录成功！")
        return True
    except Exception as e:
        print(f"登录过程中出现异常：{e}")
        if driver is not None:
            driver.quit()
        return False

def select_date():
    driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
    driver.get("https://hdu.huitu.zhishulib.com/content/index/startUp/openid/okOhQt_N4h7yYsfY0gWCa4EvBGXA/#!/Seat/Index/searchSeats?space_category%5Bcategory_id%5D=591&space_category%5Bcontent_id%5D=3")

    select_elements = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "lrnw-picker"))
    )

    select = Select(select_elements[0])
    max_value_option = max(select.options, key=lambda option: int(option.get_attribute('value')))
    select.select_by_value(max_value_option.get_attribute('value'))
    print(f"使用日期: {max_value_option.text}")

    select = Select(select_elements[1])
    select.select_by_value("2")
    selected_option = select.first_selected_option
    print(f"开始时间: {selected_option.text}")

    select = Select(select_elements[2])
    max_value_option = max(select.options, key=lambda option: int(option.get_attribute('value')))
    select.select_by_value(max_value_option.get_attribute('value'))
    print(f"使用时长: {max_value_option.text}小时")

    select = Select(select_elements[3])
    select.select_by_value("0")
    selected_option = select.first_selected_option
    print(f"使用人数: {selected_option.text}人")


    start_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//div[span[contains(text(), '开始选座')]]"))
    )
    start_button.click()
    print("开始选座")
    print("当前默认你今日使用的座位。")

    confirm_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'lrnw-touchable') and .//span[contains(text(), '确认预约')]]"))
    )
    confirm_button.click()
    print("选座成功！座位信息如下:")

    seat_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '座位')]/following-sibling::span"))
    )
    print(f"座位：{seat_element.text}")

    room_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '房间')]/following-sibling::span"))
    )
    print(f"房间：{room_element.text}")

    start_time_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '开始时间')]/following-sibling::span"))
    )
    print(f"开始时间：{start_time_element.text}")

    end_time_element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '结束时间')]/following-sibling::span"))
    )
    print(f"结束时间：{end_time_element.text}")

    driver.quit()

def login_and_select_date(username, password):
    if login(username, password):
        select_date()
    else:
        print("登录失败，无法进行选座")

def job():
    print("开始选座:", datetime.now())
    login_and_select_date("264747121981sfda1", "RJawdfgersa")

def run_scheduled_job():
    schedule.every().day.at("20:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    run_scheduled_job()


