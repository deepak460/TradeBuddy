import json

def filter_stocks(json_data, fno_200_symbols):
    # Filter for stocks that are in the FNO 200 list.
    fno_200_stocks = [stock for stock in json_data if stock['symbol'] in fno_200_symbols]
    return fno_200_stocks

def load_data(filepath):
    # Load JSON data from a file.
    with open(filepath, 'r') as file:
        return json.load(file)

def save_data(filepath, data):
    # Save data to a JSON file.
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
if __name__ == "__main__":
    # Load the original JSON data
    data = load_data('C:/Users/celeb/Desktop/angelone-api/OpenAPIScripMaster.json')

    # Define your FNO 200 stock symbols
    fno_200_symbols = ["ABB-EQ", "ACC-EQ", "AARTIIND-EQ", "ABBOTINDIA-EQ", "ADANIENT-EQ", "AUBANK-EQ", "ADANIPORTS-EQ", "ABCAPITAL-EQ", "AMBUJACEM-EQ", "ABFRL-EQ", "ALKEM-EQ", "APOLLOHOSP-EQ", "APOLLOTYRE-EQ", "ASHOKLEY-EQ", "ASIANPAINT-EQ", "ASTRAL-EQ", "ATUL-EQ", "AUROPHARMA-EQ", "AXISBANK-EQ", "BSOFT-EQ", "BAJAJ-AUTO-EQ", "BAJFINANCE-EQ", "BAJAJFINSV-EQ", "BALKRISIND-EQ", "BALAMINES-EQ", "BALRAMCHIN-EQ", "BANDHANBNK-EQ", "BANKBARODA-EQ", "BATAINDIA-EQ", "BERGEPAINT-EQ", "BEL-EQ", "BHARATFORG-EQ", "BHEL-EQ", "BHARTIARTL-EQ", "BIOCON-EQ", "BOSCHLTD-EQ", "BRITANNIA-EQ", "CANFINHOME-EQ", "CANBK-EQ", "CHAMBLFERT-EQ", "CHOLAFIN-EQ", "CIPLA-EQ", "CUB-EQ", "COALINDIA-EQ", "COFORGE-EQ", "COLPAL-EQ", "CONCOR-EQ", "COROMANDEL-EQ", "CROMPTON-EQ", "CUMMINSIND-EQ","DLF-EQ", "DABUR-EQ", "DALBHARAT-EQ", "DEEPAKNTR-EQ", "DIVISLAB-EQ", "DIXON-EQ", "LALPATHLAB-EQ", "DRREDDY-EQ", "EICHERMOT-EQ", "ESCORTS-EQ", "EXIDEIND-EQ", "GAIL-EQ", "GMRINFRA-EQ", "GLENMARK-EQ", "GODREJCP-EQ", "GODREJPROP-EQ", "GRANULES-EQ", "GRASIM-EQ", "GUJGASLTD-EQ", "GNFC-EQ", "HCLTECH-EQ", "HDFCAMC-EQ", "HDFCBANK-EQ", "HDFCLIFE-EQ", "HAVELLS-EQ", "HINDPETRO-EQ", "HEROMOTOCO-EQ", "HINDALCO-EQ", "HAL-EQ", "HINDCOPPER-EQ", "HINDUNILVR-EQ", "ICICIBANK-EQ", "ICICIGI-EQ", "ICICIPRULI-EQ", "IDEC-EQ", "IDFCFIRSTB-EQ", "IPCALAB-EQ", "ITC-EQ", "INDIAMART-EQ", "IEX-EQ", "IOC-EQ", "IRCTC-EQ", "IGL-EQ", "INDUSTOWER-EQ", "INDUSINDBK-EQ", "NAUKRI-EQ", "INFY-EQ", "INDIGO-EQ", "JKCEMENT-EQ", "JSWSTEEL-EQ", "JINDALSTEL-EQ", "JUBLFOOD-EQ", "KOTAKBANK-EQ", "LTTS-EQ", "LICHSGFIN-EQ", "LTIM-EQ", "LT-EQ", "LAURUSLABS-EQ", "LUPIN-EQ", "MRF-EQ", "MGL-EQ", "M&MFIN-EQ", "M&M-EQ", "MANAPPURAM-EQ", "MARICO-EQ", "MARUTI-EQ", "MFSL-EQ", "METROPOLIS-EQ", "MPHASIS-EQ", "MCX-EQ", "MUTHOOTFIN-EQ", "NMDC-EQ", "NTPC-EQ", "NATIONALIJM-EQ", "NAVINFLUOR-EQ", "NESTLEIND-EQ", "OBEROIRLTY-EQ", "ONGC-EQ", "OFSS-EQ", "PIIND-EQ", "PVRINOX-EQ", "PAGEIND-EQ", "PERSISTENT-EQ", "PETRONET-EQ", "PIDILITIND-EQ", "PEL-EQ", "POLYCAB-EQ", "PFC-EQ", "POWERGRID-EQ", "PNB-EQ", "RBLBANK-EQ", "RECLTD-EQ", "RELIANCE-EQ", "SBICARD-EQ", "SBILIFE-EQ", "SHREECEM-EQ", "SRF-EQ", "MOTHERSON-EQ", "SHRIRAMFIN-EQ", "SIEMENS-EQ", "SBIN-EQ", "SAIL-EQ", "SUNPHARMA-EQ", "SUNTV-EQ", "SYNGENE-EQ", "TATACONSUM-EQ", "TVSMOTOR-EQ", "TATACHEM-EQ", "TATACOMM-EQ", "TCS-EQ", "TATAMOTORS-EQ", "TATAPOWER-EQ", "TATASTEEL-EQ", "TECHM-EQ", "FEDERALBNK-EQ", "INDIACEM-EQ", "INDHOTEL-EQ", "RAMCOCEM-EQ", "TITAN-EQ", "TORNTPHARM-EQ", "TRENT-EQ", "UPL-EQ", "ULTRACEMCO-EQ", "UBL-EQ", "MCDOWELL-N-EQ", "VEDL-EQ", "VOLTAS-EQ", "WIPRO-EQ", "ZEEL-EQ", "ZYDUSLIFE-EQ"]

    # Filter out FNO 200 stocks
    fno_200_data = filter_stocks(data, fno_200_symbols)

    # Save the filtered data to a new JSON file
    save_data('fno_200_stocks.json', fno_200_data)
    print("Filtered FNO 200 stocks data saved to 'fno_200_stocks.json'.")
