from datetime import date, timedelta

def is_weekend(day):
  return day.weekday() in [4, 4] 

def is_holiday(day, holidays):
  """check government holiday"""
  return day in holidays

def workdays(start_date, end_date, holidays=[]):
  """Calculates working days """
  days = (end_date - start_date).days + 1
  work_days = 0
  for day in range((end_date - start_date).days + 1):
    current_date = start_date + timedelta(days=day)
    if not (is_weekend(current_date) or is_holiday(current_date, holidays)):
      work_days += 1
  return work_days

while True:
  try:
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    start_date = date(*map(int, start_date_str.split('-')))
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    end_date = date(*map(int, end_date_str.split('-')))
    if start_date > end_date:
      print("Start date cannot be after end date.")
    else:
      break
  except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")

holidays = []
user_choice = input("Do you want to enter government holidays (y/n)? ")
if user_choice.lower() == 'y':
  while True:
    try:
      holiday_str = input("Enter holiday date (YYYY-MM-DD) or 'done': ")
      if holiday_str == 'done':
        break
      holiday = date(*map(int, holiday_str.split('-')))
      holidays.append(holiday)
    except ValueError:
      print("Invalid date format. Please use YYYY-MM-DD.")

total_workdays = workdays(start_date, end_date, holidays)
print(f"Total {total_workdays} working days in this period.")
