nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
altura = input("Ingrese su altura: ")
barrio = input("Ingrese el barrio donde vive: ")
calle = input("Ingrese la calle y complemento de residencia: ")
titulos = input("Ingrese titulos adquiridos: ")
cursos = input("Ingrese los cursos que ha realizado: ")
trabajos = input("Ingrese su experiencia laboral")
informacion = tuple((nombre, edad, altura))
direccion = tuple((barrio, calle))
experiencia = tuple((titulos, cursos, trabajos))

print("informaciòn personal:", informacion )
print("Direcciòn:", direccion)
print("Experiencias:",experiencia)
