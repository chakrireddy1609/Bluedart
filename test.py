from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions


options = ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
driver.get("https://www.bluedart.com/home")
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"home-dart-box")))
driver.find_element(By.ID,"trackingNoTrackDart").send_keys("76712674603")
driver.find_element(By.ID,"goBtnTrackDart").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()=' Status and Scan ']")))
driver.find_element(By.XPATH,"//a[text()=' Status and Scan ']").click()
details = driver.find_element(By.XPATH,"(//div[@class='table-responsive'])/table/tbody/tr[1]/td[2]").text
time = driver.find_element(By.XPATH,"(//div[@class='table-responsive'])/table/tbody/tr[1]/td[4]").text

print(details,time)
