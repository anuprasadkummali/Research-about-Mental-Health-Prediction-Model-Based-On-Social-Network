import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 11`, `COL 87`, `COL 88`, `COL 89`, `COL 90` FROM `MCQ`;';
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

average1 = 4308/6462; # MCQ080
average1 = round(average1, 8);
average2 = 4781/6463; # 365a
average2 = round(average2, 8);
average3 = 4220/6464; # 365b
average3 = round(average3, 8);
average4 = 4913/6456; # 365c
average4 = round(average4, 8);
average5 = 4713/6459; # 365d
average5 = round(average4, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '1':
        data2[i][1] = 0;
    elif data2[i][1] == '2':
        data2[i][1] = 1;
    else:
        data2[i][1] =  average1;

    if data2[i][2] == '1':
        data2[i][2] = 0;
    elif data2[i][2] == '2':
        data2[i][2] = 1;
    else:
        data2[i][2] = average2;

    if data2[i][3] == '1':
        data2[i][3] = 0;
    elif data2[i][3] == '2':
        data2[i][3] = 1;
    else:
        data2[i][3] = average3;

    if data2[i][4] == '1':
        data2[i][4] = 0;
    elif data2[i][4] == '2':
        data2[i][4] = 1;
    else:
        data2[i][4] = average4;

    if data2[i][5] == '1':
        data2[i][5] = 0;
    elif data2[i][5] == '2':
        data2[i][5] = 1;
    else:
        data2[i][5] = average5;

    data2[i][1] = (float(data2[i][1])+float(data2[i][2])+float(data2[i][3])+float(data2[i][4])+float(data2[i][5]))/5;
# end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F31` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F31` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();