import json
import hashlib
from sqlDBInit import create_connection


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

def writeLinesTable(lines, conn):

    cursor = conn.cursor()

    linesRows = []
    lineToStationsRow = []

    for line in lines:
        currentLineID = getIdFromName(line["name"])

        linesRows.append((
            currentLineID,
            line["name"]
        ))

        for stationID in line["stations"]:
            lineToStationsRow.append((
                currentLineID,
                stationID
             )
            )

    insertQueryLines = """ insert into Lines(id, name) values (?, ?) """

    try:
        cursor.executemany(insertQueryLines, linesRows)
        conn.commit()
        print("Lines data inserted into SQLite DB correctly")
    except Exception as e:
        conn.rollback()
        print("There was a mistake during the writing of the Line records in the DB")
        print(e)
    
    insertQueryLinesToStations = """ insert into LinesToStations(lineID, stationID) values (?, ?) """

    try:
        cursor.executemany(insertQueryLinesToStations, lineToStationsRow)
        conn.commit()
        print("Lines data inserted into SQLite DB correctly")
    except Exception as e:
        conn.rollback()
        print("There was a mistake during the writing of the LineToStations records in the DB")
        print(e)

def getIdFromName(name): # Generates an unique id from a name string
    m = hashlib.md5()
    m.update(name.encode('utf-8'))
    return m.hexdigest()

if __name__ == '__main__':

    tube_data_file = open('./train-network.json')
    tube_data = json.load(tube_data_file)              # load JSON dataset into list of dictionaries

    conn = create_connection("train_network")          # connects to the SQLite DB

    writeStationsTable(tube_data["stations"], conn)    # writes the station data to the DB

    writeLinesTable(tube_data["lines"], conn)          # writes the lines data to the DB

    conn.close()