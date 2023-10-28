from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Creating an instance
webdriver_path ="C:/Users/Anupam/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Logging into LinkedIn
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(6)

username = driver.find_element(By.ID, "username")
username.send_keys("na@na.com")

pword = driver.find_element(By.ID, "password")
pword.send_keys("password")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Opening Profile
# paste the URL of profile here
profile_url = "https://www.linkedin.com/in/anupamcharanpahari/"

driver.get(profile_url)  # this will open the link
start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
    driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000

    # we will stop the script for 3 seconds so that
    # the data can load
    time.sleep(3)
    # We can change it as per your needs and internet speed

    end = time.time()

    # We will scroll for 20 seconds.
    # We can change it as per your needs and internet speed
    if round(end - start) > 20:
        break

src = driver.page_source

# Now using beautiful soup
soup = BeautifulSoup(src, 'html.parser')
# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

# In case of an error, try changing the tags used here.

name_loc = intro.find("h1")

# Extracting the Name
name = name_loc.text.strip()
# strip() is used to remove any extra blank spaces

works_at_loc = intro.find("div", {'class': 'text-body-medium'})

# this gives us the HTML of the tag in which the Company Name is present
# Extracting the Company Name
works_at = works_at_loc.text.strip()

location_loc = intro.find_all("span", {'class': 'text-body-small'})

# Extracting the Location
# The 2nd element in the location_loc variable has the location
location = location_loc[0].get_text().strip()

print("Name -->", name,
      "\nWorks At -->", works_at,
      "\nLocation -->", location)
