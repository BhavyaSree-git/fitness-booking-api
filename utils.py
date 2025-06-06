from pytz import timezone, all_timezones
from datetime import datetime

def convert_ist_to_timezone(ist_datetime, tz_name):
    try:
        if tz_name not in all_timezones:
            return None
        ist = timezone('Asia/Kolkata')
        target_tz = timezone(tz_name)
        return ist_datetime.replace(tzinfo=ist).astimezone(target_tz)
    except Exception:
        return None
