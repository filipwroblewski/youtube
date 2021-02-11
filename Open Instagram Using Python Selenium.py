from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# open Chrome website
driver.get('http://fwroblewski.cba.pl/')

# print website title
print(driver.title)

# locate element with class name: fa-instagram
ig_elem = driver.find_element_by_class_name('fa-instagram')
ig_elem.click()

# close window
# driver.quit()