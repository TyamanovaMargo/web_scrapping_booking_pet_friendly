На основе упрощённой версии веб-скрапера, вот обновлённый README.md:

```markdown
# Pet-Friendly Camping Scraper - Booking.com

A simple Python web scraper to find pet-friendly camping sites on Booking.com and save results to CSV.

## 🎯 Project Overview

This tool automatically searches Booking.com for camping accommodations that allow pets in any location worldwide, extracts detailed information, and saves it to a CSV file for easy analysis.

## ✨ Features

- **Automated Web Scraping**: Uses Selenium to search Booking.com directly
- **Pet-Friendly Filter**: Only collects campsites that explicitly allow pets
- **Flexible Location Search**: Search any country or region, not just Israel
- **Comprehensive Data**: Extracts name, location, description, rating, price, and URL
- **CSV Export**: Saves all data in structured CSV format
- **Interactive Interface**: User-friendly prompts for location and result limits
- **Error Handling**: Robust handling of missing elements and timeouts

## 🛠️ Requirements

### System Requirements
- Python 3.7+
- Google Chrome browser
- Internet connection

### Dependencies
```
pip install pandas selenium webdriver-manager
```

## 🚀 Quick Start

### 1. Installation
```
# Clone or download the project
git clone https://github.com/yourusername/pet-friendly-camping-scraper.git
cd pet-friendly-camping-scraper

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Scraper
```
python scraper.py
```

### 3. Interactive Setup
The scraper will prompt you for:
- **Location**: Enter any location (e.g., "Israel", "Italy", "California")
- **Max Results**: Number of campsites to collect (default: 20)

## 📊 Output Data

The scraper generates a CSV file with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `name` | Campsite name | "Desert Oasis Camping" |
| `location` | Full location/address | "Eilat, Southern District" |
| `description` | Property description | "Family-friendly desert camping..." |
| `pet_policy` | Pet policy info | "Pets allowed - Check property details" |
| `rating` | Guest rating | "8.5" |
| `price` | Price information | "From $45/night" |
| `url` | Direct Booking.com link | "https://www.booking.com/..." |

## 💻 Usage Examples

### Basic Usage
```
python scraper.py
# Enter: Italy
# Enter: 30
```

### Programmatic Usage
```
from scraper import scrape_booking_pet_friendly_camping, save_to_csv

# Scrape data
campsites = scrape_booking_pet_friendly_camping("France", max_results=25)

# Save to CSV
df = save_to_csv(campsites, "france_pet_camping.csv")

print(f"Collected {len(campsites)} pet-friendly campsites")
```

## 🔧 Configuration

### Chrome Options
The scraper runs in headless mode by default. To see the browser:
```
# In setup_driver() function, comment out:
# chrome_options.add_argument("--headless")
```

### Search Parameters
- **Location**: Any country, region, or city
- **Max Results**: Adjust based on your needs (default: 20)
- **Delay**: 2-second delay between requests (respectful scraping)

## 📈 Sample Output

```
name,location,description,pet_policy,rating,price,url
Faran Camping,Eilat Israel,Desert camping near Red Sea,Pets allowed - Check details,8.2,From $35/night,https://booking.com/...
Mountain View Camp,Galilee Israel,Scenic camping in nature,Pets welcome with advance notice,9.1,From $42/night,https://booking.com/...
```

## 🛡️ Error Handling

The scraper includes:
- **Timeout Protection**: 15-second wait for page loads
- **Missing Element Handling**: Graceful handling of incomplete data
- **Cookie Consent**: Automatic handling of cookie banners
- **Rate Limiting**: Respectful 2-second delays between requests

## 🔍 Troubleshooting

### Common Issues

**ChromeDriver Not Found:**
```
# The script auto-downloads ChromeDriver, but if it fails:
pip install webdriver-manager --upgrade
```

**No Results Found:**
- Check your internet connection
- Try a different location (e.g., "France" instead of "Paris")
- Verify Booking.com is accessible in your region

**Timeout Errors:**
- Increase timeout in the script (line with `WebDriverWait(driver, 15)`)
- Check if your internet connection is stable

## ⚠️ Important Notes

- **Respect Terms of Service**: This tool is for educational/research purposes
- **Rate Limiting**: Built-in delays to be respectful to Booking.com servers
- **Data Accuracy**: Always verify pet policies directly with properties
- **Regional Variations**: Results may vary by location and booking policies

## 📝 Project Structure

```
pet-friendly-camping-scraper/
├── scraper.py           # Main scraper script
├── requirements.txt     # Python dependencies
├── README.md           # This documentation
└── pet_friendly_camping_booking.csv  # Output file (generated)
```

## 🎯 Use Cases

- **Trip Planning**: Find pet-friendly camping for vacations
- **Research**: Analyze pet-friendly accommodation availability
- **Business Intelligence**: Market research for pet travel industry
- **Personal Database**: Build your own list of verified pet-friendly camps

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make improvements (better error handling, additional data fields, etc.)
4. Submit a pull request

## 📄 License

This project is for educational and research purposes. Please respect Booking.com's terms of service.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure all dependencies are installed correctly
3. Verify Chrome browser is installed and updated
4. Try running with a different location

## 🎉 Success Metrics

After running the scraper, you should have:
- ✅ CSV file with pet-friendly camping data
- ✅ Valid Booking.com URLs for each property
- ✅ Complete property information (name, location, rating, etc.)
- ✅ Ready-to-use data for trip planning

---

**Happy Pet-Friendly Camping! 🏕️🐕**

## 📊 Status

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.0+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
```

