# -*- coding: utf8 -*-

import os

from django.core.management.base import BaseCommand, CommandError
from faver.models import Station, Route, StationStop, StopTime
from datetime import datetime
import xlrd

DATA_DIR = "rtec_data/"
MON_FRI = range(1, 9)
SAT = range(9, 16)
SUN = range(16, 22)
STOP_HOURS = range(7,43)

class Command(BaseCommand):
    help = 'Loads data from excel files'

    def handle(self, *args, **options):
        for dirname, dirnames, filenames in os.walk(DATA_DIR):
            route_name = dirname.replace(DATA_DIR, "").split('-')[0]
            if route_name:
                print 'Importing {0}'.format(route_name)
                route, cr = Route.objects.get_or_create(nr=int(route_name))
                route.stops.all().delete()
                for filename in filenames:
                    station = station_data(filename)
                    book = open_workbook(dirname, filename)
                    sheet = open_sheet(book)
                    import_hours(sheet, MON_FRI, route, station, 1)



def sheet_name(book):
    return book.sheet_names()[0]

def print_sheet(s):
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            if s.cell(row, col).value:
                print "%s -> %s, %s" % (s.cell(row, col).value, row, col)

def station_data(filename):
    """
    Returns data from filename such as
    Route number, station index, station id, station name
    """

    station = dict()
    raw_data = filename.split('-')
    station['route_nr'] = raw_data[0]
    station['order'] = raw_data[1]
    station_data_raw = ''.join(raw_data[2:])
    station_data = station_data_raw.split(' ')
    station['id'] = station_data[0]
    station['name']  = ''.join(station_data[1:]).replace('.xls', '')
    return station

def open_workbook(dirname, filename):
    """
    returns a book object in case file is xls
    """
    if filename.split('.')[-1] == 'xls':
        return xlrd.open_workbook(os.path.join(dirname, filename))
    return False

def open_sheet(book):
    """
    returns a sheet object in case there is a book object
    """
    if book:
        return book.sheet_by_name(sheet_name(book))
    return False


def print_hours(s, minutes_index):
    """
    test function to print hours
    """
    time = datetime.now()
    for row in STOP_HOURS:
        if row % 2 == 1:
            p_time = time.replace(hour=int(s.cell(row, 0).value)) 
        for col in minutes_index:
            if s.cell(row, col).value:
                p_time = p_time.replace(minute=int(s.cell(row, col).value)) 


def import_hours(s, minutes_index, route, station_data, day_type):
    """
    function to add StopTime to stations_stops from excel file
    """
    time = datetime.now()
    station_name = s.cell(2, 0).value[8:]
    station, cr = Station.objects.get_or_create(name = station_name)
    station_stop, cr = StationStop.objects.get_or_create(order_nr=int(station_data['order']),station=station,day_type=day_type)
    StopTime.objects.filter(station=station_stop).delete()
    route.stops.add(station_stop)
    for row in range(7, s.nrows-3):
        if s.cell(row, 0).value:
            p_time = time.replace(hour=int(s.cell(row, 0).value)) 
        for col in minutes_index:
            if s.cell(row, col).value:
                p_time = p_time.replace(minute=int(s.cell(row, col).value)) 
                StopTime.objects.create(time=p_time, station=station_stop)
