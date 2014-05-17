import datetime


def get_normalized_time():
    DATE_REPLACE = {
    'year': 2014,
    'month': 5,
    'day': 7,
    }
    now = datetime.datetime.now()
    n_time = now.replace(year=DATE_REPLACE['year'],
                month=DATE_REPLACE['month'],
                day=DATE_REPLACE['day'])
    return n_time