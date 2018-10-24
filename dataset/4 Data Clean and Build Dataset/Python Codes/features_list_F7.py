import pymysql
import decimal
import numpy

# connect to DB
conn = pymysql.connect(host='localhost', user='root', password='', db='NHANES2014_Features', autocommit=True);
cursor = conn.cursor();

# select input
sql = 'SELECT `COL 1`, `COL 2`, `COL 3`, `COL 4`, `COL 5`, `COL 6` FROM `CBQ`;';
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

average1 = 0; #070
average2 = 0; #090
average3 = 0; #110
average4 = 0; #120
average5 = 0; #130
num1 = num2 = num3 = num4 = num5 = 0;

# calculate average
for i in range(1, size):
    if data2[i][1] != '#NULL!' and float(data2[i][1])>0 and float(data2[i][1])<5000:
        average1 = average1 + float(data2[i][1]);
        num1 = num1 + 1;

    if data2[i][2] != '#NULL!' and float(data2[i][2])>0 and float(data2[i][2])<5000:
        average2 = average2 + float(data2[i][2]);
        num2 = num2 + 1;

    if data2[i][3] != '#NULL!' and float(data2[i][3])>0 and float(data2[i][3])<5000:
        average3 = average3 + float(data2[i][3]);
        num3 = num3 + 1;

    if data2[i][4] != '#NULL!' and float(data2[i][4]) > 0 and float(data2[i][4]) < 5000:
        average4 = average4 + float(data2[i][4]);
        num4 = num4 + 1;

    if data2[i][5] != '#NULL!' and float(data2[i][5]) > 0 and float(data2[i][5]) < 5000:
        average5 = average5 + float(data2[i][5]);
        num5 = num5 + 1;
# end of loop

average1 = round(average1/num1, 8);
average2 = round(average2/num2, 8);
average3 = round(average3/num3, 8);
average4 = round(average4/num4, 8);
average5 = round(average5/num5, 8);
print(average1);
print(average2);
print(average3);
print(average4);
print(average5);

# calculate and normalise
for i in range(1, size):
    # give option values
    #
    if data2[i][1] == '777777':
        data2[i][1] = average1;
    elif data2[i][1] == '999999':
        data2[i][1] = average1;
    elif data2[i][1] == '#NULL!':
        data2[i][1] = average1;
    else:
        data2[i][1] =  float(data2[i][1]);

    if data2[i][3] == '777777':
        data2[i][3] = average3;
    elif data2[i][3] == '999999':
        data2[i][3] = average3;
    elif data2[i][3] == '#NULL!':
        data2[i][3] = average3;
    else:
        data2[i][3] =  float(data2[i][3]);

    if data2[i][4] == '777777':
        data2[i][4] = average4;
    elif data2[i][4] == '999999':
        data2[i][4] = average4;
    elif data2[i][4] == '#NULL!':
        data2[i][4] = average4;
    else:
        data2[i][4] =  float(data2[i][4]);

    if data2[i][5] == '777777':
        data2[i][5] = average5;
    elif data2[i][5] == '999999':
        data2[i][5] = average5;
    elif data2[i][5] == '#NULL!':
        data2[i][5] = average5;
    else:
        data2[i][5] =  float(data2[i][5]);

    if float(data2[i][1])==0 and float(data2[i][3])==0 and float(data2[i][4])==0 and float(data2[i][5])==0:
        data2[i][1] = 1-(average4+average5)/(average1+average3+average4+average5);
    else:
        data2[i][1] = 1-(float(data2[i][4])+float(data2[i][5])) /(float(data2[i][1])+float(data2[i][3])+float(data2[i][4])+float(data2[i][5]));
# end of loop

# test and valid values after first line
print(data2);

# create new column in table
sql = 'ALTER TABLE `features_list` ADD `F7` VARCHAR(10) NOT NULL;';
cursor.execute(sql);

# store into correct table in DB
query = 'UPDATE `features_list` SET `F7` = %s WHERE `QN` = %s;'
for i in range(1, size):
     cursor.execute(query, (data2[i][1], data2[i][0]));
conn.commit() # very important for update sql server

# close DB
cursor.close();
del cursor;
conn.close();