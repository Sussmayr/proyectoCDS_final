from Conexion import conn

try:
    # mostrar valores de SQL
    with conn.cursor() as cursor:
        cursor.execute("Select * from usuarios;")

        result = cursor.fetchone()

        while result:
            print(result)
            result = cursor.fetchone()

    # Actualizar datos
    while True:
        Actualizar = input("Quieres actualzar un registro? s/n ")
        if Actualizar.lower() == "s":
            with conn.cursor() as cursor:
                id = input("ingresa el id del registro a modificar: ")
                consultaverificacion = ("select id from usuarios where id = ?;")
                cursor.execute(consultaverificacion, (id))
                result = cursor.fetchone()
                print(result)
                if result:
                    Name = input("Ingrese un nuevo usuario: ")
                    password = input("Ingrese un nuevo password: ")

                    consulta = "update usuarios SET Name = ?, pass = ? where id = ?"
                    cursor.execute(consulta, (Name, password, id))
                    conn.commit()
                    print("Su registro ha sido actualizado")
                else:
                    print("el ID ingresado es incorrecto")
        else:
            print("salio de opcion")
            break
    
    # Eliminar datos
    while True:
        elimiar = input("quieres eliminar? s/n ")
        if elimiar.lower() == "s":
            with conn.cursor() as cursor:
                id = input("ingresa el id del registro a eliminar: ")
                consultaverificacion = ("select id from usuarios where id = ?;")
                cursor.execute(consultaverificacion, (id))
                result = cursor.fetchone()
                print(result)
                if result:
                    consulta = "Delete from usuarios where id = ?;"
                    cursor.execute(consulta, (id))

                    conn.commit()
                    print("su registro se elimino")
                else:
                    print("el ID ingresado es incorrecto")
        else:
            print("salio de opcion")
            break

except Exception as e:
    print("ocurrio un error:", e)
finally:
    conn.close()