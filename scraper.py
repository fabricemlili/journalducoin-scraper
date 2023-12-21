import argparse
import requests
from bs4 import BeautifulSoup
import os

def scrape_journalducoin(pages_number):
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Open a file for writing scraped content
    file_path = f'{script_dir}/journalducoin.txt'
    file = open(file_path, 'w')

    # URL of the news website
    URL = "https://journalducoin.com/news/"
    
    # Generate a list of URLs for the specified number of pages
    urls_page = [URL + f'page/{i}/' for i in range(1, pages_number + 1)]

    # URLs to exclude from scraping
    with open(f'{script_dir}/excluded_urls.txt') as exclu_f:
        exclusions = exclu_f.readlines()
    
    # Set to store unique lines to avoid duplicates
    unique_lines = set()

    # Iterate through each page URL
    for url_page in urls_page:
        print(url_page)
        
        # Send a request to the page
        page = requests.get(url_page)
        
        # Parse the HTML content
        soup = BeautifulSoup(page.content, "html.parser")
        
        # Find all elements with the specified class
        a_elements = soup.find_all('a', class_='column is-one-quarter-desktop is-one-third-tablet is-full-mobile category-element')
        
        # Iterate through each news element
        for element in a_elements:
            if element['href'] not in exclusions:
                print(element['href'])
                
                # Send a request to the news article
                news_resp = requests.get(element['href'])
                
                # Parse the HTML content of the news article
                soup = BeautifulSoup(news_resp.content, "html.parser")
                
                try:
                    # Extract text content from the specified div
                    txt_content = soup.select_one('div.content').get_text()
                    
                    # Iterate through each line in the text content
                    for line in txt_content.split("\n"):
                        if line not in unique_lines:
                            # Add unique lines to the set and write to the file
                            unique_lines.add(line)
                            file.write(line + '\n')
                except AttributeError as e:
                    # Handle the case where the 'div.content' element is not found
                    print(f"Raised error: {e}")
                    print(f"This error is probably due to the fact that the news URL is no longer available.")
    
    # Close the file after scraping
    file.close()

if __name__ == "__main__":
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description='Scrape news content from journalducoin.com')
    
    # Define command-line argument for the number of pages to scrape
    parser.add_argument('-p', '--pagesnumber', type=int, default=500, help='Number of pages to scrape (default: 500)')
    
    # Call the scraping function with the specified number of pages
    scrape_journalducoin(parser.parse_args().pagesnumber)
