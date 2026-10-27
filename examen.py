saldo_i = 1000

def menu():
    print("""
    ======MENÚ========
a.Consultar saldo
b.Depositar dinero
c.Retirar dinero
d.Salir""")

def consultar_saldo():
    return saldo_i

def depositar(monto):
    if monto < 0:
        print("Monto no válido")
        return saldo_i
    else:
        print("Deposito exitoso")
        return saldo_i + monto

def retirar(retiro):
    retirar = saldo_i - retiro
    if retiro > saldo_i or retiro < 0:
        print("Monto no válido")
        return saldo_i
    else:
        print("Retiro exitoso")
        return retirar

while True:
    menu()
    opcion = input("Ingrese opción: ")
    match opcion:
        case "a":
            print("Consultar saldo")
            print("Su saldo actual es:",round(consultar_saldo()))
        case "b":
            print("Depositar Dinero")
            deposito = float(input("Ingrese el monto a consginar: "))
            saldo_i = depositar(deposito)
            print(round(saldo_i))
        case "c":
            print("Retirar Dinero")
            retiro = float(input("Ingrese el monto a retirar: "))
            saldo_i = retirar(retiro)
            print(round(saldo_i))
        case "d":
            print("Has salido")
            break
        case _:
            print("Opción no válida\n\nIngrese otra opción nuevamente")

