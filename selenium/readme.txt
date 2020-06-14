D:\devtools\Anaconda3\python.exe D:/MyStudio/resources/spider/src/selenium/test.py
Traceback (most recent call last):
  File "D:/MyStudio/resources/spider/src/selenium/test.py", line 3, in <module>
    webdriver.Chrome("./webdriver/chromedriver.exe")
  File "D:\devtools\Anaconda3\lib\site-packages\selenium\webdriver\chrome\webdriver.py", line 81, in __init__
    desired_capabilities=desired_capabilities)
  File "D:\devtools\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 157, in __init__
    self.start_session(capabilities, browser_profile)
  File "D:\devtools\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 252, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "D:\devtools\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "D:\devtools\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: Chrome version must be between 70 and 73
  (Driver info: chromedriver=73.0.3683.68 (47787ec04b6e38e22703e856e101e840b65afe72),platform=Windows NT 10.0.17134 x86_64)


Process finished with exit code 1
