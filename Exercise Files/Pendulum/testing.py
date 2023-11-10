import pendulum

dt1=pendulum.datetime(2020,7,5,10,00)
dt2=pendulum.datetime(2020,7,6,12,00)
diff=dt1.diff_for_humans(dt2)
print(diff)

new = dt1.in_timezone("Europe/London")

print(new)