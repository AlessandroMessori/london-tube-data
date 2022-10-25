
from sqlDBInit import create_connection

if __name__ == '__main__':
    
    inputType = input("Are you looking for Stations or for Lines? (insert s for Stations, any other key for lines)")

    conn = create_connection("train_network")
    cur = conn.cursor()

    if inputType == "s":
        station = input("What Station are you looking for?")
        cur.execute("SELECT * FROM Stations AS S, LinesToStations AS LS, Lines AS L WHERE S.id = LS.stationID and L.id = LS.lineID AND S.name = ?", (station,))

        rows = cur.fetchall()

        for row in rows:
            print(row)
    else:
        line = input("What Line are you looking for?")
        cur.execute("SELECT * FROM Stations AS S, LinesToStations AS LS, Lines AS L WHERE S.id = LS.stationID and L.id = LS.lineID AND L.name = ?", (line,))

        rows = cur.fetchall()

        for row in rows:
            print(row)

    conn.close()