import pendulum

now = pendulum.now()
icd = pendulum.datetime(now.year,2,7)

print("Today is:", now.format("dddd, MMMM Do"))

print("International Clash Dat is:", icd.format("dddd, MMMM Do"))

diff = icd.diff(now)

if icd < now:
    print("International Clash Day went by", diff.days, "days ago")
    furdiff = icd.add(years=1).diff(now)
    print("It's", furdiff.days, "days until International Clash Day!")
else:
    print("It's", diff.days, "days until International Clash Day!")