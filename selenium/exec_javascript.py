from selenium import webdriver
browser = webdriver.Chrome('./webdriver/chromedriver')
browser.get('https://www.jd.com')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_async_script('alert("已经到达页面底端")')
