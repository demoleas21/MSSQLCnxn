"""SQL Connection"""

import pymssql
from os import getenv

server = getenv("WIN-HKE58QH56U4\LYTECMD")  # Server name
user = getenv("sa")                         # User name for db
password = getenv("Clinical$1")             # Password for db

if __name__=='__main__':
    conection = pymssql.connect(server, user, password, "LytecMD") # Create connection object
    cursor = connection.cursor() # Used to define result set
    cursor.execute("""
        SELECT * FROM "Lytec Tutorial".dbo.Patient 
        """)
    row = cursor.fetchone() # Gets row
    while row:
        """Used to iteate rows"""
        print("Last name: {}, First name: {}".format(row[1], row[2]))

    connection.close() # Must close connection when finished