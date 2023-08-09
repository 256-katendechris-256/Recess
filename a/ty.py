from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable
#chrome_driver_path = 'chromedriver'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome()

# URL of the webpage to scrape
url = 'https://xeno-canto.org/explore?query=since:31&dir=0&order=xc'  # Replace this with the actual URL

# Open the webpage
driver.get(url)

# Find the table rows containing the data
rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'new-species')] | //tr[not(contains(@class, 'new-species'))]")

# Loop through each row and extract the data
for row in rows:
    columns = row.find_elements(By.XPATH, ".//td")
    if len(columns) == 12:  # Verify if it's a valid row with 12 columns
        common_name = columns[1].text
        scientific_name = columns[1].find_element(By.XPATH, "./span[@class='sci-name']").text
        length = columns[2].text
        recordist = columns[3].text
        date = columns[4].text
        time = columns[5].text
        country = columns[6].text
        location = columns[7].text
        elevation = columns[8].text
        _type = columns[9].text
        remarks = columns[10].text
        actions = columns[11].text

        # Do whatever you want with the extracted data
        print("Common Name:", common_name)
        print("Scientific Name:", scientific_name)
        print("Length:", length)
        # ... and so on

# Close the browser
driver.quit()
