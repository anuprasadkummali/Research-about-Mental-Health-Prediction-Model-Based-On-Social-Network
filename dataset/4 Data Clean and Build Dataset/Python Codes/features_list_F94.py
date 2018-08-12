#wrong file mistake of copy files
import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 2`, `COL 3`, `COL 4` FROM `SMQSMOKING`;';
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

average1 = (7601+1403*0.6667+849*0.3333)/10053; #460
average1 = round(average1, 8);
average2 = (1145+724*0.6667+551*0.3333)/2452; #470
average2 = round(average2, 8);
average3 = (0.1429*7+0.2857*27+0.4286*35+0.5714*49+0.7143*230+0.8571*179+98)/1304; #480
average3 = round(average3, 8);

# calculate and normalise
for i in range(1, size):
    # give option values
    if data2[i][1] == '0':
            data2[i][1] = 1;
    elif data2[i][1] == '1':
            data2[i][1] = 0.6667;
    elif data2[i][1] == '2':
        data2[i][1] = 0.3333;
    elif data2[i][1] == '3':
        data2[i][1] = 0;
    else:
        data2[i][1] = average1;

    if data2[i][2] == '0':
            data2[i][2] = 1;
    elif data2[i][2] == '1':
            data2[i][2] = 0.6667;
    elif data2[i][2] == '2':
        data2[i][2] = 0.3333;
    elif data2[i][2] == '3':
        data2[i][2] = 0;
    elif data2[i][2] == '777':
        data2[i][2] = average2;
    elif data2[i][2] == '999':
        data2[i][2] = average2;
    else:
        data2[i][2] = 1;

    if data2[i][3] == '0':
            data2[i][3] = 1;
    elif data2[i][3] == '1':
            data2[i][3] = 0.8571;
    elif data2[i][3] == '2':
        data2[i][3] = 0.7143;
    elif data2[i][3] == '3':
        data2[i][3] = 0.5714;
    elif data2[i][3] == '4':
            data2[i][3] = 0.4286;
    elif data2[i][3] == '5':
        data2[i][3] = 0.2857;
    elif data2[i][3] == '6':
        data2[i][3] = 0.1429;
    elif data2[i][3] == '7':
            data2[i][3] = 0;
    elif data2[i][3] == '777':
        data2[i][3] = average3;
    elif data2[i][3] == '999':
        data2[i][3] = average3;
    else:
        data2[i][3] = 1;

    x = (float(data2[i][1])+float(data2[i][2])+float(data2[i][3]))/3;
    data2[i][1] = round(x,8);
    x = 0;
#end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F94` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F94` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();