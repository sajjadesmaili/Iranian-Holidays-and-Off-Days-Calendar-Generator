#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Iranian Holidays and Off-Days Calendar Generator
===============================================

This module generates a comprehensive calendar of Iranian holidays and off-days
for a specified year, including official holidays and weekly off-days.

Author: Sajjad Esmaili with the help of Claude
Date: August 30, 2025
Version: 1.0
"""

import csv
import json
from datetime import date, timedelta
from pathlib import Path
from typing import List, Tuple, Dict, Optional
import holidays
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('holidays.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

class IranianHolidayCalendar:
    """A comprehensive Iranian holiday calendar generator."""
    
    def __init__(self, year: int = 2025):
        """
        Initialize the Iranian Holiday Calendar.
        
        Args:
            year (int): The year to generate holidays for
        """
        self.year = year
        self.holidays = holidays.country_holidays("IR", years=year)
        self.off_days: List[Tuple[str, int, int, str]] = []
        
        # Persian month names
        self.persian_months = {
            1: "فروردین", 2: "اردیبهشت", 3: "خرداد", 4: "تیر",
            5: "مرداد", 6: "شهریور", 7: "مهر", 8: "آبان",
            9: "آذر", 10: "دی", 11: "بهمن", 12: "اسفند"
        }
        
        # Persian weekday names
        self.persian_weekdays = {
            0: "دوشنبه", 1: "سه‌شنبه", 2: "چهارشنبه", 3: "پنج‌شنبه",
            4: "جمعه", 5: "شنبه", 6: "یکشنبه"
        }
        
        logging.info(f"Initialized Iranian Holiday Calendar for year {year}")
    
    def generate_off_days(self) -> List[Tuple[str, int, int, str]]:
        """
        Generate all off-days including official holidays and weekly offs.
        
        Returns:
            List of tuples containing (iso_date, day, month, label)
        """
        start_date = date(self.year, 1, 1)
        end_date = date(self.year, 12, 31)
        
        current_date = start_date
        
        while current_date <= end_date:
            # Check if it's Thursday (3) or Friday (4) - Iranian weekend
            is_thursday = current_date.weekday() == 3
            is_friday = current_date.weekday() == 4
            
            # Check for official holidays
            holiday_label = self.holidays.get(current_date)
            
            if holiday_label:
                # Official holiday
                self.off_days.append((
                    current_date.isoformat(),
                    current_date.day,
                    current_date.month,
                    f"🎌 {holiday_label}"
                ))
            elif is_thursday:
                # Thursday off-day
                self.off_days.append((
                    current_date.isoformat(),
                    current_date.day,
                    current_date.month,
                    "📅 تعطیلی هفتگی (پنج‌شنبه)"
                ))
            elif is_friday:
                # Friday off-day
                self.off_days.append((
                    current_date.isoformat(),
                    current_date.day,
                    current_date.month,
                    "🕌 تعطیلی هفتگی (جمعه)"
                ))
            
            current_date += timedelta(days=1)
        
        logging.info(f"Generated {len(self.off_days)} off-days for year {self.year}")
        return self.off_days
    
    def print_calendar(self, show_persian_dates: bool = True) -> None:
        """
        Print the holiday calendar to console.
        
        Args:
            show_persian_dates (bool): Whether to show Persian month names
        """
        if not self.off_days:
            self.generate_off_days()
        
        print(f"\n{'='*80}")
        print(f"🇮🇷 تقویم تعطیلات ایران - سال {self.year}")
        print(f"Iranian Holidays Calendar - Year {self.year}")
        print(f"{'='*80}\n")
        
        current_month = 0
        
        for iso_date, day, month, label in self.off_days:
            if month != current_month:
                current_month = month
                month_name = self.persian_months.get(month, str(month)) if show_persian_dates else f"Month {month}"
                print(f"\n📅 {month_name} ({month:02d}):")
                print("-" * 50)
            
            # Get weekday
            date_obj = date.fromisoformat(iso_date)
            weekday_persian = self.persian_weekdays.get(date_obj.weekday(), "نامعلوم")
            weekday_english = date_obj.strftime("%A")
            
            print(f"{iso_date} | {day:02d}/{month:02d} | {weekday_persian} ({weekday_english}) | {label}")
    
    def save_to_csv(self, filename: Optional[str] = None) -> str:
        """
        Save holidays to CSV file.
        
        Args:
            filename (str, optional): Custom filename for the CSV file
            
        Returns:
            str: The filename of the saved file
        """
        if not self.off_days:
            self.generate_off_days()
        
        if filename is None:
            filename = f"iran_holidays_{self.year}.csv"
        
        filepath = Path(filename)
        
        try:
            with open(filepath, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.writer(csvfile)
                # Write header
                writer.writerow([
                    "Date", "Day", "Month", "Label", 
                    "Persian_Month", "Weekday_Persian", "Weekday_English"
                ])
                
                # Write data
                for iso_date, day, month, label in self.off_days:
                    date_obj = date.fromisoformat(iso_date)
                    writer.writerow([
                        iso_date,
                        day,
                        month,
                        label,
                        self.persian_months.get(month, str(month)),
                        self.persian_weekdays.get(date_obj.weekday(), "Unknown"),
                        date_obj.strftime("%A")
                    ])
            
            logging.info(f"Saved calendar to CSV: {filepath.absolute()}")
            return str(filepath)
            
        except Exception as e:
            logging.error(f"Error saving CSV file: {e}")
            raise
    
    def save_to_json(self, filename: Optional[str] = None) -> str:
        """
        Save holidays to JSON file.
        
        Args:
            filename (str, optional): Custom filename for the JSON file
            
        Returns:
            str: The filename of the saved file
        """
        if not self.off_days:
            self.generate_off_days()
        
        if filename is None:
            filename = f"iran_holidays_{self.year}.json"
        
        filepath = Path(filename)
        
        try:
            data = {
                "year": self.year,
                "total_off_days": len(self.off_days),
                "holidays": []
            }
            
            for iso_date, day, month, label in self.off_days:
                date_obj = date.fromisoformat(iso_date)
                data["holidays"].append({
                    "date": iso_date,
                    "day": day,
                    "month": month,
                    "label": label,
                    "persian_month": self.persian_months.get(month),
                    "weekday_persian": self.persian_weekdays.get(date_obj.weekday()),
                    "weekday_english": date_obj.strftime("%A"),
                    "is_official_holiday": "🎌" in label
                })
            
            with open(filepath, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, ensure_ascii=False, indent=2)
            
            logging.info(f"Saved calendar to JSON: {filepath.absolute()}")
            return str(filepath)
            
        except Exception as e:
            logging.error(f"Error saving JSON file: {e}")
            raise
    
    def get_statistics(self) -> Dict[str, int]:
        """
        Get statistics about holidays and off-days.
        
        Returns:
            Dict containing various statistics
        """
        if not self.off_days:
            self.generate_off_days()
        
        official_holidays = sum(1 for _, _, _, label in self.off_days if "🎌" in label)
        thursday_offs = sum(1 for _, _, _, label in self.off_days if "پنج‌شنبه" in label)
        friday_offs = sum(1 for _, _, _, label in self.off_days if "جمعه" in label)
        
        return {
            "total_off_days": len(self.off_days),
            "official_holidays": official_holidays,
            "thursday_weekly_offs": thursday_offs,
            "friday_weekly_offs": friday_offs,
            "weekend_days": thursday_offs + friday_offs,
            "working_days": 365 - len(self.off_days) if self.year % 4 != 0 else 366 - len(self.off_days)
        }
    
    def print_statistics(self) -> None:
        """Print detailed statistics about the calendar."""
        stats = self.get_statistics()
        
        print(f"\n{'='*60}")
        print(f"📊 آمار تقویم سال {self.year}")
        print(f"Calendar Statistics for {self.year}")
        print(f"{'='*60}")
        print(f"🗓️  کل روزهای تعطیل: {stats['total_off_days']}")
        print(f"🎌 تعطیلات رسمی: {stats['official_holidays']}")
        print(f"📅 پنج‌شنبه‌ها: {stats['thursday_weekly_offs']}")
        print(f"🕌 جمعه‌ها: {stats['friday_weekly_offs']}")
        print(f"🏠 کل آخر هفته‌ها: {stats['weekend_days']}")
        print(f"💼 روزهای کاری: {stats['working_days']}")
        print(f"{'='*60}\n")


def main():
    """Main function to demonstrate the Iranian Holiday Calendar."""
    try:
        # Create calendar instance
        calendar = IranianHolidayCalendar(2025)
        
        # Generate and display calendar
        calendar.print_calendar()
        
        # Show statistics
        calendar.print_statistics()
        
        # Save to files
        csv_file = calendar.save_to_csv()
        json_file = calendar.save_to_json()
        
        print(f"✅ Files saved successfully:")
        print(f"   📄 CSV: {csv_file}")
        print(f"   📄 JSON: {json_file}")
        
        # Example of accessing specific data
        print(f"\n🔍 Example queries:")
        off_days = calendar.get_statistics()
        print(f"   Total working days in 2025: {off_days['working_days']}")
        print(f"   Total holidays: {off_days['official_holidays']}")
        
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
