CREATE USER IF NOT EXISTS 'mahya'@'%' IDENTIFIED BY '201828Bar';
CREATE USER IF NOT EXISTS 'shima'@'%' IDENTIFIED BY 'Shima2024';
CREATE USER IF NOT EXISTS 'app'@'%' IDENTIFIED BY 'CT4WzxeLhHOwxTdoU1TThQzMpD3TwWp4';
CREATE ROLE IF NOT EXISTS 'Auth_developer','fish_admin','app_wr';
GRANT ALL PRIVILEGES ON fish_db.* TO  'app_wr' ;
GRANT ALL PRIVILEGES ON  fish_db.fishes_table TO 'fish_admin';
GRANT 'fish_admin' to  'mahya'@'%';
GRANT 'app_wr' to 'app'@'%';
FLUSH PRIVILEGES;