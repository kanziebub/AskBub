import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://kanziebub.github.io/ProjectSEA/rulebook.html"

# Send a request to the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all text content
content = soup.get_text(separator="\n")
print(content)  # This will display the extracted text
