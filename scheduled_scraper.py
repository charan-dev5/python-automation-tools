from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

all_quotes = []

for page in range(1, 4):
    driver.get(f"https://quotes.toscrape.com/page/{page}/")
    time.sleep(2)
    quotes = driver.find_elements(By.CLASS_NAME, "text")
    for quote in quotes:
        all_quotes.append(quote.text)

driver.quit()

today = datetime.datetime.now().strftime("%Y-%m-%d")
filename = rf"c:\Dev\Floor8\schedule\quotes_{today}.txt"

with open(filename, "w", encoding="utf-8") as f:
    for q in all_quotes:
        f.write(q + "\n")

print(f"Done. {len(all_quotes)} quotes saved to {filename}")        
