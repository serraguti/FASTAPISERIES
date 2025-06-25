import mysql.connector
from models.serie import Serie

class ServiceSeriesMySql():
    def __init__(self):
        self.connection = mysql.connector.connect(host = "servidorpythonfastapi.mysql.database.azure.com", user = "adminsql", password = "MySql123", database = "series")
    
    def getSeries(self):
        sql = "select * from SERIES"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = []
        for row in cursor:
            serie: Serie = Serie()
            serie.id = row[0]
            serie.nombre = row[1]
            serie.imagen = row[2]
            serie.year = row[3]
            data.append(serie)
        cursor.close()
        return data
    
    def findSerie(self, idSerie: int):
        sql = "select * from SERIES where IDSERIE=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (idSerie))
        row = cursor.fetchone()
        if (not row):
            cursor.close()
            return None
        else:
            serie: Serie = Serie()
            serie.id = row[0]
            serie.nombre = row[1]
            serie.imagen = row[2]
            serie.year = row[3]
            cursor.close()
            return serie
    
    def insertSerie(self, idserie:int, nombre: str, imagen: str, year: int):
        sql = "insert into SERIES values (?,?,?,?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (idserie, nombre, imagen, year))
        cursor.commit()
        cursor.close()

    def updateSerie(self, idserie:int, nombre: str, imagen: str, year: int):
        sql = "update SERIES set SERIE=?, IMAGEN=?, ANYO=? where IDSERIE=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, imagen, year, idserie))
        cursor.commit()
        cursor.close()

    def deleteSerie(self, idserie:int):
        sql = "delete from SERIES where IDSERIE=?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (idserie))
        cursor.commit()
        cursor.close()        

    