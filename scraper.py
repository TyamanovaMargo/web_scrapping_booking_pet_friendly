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
    # Убираем headless чтобы видеть что происходит
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
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

def simple_pet_check(driver, url, property_name):
    """
    Упрощенная проверка - ищем любые упоминания о животных
    """
    try:
        print(f"   🔍 Checking: {property_name}")
        driver.get(url)
        time.sleep(3)
        
        # Получаем текст страницы
        page_text = driver.page_source.lower()
        
        # Упрощенная проверка - если есть слово pets/animals и нет явного запрета
        has_pet_mention = any(word in page_text for word in [
            'pet', 'dog', 'cat', 'animal', 'puppy', 'kitten'
        ])
        
        has_explicit_ban = any(phrase in page_text for phrase in [
            'no pets', 'pets not allowed', 'no animals'
        ])
        
        print(f"      Pet mention: {has_pet_mention}")
        print(f"      Explicit ban: {has_explicit_ban}")
        
        # Простая логика: если есть упоминание и нет запрета - считаем подходящим
        if has_pet_mention and not has_explicit_ban:
            return True, "Pets likely allowed"
        elif has_explicit_ban:
            return False, "Pets explicitly banned"
        else:
            return False, "No pet policy found"
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False, f"Error: {e}"

def scrape_any_pet_friendly_accommodation():
    """
    Упрощенный скрапер - ищем любые объекты размещения с животными
    """
    
    driver = setup_driver()
    found_places = []
    
    try:
        # Простой поиск по Израилю с pet фильтром
        search_url = "https://www.booking.com/searchresults.html?ss=Israel&pets=1"
        
        print(f"🔍 Searching: {search_url}")
        driver.get(search_url)
        time.sleep(5)
        
        # Handle cookies
        try:
            cookie_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
            time.sleep(2)
        except:
            pass
        
        # Ищем любые карточки объектов
        property_selectors = [
            "[data-testid='property-card']",
            ".sr_property_block",
            ".sr_item"
        ]
        
        properties = []
        for selector in property_selectors:
            properties = driver.find_elements(By.CSS_SELECTOR, selector)
            if properties:
                print(f"✅ Found {len(properties)} properties with selector: {selector}")
                break
        
        if not properties:
            print("❌ No properties found with any selector")
            # Попробуем посмотреть что вообще есть на странице
            print("Page title:", driver.title)
            print("Current URL:", driver.current_url)
            return []
        
        # Берем первые 10 для проверки
        for i, card in enumerate(properties[:10]):
            try:
                print(f"\n[{i+1}/10] Processing property...")
                
                # Ищем название
                name = "Unknown Property"
                name_selectors = [
                    "[data-testid='title']",
                    "h3 a span",
                    ".sr-hotel__name",
                    "h3"
                ]
                
                for selector in name_selectors:
                    try:
                        name_element = card.find_element(By.CSS_SELECTOR, selector)
                        name = name_element.text.strip()
                        if name and len(name) > 3:
                            break
                    except:
                        continue
                
                print(f"   Name: {name}")
                
                # Ищем URL
                url = ""
                url_selectors = [
                    "a[href*='hotel']",
                    "h3 a", 
                    "a"
                ]
                
                for selector in url_selectors:
                    try:
                        link_element = card.find_element(By.CSS_SELECTOR, selector)
                        url = link_element.get_attribute('href')
                        if url and 'booking.com' in url:
                            break
                    except:
                        continue
                
                if not url:
                    print(f"   ⚠️ No URL found")
                    continue
                
                print(f"   URL: {url[:50]}...")
                
                # Простая проверка
                is_pet_friendly, reason = simple_pet_check(driver, url, name)
                
                if is_pet_friendly:
                    # Возвращаемся к списку
                    driver.back()
                    time.sleep(2)
                    
                    property_data = {
                        'name': name,
                        'location': 'Israel',
                        'description': 'Pet-friendly accommodation in Israel',
                        'pet_policy': reason,
                        'rating': 'Check on site',
                        'price': 'Check on site',
                        'url': url
                    }
                    
                    found_places.append(property_data)
                    print(f"   ✅ ADDED: {name}")
                else:
                    print(f"   ❌ REJECTED: {reason}")
                    # Возвращаемся к списку
                    driver.back()
                    time.sleep(2)
                
            except Exception as e:
                print(f"   ❌ Error processing property {i+1}: {e}")
                continue
        
    except Exception as e:
        print(f"❌ Main error: {e}")
    finally:
        driver.quit()
    
    return found_places

def main():
    """Упрощенная главная функция"""
    print("🏕️ SIMPLIFIED Pet-Friendly Accommodation Finder")
    print("=" * 50)
    
    print("🔍 Looking for ANY pet-friendly places in Israel...")
    print("⚠️ Browser will be visible for debugging")
    
    # Запускаем поиск
    places = scrape_any_pet_friendly_accommodation()
    
    if places:
        # Сохраняем
        df = pd.DataFrame(places)
        df.to_csv('simple_pet_friendly_israel.csv', index=False, encoding='utf-8')
        
        print(f"\n🎉 SUCCESS! Found {len(places)} places:")
        for i, place in enumerate(places, 1):
            print(f"{i}. {place['name']}")
        
        print(f"\n📁 Saved to: simple_pet_friendly_israel.csv")
    else:
        print("\n❌ No places found. Possible issues:")
        print("1. Booking.com changed their structure")
        print("2. No pet-friendly places in Israel")
        print("3. Geo-blocking or captcha")
        print("\n💡 Try running without --headless to see what's happening")

if __name__ == "__main__":
    main()

