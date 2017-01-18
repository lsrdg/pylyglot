
# -*- coding: utf-8 -*-
from datetime import datetime, date, time

now = date.today()
week_day = now.strftime("%w")

lingvoj = ['Dana, ', 'Franca, ', 'Japana, ', 'Sveda!', 'Germana!', 'Norvega!', 'Turka!', 'Itala!']

baseling = lingvoj[0] + lingvoj[1] + lingvoj[2]
apudling = lingvoj[3] + lingvoj[4] + lingvoj[5] + lingvoj[6] + lingvoj[7]

lundo = baseling + lingvoj[3]
mardo = baseling + lingvoj[4]
merkredo = baseling + lingvoj[5]
jauxdo = baseling + lingvoj[6]
vendredo = baseling + lingvoj[7]

should_study = "Vi devus studi la %s hodiaux!" % week_day

if week_day == "1":
    print lundo
elif week_day == "2":
    print mardo
elif week_day == "3":
    print merkredo
elif week_day == "4":
    print jauxdo
elif week_day == "5":
    print vendredo

