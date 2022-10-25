import json
from sqlDBInit import create_connection

tube_data_file = open('./train-network.json')

tube_data = json.load(tube_data_file)

def writeStationsTable(stations, cursor, conn):

    stationRows = []

    for station in stations:
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

