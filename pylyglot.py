# -*- coding: utf-8 -*-
from sys import argv
from datetime import datetime, date, time
from langs import langs, base_langs 


# sys.argv
script, option = argv

# datetime 
now = date.today()
week_day = now.strftime("%w")
#-----------------------------

# Languages to be studied (from langs.py)
monday = base_langs + langs[3]
tuesday = base_langs + langs[4]
wednesday = base_langs + langs[5]
thursday = base_langs + langs[6]
friday = base_langs + langs[7]
saturday = base_langs
sunday = base_langs

def study_today(week_day):
    print "You should study:"
    if week_day == "1":
        print monday
    elif week_day == "2":
        print tuesday
    elif week_day == "3":
        print wednesday
    elif week_day == "4":
        print thursday
    elif week_day == "5":
        print friday
    elif week_day == "6":
        print saturday
    elif week_day == "0":
        print sunday

if option == "l":
    study_today(week_day)

if option == "b":
    print base_langs

if option == "s":
    print side_langs

if option == "a":
    for l in langs:
        print l
