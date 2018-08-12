import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features');
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 36` FROM `DBQ`;';
cursor.execute(sql);

# store into variable 'data'
data = cursor.fetchall();
size = len(data);

# convert into numpy str array
data2 = [];
data2 = numpy.array(data);
data2.flatten();

average = 1 - 3.75245/21;
average = round(average, 8);
# calculate and normalise
for i in range(0, size):
    # except first line and null
    if data2[i][1] != 'DBD895' and data2[i][1] != '#NULL!':
        # calculate
        data2[i][1] = 1 - decimal.Decimal(data[i][1])/21;
        # exceptional values
        if decimal.Decimal(data[i][1]) == 5555 :
            data2[i][1] = decimal.Decimal(0);
        if decimal.Decimal(data[i][1]) == 7777:
            data2[i][1] = decimal.Decimal(average);
        if decimal.Decimal(data[i][1]) == 9999 :
            data2[i][1] = decimal.Decimal(average);
    else:
        # deal with first line and null
        data2[i][1] = decimal.Decimal(0);

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F8` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F8` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();