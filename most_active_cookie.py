#!/usr/bin/python
# -*- coding: UTF-8 -*-
from datetime import datetime,timedelta
import csv
import argparse
def most_active_cookie(log_file,date):
    cookie_counter = {}
    # cookie counter to count active times
    with open(log_file,"r") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            cookie, time = line[0],line[1]
            local_time,time_difference = time[:-6], time[-6:]
            # eg. local time:2018-12-09T14:19:00 time difference:+00:00
            timestamp = datetime.strptime(local_time, '%Y-%m-%dT%H:%M:%S')
            hours = int(time_difference[1:3])
            minutes = int(time_difference[4:6])
            # convert local time to utc time according to time difference
            if time_difference[0] == '+':
                timestamp += timedelta(hours=hours, minutes=minutes)
            elif time_difference[0] == '-':
                timestamp -= timedelta(hours=hours, minutes=minutes)
            if timestamp.date() == date:
                # count active times for each cookie
                count = cookie_counter.get(cookie, 0)+1
                cookie_counter[cookie] = count
    # retrieve the max time and get all cookies with the max activate time
    max_val = max(cookie_counter.values())
    for k, v in cookie_counter.items():
        if v == max_val:
            print(k)
if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="path to the cookie log file")
    parser.add_argument("-d", "--date", help="date to activate cookie")
    args = parser.parse_args()
    # retrieve params and sent it to func
    log_file = args.file
    date_str = args.date
    most_active_cookie("cookie_log.csv", datetime.strptime(date_str, '%Y-%m-%d').date())
