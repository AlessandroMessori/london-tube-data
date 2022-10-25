import json
from sqlDBInit import create_connection

tube_data_file = open('./train-network.json')

tube_data = json.load(tube_data_file)

def writeStationsTable(stations, conn):

    cursor = conn.cursor()

    stationRows = []

    for station in stations:
        stationRows.append((
            station["id"], 
            station["name"]
        ))

    insertQuery = """ insert into Stations(id, name) values (?, ?) """

    try:
        cursor.executemany(insertQuery, stationRows)
        conn.commit()
        print("Stations data inserted into SQLite DB correctly")
    except Exception as e:
        conn.rollback()
        print("There was a mistake during the writing of the records in the DB")
        print(e)

def writeLinesTable(lines, cursor, conn):

    linesRows = []

    for line in lines:
        stationRows.append((
            station["id"], 
            station["name"]
        ))

    insertQuery = """ insert ignore into Stations (
         ) 
        values (%s,%s)           
    """

    try:
        cursor.executemany(insertQuery, stationRows)
        conn.commit()
    except:
        conn.rollback()


if __name__ == '__main__':
    conn = create_connection("train_network")
    cursor = conn.cursor()

    writeStationsTable(tube_data["stations"], conn)

    conn.close()

#print(tube_data)