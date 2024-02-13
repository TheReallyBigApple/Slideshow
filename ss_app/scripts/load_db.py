import csv
from ss_app.models import Photos

# run from          ss_project
# python manage.py runscript load_db -v2

def run():
    update_file='ss_app/scripts/db_records.csv'
    print("Loading ", update_file)
    fhand = open(update_file)
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Photos.objects.all().delete()
    

   
    for row in reader:
        print(row)
        new_entry = Photos(file_name=row[0], when_where=row[2] + " :      " + row[1], sort_order=row[3], caption=row[4], image=row[0])
        new_entry.save()