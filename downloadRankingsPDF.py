from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64
from datetime import datetime  # Import datetime module

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.ncaa.com/rankings/lacrosse-men/d1/ncaa-mens-lacrosse-rpi")

# Wait for the necessary elements to load
driver.implicitly_wait(5)

# Use the built-in Selenium method to execute a CDP command
# The command 'Page.printToPDF' is used here to generate the PDF from the current page
pdf = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})

# Convert the base64 encoded data to bytes
pdf_content = base64.b64decode(pdf['data'])

# Get current month and timestamp
current_time = datetime.now().strftime("%m-%d_%H-%M-%S")

# Write the PDF data to a file with month and timestamp appended to the filename
with open(f"./data/rankings_{current_time}.pdf", "wb") as file:
    file.write(pdf_content)

driver.quit()
