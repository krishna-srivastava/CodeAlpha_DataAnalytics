import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "http://quotes.toscrape.com/"
quotes_data = []
page_url = url

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

while page_url:
    try:
        print(f"Scraping: {page_url}")
        
        # Timeout add kro aur headers
        response = requests.get(page_url, headers=headers, timeout=10)
        response.raise_for_status()  # Error check
        
        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            quotes_data.append({
                'Quote': text,
                'Author': author,
                'Tags': ', '.join(tags)
            })
        
        time.sleep(2)
        
        next_btn = soup.find('li', class_='next')
        if next_btn:
            page_url = url + next_btn.find('a')['href']
        else:
            page_url = None
    
    except requests.exceptions.ConnectionError:
        print("⚠️ Connection Error! Retrying in 5 seconds...")
        time.sleep(5)
        continue
    
    except Exception as e:
        print(f"❌ Error: {e}")
        break

# Data save kro
df = pd.DataFrame(quotes_data)
df.to_csv('quotes_scraped.csv', index=False, encoding='utf-8')

print(f"\nSuccess! {len(quotes_data)} quotes scraped")
print(df.head())