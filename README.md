Вот README.md переписанный в одном блоке с правильным markdown форматированием:

```markdown
# Pet-Friendly Campsites in Israel - Booking.com Collector

A Python project to automatically collect information about pet-friendly camping sites in Israel from Booking.com and save the results in a structured CSV file.

## 🎯 Project Overview

This tool searches Booking.com for campsites and camping accommodations in Israel that explicitly allow pets, extracts relevant information, and saves it to a CSV file for easy analysis and reference.

## 📋 Features

- **Automated Web Scraping**: Uses Selenium WebDriver to automatically search and extract data
- **Manual Collection Option**: Fallback method with example data and clear instructions
- **Pet-Friendly Focus**: Only collects campsites that explicitly allow pets
- **Structured Output**: Saves data in CSV format with standardized columns
- **Error Handling**: Robust error handling and fallback options
- **User-Friendly**: Interactive menu system for easy operation

## 🛠️ Requirements

### System Requirements
- Python 3.7+
- Chrome browser (for automated scraping)
- Internet connection

### Python Packages
```
pip install -r requirements.txt
```

## 🚀 Installation

1. **Clone the repository**
```
git clone https://github.com/yourusername/pet-friendly-campsites-israel.git
cd pet-friendly-campsites-israel
```

2. **Create virtual environment (recommended)**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

## 📁 Project Structure

```
pet-friendly-campsites-israel/
│
├── main.py                    # Main execution script
├── requirements.txt           # Python dependencies
├── requirements-dev.txt       # Development dependencies
├── README.md                 # This file
├── .gitignore                # Git ignore rules
│
├── data/
│   └── pet_friendly_campsites_israel_booking.csv  # Output file
│
└── docs/
    └── manual_collection_guide.md  # Manual collection instructions
```

## 🚀 Quick Start

### Option 1: Automated Collection

```
python main.py
# Choose option 1 when prompted
```

### Option 2: Manual Collection

```
python main.py
# Choose option 2 when prompted
```

## 📊 Output Format

The tool generates a CSV file with the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `name` | Campsite name | "Faran Camping" |
| `location` | Location/Region | "Eilat, Southern District" |
| `description` | Brief description | "Desert camping experience near Eilat..." |
| `pet_policy` | Pet policy details | "Pets allowed. Contact property for policies." |
| `url` | Booking.com URL | "https://www.booking.com/hotel/il/..." |

## 💻 Usage Examples

### Basic Usage
```
from main import search_booking_campsites, save_to_csv

# Automated collection
campsites = search_booking_campsites()
df = save_to_csv(campsites)

print(f"Collected {len(df)} pet-friendly campsites")
```

### Manual Data Addition
```
# Add your own campsite data
new_campsite = {
    "name": "My Campsite",
    "location": "Tel Aviv, Central District", 
    "description": "Great camping spot",
    "pet_policy": "Pets welcome",
    "url": "https://www.booking.com/..."
}
```

## 🔧 Configuration

### Selenium WebDriver Setup
```
# Chrome options for automated scraping
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
```

### Search Parameters
```
# Booking.com search parameters
params = {
    'ss': 'Israel',      # Destination
    'ht_id': '204',      # Property type: Camping
    'pets': '1',         # Pets allowed filter
}
```

## 📖 Manual Collection Guide

If automated scraping doesn't work, follow these steps:

1. **Go to Booking.com**
2. **Search for "Israel"**
3. **Apply Filters:**
   - Property type: "Camping"
   - Facilities: "Pets allowed"
4. **For each result, collect:**
   - Exact name from listing
   - Location/address
   - Description from property page
   - Pet policy from "House rules"
   - Full Booking.com URL

## 🛡️ Error Handling

The script includes comprehensive error handling:

- **Timeout Protection**: Waits for page elements to load
- **Missing Data**: Handles cases where some information isn't available
- **Network Issues**: Graceful degradation with manual fallback
- **Rate Limiting**: Includes delays to respect server resources

## 📈 Sample Output

```
name,location,description,pet_policy,url
Faran Camping,Eilat Southern District,Desert camping experience near Eilat,Pets allowed. Contact property for policies,https://www.booking.com/hotel/il/faran-camping.html
Kfar Blum Camping,Upper Galilee Northern District,Camping site in Jordan Valley,Pets welcome. Inform in advance,https://www.booking.com/hotel/il/kfar-blum-camping.html
```

## ⚠️ Important Notes

- **Respect Booking.com's Terms**: This tool is for educational/research purposes
- **Verify Pet Policies**: Always confirm pet policies directly with properties
- **Rate Limiting**: Script includes delays to be respectful to servers
- **Data Accuracy**: Information is collected from public listings; verify independently

## 🔍 Troubleshooting

### Common Issues

**Chrome Driver Not Found:**
```
# Install ChromeDriver
# For Ubuntu/Debian:
sudo apt-get install chromium-chromedriver

# For macOS:
brew install chromedriver
```

**Selenium Errors:**
```
# Try headless mode if GUI issues occur
chrome_options.add_argument("--headless")
```

**No Results Found:**
- Check internet connection
- Verify Booking.com is accessible
- Try manual collection method

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Add new campsites to manual data
4. Improve error handling
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is for educational and research purposes. Please respect Booking.com's terms of service and robots.txt file.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Thanks to Booking.com for providing accessible camping data
- Selenium and BeautifulSoup communities for excellent documentation
- Pet-friendly camping community in Israel

## 📞 Support

If you encounter any issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the manual collection guide
3. Ensure all dependencies are installed correctly
4. Open an issue on GitHub

## 🎉 Success Metrics

After running the script, you should have:

- ✅ CSV file with pet-friendly campsites
- ✅ Valid URLs for each campsite
- ✅ Clear pet policy information
- ✅ Location data for trip planning

---

**Happy Camping with Your Pets! 🏕️🐕**

## 📊 Project Status

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
и.

