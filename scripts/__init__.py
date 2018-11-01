#
#  sudo apt-get update
#  sudo apt install python-pip
#  https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-2017
#  Ubuntu 14.04, 16.04, 17.10 and 18.04
#  pip install pyodbc
#  sudo su
#  wget https://gallery.technet.microsoft.com/ODBC-Driver-13-for-Ubuntu-b87369f0/file/154097/2/installodbc.sh
#    sh installodbc.sh

#import pypyodbc
#cnxn = pypyodbc.connect("Driver={SQL Server};"
#                      "Server=localhost;"
#                      "Database=master;"
#                      "Trusted_Connection=yes;")
#  cursor = cnxn.cursor()
#  cursor.execute('SELECT * FROM dbo.MSreplication_options')
#  for row in cursor:
#      print('row = %r' % (row,))
#import pyodbc
#import pandas as pd

#print pyodbc.drivers()
#conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=OVIDIU;DATABASE=BIGDATA;UID=sa;PWD=Student170034')
#df = pd.read_sql_query('select * from dbo.MSreplication_options ', cnxn)
#

import pyodbc
conn_str = (
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=OVIDIU;'
    r'DATABASE=BIGDATA;'
    r'Trusted_Connection=yes;'
)
cnxn = pyodbc.connect(conn_str)