import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 10`, `COL 13` FROM `BPQ`;';
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

average = 0.6831051649;
average = round(average, 8);
average2 = 3163/4613;
average2 = round(average2, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '0':
            data2[i][1] = average;
    elif data2[i][1] == '1':
            data2[i][1] = 0;
    elif data2[i][1] == '2':
            data2[i][1] = 1;
    elif data2[i][1] == '3':
            data2[i][1] = average;
    elif data2[i][1] == '4':
            data2[i][1] = average;
    elif data2[i][1] == '5':
            data2[i][1] = average;
    elif data2[i][1] == '6':
            data2[i][1] = average;
    elif data2[i][1] == '7':
            data2[i][1] = average;
    elif data2[i][1] == '9':
            data2[i][1] = average;
    elif data2[i][1] == '77':
            data2[i][1] =  average;
    elif data2[i][1] == '99':
            data2[i][1] =  average;
    elif data2[i][1] == '5555':
            data2[i][1] =  average;
    elif data2[i][1] == '7777':
            data2[i][1] =  average;
    elif data2[i][1] == '9999' :
            data2[i][1] =  average;
    else:
        # deal with first line and null
        data2[i][1] =  average;

    if data2[i][2] == '1':
            data2[i][2] = 0;
    elif data2[i][2] == '2':
            data2[i][2] = 1;
    elif data2[i][2] == '7':
        data2[i][2] = average2;
    elif data2[i][2] == '9':
        data2[i][2] = average2;
    else:
        data2[i][2] = 1;

    data2[i][1] = (float(data2[i][1])+float(data2[i][2]))/2;
# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F76` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F76` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();