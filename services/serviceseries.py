import pyodbc
from models.serie import Serie

class ServiceSeries():
    servidor = "sqltajamarpgs.database.windows.net"
    bbdd = "AZURETAJAMAR"
    usuario = "adminsql"
    password = "Admin123"

    def __init__(self):
        self.connectionString = "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + self.servidor + "; DATABASE=" + self.bbdd + "; UID=" + self.usuario + "; PWD=" + self.password    
        self.conection = pyodbc.connect(self.connectionString)
    
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
        self.conection.close()
        return data