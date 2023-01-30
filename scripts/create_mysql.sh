#!/bin/bash

DB_NAME="nba" DB_HOST="testserver09.mysql.database.azure.com" DB_USER=promise DB_PASSWORD=password@123 python stats/nba_sql.py --default-mode --database="mysql" --create-schema
