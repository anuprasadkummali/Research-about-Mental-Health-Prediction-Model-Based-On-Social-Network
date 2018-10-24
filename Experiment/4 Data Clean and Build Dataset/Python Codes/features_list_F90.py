#wrong file mistake of copy files
import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 3`, `COL 4`, `COL 5`, `COL 6` FROM `CKQ`;';
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

average1 = 893/2059; #020
average1 = round(average1, 8);
average2 = 6021/6451; #030
average2 = round(average2, 8);# CKQ030 is useless
average3 = 161/430; #040
average3 = round(average3, 8);
average4 = 5081/6452; #060
average4 = round(average4, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '1':
            data2[i][1] = 0;
    elif data2[i][1] == '2':
            data2[i][1] = 1;
    elif data2[i][1] == '7':
        data2[i][1] = average1;
    elif data2[i][1] == '9':
        data2[i][1] = average1;
    else:
        data2[i][1] = 1;


    if data2[i][2] == '1':
            data2[i][2] = 0;
    elif data2[i][2] == '2':
            data2[i][2] = 1;
    elif data2[i][2] == '3':
            data2[i][2] = average2;
    elif data2[i][2] == '7':
        data2[i][2] = average2;
    elif data2[i][2] == '9':
        data2[i][2] = average2;
    else:
        data2[i][2] = 1;


    if data2[i][3] == '1':
            data2[i][3] = 0;
    elif data2[i][3] == '2':
            data2[i][3] = 1;
    elif data2[i][3] == '7':
        data2[i][3] = average3;
    elif data2[i][3] == '9':
        data2[i][3] = average3;
    else:
        data2[i][3] = 1;

    if data2[i][4] == '1':
        data2[i][4] = 0;
    elif data2[i][4] == '2':
        data2[i][4] = 1;
    elif data2[i][4] == '7':
        data2[i][4] = average4;
    elif data2[i][4] == '9':
        data2[i][4] = average4;
    else:
        data2[i][4] = 1;

    data2[i][1] = min(float(data2[i][1]),float(data2[i][3]),float(data2[i][4]));
#end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F90` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F90` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();