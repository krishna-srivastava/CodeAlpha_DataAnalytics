# Task 1: Web Scraping

## Overview
Scraped 100+ famous quotes from **quotes.toscrape.com** using Python. Extracted author names, quote text, and category tags. Saved all data in CSV and Excel format for further analysis.

---

## What I Did

### 1. **Website Selection**
Chose quotes.toscrape.com because:
- Specifically designed for learning web scraping
- Clean HTML structure (easy to parse)
- Legal to scrape (no robots.txt restrictions)
- No anti-scraping measures
- Perfect for beginners

### 2. **Tools Used**
```
- Python 3.11
- BeautifulSoup4 (HTML parsing)
- Requests (fetching web pages)
- Pandas (data organization)
```

### 3. **Data Extracted**
Each quote entry contains:
- **Quote Text** - Full quote with quotation marks
- **Author** - Person who said/wrote it
- **Tags** - Category labels (e.g., "inspirational", "life", "humor")

---

## How It Works

### Step 1: Fetch Website
```python
import requests
url = "http://quotes.toscrape.com/"
response = requests.get(url)
html_content = response.text
```

### Step 2: Parse HTML
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
quotes = soup.find_all('div', class_='quote')
```

### Step 3: Extract Data
```python
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]
```

### Step 4: Handle Pagination
Loop through all 10 pages and extract data from each page automatically.

### Step 5: Save Data
```python
df.to_csv('quotes_scraped.csv', index=False)
```

---

## Results

✅ **Successfully scraped:** 100 quotes  
✅ **Data points:** 3 columns (Quote, Author, Tags)  
✅ **Output formats:** CSV + Excel  
✅ **Execution time:** ~20 seconds (with delays)  

### Sample Output
| Quote | Author | Tags |
|-------|--------|------|
| "The way to get started is to quit talking and begin doing." | Walt Disney | action, inspirational, motivation |
| "Life is what happens when you're busy making other plans." | John Lennon | life, philosophy |
| "The way to get started is to quit talking and begin doing." | Walt Disney | action, inspirational |

---

## Key Features Implemented

### ✨ Error Handling
- Try-catch blocks for network errors
- Connection timeout handling
- Graceful retry logic

### ⏱️ Polite Scraping
- 2-second delays between requests
- User-Agent headers added
- Respects server load

### 📊 Data Cleaning
- Removed extra whitespace
- Proper encoding (UTF-8)
- Duplicate handling

### 🔄 Pagination
- Automatically detects next page button
- Loops until all pages scraped
- Prints progress updates

---

## Installation & Running

```bash
# Install dependencies
pip install requests beautifulsoup4 pandas openpyxl

# Run the script
python python.py

# Output files generated
- quotes_scraped.csv
- quotes_scraped.xlsx
```

---

## What I Learned

1. How to inspect website HTML using DevTools
2. CSS selectors for finding specific elements
3. Handling pagination in web scraping
4. Difference between requests and BeautifulSoup
5. Best practices (delays, headers, error handling)
6. Data export to multiple formats (CSV/Excel)

---

## Conclusion

Successfully completed Task 1 by scraping 100+ real-world data points, handling errors gracefully, and exporting in multiple formats. Ready for Task 2 (EDA - Exploratory Data Analysis) where we'll analyze this data deeper.

---
