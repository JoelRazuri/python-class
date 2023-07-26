"""
    a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
    instantes de tiempo (números enteros expresados en segundos), con la condición desde
    < hasta.
    b) Implementar el método duracion que devuelve la duración en segundos del intervalo.
    c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo
    resultante de la intersección entre ambos, o lanzar una excepción si la intersección
    es nula.
    d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes
    ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo intervalo resultante 
    de la unión entre ambos.
"""



class Intervalo:
    def __init__(self,desde,hasta):
        self.desde = desde
        self.hasta = hasta

    def duracion(self):
        # Devuelve la duración en segundos del intervalo.
        return (self.hasta - self.desde)

    def interseccion(self,intervalo_1,intervalo_2):
        # Recibe dos intervalos y devuelve un nuevo intervalo resultante de la intersección entre ambos
        # , o lanzar una excepción si la intersección es nula.
        
        if (intervalo_1.desde>intervalo_2.desde):
            desde = intervalo_1.desde
        else:
            desde = intervalo_2.desde

        if (intervalo_2.hasta<intervalo_1.hasta):
            hasta = intervalo_2.hasta
        else:
            hasta = intervalo_1.hasta

        if desde>hasta:
            desde = 0
            hasta = 0
            intervalo_inter = Intervalo(desde,hasta)
            return intervalo_inter
        else:
            intervalo_inter = Intervalo(desde,hasta)
            return intervalo_inter




intervalo_1 = Intervalo(5,20)
intervalo_2 = Intervalo(-5,3)

print("La duracion del intervalo 1 es " + str(intervalo_1.duracion()))




intervalo_3 = intervalo_1.interseccion(intervalo_1,intervalo_2)

if (intervalo_3.desde == 0 and intervalo_3.hasta == 0):
    print("La intersección es nula.")
else:
    print(f"La interseccion del intervalo 1 ({intervalo_1.desde},{intervalo_1.hasta}) y el intervalo 2 ({intervalo_2.desde},{intervalo_2.hasta}) es ({intervalo_3.desde},{intervalo_3.hasta})")



