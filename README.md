# Journalducoin Scraper

A simple Python script to scrape news content from [journalducoin.com](https://journalducoin.com). It utilizes the BeautifulSoup library for web scraping and requests for making HTTP requests.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3
- BeautifulSoup
- Requests

Install the required Python packages using the following command:

```bash
pip install beautifulsoup4 requests
```

## Usage
To use the script, follow these steps:

1. Clone the repository or download the script.

```bash
git clone https://github.com/fabricemlili/journalducoin-scraper.git
```
2. Navigate to the script's directory.
```bash
cd journalducoin-scraper
```
3. Run the script by executing the following command in your terminal:
```bash
python scraper.py -p <number_of_pages>
```
Replace `<number_of_pages>` with the desired number of pages to scrape. If not specified, the default is set to 500.

## Output

The scraped content will be saved to a file named `journalducoin.txt` in the same directory as the script.

## Example

To scrape content from 200 pages:

```bash
python script.py -p 200
```

## Notes
- Some URLs are excluded from scraping. Check the exclusions list in file `excluded_urls.txt` to customize exclusions (one url by row). A first url is already entered because it corresponds to a too-many-redirects error.
- The script handles cases where the "div.content" element is not found on a news page, meaning that it is no longer available.

## Author

Fabrice Mlili

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
