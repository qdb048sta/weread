from selenium.webdriver import Chrome, ChromeOptions
from WeReadScan import WeRead
# 重要！为webdriver设置headless
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')

# 启动webdriver(--headless)
headless_driver = Chrome(executable_path="C:\\Users\\starg\\Downloads\\chromedriver_win32\\chromedriver.exe",options=chrome_options)

# debug 模式启动，可以保留png缓存
weread=WeRead(headless_driver)
weread.debug=True
# 重要！登陆
weread.login()
# 爬去指定url对应的图书资源并保存到当前文件夹
weread.scan2pdf('https://weread.qq.com/web/reader/be132df07212f03ebe1ca02')