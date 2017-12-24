
# -*- coding: utf-8 -*-
from datetime import datetime, date, time

now = date.today()
week_day = now.strftime("%w")

languages = [
    'Danish, ',
    'French, ',
    'Japanese, ',
    'Swedish!',
    'German!',
    'Norwegian!',
    'Turkish!',
    'Italian!']

base_language = languages[0] + languages[1] + languages[2]

monday = base_language + languages[3]
tuesday = base_language + languages[4]
wendnesday = base_language + languages[5]
thursday = base_language + languages[6]
friday = base_language + languages[7]

should_study = "Vi devus studi la %s hodiaux!" % week_day

if week_day == "1":
    print(monday)
elif week_day == "2":
    print(tuesday)
elif week_day == "3":
    print(wendnesday)
elif week_day == "4":
    print(thursday)
elif week_day == "5":
    print(friday)
