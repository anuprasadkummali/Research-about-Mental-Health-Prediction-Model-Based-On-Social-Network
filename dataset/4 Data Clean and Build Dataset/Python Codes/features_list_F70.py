import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 49`, `COL 50` FROM `OHQ`;';
cursor.execute(sql);

# store into variable 'data'
data = cursor.fetchall();
size = len(data);

print(data);

# convert into numpy str array
data2 = [];
data2 = numpy.array(data);
data2.flatten();

# test and valid values after first line
print(data2);

average1 = 0; # 870
num1 =0;

average2 = 0; # 875
num2 = 0;

for i in range(1, size):
    if data2[i][1]!= '#NULL!' and float(data2[i][1])>=0 and float(data2[i][1]) <10:
        num1 = num1 + 1;
        average1 = average1 + float(data2[i][1]);

    if data2[i][2]!= '#NULL!' and float(data2[i][2])>=0 and float(data2[i][2]) <10:
        num2 = num2 + 1;
        average2 = average2 + float(data2[i][2]);
# end of loop


average1 = round(average1/num1, 8);
average2 = round(average2/num2, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1]== '#NULL!' or float(data2[i][1]) > 10:
        data2[i][1] = average1;

    if data2[i][2]== '#NULL!' or float(data2[i][2]) > 10:
        data2[i][2] = average2;

    data2[i][1] = (float(data2[i][1])+float(data2[i][2]))/14;
# end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F70` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F70` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();