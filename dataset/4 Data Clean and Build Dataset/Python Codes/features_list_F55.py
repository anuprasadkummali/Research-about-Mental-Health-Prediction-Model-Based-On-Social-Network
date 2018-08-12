#wrong file mistake of copy files
import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 24`, `COL 26`, `COL 27`, `COL 2`, `COL 4`, `COL 5` , `COL 8`, `COL 13`, `COL 14` FROM `CSQ`;';
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

average1 = 1540/1685; #160
average1 = round(average1, 8);
average2 = 1; #180
average2 = round(average2, 8);
average3 = 1647/1685; #190
average3 = round(average3, 8);
average4 = 3504/3810; #010
average4 = round(average4, 8);
average5 = 2762/3798; #030
average5 = round(average5, 8);
average6 = 3534/3808; #040
average6 = round(average6, 8);
average7 = 3614/3813; #080
average7 = round(average7, 8);
average8 = 265/3793; #100
average8 = round(average8, 8);
average9 = 3570/3813; #110
average9 = round(average9, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '1':
        data2[i][1] = 0;
    elif data2[i][1] == '2':
        if data2[i][2] == '1':
            data2[i][1] = 0;
        else:
            data2[i][1] = 1;
    elif data2[i][1] == '7':
        if data2[i][2] == '1':
            data2[i][1] = 0;
        else:
            data2[i][1] = average1;
    elif data2[i][1] == '9':
        if data2[i][2] == '1':
            data2[i][1] = 0;
        else:
            data2[i][1] = average1;
    else:
        data2[i][1] = 1;

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


    if data2[i][5] == '1':
            data2[i][5] = 0;
    elif data2[i][5] == '2':
            data2[i][5] = 1;
    elif data2[i][5] == '7':
        data2[i][5] = average5;
    elif data2[i][5] == '9':
        data2[i][5] = average5;
    else:
        data2[i][5] = 1;


    if data2[i][6] == '1':
            data2[i][6] = 0;
    elif data2[i][6] == '2':
            data2[i][6] = 1;
    elif data2[i][6] == '7':
        data2[i][6] = average6;
    elif data2[i][6] == '9':
        data2[i][6] = average6;
    else:
        data2[i][6] = 1;

    if data2[i][7] == '1':
            data2[i][7] = 0;
    elif data2[i][7] == '2':
            data2[i][7] = 1;
    elif data2[i][7] == '7':
        data2[i][7] = average7;
    elif data2[i][7] == '9':
        data2[i][7] = average7;
    else:
        data2[i][7] = 1;

    if data2[i][8] == '1':
            data2[i][8] = 0;
    elif data2[i][8] == '2':
            data2[i][8] = 1;
    elif data2[i][8] == '7':
        data2[i][8] = average8;
    elif data2[i][8] == '9':
        data2[i][8] = average8;
    else:
        data2[i][8] = 1;

    if data2[i][9] == '1':
            data2[i][9] = 0;
    elif data2[i][9] == '2':
            data2[i][9] = 1;
    elif data2[i][9] == '7':
        data2[i][9] = average9;
    elif data2[i][9] == '9':
        data2[i][9] = average9;
    else:
        data2[i][9] = 1;

    x = (float(data2[i][1])+float(data2[i][3])+float(data2[i][4])+float(data2[i][5])+float(data2[i][6])+float(data2[i][7])+float(data2[i][8])+float(data2[i][9]))/8;
    data2[i][1] = round(x, 8);
    x = 0;
#end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F55` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F55` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();