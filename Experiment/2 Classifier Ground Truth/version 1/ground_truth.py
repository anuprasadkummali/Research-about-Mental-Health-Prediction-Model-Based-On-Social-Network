import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='y2x8JQOR7KaWDGJb', db='NHANES2014', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 2`, `COL 3`, `COL 4`, `COL 5`, `COL 6`, `COL 7`, `COL 8`, `COL 9`, `COL 10` FROM `mental_origin`;';
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

average1 = (881+293*2+242*3)/5392;
average1 = round(average1, 8);
average2 = (903+214*2+202*3)/5390;
average2 = round(average2, 8);
average3 = (1127+350*2+501*3)/5394;
average3 = round(average3, 8);
average4 = (1829+423*2+492*3)/5394;
average4 = round(average4, 8);
average5 = (832+278*2+247*3)/5393;
average5 = round(average5, 8);
average6 = (620+154*2+167*3)/5390;
average6 = round(average6, 8);
average7 = (586+193*2+189*3)/5391;
average7 = round(average7, 8);
average8 = (367+134*2+104*3)/5391;
average8 = round(average8, 8);
average9 = (122+31*2+32*3)/5390;
average9 = round(average9, 8);




# calculate and normalise
for i in range(0, size):
    # give option values
    if data2[i][1] == '0':
            data2[i][1] = 0;
    elif data2[i][1] == '1':
            data2[i][1] = 1;
    elif data2[i][1] == '2':
            data2[i][1] = 2;
    elif data2[i][1] == '3':
            data2[i][1] = 3;
    elif data2[i][1] == '7':
            data2[i][1] = average1;
    elif data2[i][1] == '9':
            data2[i][1] = average1;
    else:
        # deal with first line and null
        data2[i][1] =  average1;

    if data2[i][2] == '0':
            data2[i][2] = 0;
    elif data2[i][2] == '1':
            data2[i][2] = 1;
    elif data2[i][2] == '2':
            data2[i][2] = 2;
    elif data2[i][2] == '3':
            data2[i][2] = 3;
    elif data2[i][2] == '7':
            data2[i][2] = average2;
    elif data2[i][2] == '9':
            data2[i][2] = average2;
    else:
        # deal with first line and null
        data2[i][2] =  average2;

    if data2[i][3] == '0':
            data2[i][3] = 0;
    elif data2[i][3] == '1':
            data2[i][3] = 1;
    elif data2[i][3] == '2':
            data2[i][3] = 2;
    elif data2[i][3] == '3':
            data2[i][3] = 3;
    elif data2[i][3] == '7':
            data2[i][3] = average3;
    elif data2[i][3] == '9':
            data2[i][3] = average3;
    else:
        # deal with first line and null
        data2[i][3] =  average3;

    if data2[i][4] == '0':
            data2[i][4] = 0;
    elif data2[i][4] == '1':
            data2[i][4] = 1;
    elif data2[i][4] == '2':
            data2[i][4] = 2;
    elif data2[i][4] == '3':
            data2[i][4] = 3;
    elif data2[i][4] == '7':
            data2[i][4] = average4;
    elif data2[i][4] == '9':
            data2[i][4] = average4;
    else:
        # deal with first line and null
        data2[i][4] =  average4;

    if data2[i][5] == '0':
            data2[i][5] = 0;
    elif data2[i][5] == '1':
            data2[i][5] = 1;
    elif data2[i][5] == '2':
            data2[i][5] = 2;
    elif data2[i][5] == '3':
            data2[i][5] = 3;
    elif data2[i][5] == '7':
            data2[i][5] = average5;
    elif data2[i][5] == '9':
            data2[i][5] = average5;
    else:
        # deal with first line and null
        data2[i][5] =  average5;

    if data2[i][6] == '0':
            data2[i][6] = 0;
    elif data2[i][6] == '1':
            data2[i][6] = 1;
    elif data2[i][6] == '2':
            data2[i][6] = 2;
    elif data2[i][6] == '3':
            data2[i][6] = 3;
    elif data2[i][6] == '7':
            data2[i][6] = average6;
    elif data2[i][6] == '9':
            data2[i][6] = average6;
    else:
        # deal with first line and null
        data2[i][6] =  average6;

    if data2[i][7] == '0':
            data2[i][7] = 0;
    elif data2[i][7] == '1':
            data2[i][7] = 1;
    elif data2[i][7] == '2':
            data2[i][7] = 2;
    elif data2[i][7] == '3':
            data2[i][7] = 3;
    elif data2[i][7] == '7':
            data2[i][7] = average7;
    elif data2[i][7] == '9':
            data2[i][7] = average7;
    else:
        # deal with first line and null
        data2[i][7] =  average7;

    if data2[i][8] == '0':
            data2[i][8] = 0;
    elif data2[i][8] == '1':
            data2[i][8] = 1;
    elif data2[i][8] == '2':
            data2[i][8] = 2;
    elif data2[i][8] == '3':
            data2[i][8] = 3;
    elif data2[i][8] == '7':
            data2[i][8] = average8;
    elif data2[i][8] == '9':
            data2[i][8] = average8;
    else:
        # deal with first line and null
        data2[i][8] =  average8;


    if data2[i][9] == '0':
            data2[i][9] = 0;
    elif data2[i][9] == '1':
            data2[i][9] = 1;
    elif data2[i][9] == '2':
            data2[i][9] = 2;
    elif data2[i][9] == '3':
            data2[i][9] = 3;
    elif data2[i][9] == '7':
            data2[i][9] = average9;
    elif data2[i][9] == '9':
            data2[i][9] = average9;
    else:
        # deal with first line and null
        data2[i][9] =  average9;

    marks = float(data2[i][1])+float(data2[i][2])+float(data2[i][3])+float(data2[i][4])+float(data2[i][5])+float(data2[i][6])+float(data2[i][7])+float(data2[i][8])+float(data2[i][9]);

    if marks < 10:
        marks1 = 1;
    else:
        marks1 = 0;

    if marks <5:
        marks2 = 1;
    elif marks <10:
        marks2 = 0.75;
    elif marks <15:
        marks2 = 0.5;
    elif marks <20:
        marks2 = 0.25;
    else:
        marks2 = 0;

    data2[i][1] = round(marks, 0);
    data2[i][2] = marks1;
    data2[i][3] = marks2;
    marks = marks2 = marks1 = 0;
# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `ground_truth` ADD `marks` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `ground_truth` SET `marks` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# create new column in table
sql = 'ALTER TABLE `ground_truth` ADD `ground_truth_binary` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `ground_truth` SET `ground_truth_binary` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][2], data2[i][0]));
conn.commit() # very important for update sql server

# create new column in table
sql = 'ALTER TABLE `ground_truth` ADD `ground_truth` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `ground_truth` SET `ground_truth` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][3], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();

# totally 426 marks >10
# 57 marks > 20
# 142 15~19
# 317 10~14
# 850 5~9
# 4558 0~4