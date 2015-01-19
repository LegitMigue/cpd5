from multiprocessing.connection import Client
from array import array
address = ('localhost',6000)
conn = Client(address, authkey= 'josemi')
conn.send('close')
conn.send(['a', 2.5, None, int, sum]) # Se pueden enviar objetos arbitrarios
conn.close()
print "Conexion exitosa"