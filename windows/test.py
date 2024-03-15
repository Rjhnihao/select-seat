import schedule
import time
import requests
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Host": "hdu.huitu.zhishulib.com",
    "Referer":"https://hdu.huitu.zhishulib.com/",
    "Sec-Ch-Ua":"",
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":"Windows",
}

def login(username,password):
    for attempt in range(3):
        driver=None
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')  # 无头模式
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

            wait = WebDriverWait(driver, 10)

            pwd_path_selector = """//*[@id="react-root"]/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div[3]/div/div[2]/input"""
            button_path_selector = """//*[@id="react-root"]/div/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div[1]/div[3]"""


            driver.get("https://hdu.huitu.zhishulib.com/")
            #等待加载
            wait.until(EC.presence_of_element_located((By.NAME, "login_name")))
            wait.until(EC.presence_of_element_located((By.XPATH, pwd_path_selector)))
            wait.until(EC.presence_of_element_located((By.XPATH, button_path_selector)))
            #寻找元素
            driver.find_element(By.NAME, 'login_name').clear()
            driver.find_element(By.NAME, 'login_name').send_keys(username)
            driver.find_element(By.XPATH, pwd_path_selector).clear()
            driver.find_element(By.XPATH, pwd_path_selector).send_keys(password)
            driver.find_element(By.XPATH, button_path_selector).click()
            time.sleep(5)

            cookie_list = driver.get_cookies()
            cookie = ";".join([f"{item['name']}={item['value']}" for item in cookie_list])

            print(f"用户{username}登录成功！")
            return {'Cookie': cookie}
        except Exception as e:
            print(f"用户{username}登录失败，尝试次数 {attempt + 1}: {e}")
        finally:
            driver.quit()

    return None

def select(cookie,seat):
    for attempt in range(3):
        try:
            uid = None
            try:    #获取uid
                response=requests.get("https://hdu.huitu.zhishulib.com/Seat/Index/searchSeats?LAB_JSON=1",headers=headers,cookies=cookie)
                uid=response.json()['DATA']["uid"]
            except :
                print("uid参数获取失败！")
            now = datetime.now()
            start_time_of_the_day = datetime(now.year, now.month, now.day)
            target_start_time = start_time_of_the_day + timedelta(days=1, hours=-1) #-1+8=7(7点) day=1,表明是明天
            duration = 3600
            begintime = int((target_start_time - datetime(1970, 1, 1)).total_seconds())

            data = {
                "beginTime": begintime,
                "duration": duration,
                "seats[0]": seat,
                "seatBookers[0]": uid,
                "is_recommend":1,
            }

            response = requests.post("https://hdu.huitu.zhishulib.com/Seat/Index/bookSeats?LAB_JSON=1", data=data, headers=headers,cookies=cookie)
            #查看预约情况
            msg=response.json()['MESSAGE']
            print(f"当前账号{msg}")
            return True

        except Exception as e:
            print(f"预约失败,尝试次数 {attempt + 1}: {e}")

    return None


def comfirm(username, password,seat):
    cookie = login(username, password)
    if cookie:
        msg=select(cookie,seat)
        if not msg:
            print("登录成功，选座失败。")
    else:
        print("登录失败!!!!!!!")


def job():
    print("开始选座:", datetime.now())
    #comfirm("dasfsd","dsadv","das") #输入账号，密码，座位
    comfirm("dasewfsd","dwfdgfsd","sdsaz") #输入账号，密码，座位

def run_scheduled_job():
    print("开始运行。")
    schedule.every().day.at("20:01").do(job)

    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    run_scheduled_job()


