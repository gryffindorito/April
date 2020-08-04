import sqlite3

conn = sqlite3.connect('../medicine.db')
print "Opened database successfully";

conn.execute('CREATE TABLE details (sno Text, name TEXT, time TIME, dose TEXT)')
print "Table created successfully";
conn.close()
