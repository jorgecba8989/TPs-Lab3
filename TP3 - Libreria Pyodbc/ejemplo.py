import pyodbc

# CONFIGURACION PARA ACCESO A LA BASE DE DATOS
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' 
                        'Server=localhost;' 
                        'Database=testPy;' 
                        'UID=sa;' 
                        'PWD=jmilia')
cursor = conn.cursor();



# VISUALIAZACION DE LOS REGISTROS DE LA TABLA PERSONAS
cursor.execute('select * from personas')
print('Tabla original...')
for dato in cursor:
    print(dato)

print(" ") #PARA HACER UN SALTO DE LINEA ENTRE BLOQUE DE DATOS



# INSERCION DE NUEVOS REGISTROS
cursor.execute('''
                INSERT INTO personas (id_persona, nombre_persona, dni)
                VALUES
                (4,'jhon',2100021),
                (5,'maira', 7058473)
                ''')
conn.commit ()


cursor.execute('select * from personas')
print('Tabla con nuevos registros insertados...')
for dato in cursor:
    print(dato)

print(" ") #PARA HACER UN SALTO DE LINEA ENTRE BLOQUE DE DATOS



# ACTUALIZACION DE UN REGISTRO Y VISUALIZACION DE LA TABLA MODIFICADA
cursor.execute ('''
                update personas
                SET nombre_persona = 'pepo' 
                where dni = 2100021
                ''')
conn.commit ()


cursor.execute('select * from personas')
print('Tabla con el registro modificado...')
for dato in cursor:
    print(dato)

print(" ") #PARA HACER UN SALTO DE LINEA ENTRE BLOQUE DE DATOS



# ELIMINACION DE UN REGISTRO Y VISUALIZACION DE LA TABLA MODIFICADA
cursor.execute ('''
                delete personas
                where dni = 50999888
                ''')
conn.commit ()


cursor.execute('select * from personas')
print('Tabla con un registro eliminado...')
for dato in cursor:
    print(dato)

print(" ") #PARA HACER UN SALTO DE LINEA ENTRE BLOQUE DE DATOS


# VISUALIZACION DE UN REGISTRO CON PK COMPUESTA
cursor.execute ('''
                select p.nombre_persona, e.nombre_empresa 
                from personas p
                join personas_empresas pe on pe.id_persona = p.id_persona
                join empresas e on pe.id_empresa = e.id_empresa 
                where p.id_persona = 1
                ''')

print('Mostrar en que empresa/s trabaja la persona con id=1 ...')
for dato in cursor:
    print(dato)

