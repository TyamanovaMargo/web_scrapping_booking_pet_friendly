import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def setup_driver():
    """Setup Chrome WebDriver with options"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except ImportError:
        driver = webdriver.Chrome(options=chrome_options)
        return driver

def scrape_booking_pet_friendly_camping(location="Israel", max_results=50):
    """
    Scrape pet-friendly camping sites from Booking.com
    
    Args:
        location (str): Location to search for (default: "Israel")
        max_results (int): Maximum number of results to collect
    
    Returns:
        list: List of dictionaries with camping site data
    """
    
    driver = setup_driver()
    campsites_data = []
    
    try:
        # Build search URL with filters
        base_url = "https://www.booking.com/searchresults.html"
        search_params = f"ss={location}&ht_id=204&pets=1&nflt=ht_id%3D204%3Bpets%3D1"
        search_url = f"{base_url}?{search_params}"
        
        print(f"🔍 Searching: {search_url}")
        driver.get(search_url)
        
        # Wait for results to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='property-card']"))
        )
        
        # Handle cookie banner if present
        try:
            cookie_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            cookie_button.click()
            time.sleep(2)
        except NoSuchElementException:
            pass
        
        # Get all property cards
        property_cards = driver.find_elements(By.CSS_SELECTOR, "[data-testid='property-card']")
        
        print(f"📊 Found {len(property_cards)} properties")
        
        for i, card in enumerate(property_cards[:max_results]):
            try:
                print(f"Processing property {i+1}/{min(len(property_cards), max_results)}...")
                
                # Extract name
                try:
                    name_element = card.find_element(By.CSS_SELECTOR, "[data-testid='title']")
                    name = name_element.text.strip()
                except NoSuchElementException:
                    name = "Unknown Campsite"
                
                # Extract URL
                try:
                    link_element = card.find_element(By.CSS_SELECTOR, "[data-testid='title-link']")
                    url = link_element.get_attribute('href')
                except NoSuchElementException:
                    try:
                        link_element = name_element.find_element(By.XPATH, ".//a")
                        url = link_element.get_attribute('href')
                    except:
                        url = "No URL available"
                
                # Extract location
                try:
                    location_element = card.find_element(By.CSS_SELECTOR, "[data-testid='address']")
                    location_text = location_element.text.strip()
                except NoSuchElementException:
                    location_text = location
                
                # Extract description
                try:
                    desc_elements = card.find_elements(By.CSS_SELECTOR, "[data-testid='property-card:property-description']")
                    if desc_elements:
                        description = desc_elements[0].text.strip()[:300] + "..."
                    else:
                        description = "Camping accommodation with pet-friendly facilities"
                except:
                    description = "Pet-friendly camping site"
                
                # Extract rating if available
                try:
                    rating_element = card.find_element(By.CSS_SELECTOR, "[data-testid='review-score']")
                    rating = rating_element.text.strip()
                except NoSuchElementException:
                    rating = "No rating"
                
                # Extract price if available
                try:
                    price_element = card.find_element(By.CSS_SELECTOR, "[data-testid='price-and-discounted-price']")
                    price = price_element.text.strip()
                except NoSuchElementException:
                    price = "Price on request"
                
                # Compile data
                campsite_data = {
                    'name': name,
                    'location': location_text,
                    'description': description,
                    'pet_policy': 'Pets allowed - Check property details for specific policies',
                    'rating': rating,
                    'price': price,
                    'url': url
                }
                
                campsites_data.append(campsite_data)
                print(f"✅ Collected: {name}")
                
            except Exception as e:
                print(f"❌ Error processing property {i+1}: {e}")
                continue
            
            # Respectful delay
            time.sleep(2)
        
        # Try to load more results if needed
        if len(campsites_data) < max_results:
            try:
                load_more_button = driver.find_element(By.CSS_SELECTOR, "[data-testid='search-results-load-more']")
                load_more_button.click()
                time.sleep(3)
                print("🔄 Loading more results...")
            except NoSuchElementException:
                print("📄 No more results to load")
                
    except TimeoutException:
        print("❌ Timeout: Page took too long to load")
    except Exception as e:
        print(f"❌ Error during scraping: {e}")
    finally:
        driver.quit()
    
    return campsites_data

def save_to_csv(data, filename='pet_friendly_camping_booking.csv'):
    """Save scraped data to CSV file"""
    if not data:
        print("❌ No data to save")
        return None
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')
    
    print(f"✅ Data saved to {filename}")
    print(f"📊 Total campsites: {len(data)}")
    print(f"📋 Columns: {list(df.columns)}")
    
    return df

def main():
    """Main scraper function"""
    print("🏕️ Pet-Friendly Camping Scraper for Booking.com")
    print("=" * 50)
    
    # Get user input
    location = input("Enter location to search (default: Israel): ").strip() or "Israel"
    max_results = input("Max results to collect (default: 20): ").strip()
    max_results = int(max_results) if max_results.isdigit() else 20
    
    print(f"🔍 Searching for pet-friendly camping in {location}...")
    
    # Scrape data
    campsites = scrape_booking_pet_friendly_camping(location, max_results)
    
    if campsites:
        # Save to CSV
        df = save_to_csv(campsites)
        
        # Display sample
        print("\n📋 Sample of collected data:")
        print(df[['name', 'location', 'rating']].head())
        
        print(f"\n🎉 Scraping completed successfully!")
        print(f"📁 File saved: pet_friendly_camping_booking.csv")
    else:
        print("❌ No data collected. Try adjusting search parameters.")

if __name__ == "__main__":
    main()
