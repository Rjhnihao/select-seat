from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_chrome_driver():
    # 配置 ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式运行（可选）
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # 设置 ChromeDriver 的路径
    chromedriver_path = './chromedriver'  # 替换为 ChromeDriver 的实际路径

    # 启动 ChromeDriver
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

    try:
        # 访问百度
        driver.get("https://www.baidu.com")

        # 等待页面加载
        time.sleep(5)

        # 检查页面标题
        if "百度一下" in driver.title:
            print("Chrome 和 ChromeDriver 匹配，访问 baidu.com 成功！")
        else:
            print("访问 baidu.com 失败，页面标题不匹配。")

    except Exception as e:
        print(f"测试失败：{e}")

    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    test_chrome_driver()
