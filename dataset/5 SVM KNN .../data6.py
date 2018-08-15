# Import Library
import pymysql
import numpy
import sklearn
import scipy
import pandas
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier


# Read data from csv file
data = pandas.read_csv("data.csv");
# print(data.head());

# Divide data into training data and ground truth
QN = data['QN'];
F1 = data['F1'];
F1 = data['F1'];
F2 = data['F2'];
F3 = data['F3'];
F4 = data['F4'];
F5 = data['F5'];
F6 = data['F6'];
F7 = data['F7'];
F8 = data['F8'];
F9 = data['F9'];
F10 = data['F10'];
F11 = data['F11'];
F12 = data['F12'];
F13 = data['F13'];
F14 = data['F14'];
F15 = data['F15'];
F16 = data['F16'];
F17 = data['F17'];
F18 = data['F18'];
F19 = data['F19'];
F20 = data['F20'];
F21 = data['F21'];
F22 = data['F22'];
F23 = data['F23'];
F24 = data['F24'];
F25 = data['F25'];
F26 = data['F26'];
F27 = data['F27'];
F28 = data['F28'];
F29 = data['F29'];
F30 = data['F30'];
F31 = data['F31'];
F32 = data['F32'];
F33 = data['F33'];
F34 = data['F34'];
F35 = data['F35'];
F36 = data['F36'];
F37 = data['F37'];
F38 = data['F38'];
F39 = data['F39'];
F40 = data['F40'];
F41 = data['F41'];
F42 = data['F42'];
F43 = data['F43'];
F44 = data['F44'];
F45 = data['F45'];
F46 = data['F46'];
F47 = data['F47'];
F48 = data['F48'];
F49 = data['F49'];
F50 = data['F50'];
F51 = data['F51'];
F52 = data['F52'];
F53 = data['F53'];
F54 = data['F54'];
F55 = data['F55'];
F56 = data['F56'];
F57 = data['F57'];
F58 = data['F58'];
F59 = data['F59'];
F60 = data['F60'];
F61 = data['F61'];
F62 = data['F62'];
F63 = data['F63'];
F64 = data['F64'];
F65 = data['F65'];
F66 = data['F66'];
F67 = data['F67'];
F68 = data['F68'];
F69 = data['F69'];
F70 = data['F70'];
F71 = data['F71'];
F72 = data['F72'];
F73 = data['F73'];
F74 = data['F74'];
F75 = data['F75'];
F76 = data['F76'];
F77 = data['F77'];
F78 = data['F78'];
F79 = data['F79'];
F80 = data['F80'];
F81 = data['F81'];
F82 = data['F82'];
F83 = data['F83'];
F84 = data['F84'];
F85 = data['F85'];
F86 = data['F86'];
F87 = data['F87'];
F88 = data['F88'];
F89 = data['F89'];
F90 = data['F90'];
F91 = data['F91'];
F92 = data['F92'];
F93 = data['F93'];
F94 = data['F94'];
F95 = data['F95'];
F96 = data['F96'];
F97 = data['F97'];
F98 = data['F98'];
ground_truth = data['ground_truth'];
ground_truth_binary = data['ground_truth_binary'];

physical = [None] * 5398;
role = [None] * 5398;
social = [None] * 5398;
mental = [None] * 5398;
general = [None] * 5398;
pain = [None] * 5398;

for i in range(0, 5398):
    physical[i] = F1[i] + F2[i] + F3[i] + F16[i] + F17[i] + F31[i] + F80[i];
    role[i] = F2[i] + F8[i] + F18[i] + F23[i] + F26[i] + F46[i] + F66[i] + F85[i] + F95[i];
    social[i] = F4[i] + F6[i] + F7[i] + F22[i] + F32[i] + F67[i];
    mental[i] = F34[i] + F50[i] + F78[i] + F98[i];
    pain[i] = F83[i] + F90[i];
    general[i] = 0;

    for k in range(1, 99):
        general[i] = general[i] + data['F'+ str(k)][i];
    general[i] = general[i] - physical[i] - role[i] - social[i] - mental[i] - pain[i];

    physical[i] = physical[i]/7;
    role[i] = role[i]/9;
    social[i] = social[i]/6;
    mental[i] = mental[i]/4;
    pain[i] = pain[i]/2;
    general[i] = general[i]/(98-7-9-6-4-2);

    # Convert numpy float64 into float
    physical[i] = physical[i].astype(type('float', (float,), {}));
    role[i] = role[i].astype(type('float', (float,), {}));
    social[i] = social[i].astype(type('float', (float,), {}));
    mental[i] = mental[i].astype(type('float', (float,), {}));
    pain[i] = pain[i].astype(type('float', (float,), {}));
    general[i] = general[i].astype(type('float', (float,), {}));
# connection
conn = pymysql.connect(host='localhost', user='root', password='y2x8JQOR7KaWDGJb', db='NHANES2014')

cursor = conn.cursor()

# create new column in table
sql = 'ALTER TABLE `data6` ADD `physical` VARCHAR(10) NOT NULL;';
cursor.execute(sql);
# store into correct table in DB
query = 'UPDATE `data6` SET `physical` = %s WHERE `QN` = %s;';
for i in range(0, 5398):
    cursor.execute(query, (round(physical[i], 8), int(QN[i])));
    conn.commit() # very important for update sql server

# create new column in table
sql = 'ALTER TABLE `data6` ADD `role` VARCHAR(10) NOT NULL;';
cursor.execute(sql);
# store into correct table in DB
query = 'UPDATE `data6` SET `role` = %s WHERE `QN` = %s;';
for i in range(0, 5398):
    cursor.execute(query, (round(role[i],8), int(QN[i])));
    conn.commit()  # very important for update sql server

# create new column in table
sql = 'ALTER TABLE `data6` ADD `social` VARCHAR(10) NOT NULL;';
cursor.execute(sql);
# store into correct table in DB
query = 'UPDATE `data6` SET `social` = %s WHERE `QN` = %s;';
for i in range(0, 5398):
    cursor.execute(query, (round(social[i],8), int(QN[i])));
    conn.commit()  # very important for update sql server

# create new column in table
sql = 'ALTER TABLE `data6` ADD `mental` VARCHAR(10) NOT NULL;';
cursor.execute(sql);
# store into correct table in DB
query = 'UPDATE `data6` SET `mental` = %s WHERE `QN` = %s;';
for i in range(0, 5398):
    cursor.execute(query, (round(mental[i], 8), int(QN[i])));
    conn.commit()  # very important for update sql server

# create new column in table
sql = 'ALTER TABLE `data6` ADD `pain` VARCHAR(10) NOT NULL;';
cursor.execute(sql);
# store into correct table in DB
query = 'UPDATE `data6` SET `pain` = %s WHERE `QN` = %s;';
for i in range(0, 5398):
    cursor.execute(query, (round(pain[i], 8), int(QN[i])));
    conn.commit()  # very important for update sql server

# create new column in table
sql = 'ALTER TABLE `data6` ADD `general` VARCHAR(10) NOT NULL;';
cursor.execute(sql);
# store into correct table in DB
query = 'UPDATE `data6` SET `general` = %s WHERE `QN` = %s;';
for i in range(0, 5398):
    cursor.execute(query, (round(general[i],8), int(QN[i])));
    conn.commit()  # very important for update sql server

# close connection
cursor.close();
del cursor;
conn.close();

