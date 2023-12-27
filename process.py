# import mysql.connector

def input_process(xInput):
    #x = sql_process("apple")
    xTemp = xInput.decode("utf-8")
    xTempStripped = xTemp.replace('  ', ' ')

    xSplit = xTempStripped.split(" ")
    xOut = ""
    for x in xSplit:
        xOut = xOut + sql_process(x) + " "
    return xOut

def db_connect(xInput):

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='dbjc',
                                             user='root',
                                             password='sql123')

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            #cursor.close()
        print("MySQL connection failedsed")

    return x

def sql_process(xIn):

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='dbjc',
                                             user='root',
                                             password='sql123')

        #sql_select_Query = "select * from tbleng_kor where engRoot = 'apple'"
        sql_select_Query = "select * from tbleng_kor where engRoot = '"
        sql_select_Query = sql_select_Query + xIn
        sql_select_Query = sql_select_Query + "'"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("Id = ", row[0], )
            print("engRoot = ", row[1])
            print("engPart  = ", row[2])
            print("korRoot  = ", row[3], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            #cursor.close()
            #print("MySQL connection is closed")

    return row[3]
