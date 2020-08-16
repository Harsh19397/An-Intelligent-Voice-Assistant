import datetime
import pytz

def get_date_time():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    months = {1: 'January',
              2: 'Feburary',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'Decemeber'}
    return current_time, months[current_time.month]

