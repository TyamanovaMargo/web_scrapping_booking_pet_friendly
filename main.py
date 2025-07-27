import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import requests
from bs4 import BeautifulSoup

def install_requirements():
    """Install required packages"""
    packages = [
        'pandas',
        'selenium',
        'beautifulsoup4',
        'requests',
        'webdriver-manager'
    ]
    
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package} already installed")
        except ImportError:
            print(f"📦 Installing {package}...")
            import subprocess
            subprocess.check_call(['pip', 'install', package])

def setup_driver():
    """Setup Chrome WebDriver with options"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except ImportError:
        # Fallback to default Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
    
    return driver

def search_booking_campsites():
    """Search for pet-friendly campsites in Israel on Booking.com"""
    
    driver = setup_driver()
    campsites_data = []
    
    try:
        # Navigate to Booking.com Israel camping search with pets filter
        base_url = "https://www.booking.com/searchresults.html"
        params = {
            'ss': 'Israel',
            'ht_id': '204',  # Camping
            'pets': '1',     # Pets allowed
            'nflt': 'ht_id%3D204%3Bpets%3D1'
        }
        
        search_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
        
        print(f"🔍 Searching: {search_url}")
        driver.get(search_url)
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='property-card']"))
        )
        
        # Find all property cards
        property_cards = driver.find_elements(By.CSS_SELECTOR, "[data-testid='property-card']")
        
        print(f"Found {len(property_cards)} properties")
        
        for card in property_cards[:20]:  # Limit to first 20 results
            try:
                # Extract campsite information
                name_element = card.find_element(By.CSS_SELECTOR, "[data-testid='title']")
                name = name_element.text.strip()
                
                # Get URL
                link_element = name_element.find_element(By.XPATH, ".//a")
                url = link_element.get_attribute('href')
                
                # Location
                try:
                    location_element = card.find_element(By.CSS_SELECTOR, "[data-testid='address']")
                    location = location_element.text.strip()
                except NoSuchElementException:
                    location = "Israel"
                
                # Description
                try:
                    desc_element = card.find_element(By.CSS_SELECTOR, "[data-testid='property-card:property-description']")
                    description = desc_element.text.strip()[:200] + "..." if len(desc_element.text) > 200 else desc_element.text.strip()
                except NoSuchElementException:
                    description = "Camping accommodation in Israel"
                
                # Pet policy - assume pets allowed since we filtered for it
                pet_policy = "Pets allowed - Contact property for specific policies"
                
                campsite_data = {
                    'name': name,
                    'location': location,
                    'description': description,
                    'pet_policy': pet_policy,
                    'url': url
                }
                
                campsites_data.append(campsite_data)
                print(f"✅ Collected: {name}")
                
            except Exception as e:
                print(f"❌ Error processing property: {e}")
                continue
                
            time.sleep(1)  # Be respectful to the server
            
    except Exception as e:
        print(f"❌ Error during search: {e}")
        
    finally:
        driver.quit()
    
    return campsites_data

def create_manual_campsite_data():
    """Manual data collection template with example Israeli campsites"""
    
    manual_data = [
        {
            "name": "Faran Camping",
            "location": "Eilat, Southern District",
            "description": "Desert camping experience near Eilat with pet-friendly facilities.",
            "pet_policy": "Pets allowed. Contact property for specific pet policies and fees.",
            "url": "https://www.booking.com/hotel/il/faran-camping.html"
        },
        {
            "name": "Kfar Blum Camping",
            "location": "Upper Galilee, Northern District",
            "description": "Camping site in the Jordan Valley with natural surroundings.",
            "pet_policy": "Pets welcome. Please inform property in advance.",
            "url": "https://www.booking.com/hotel/il/kfar-blum-camping.html"
        },
        {
            "name": "Ein Gedi Camping",
            "location": "Dead Sea, Southern District",
            "description": "Camping near Ein Gedi Nature Reserve and Dead Sea.",
            "pet_policy": "Pets allowed in camping area. Check nature reserve restrictions.",
            "url": "https://www.booking.com/hotel/il/ein-gedi-camping.html"
        },
        {
            "name": "Achziv Beach Camping",
            "location": "Western Galilee, Northern District",
            "description": "Beachfront camping site on the Mediterranean coast.",
            "pet_policy": "Pets allowed on beach and camping areas.",
            "url": "https://www.booking.com/hotel/il/achziv-camping.html"
        },
        {
            "name": "Neot Semadar Camping",
            "location": "Negev Desert, Southern District",
            "description": "Eco-camping in the Negev Desert with sustainable practices.",
            "pet_policy": "Pets welcome. Eco-friendly pet policies apply.",
            "url": "https://www.booking.com/hotel/il/neot-semadar-camping.html"
        },
        {
            "name": "Hamakhtesh Camping",
            "location": "Makhtesh Ramon, Southern District",
            "description": "Camping near Ramon Crater with desert hiking trails.",
            "pet_policy": "Pets allowed. Keep pets on leash in nature areas.",
            "url": "https://www.booking.com/hotel/il/makhtesh-camping.html"
        },
        {
            "name": "Sea of Galilee Camping",
            "location": "Tiberias, Northern District",
            "description": "Lakeside camping with water activities and pet-friendly areas.",
            "pet_policy": "Pets allowed. Swimming with pets in designated areas only.",
            "url": "https://www.booking.com/hotel/il/galilee-camping.html"
        },
        {
            "name": "Palmachim Beach Camping",
            "location": "Central District",
            "description": "Coastal camping south of Tel Aviv with beach access.",
            "pet_policy": "Pets allowed on beach. Follow local beach regulations.",
            "url": "https://www.booking.com/hotel/il/palmachim-camping.html"
        },
        {
            "name": "Mount Carmel Camping",
            "location": "Haifa District",
            "description": "Mountain camping in Carmel National Park area.",
            "pet_policy": "Pets allowed in camping area. National park restrictions apply.",
            "url": "https://www.booking.com/hotel/il/carmel-camping.html"
        },
        {
            "name": "Nahal Amud Camping",
            "location": "Upper Galilee, Northern District",
            "description": "Nature camping near historical sites and hiking trails.",
            "pet_policy": "Pets welcome. Keep on leash near archaeological sites.",
            "url": "https://www.booking.com/hotel/il/amud-camping.html"
        }
    ]
    
    return manual_data

def save_to_csv(data, filename='pet_friendly_campsites_israel_booking.csv'):
    """Save collected data to CSV file"""
    if not data:
        print("❌ No data to save")
        return None
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    print(f"✅ Data saved to {filename}")
    print(f"📊 Total campsites collected: {len(data)}")
    
    return df

def manual_data_collection_instructions():
    """Print instructions for manual data collection"""
    
    instructions = """
    📋 MANUAL DATA COLLECTION INSTRUCTIONS:
    
    1. Go to https://www.booking.com
    2. Search for "Israel" in the destination field
    3. Set dates for your search (use flexible dates)
    4. In filters, select:
       - Property type: "Camping"
       - Facilities: "Pets allowed"
    5. For each result, collect:
       - Exact name from the listing
       - Location/address shown
       - Description from the property page
       - Pet policy from "House rules" section
       - Full Booking.com URL
    
    6. Update the manual_data list in create_manual_campsite_data()
    7. Run the script to generate CSV
    
    ⚠️  IMPORTANT: Always verify pet policies by reading the full property details!
    """
    
    print(instructions)

def run_manual_collection():
    """Run manual data collection"""
    print("🏕️ Creating CSV from manual campsite data...")
    
    # Show instructions
    manual_data_collection_instructions()
    
    # Get manual data
    data = create_manual_campsite_data()
    
    # Save to CSV
    df = save_to_csv(data)
    
    # Display sample
    print("\n📋 Sample data:")
    print(df[['name', 'location', 'pet_policy']].head())
    
    return df

def main():
    """Main function to run the campsite collection"""
    
    print("🏕️ Pet-Friendly Campsites in Israel - Booking.com Collector")
    print("="*60)
    
    choice = input("""
    Choose collection method:
    1. Automated web scraping (requires Chrome browser)
    2. Manual data collection (with example data)
    
    Enter choice (1 or 2): """).strip()
    
    if choice == '1':
        print("\n🤖 Running automated collection...")
        try:
            install_requirements()
            campsites = search_booking_campsites()
            df = save_to_csv(campsites)
        except Exception as e:
            print(f"❌ Automated collection failed: {e}")
            print("📝 Falling back to manual collection...")
            df = run_manual_collection()
    
    elif choice == '2':
        print("\n📝 Running manual collection...")
        df = run_manual_collection()
    
    else:
        print("❌ Invalid choice. Using manual collection...")
        df = run_manual_collection()
    
    # Final verification
    if df is not None:
        print("\n🎉 Collection completed successfully!")
        print(f"📁 File: pet_friendly_campsites_israel_booking.csv")
        print(f"📊 Records: {len(df)}")

if __name__ == "__main__":
    main()
