import myfitnesspal
import os
from datetime import timedelta, date

username = os.getenv('MFP_USERNAME')
password = os.getenv('MFP_PASSWORD')

client = myfitnesspal.Client(username, password)
start_date = date(2015, 4, 19)
end_date = date(2015, 11, 29)
outfile = open('logs.txt', 'w')

mfp_start = client.get_date(start_date)
mfp_end = client.get_date(end_date)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

for day in daterange(start_date, end_date):
    mfp_day = client.get_date(day)
    meal_names = mfp_day.keys()
    meals = mfp_day.meals
    outfile.write(str(mfp_day) + '\n')
    for i in range(len(meals)):
        meal = meals[i]
        outfile.write(meal_names[i] + ': ' + str(meal.entries) + '\n')
    if mfp_day.notes:
        outfile.write('notes: ' + mfp_day.notes)
    outfile.write('\n\n\n')

outfile.close()
