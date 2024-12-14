DB_HOST='localhost'
DB_NAME='your_db_name_goes_here'
DB_USER='your_username_goes_here'
DB_PASSWORD='your_password_goes_here'

mysql -u $DB_USER -p$DB_PASSWORD -h $DB_HOST -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

mysql -u $DB_USER -p$DB_PASSWORD -h $DB_HOST $DB_NAME < migrate.sql
mysql -u $DB_USER -p$DB_PASSWORD -h $DB_HOST $DB_NAME < seed.sql