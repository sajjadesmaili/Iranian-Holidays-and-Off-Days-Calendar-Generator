# 🇮🇷 Iranian Holidays Calendar Generator

A comprehensive Python application for generating Iranian holidays and off-days calendar with support for both Persian and English languages.

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [Output Formats](#-output-formats)
- [API Reference](#-api-reference)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **🗓️ Complete Calendar Generation**: Official Iranian holidays + weekly off-days (Thursday & Friday)
- **🌏 Bilingual Support**: Persian and English month/weekday names
- **📊 Detailed Statistics**: Working days, holidays count, and comprehensive analytics
- **💾 Multiple Export Formats**: CSV, JSON, and console output
- **🎨 Beautiful Display**: Emoji icons and organized formatting
- **📝 Comprehensive Logging**: Track operations and errors
- **🔧 Professional Structure**: Object-oriented design with proper error handling

## 🚀 Installation

### Prerequisites

```bash
python >= 3.7
```

### Required Dependencies

```bash
pip install holidays
```

### Optional Dependencies (for enhanced features)

```bash
pip install pathlib  # Usually included in Python 3.4+
```

### Install from Source

```bash
git clone https://github.com/yourusername/iranian-holidays-calendar.git
cd iranian-holidays-calendar
pip install -r requirements.txt
```

## ⚡ Quick Start

```python
from iranian_holidays import IranianHolidayCalendar

# Create calendar for 2025
calendar = IranianHolidayCalendar(2025)

# Display calendar
calendar.print_calendar()

# Save to files
calendar.save_to_csv()
calendar.save_to_json()

# Get statistics
stats = calendar.get_statistics()
print(f"Total working days: {stats['working_days']}")
```

## 📖 Usage Examples

### Basic Usage

```python
# Initialize calendar
calendar = IranianHolidayCalendar(2025)

# Generate off-days data
off_days = calendar.generate_off_days()

# Print formatted calendar
calendar.print_calendar(show_persian_dates=True)
```

### Advanced Usage

```python
# Custom file names
calendar.save_to_csv("my_custom_holidays.csv")
calendar.save_to_json("holidays_data.json")

# Get detailed statistics
stats = calendar.get_statistics()
calendar.print_statistics()

# Access raw data
for date, day, month, label in calendar.off_days:
    print(f"{date}: {label}")
```

### Command Line Usage

```bash
# Run the main script
python iranian_holidays.py

# This will:
# 1. Generate and display the 2025 calendar
# 2. Show statistics
# 3. Save CSV and JSON files
```

## 📁 Output Formats

### Console Output

```
================================================================================
🇮🇷 تقویم تعطیلات ایران - سال 2025
Iranian Holidays Calendar - Year 2025
================================================================================

📅 فروردین (01):
--------------------------------------------------
2025-01-02 | 02/01 | سه‌شنبه (Tuesday) | 📅 تعطیلی هفتگی (پنج‌شنبه)
2025-01-03 | 03/01 | چهارشنبه (Wednesday) | 🕌 تعطیلی هفتگی (جمعه)
...
```

### CSV Format

| Date | Day | Month | Label | Persian_Month | Weekday_Persian | Weekday_English |
|------|-----|-------|-------|---------------|-----------------|-----------------|
| 2025-01-02 | 2 | 1 | 📅 تعطیلی هفتگی (پنج‌شنبه) | فروردین | سه‌شنبه | Tuesday |

### JSON Format

```json
{
  "year": 2025,
  "total_off_days": 104,
  "holidays": [
    {
      "date": "2025-01-02",
      "day": 2,
      "month": 1,
      "label": "📅 تعطیلی هفتگی (پنج‌شنبه)",
      "persian_month": "فروردین",
      "weekday_persian": "سه‌شنبه",
      "weekday_english": "Tuesday",
      "is_official_holiday": false
    }
  ]
}
```

## 📚 API Reference

### IranianHolidayCalendar Class

#### Constructor

```python
IranianHolidayCalendar(year: int = 2025)
```

**Parameters:**
- `year` (int): The year to generate holidays for

#### Methods

##### `generate_off_days() -> List[Tuple[str, int, int, str]]`
Generate all off-days including official holidays and weekly offs.

**Returns:** List of tuples containing (iso_date, day, month, label)

##### `print_calendar(show_persian_dates: bool = True) -> None`
Print the holiday calendar to console.

**Parameters:**
- `show_persian_dates` (bool): Whether to show Persian month names

##### `save_to_csv(filename: Optional[str] = None) -> str`
Save holidays to CSV file.

**Parameters:**
- `filename` (str, optional): Custom filename for the CSV file

**Returns:** The filename of the saved file

##### `save_to_json(filename: Optional[str] = None) -> str`
Save holidays to JSON file.

**Parameters:**
- `filename` (str, optional): Custom filename for the JSON file

**Returns:** The filename of the saved file

##### `get_statistics() -> Dict[str, int]`
Get statistics about holidays and off-days.

**Returns:** Dictionary containing various statistics

##### `print_statistics() -> None`
Print detailed statistics about the calendar.

## ⚙️ Configuration

### Custom Year

```python
# For different years
calendar_2024 = IranianHolidayCalendar(2024)
calendar_2026 = IranianHolidayCalendar(2026)
```

### Logging Configuration

The application uses Python's built-in logging module. Logs are saved to `holidays.log` and displayed in console.

```python
import logging

# Customize logging level
logging.getLogger().setLevel(logging.DEBUG)
```

### Persian Months and Weekdays

You can customize the Persian names by modifying the class attributes:

```python
calendar = IranianHolidayCalendar(2025)
calendar.persian_months[1] = "Custom فروردین"
```

## 📊 Statistics Output

The application provides comprehensive statistics:

- **Total Off Days**: Complete count of non-working days
- **Official Holidays**: Government declared holidays
- **Weekly Offs**: Thursday and Friday counts
- **Working Days**: Calculated working days in the year

Example output:
```
============================================================
📊 آمار تقویم سال 2025
Calendar Statistics for 2025
============================================================
🗓️  کل روزهای تعطیل: 104
🎌 تعطیلات رسمی: 26
📅 پنج‌شنبه‌ها: 52
🕌 جمعه‌ها: 52
🏠 کل آخر هفته‌ها: 104
💼 روزهای کاری: 261
============================================================
```

## 🛠️ Development

### Project Structure

```
iranian-holidays-calendar/
│
├── iranian_holidays.py      # Main application file
├── README.md                # This file

```

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

This project follows PEP 8 style guidelines:

```bash
# Check code style
flake8 iranian_holidays.py

# Format code
black iranian_holidays.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass

## 📝 Requirements

Create a `requirements.txt` file:

```txt
holidays>=0.34
pathlib2>=2.3.7; python_version < "3.4"
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'holidays'`
**Solution**: Install the holidays package: `pip install holidays`

**Issue**: CSV file not saving with proper encoding
**Solution**: The application uses UTF-8-BOM encoding for CSV files to ensure proper display in Excel

**Issue**: Persian text not displaying correctly
**Solution**: Ensure your terminal/console supports UTF-8 encoding

### Debug Mode

Enable debug logging:

```python
import logging
logging.getLogger().setLevel(logging.DEBUG)

calendar = IranianHolidayCalendar(2025)
```

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/sajjadesmaili/iranian-holidays-calendar/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sajjadesmaili/iranian-holidays-calendar/discussions)
- **Email**: info@sajjadesmaili.ir

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Python Holidays Library](https://pypi.org/project/holidays/) for providing Iranian holiday data
- Iranian Calendar System contributors
- Open source community for inspiration and support

## 🔄 Changelog

### Version 1.0.0
- Initial release
- Support for Iranian holidays 2025
- CSV and JSON export functionality
- Persian and English language support
- Comprehensive statistics
- Professional logging system

---

**Made with ❤️ for the Iranian developer community**

*If you find this project helpful, please consider giving it a star ⭐*
