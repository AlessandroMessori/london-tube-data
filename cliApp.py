
from sqlDBInit import create_connection

if __name__ == '__main__':
    
    # Getting the type of input the user is looking for (Station or Line)
    inputType = input("Are you looking for Stations or for Lines? (insert s for Stations, any other key for lines): ")

    conn = create_connection("train_network")
    cur = conn.cursor()

    # Getting the line or station to look for from the user
    targetType = "station" if inputType == "s" else "line"
    print("")
    target = input("Type the name of the {} you are looking for: ".format(targetType)) 

    # Running the query to find intersections
    if inputType == "s":
        query = "SELECT L.name FROM Stations AS S, LinesToStations AS LS, Lines AS L WHERE S.id = LS.stationID and L.id = LS.lineID AND S.name = ?"
    else:
        query = "SELECT S.name FROM Stations AS S, LinesToStations AS LS, Lines AS L WHERE S.id = LS.stationID and L.id = LS.lineID AND L.name = ?"

    cur.execute(query, (target,))
    rows = cur.fetchall()

    # We found some intersections, printing the list of results
    if rows: 
        print("")
        if inputType == "s":
            print("List of lines that are intersecting with the {} station:".format(target))
        else:
            print("List of stations that are intersecting with the {} line:".format(target))

        for row in rows:
            print("- ", row[0])
    else: # We didn't find any intersection
        if inputType == "s":
            print("There isn't any line intersecting with the {} station:".format(target))
        else:
            print("There isn't any station intersecting with the {} line:".format(target))

    conn.close()