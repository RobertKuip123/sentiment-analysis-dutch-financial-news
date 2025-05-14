#First scraping news articles
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import os

def scrape_company(url):
    """Extract financial news for a given company page"""
    company = url.split('/')[-2].replace('-', ' ') if '/nieuws.aspx' in url else url.split('/')[-1].replace('.aspx', '').replace('-', ' ')
    
    headers = {'User-Agent': 'Research Bot (r.kuipers@student.com)'}
    
    try:
        time.sleep(1.2)  # Slightly random delay to avoid detection
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # Extract news elements
        headlines = soup.find_all('a', id=lambda x: x and 'linkTitle' in x)
        sublines = soup.find_all('a', id=lambda x: x and 'linkIntro' in x)
        dates = soup.find_all('time', class_='previewlist__date')
        
        # Process matching news items
        data = []
        for h, s, d in zip(headlines, sublines, dates):
            if not (d and 'datetime' in d.attrs):
                continue
                
            try:
                date_parsed = datetime.strptime(d['datetime'], '%Y-%m-%d %H:%M')
                data.append({
                    'Company': company,
                    'Date': date_parsed.strftime('%Y-%m-%d %H:%M'),
                    'Headline': h.text.strip(),
                    'Subline': s.text.strip()
                })
            except ValueError:
                pass
                
        result = pd.DataFrame(data)
        print(f"✓ {company}: found {len(result)} articles")
        return result
        
    except Exception as e:
        print(f"✗ {company}: {str(e)}")
        return pd.DataFrame()

# List of AEX stocks to scrape
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
    'https://www.iex.nl/Aandeel-Koers/12218/Wereldhave/nieuws.aspx',
    'https://www.iex.nl/Aandeel-Koers/11804/ACOMO/nieuws.aspx'
]

def main():
    results = []
    
    for url in stock_urls:
        df = scrape_company(url)
        if not df.empty:
            results.append(df)
    
    if not results:
        print("No articles found")
        return
        
    # Combine and save data
    all_articles = pd.concat(results, ignore_index=True)
    
    output_dir = r"C:\Users\Gebruiker\Downloads\ScriptieDS"
    os.makedirs(output_dir, exist_ok=True)
    
    filepath = os.path.join(output_dir, 'NewsArticles.xlsx')
    all_articles.to_excel(filepath, index=False)
    
    print(f"\nSaved {len(all_articles)} articles to {filepath}")

if __name__ == "__main__":
    main()

#Matching the tickers so stock prices can be retrieved from yahoo.

# Data file location - adjust based on where I saved the news data
NEWS_FILE = r'C:\Users\Gebruiker\Downloads\ScriptieDS\NewsArticles.xlsx'

# Load my scraped news articles
print("Loading news data...")
news = pd.read_excel(NEWS_FILE)

# company names lowercase
news['Company'] = news['Company'].str.lower()

# Here correct company is matched with correct yahoo finance company ticker
AEX_TICKERS = {
    "umg": "UMG.AS",
    "unilever plc": "UNA.AS",
    "wolters kluwer": "WKL.AS",
    "abn amro bank nv": "ABN.AS",
    "air france klm": "AF.PA",
    "adyen nv": "ADYEN.AS",
    "aegon": "AGN.AS",
    "allfunds group": "ALLFG.AS",
    "ahold delhaize koninklijke": "AD.AS",
    "akzo nobel": "AKZA.AS",
    "asm international": "ASM.AS",
    "asml holding": "ASML.AS",
    "asr nederland": "ASRNL.AS",
    "be semiconductor industries": "BESI.AS",
    "dsm firmenich ag": "DSFIR.AS",
    "exor nv": "EXO.AS",
    "heineken": "HEIA.AS",
    "imcd": "IMCD.AS",
    "ing groep": "INGA.AS",
    "kpn koninklijke": "KPN.AS",
    "nn group": "NN.AS",
    "philips koninklijke": "PHIA.AS",
    "prosus": "PRX.AS",
    "randstad nv": "RAND.AS",
    "relx": "REN.AS",
    "shell plc": "SHELL.AS",
    "aalberts nv": "AALB.AS",
    "alfen nv": "ALFEN.AS",
    "amg critical materials nv": "AMG.AS",
    "aperam": "APAM.AS",
    "arcadis": "ARCAD.AS",
    "arcelormittal": "MT.AS",
    "basic fit": "BFIT.AS",
    "accsys technologies": "AXS.AS",
    "bs group sa": "BSGR.AS",
    "acomo": "ACOMO.AS",
    "corbion": "CRBN.AS",
    "ctp": "CTPNV.AS",
    "eurocommercial properties": "ECMPA.AS",
    "fagron": "FAGR.AS",
    "flow traders": "FLOW.AS",
    "fugro": "FUR.AS",
    "galapagos": "GLPG.AS",
    "inpost": "INPST.AS",
    "jde peets": "JDEP.AS",
    "just eat takeaway": "TKWY.AS",
    "oci": "OCI.AS",
    "sbm offshore": "SBMO.AS",
    "signify nv": "LIGHT.AS",
    "tkh group": "TWEKA.AS",
    "van lanschot kempen nv": "VLK.AS",
    "vopak koninklijke": "VPK.AS",
    "wdp": "WDP.BR",
    "avantium": "AVTX.AS",
    "azerion": "AZRN.AS",
    "bam groep koninklijke": "BAMNB.AS",
    "brunel international": "BRNL.AS",
    "fastned": "FAST.AS",
    "forfarmers": "FFARM.AS",
    "heijmans kon": "HEIJM.AS",
    "cmcom": "CMCOM.AS",
    "kendrion": "KENDR.AS",
    "nedap nv": "NEDAP.AS",
    "nsi": "NSI.AS",
    "nx filtration": "NXFIL.AS",
    "pharming group": "PHARM.AS",
    "postnl koninklijke": "PNL.AS",
    "renewi": "RWI.AS",
    "sif holding": "SIFG.AS",
    "sligro food group": "SLIGR.AS",
    "theon internat": "THEON.AS",
    "tomtom": "TOM2.AS",
    "vastned": "VASTN.AS",
    "wereldhave": "WHA.AS"
}

# Apply ticker mapping
missing_tickers = 0
found_tickers = 0

news['Ticker'] = None  # Initialize column
for idx, row in news.iterrows():
    company = row['Company']
    if company in AEX_TICKERS:
        news.at[idx, 'Ticker'] = AEX_TICKERS[company]
        found_tickers += 1
    else:
        missing_tickers += 1

# Saving results
out_dir = r"C:\Users\Gebruiker\Downloads\ScriptieDS"
os.makedirs(out_dir, exist_ok=True)
output_file = os.path.join(out_dir, "NewsWithTickers.xlsx")
news.to_excel(output_file, index=False)

print(f"Data saved to: {output_file}")
print(f"Processing time: {time() - start:.2f} seconds")


#NOW STOCK RETURNS ARE RETRIEVED THROUGH YAHOO FINANCE. 1. 3-day excess return, we only find aex returns for aex stpcls.
#2. One-day post return for portfolio strategy
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, time, timedelta
import os

## Input/Output file paths
NEWS_FILE = r"C:\Users\Gebruiker\Downloads\ScriptieDS\NewsWithTickers.xlsx"
OUTPUT_FILE = r"C:\Users\Gebruiker\Downloads\ScriptieDS\NewsWithReturns.xlsx"

## Load and prepare data
print("Loading news data...")
df = pd.read_excel(NEWS_FILE)
df['Date'] = pd.to_datetime(df['Date'])

## Define Dutch holidays
HOLIDAYS = [
    # 2024
    '2024-01-01', '2024-03-29', '2024-04-01', '2024-12-25', '2024-12-26',
    # 2025
    '2025-01-01', '2025-04-18'
]

## Helper functions for dates
def is_weekend(date):
    return date.weekday() >= 5  # 5=Saturday, 6=Sunday

def next_trading_day(date):
    next_day = date + timedelta(days=1)
    while is_weekend(next_day) or next_day.strftime('%Y-%m-%d') in HOLIDAYS:
        next_day += timedelta(days=1)
    return next_day

def previous_trading_day(date):
    prev_day = date - timedelta(days=1)
    while is_weekend(prev_day) or prev_day.strftime('%Y-%m-%d') in HOLIDAYS:
        prev_day -= timedelta(days=1)
    return prev_day

def add_trading_days(date, days):
    curr_day = date
    for _ in range(days):
        curr_day = next_trading_day(curr_day)
    return curr_day

## News classification
def classify_news(row):
    date = row['Date']
    
    # Weekend check
    if date.weekday() >= 5:
        return 'Weekend'
    
    # Holiday or normal day check
    is_holiday = date.strftime('%Y-%m-%d') in HOLIDAYS
    
    # Time-based classification
    if date.time() < time(9, 1):
        return 'Overnightmorning'
    elif date.time() >= time(17, 30):
        return 'Overnightevening'
    else:
        return 'Intraday'

## Stock price retrieval functions
def get_stock_data(ticker_obj, date, days_forward=0, days_backward=0):
    """Get stock data for specific date ranges"""
    try:
        start_date = date - timedelta(days=max(10, days_backward))  
        end_date = date + timedelta(days=max(10, days_forward))  
        
        # Fetch data
        hist = ticker_obj.history(start=start_date, end=end_date)
        if hist.empty:
            return None
        
        # Get closest available dates
        dates = hist.index.sort_values()
        
        # Find closest date >= our target date
        target_idx = None
        for i, d in enumerate(dates):
            if d.date() >= date.date():
                target_idx = i
                break
        
        if target_idx is None:
            return None
            
        return hist
        
    except Exception as e:
        print(f"Error getting data: {str(e)[:50]}...")
        return None

## Main processing function
def calculate_returns():
    # Add news type
    df['Type'] = df.apply(classify_news, axis=1)
    
    # Initialize return columns
    df['1D_Return'] = None
    df['3D_Return'] = None
    df['Index_3D_Return'] = None
    df['Abnormal_3D_Return'] = None
    
    # Process each ticker
    for ticker, group in df.groupby('Ticker'):
        if pd.isna(ticker) or not ticker:
            continue
            
        print(f"Processing {ticker}...")
        ticker_obj = yf.Ticker(ticker)
        
        for idx, row in group.iterrows():
            try:
                date = row['Date']
                news_type = row['Type']
                
                ## 1-Day Return calculation
                if news_type == 'Overnightmorning':
                    # Same day open to close
                    hist = get_stock_data(ticker_obj, date)
                    if hist is not None and len(hist) > 0:
                        date_idx = hist.index[hist.index.date == date.date()]
                        if len(date_idx) > 0:
                            start_price = hist.loc[date_idx[0], 'Open']
                            end_price = hist.loc[date_idx[0], 'Close']
                            df.at[idx, '1D_Return'] = ((end_price - start_price) / start_price) * 100
                
                elif news_type == 'Intraday':
                    # Current day close to next day close
                    hist = get_stock_data(ticker_obj, date, days_forward=5)
                    if hist is not None and len(hist) > 1:
                        date_idx = hist.index[hist.index.date == date.date()]
                        if len(date_idx) > 0:
                            current_date = date_idx[0]
                            next_dates = hist.index[hist.index > current_date]
                            if len(next_dates) > 0:
                                next_date = next_dates[0]
                                start_price = hist.loc[current_date, 'Close']
                                end_price = hist.loc[next_date, 'Close']
                                df.at[idx, '1D_Return'] = ((end_price - start_price) / start_price) * 100
                
                elif news_type in ['Overnightevening', 'Weekend']:
                    # Next day open to close
                    next_date = next_trading_day(date)
                    hist = get_stock_data(ticker_obj, next_date)
                    if hist is not None and len(hist) > 0:
                        next_idx = hist.index[hist.index.date == next_date.date()]
                        if len(next_idx) > 0:
                            start_price = hist.loc[next_idx[0], 'Open']
                            end_price = hist.loc[next_idx[0], 'Close']
                            df.at[idx, '1D_Return'] = ((end_price - start_price) / start_price) * 100
                
                ## 3-Day Return calculation
                if news_type == 'Weekend':
                    # Find previous Friday
                    start_date = date
                    while start_date.weekday() != 4:  # 4 = Friday
                        start_date -= timedelta(days=1)
                    
                    # First trading day after weekend
                    end_date = date
                    while is_weekend(end_date):
                        end_date += timedelta(days=1)
                    
                    # Add two more trading days
                    end_date = add_trading_days(end_date, 2)
                
                elif news_type == 'Overnightevening':
                    start_date = date
                    next_day = next_trading_day(date)
                    end_date = add_trading_days(next_day, 2)
                
                else:  # Morning or Intraday
                    start_date = previous_trading_day(date)
                    end_date = add_trading_days(date, 2)
                
                # Get stock 3-day return
                start_hist = get_stock_data(ticker_obj, start_date)
                end_hist = get_stock_data(ticker_obj, end_date)
                
                if start_hist is not None and end_hist is not None:
                    start_dates = start_hist.index[start_hist.index.date <= start_date.date()]
                    end_dates = end_hist.index[end_hist.index.date >= end_date.date()]
                    
                    if len(start_dates) > 0 and len(end_dates) > 0:
                        start_price = start_hist.loc[start_dates[-1], 'Close']
                        end_price = end_hist.loc[end_dates[0], 'Close']
                        df.at[idx, '3D_Return'] = ((end_price - start_price) / start_price) * 100
                
                ## Index Return calculation (AEX)
                index_obj = yf.Ticker('^AEX')
                start_hist = get_stock_data(index_obj, start_date)
                end_hist = get_stock_data(index_obj, end_date)
                
                if start_hist is not None and end_hist is not None and not pd.isna(df.at[idx, '3D_Return']):
                    start_dates = start_hist.index[start_hist.index.date <= start_date.date()]
                    end_dates = end_hist.index[end_hist.index.date >= end_date.date()]
                    
                    if len(start_dates) > 0 and len(end_dates) > 0:
                        start_price = start_hist.loc[start_dates[-1], 'Close']
                        end_price = end_hist.loc[end_dates[0], 'Close']
                        df.at[idx, 'Index_3D_Return'] = ((end_price - start_price) / start_price) * 100
                        
                        # Calculate abnormal return
                        df.at[idx, 'Abnormal_3D_Return'] = df.at[idx, '3D_Return'] - df.at[idx, 'Index_3D_Return']
            
            except Exception as e:
                # Just continue with next row
                continue
    
    return df

## Main execution
df = calculate_returns()

# Save results
print(f"\nSaving results to {OUTPUT_FILE}")
df.to_excel(OUTPUT_FILE, index=False)
print("Done!")

#MANUALLY sentiment in excel is set based on abnormal return. Next manually, the index returns for ascx is set by downloading in euronext ASCX movements, as this can not be retrieved with yahoo finance ticker. 
