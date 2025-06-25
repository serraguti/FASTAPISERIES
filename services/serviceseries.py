import pyodbc
from models.serie import Serie

class ServiceSeries():
    servidor = "sqltajamarpgs.database.windows.net"
    bbdd = "AZURETAJAMAR"
    usuario = "adminsql"
    password = "Admin123"

    def __init__(self):
        self.connectionString = "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + self.servidor + "; DATABASE=" + self.bbdd + "; UID=" + self.usuario + "; PWD=" + self.password    
        self.connection = pyodbc.connect(self.connectionString)
    
    def getSeries(self):
        sql = "select * from SERIES"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = []
        for row in cursor:
            serie: Serie = Serie()
            serie.id = row.IDSERIE
            serie.nombre = row.SERIE
            serie.imagen = row.IMAGEN
            serie.year = row.ANYO
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
            serie.id = row.IDSERIE
            serie.nombre = row.SERIE
            serie.imagen = row.IMAGEN
            serie.year = row.ANYO
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

    