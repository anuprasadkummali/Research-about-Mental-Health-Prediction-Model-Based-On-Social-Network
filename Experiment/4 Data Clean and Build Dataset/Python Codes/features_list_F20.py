import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 4`, `COL 5`, `COL 7`, `COL 8` FROM `ALQ`;';
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

average1 = 0;
average2 = 0;
average3 = 0;
average4 = 0;
num1 = 0;
num2 = 0;
num3 = 0;
num4 = 0;

for i in range(1, size):
    if data2[i][1]!='#NULL!' and float(data2[i][1])>= 0 and float(data2[i][1])<400:
        average1 = average1 + float(data2[i][1]);
        num1 = num1 + 1;
    if data2[i][2]!='#NULL!' and float(data2[i][2])>= 0 and float(data2[i][2])<400:
        average2 = average2 + float(data2[i][2]);
        num2 = num2 + 1;
    if data2[i][3]!='#NULL!' and float(data2[i][3])>= 0 and float(data2[i][3])<400:
        average3 = average3 + float(data2[i][3]);
        num3 = num3 + 1;
    if data2[i][4]!='#NULL!' and float(data2[i][4])>= 0 and float(data2[i][4])<400:
        average4 = average4 + float(data2[i][4]);
        num4 = num4 + 1;
# end of loop

average1 = average1/num1;
average2 = average2/num2;
average3 = average3/num3;
average4 = average4/num4;

# calculate and normalise
for i in range(1, size):
    # give option values
    # 120Q
    if data2[i][1] == '777':
            data2[i][1] = average1;
    elif data2[i][1] == '999':
            data2[i][1] = average1;
    elif data2[i][1] == '#NULL!':
            data2[i][1] = average1;
    else:
        # deal with first line and null
        data2[i][1] =  data2[i][1];

    # 120U
    if data2[i][2] == '1':
        data2[i][2] = 52;
    elif data2[i][2] == '2':
        data2[i][2] = 12;
    elif data2[i][2] == '3':
        data2[i][2] = 1;
    elif data2[i][2] == '#NULL!':
        data2[i][2] = average2;
    else:
        # deal with first line and null
        data2[i][2] = average2;

    # 141Q
    if data2[i][3] == '777':
            data2[i][3] = average3;
    elif data2[i][3] == '999':
            data2[i][3] = average3;
    elif data2[i][3] == '#NULL!':
            data2[i][3] = average3;
    else:
        # deal with first line and null
        data2[i][3] =  data2[i][3];

    # 141U
    if data2[i][4] == '1':
        data2[i][4] = 52;
    elif data2[i][4] == '2':
        data2[i][4] = 12;
    elif data2[i][4] == '3':
        data2[i][4] = 1;
    elif data2[i][4] == '#NULL!':
        data2[i][4] = average4;
    else:
        # deal with first line and null
        data2[i][2] = average4;

    data2[i][1] = float(data2[i][1])*float(data2[i][2]);
    data2[i][3] = float(data2[i][3]) * float(data2[i][4]);
    if data2[i][1] < data2[i][3]:
        data2[i][1] = data2[i][3];
    data2[i][1] = 1 - float(data2[i][1])/365;
    if float(data2[i][1]) < 0:
        data2[i][1] = 0;
    # end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F20` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F20` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();