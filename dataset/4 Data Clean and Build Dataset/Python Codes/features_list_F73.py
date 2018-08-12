#wrong file mistake of copy files
import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 2`, `COL 3` FROM `BPQ`;';
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

average1 = 4285/6459; #020
average1 = round(average1, 8);
average2 = 428/2166; #030
average2 = round(average2, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '1':
            data2[i][1] = 0;
    elif data2[i][1] == '2':
            data2[i][1] = 1;
    else:
        data2[i][1] = average1;

    if data2[i][2] == '1':
        data2[i][2] = 0;
    elif data2[i][2] == '2':
        data2[i][2] = 1;
    elif data2[i][2] == '9':
        data2[i][2] = average2;
    else:
        data2[i][2] = 1;

    data2[i][1] = (float(data2[i][1])+float(data2[i][2]))/2;
#end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F73` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F73` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();