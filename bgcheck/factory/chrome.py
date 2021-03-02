from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugin-port=9222")
options.add_argument("--screen-size=1200x800")
options.add_argument("--disable-popup-blocking")
options.add_argument("test-type")


def chrome():
    return webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=options.to_capabilities())
