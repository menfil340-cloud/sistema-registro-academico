
# ==========================================
# PROYECTO FINAL: Sistema de Registro Académico
# Asignatura: Programación Estructurada
# Estudiante: Menfi Augusto López Sovalbarro
# ==========================================

# PASO 1: Estructura de datos
# Lista para guardar los datos de todos los estudiantes
estudiantes = []

print("--- SISTEMA DE REGISTRO DE CALIFICACIONES ---")

# Utilizamos un ciclo for para registrar a 3 estudiantes
for i in range(3):
    print(f"\n--- Ingresando datos del Estudiante {i + 1} ---")

    nombre = input("Nombre y Apellido: ")

    # PASO 2: Validaciones
    # Solicitamos las notas y evitamos que el programa colapse
    try:
        nota1 = float(input("Nota del Parcial 1: "))
        nota2 = float(input("Nota del Parcial 2: "))

    except ValueError:
        print(
            "Error: Ingresaste un valor no válido. "
            "Se asignará 0 a ambas notas."
        )
        nota1 = 0.0
        nota2 = 0.0

    # PASO 3: Cálculo de la nota final
    nota_final = (nota1 + nota2) / 2

    # Guardamos los datos del estudiante en una lista
    estudiantes.append([nombre, nota1, nota2, nota_final])


# PASO 4: Evaluación de resultados
print("\n==========================================")
print("REPORTE FINAL DE ESTUDIANTES")
print("==========================================")

for alumno in estudiantes:
    # Extraemos los datos de la lista
    nombre_alumno = alumno[0]
    promedio = alumno[3]

    # Determinamos el estado académico
    if promedio < 60:
        estado = "Reprobado"

    elif promedio > 95:
        estado = "Sobresaliente"

    else:
        estado = "Aprobado"

    # Mostramos los resultados
    print(
        f"Estudiante: {nombre_alumno} | "
        f"Promedio: {promedio:.2f} | "
        f"Estado: {estado}"
    )

print("==========================================")
print("Registro finalizado.")
