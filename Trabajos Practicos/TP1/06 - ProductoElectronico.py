class ProductoElectronico:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.disponibilidad = True
        self.garantia = True
        
    def comprar(self):
        if self.disponibilidad == True:
            self.disponibilidad = False
            return f"El producto {self.nombre} - {self.marca} fue vendido"
        else:
            return "Producto no disponible"
    
    def verificarGarantia(self, defectos):
        if self.garantia:
            if defectos:
                return f"El producto {self.nombre} de la marca {self.marca} tiene defectos. Se puede usar la garantia"
            else:
                return f"El producto {self.nombre} de la marca {self.marca} no tiene defectos. No es necesario usar la garantia"
        else:
            return f"El producto {self.nombre} de la marca {self.marca} no tiene garantia vigente"
            
    def __str__(self):
        return f"Producto: {self.nombre} - Marca: {self.marca} - Precio: {self.precio} - Disponible: {self.disponibilidad}"

ventilador = ProductoElectronico("Ventilador", "Liliana", 50000)
print(ventilador)
print(ventilador.comprar())
print(ventilador)
print(ventilador.verificarGarantia(True))
print(ventilador.verificarGarantia(False))
