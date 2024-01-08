"""
Se desea tener un sistema de notas para los alumnos. Cada alumno se registra
con un DNI, un Nombre y un listado de notas. Las notas tienen el nombre de la
materia y el valor númerico de la nota.

Se desea además, tener una base de datos sencilla en formato JSON.

Restricciones:
- Utilizar 2 dataclasses
- No utilizar métodos de instancia
- No utilizar métodos de clase
"""



# NO MODIFICAR - INICIO
juan_programacion_1 = Nota("Programación 1", 6)
maria_programacion_1 = Nota("Programación 1", 8)
maria_programacion_2 = Nota("Programación 2", 6)
pedro_base_de_datos = Nota("Base de datos", 5)

init_data = [
    Estudiante("47526381", "Juan", [juan_programacion_1]),
    Estudiante("46193480", "María", [maria_programacion_1, maria_programacion_2]),
    Estudiante("43796248", "Pedro", [pedro_base_de_datos])
]

db = TinyDB(f"{Path(__file__).parent}/db.json", **DATABASE_PARAMS)
db.default_table_name = "estudiantes"
db.truncate()


for estudiante in init_data:
    insert_estudiante(estudiante)

todos = get_all()
assert todos == init_data

juan = get_by_dni(dni="47526381")

print(juan)
print(init_data[0])

assert juan == init_data[0]

delete_by_id(juan.dni)

todos = get_all()

assert todos == init_data[1:]

maria = todos[0]

maria.notas = maria.notas + [Nota("Base de datos", 8)]

update(maria)

maria_actualizada = get_all()[0]
assert maria_actualizada == maria
# NO MODIFICAR - FIN
