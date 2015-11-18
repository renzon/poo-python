import datetime

dt=datetime.datetime.now()

intervalo=datetime.timedelta(days=2,hours=23);

print(dt+intervalo)
print(dt-intervalo)
print(dt.strftime('%d/%m/%Y'))

