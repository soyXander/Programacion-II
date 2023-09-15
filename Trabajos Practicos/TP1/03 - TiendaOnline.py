class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio}"

class TiendaOnline:
    def __init__(self, nombre_tienda, productos_disponibles, ubicacion, ventas_mensuales):
        self.nombre_tienda = nombre_tienda
        self.productos_disponibles = productos_disponibles
        self.ubicacion = ubicacion
        self.ventas_mensuales = ventas_mensuales
        
    def buscar_producto(self, producto):
        for p in self.productos_disponibles:
            if p.nombre == producto:
                return p
        return "No se encuentra el producto"
        
    def calcular_descuento(self, monto_compra):
        if monto_compra >= 200:
            return monto_compra * 0.8
        elif monto_compra >= 100:
            return monto_compra * 0.9
        else:
            return monto_compra
        
productos = [Producto("Pan", 50), Producto("Gaseosa", 120), Producto("Cigarrillo", 210)]
palote = TiendaOnline("Palote 24", productos, "Av. Facundo Quiroga", 250)
print(palote.buscar_producto("Pan"))
print(palote.calcular_descuento(100))
print(palote.buscar_producto("Gaseosa"))