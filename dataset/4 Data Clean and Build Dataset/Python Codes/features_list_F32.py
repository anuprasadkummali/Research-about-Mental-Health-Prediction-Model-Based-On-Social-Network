import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 91`, `COL 92`, `COL 93`, `COL 94` FROM `MCQ`;';
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

average1 = 3923/6460; # 370a
average1 = round(average1, 8);
average2 = 3816/6463; # 370b
average2 = round(average2, 8);
average3 = 3198/6462; # 370c
average3 = round(average3, 8);
average4 = 3454/6460; # 370d
average4 = round(average4, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '1':
        data2[i][1] = 1;
    elif data2[i][1] == '2':
        data2[i][1] = 0;
    elif data2[i][1] == '7':
        data2[i][1] = average1;
    elif data2[i][1] == '9':
        data2[i][1] = average1;
    else:
        data2[i][1] =  average1;

    if data2[i][2] == '1':
        data2[i][2] = 1;
    elif data2[i][2] == '2':
        data2[i][2] = 0;
    elif data2[i][2] == '7':
        data2[i][2] = average2;
    elif data2[i][2] == '9':
        data2[i][2] = average2;
    else:
        data2[i][2] = average2;

    if data2[i][3] == '1':
        data2[i][3] = 1;
    elif data2[i][3] == '2':
        data2[i][3] = 0;
    elif data2[i][3] == '7':
        data2[i][3] = average3;
    elif data2[i][3] == '9':
        data2[i][3] = average3;
    else:
        data2[i][3] = average3;

    if data2[i][4] == '1':
        data2[i][4] = 1;
    elif data2[i][4] == '2':
        data2[i][4] = 0;
    elif data2[i][4] == '7':
        data2[i][4] = average4;
    elif data2[i][4] == '9':
        data2[i][4] = average4;
    else:
        data2[i][4] = average4;

    data2[i][1] = (float(data2[i][1])+float(data2[i][2])+float(data2[i][3])+float(data2[i][4]))/4;
# end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F32` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F32` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();