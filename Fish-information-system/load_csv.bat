type *.sql | mysql -u root -p
mysqlimport --ignore-lines=1  --fields-terminated-by=,  --local -u root -p fish_db  fishes_table.csv
@M1r@rsh1@m1rz@e181