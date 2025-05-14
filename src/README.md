import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import os

def scrape_iex_news(url, company_name):
    """Scrape news for a single company"""
    headers = {
        'User-Agent': 'Custom Scraper Bot (contact@youremail.com)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    try:
        time.sleep(1)  # Be polite and wait 1 second between requests
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all news elements
        news_headlines = soup.find_all('a', id=lambda x: x and 'linkTitle' in x)
        news_sublines = soup.find_all('a', id=lambda x: x and 'linkIntro' in x)
        news_dates = soup.find_all('time', class_='previewlist__date')

        # Create lists to store data
        articles = []
        
        # Ensure we process only matching sets of data
        for headline, subline, date in zip(news_headlines, news_sublines, news_dates):
            if date and 'datetime' in date.attrs:
                try:
                    date_obj = datetime.strptime(date['datetime'], '%Y-%m-%d %H:%M')
                    formatted_date = date_obj.strftime('%Y-%m-%d %H:%M')
                    
                    articles.append({
                        'Company': company_name,
                        'Date': formatted_date,
                        'Headline': headline.text.strip(),
                        'Subline': subline.text.strip()
                    })
                except ValueError:
                    continue

        return pd.DataFrame(articles)

    except Exception as e:
        print(f"Error scraping {company_name}: {e}")
        return pd.DataFrame()

def get_company_name(url):
    """Extract company name from URL"""
    parts = url.split('/')
    if 'nieuws.aspx' in parts[-1]:
        company_part = parts[-2]
    else:
        company_part = parts[-1].replace('.aspx', '')
    return company_part.replace('-', ' ')

# List of stock URLs
stock_urls = [
    'https://www.iex.nl/Aandeel-Koers/360114884/Air-France-KLM/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600825866/ALLFUNDS-GROUP/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/247828/Accsys-Technologies/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/613006/BS-Group-SA/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/596722/Basic-Fit/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/60124608/VASTNED/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11804/ACOMO/nieuws.aspx'
]

def main():
    # List to store all company dataframes
    all_news = []
    
    # Scrape news for each company
    for url in stock_urls:
        company_name = get_company_name(url)
        print(f"Scraping news for {company_name}...")
        
        company_df = scrape_iex_news(url, company_name)
        if not company_df.empty:
            all_news.append(company_df)
            print(f"Found {len(company_df)} articles for {company_name}")
        else:
            print(f"No news found for {company_name}")
    
    # Combine all news into one dataframe
    if all_news:
        combined_df = pd.concat(all_news, ignore_index=True)
        
        # Save to Excel
        output_dir = r"C:\Users\Gebruiker\Downloads\R-Assignment\Scriptie"
        os.makedirs(output_dir, exist_ok=True)
        excel_path = os.path.join(output_dir, 'forgottenstuff.xlsx')
        combined_df.to_excel(excel_path, index=False, sheet_name='News')
        
        print(f"\nSaved {len(combined_df)} articles to {excel_path}")
    else:
        print("No news articles were found")

if __name__ == "__main__":
    main()



import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import os

def scrape_iex_news(url, company_name):
    """Scrape news for a single company"""
    headers = {
        'User-Agent': 'Custom Scraper Bot (contact@youremail.com)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    try:
        time.sleep(1)  # Be polite and wait 1 second between requests
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all news elements
        news_headlines = soup.find_all('a', id=lambda x: x and 'linkTitle' in x)
        news_sublines = soup.find_all('a', id=lambda x: x and 'linkIntro' in x)
        news_dates = soup.find_all('time', class_='previewlist__date')

        # Create lists to store data
        articles = []
        
        # Ensure we process only matching sets of data
        for headline, subline, date in zip(news_headlines, news_sublines, news_dates):
            if date and 'datetime' in date.attrs:
                try:
                    date_obj = datetime.strptime(date['datetime'], '%Y-%m-%d %H:%M')
                    formatted_date = date_obj.strftime('%Y-%m-%d %H:%M')
                    
                    articles.append({
                        'Company': company_name,
                        'Date': formatted_date,
                        'Headline': headline.text.strip(),
                        'Subline': subline.text.strip()
                    })
                except ValueError:
                    continue

        return pd.DataFrame(articles)

    except Exception as e:
        print(f"Error scraping {company_name}: {e}")
        return pd.DataFrame()

def get_company_name(url):
    """Extract company name from URL"""
    parts = url.split('/')
    if 'nieuws.aspx' in parts[-1]:
        company_part = parts[-2]
    else:
        company_part = parts[-1].replace('.aspx', '')
    return company_part.replace('-', ' ')

# List of stock URLs
stock_urls = [
    'https://www.iex.nl/Aandeel-Koers/600826062/UMG/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11962/UNILEVER-PLC/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/360114884/Air-France-KLM/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600825866/ALLFUNDS-GROUP/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/247828/Accsys-Technologies/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/613006/BS-Group-SA/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11795/Wolters-Kluwer/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/612967/ABN-AMRO-BANK-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/613007/ADYEN-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11754/Aegon/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11755/Ahold-Delhaize-Koninklijke/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11756/Akzo-Nobel/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11895/ArcelorMittal/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11808/ASM-International/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/16923/ASML-Holding/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/596718/ASR-Nederland/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11820/BE-Semiconductor-Industries/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11764/DSM-FIRMENICH-AG/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600826527/EXOR-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11770/Heineken/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/610603/IMCD/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11773/ING-Groep/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/25845/KPN-Koninklijke/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/610720/NN-Group/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11783/Philips-Koninklijke/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600539912/PROSUS/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11785/RANDSTAD-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11765/RELX/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/210964/SHELL-PLC/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11797/AALBERTS-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600826062/UMG/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/613004/Alfen-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/244002/AMG-Critical-Materials-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/383621/Aperam/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/16953/Arcadis/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/596722/Basic-Fit/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11762/Corbion/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600825744/CTP/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/12181/Eurocommercial-Properties/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/60194088/Fagron/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/612908/Flow-Traders/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11859/Fugro/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/60189120/Galapagos/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600825682/INPOST/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/386055/JDE-PEETS/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/561749/JUST-EAT-TAKEAWAY/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/524777/OCI/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11889/SBM-Offshore/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/596711/SIGNIFY-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11958/TKH-Group/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/97058/Van-Lanschot-Kempen-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/101431/Vopak-Koninklijke/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/60115830/WDP/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600324580/Avantium/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600825747/AZERION/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11816/BAM-Groep-Koninklijke/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11829/Brunel-International/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/613003/CMCOM/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600503149/FASTNED/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/596708/ForFarmers/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11881/HEIJMANS-KON/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11949/Kendrion/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11924/Nedap-NV/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/22987/NSI/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600825950/NX-FILTRATION/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/96535/Pharming-Group/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/25755/PostNL-Koninklijke/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600598926/RENEWI/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600259743/Sif-Holding/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11951/Sligro-Food-Group/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/600827415/THEON-INTERNAT/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/208564/TomTom/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/60124608/VASTNED/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/12218/Wereldhave/nieuws.aspx'
    'https://www.iex.nl/Aandeel-Koers/11804/ACOMO/nieuws.aspx'
]

def main():
    # List to store all company dataframes
    all_news = []
    
    # Scrape news for each company
    for url in stock_urls:
        company_name = get_company_name(url)
        print(f"Scraping news for {company_name}...")
        
        company_df = scrape_iex_news(url, company_name)
        if not company_df.empty:
            all_news.append(company_df)
            print(f"Found {len(company_df)} articles for {company_name}")
        else:
            print(f"No news found for {company_name}")
    
    # Combine all news into one dataframe
    if all_news:
        combined_df = pd.concat(all_news, ignore_index=True)
        
        # Save to Excel
        output_dir = r"C:\Users\Gebruiker\Downloads\R-Assignment\Scriptie"
        os.makedirs(output_dir, exist_ok=True)
        excel_path = os.path.join(output_dir, 'april.xlsx')
        combined_df.to_excel(excel_path, index=False, sheet_name='News')
        
        print(f"\nSaved {len(combined_df)} articles to {excel_path}")
    else:
        print("No news articles were found")

if __name__ == "__main__":
    main()


