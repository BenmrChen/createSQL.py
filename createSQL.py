#coding:utf-8
import csv

temp_sql = 'UPDATE `tableA`  INNER JOIN `tableB` ON `tableA`.`foreign_id` = `tableB`.`id` SET `setting_value`  = "{setting_value}" WHERE `tableB`.`test_name` = "{test_name}";'

with open('/your-path-to-file/testFile.csv') as csvfile:  # 打開 csv
    rows = csv.reader(csvfile, ) # 將 csv 內容一行一行存到 rows
    next(rows);
    for row in rows: # 一列一列更新
        print (temp_sql.replace('{setting_value}','{number' + row[2] + '}').replace('{prod_level2_oid}',row[3])) # row[2]代表第二欄 、row[3]代表第三欄