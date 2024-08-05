from django import template
from datetime import datetime

register = template.Library()

@register.filter
def l2l_dt(value):
    if isinstance(value, str):
        try:
            # Parse the string into a datetime object
            date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
            return date_obj.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            return "Invalid date format. Expected format: YYYY-MM-DDTHH:MM:SS"
    elif isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    else:
        # Handle other types gracefully
        return "Unsupported type"