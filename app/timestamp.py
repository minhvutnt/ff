from datetime import datetime

def date_to_timestamp(date_check):
    timestamp = datetime.timestamp(date_check)
    return timestamp

def timestamp_to_date(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object

def time_now():
    result = datetime.now()
    return result

def convert_string_to_date(year_month_day):
    return datetime.strptime(year_month_day, '%Y-%m-%d')

def short_month(t):
    return t.strftime('%B')

def get_next_sunday():
    import datetime
    today = datetime.date.today()
    days_ahead = 6 - today.weekday() 
    if days_ahead <= 0:
        days_ahead += 7
    next_sunday = today + datetime.timedelta(days=days_ahead)
    next_sunday_midnight = datetime.datetime.combine(next_sunday, datetime.time.min)
    return next_sunday_midnight

