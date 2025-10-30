from datetime import datetime

# ===========================================
#           CLASES CON HERENCIA
# ===========================================

class Persona:
    def __init__(self, nombre, correo, direccion, telefono):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")


class Cliente(Persona):  # Hereda de Persona
    def __init__(self, nombre, correo, direccion, telefono, rfc):
        super().__init__(nombre, correo, direccion, telefono)
        self.rfc = rfc

    def mostrar_info(self):
        super().mostrar_info()
        print(f"RFC: {self.rfc}")
        print("-----------------------------------------")


class Empleado(Persona):  # Hereda de Persona
    def __init__(self, nombre, correo, direccion, telefono, id_empleado, departamento, usuario, contrasena):
        super().__init__(nombre, correo, direccion, telefono)
        self.id_empleado = id_empleado
        self.departamento = departamento
        self.usuario = usuario
        self.contrasena = contrasena

    def mostrar_info(self):
        super().mostrar_info()
        print(f"ID Empleado: {self.id_empleado}")
        print(f"Departamento: {self.departamento}")
        print("-----------------------------------------")


# ===========================================
#           CLASES DEL INVENTARIO
# ===========================================

class Producto:
    def __init__(self, codigo, nombre, categoria, precio_unitario):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio_unitario = precio_unitario

    def mostrar_info(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio unitario: ${self.precio_unitario:.2f}")
        print("-----------------------------------------")


class InventarioProducto:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.vendidos = 0

    def disponibles(self):
        return self.cantidad - self.vendidos

    def vender(self, cantidad):
        if cantidad <= self.disponibles():
            self.vendidos += cantidad
            print(f"✅ Venta registrada ({cantidad} unidades).")
            return True
        else:
            print("❌ No hay suficiente inventario disponible.")
            return False

    def mostrar_estado(self):
        print(f"Producto: {self.producto.nombre}")
        print(f"Stock total: {self.cantidad}")
        print(f"Vendidos: {self.vendidos}")
        print(f"Disponibles: {self.disponibles()}")
        print("-----------------------------------------")


class Venta:
    def __init__(self, folio, id_cliente, codigo_producto, fecha, cantidad, total):
        self.folio = folio
        self.id_cliente = id_cliente
        self.codigo_producto = codigo_producto
        self.fecha = fecha
        self.cantidad = cantidad
        self.total = total

    def mostrar_info(self):
        print(f"Folio: {self.folio}")
        print(f"Cliente: {self.id_cliente}")
        print(f"Producto: {self.codigo_producto}")
        print(f"Fecha: {self.fecha}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Total: ${self.total:.2f}")
        print("-----------------------------------------")


# ===========================================
#          LISTAS Y ADMIN POR DEFECTO
# ===========================================

productos = []
clientes = []
ventas = []
empleados = []
folio_actual = 1

# ✅ Empleado administrador por defecto
admin = Empleado(
    "Administrador General", "admin@ferreteria.com", "Sin dirección", "0000000000",
    "EMP001", "Administración", "admin", "1234"
)
empleados.append(admin)


# ===========================================
#            FUNCIONES DEL SISTEMA
# ===========================================

def alta_producto():
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad inicial: "))

    nuevo_producto = Producto(codigo, nombre, categoria, precio)
    inventario = InventarioProducto(nuevo_producto, cantidad)
    productos.append(inventario)
    print("✅ Producto agregado correctamente.\n")


def mostrar_inventario():
    if not productos:
        print("No hay productos registrados.\n")
    else:
        for inv in productos:
            inv.mostrar_estado()


def consultar_producto():
    codigo = input("Código del producto: ")
    for inv in productos:
        if inv.producto.codigo == codigo:
            inv.producto.mostrar_info()
            inv.mostrar_estado()
            return
    print("❌ Producto no encontrado.\n")


def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    correo = input("Correo: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    rfc = input("RFC: ")

    nuevo = Cliente(nombre, correo, direccion, telefono, rfc)
    clientes.append(nuevo)
    print("✅ Cliente registrado.\n")


def consultar_cliente():
    nombre = input("Nombre del cliente: ")
    for c in clientes:
        if c.nombre == nombre:
            c.mostrar_info()
            return
    print("❌ Cliente no encontrado.\n")


def mostrar_clientes():
    if not clientes:
        print("No hay clientes registrados.\n")
    else:
        for c in clientes:
            c.mostrar_info()


def registrar_venta():
    global folio_actual
    codigo = input("Código del producto: ")
    cantidad = int(input("Cantidad a vender: "))
    cliente = input("Nombre del cliente (o 'publico'): ")

    for inv in productos:
        if inv.producto.codigo == codigo:
            if inv.vender(cantidad):
                total = cantidad * inv.producto.precio_unitario
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                venta = Venta(folio_actual, cliente, codigo, fecha, cantidad, total)
                ventas.append(venta)
                folio_actual += 1
                print("✅ Venta registrada.\n")
            return
    print("❌ Producto no encontrado.\n")


def mostrar_ventas():
    if not ventas:
        print("No hay ventas registradas.\n")
    else:
        for v in ventas:
            v.mostrar_info()


# ===========================================
#               LOGIN
# ===========================================

def login():
    print("===== INICIO DE SESIÓN =====")
    while True:
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        for emp in empleados:
            if emp.usuario == user and emp.contrasena == pwd:
                print(f"\nBienvenido {emp.nombre} ✅\n")
                return
        print("❌ Usuario o contraseña incorrectos.\n")


# ===========================================
#               MENÚ PRINCIPAL
# ===========================================

def menu():
    while True:
        print("""
===== SISTEMA DE FERRETERÍA =====
1. Dar de alta producto
2. Mostrar inventario
3. Consultar producto
4. Registrar cliente
5. Consultar cliente
6. Mostrar lista de clientes
7. Registrar venta
8. Mostrar ventas
9. Salir
""")
        op = input("Opción: ")

        if op == "1":
            alta_producto()
        elif op == "2":
            mostrar_inventario()
        elif op == "3":
            consultar_producto()
        elif op == "4":
            registrar_cliente()
        elif op == "5":
            consultar_cliente()
        elif op == "6":
            mostrar_clientes()
        elif op == "7":
            registrar_venta()
        elif op == "8":
            mostrar_ventas()
        elif op == "9":
            print("Hasta luego")
            break
        else:
            print("Opción no válida.\n")


# ===========================================
#           EJECUCIÓN DEL PROGRAMA
# ===========================================
login()
menu()



