def infijo_a_postfijo(expresion):
    # La asignación tiene menor prioridad que los operadores aritméticos.
    precedencia = {'=': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    asociatividad_derecha = '^='

    pila = []
    salida = []
    for token in expresion:
        if token.isalnum():
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            if not pila:
                print("Hay un parentesis de cierre sin apertura")
                return False
            pila.pop()
        elif token in precedencia:
            while pila and pila[-1] != '(':
                prioridad_tope = precedencia[pila[-1]]
                prioridad_actual = precedencia[token]
                if prioridad_tope < prioridad_actual:
                    break
                if prioridad_tope == prioridad_actual and token in asociatividad_derecha:
                    break
                salida.append(pila.pop())
            pila.append(token)
        elif not token.isspace():
            print("Simbolo no reconocido " + token)
            return False

    while pila:
        operador = pila.pop()
        if operador == '(':
            print("Hay un parentesis de apertura sin cierre")
            return False
        salida.append(operador)

    return "".join(salida)


def generar_cuartetos(postfijo):
    pila = []
    cuartetos = []
    numero = 1

    for token in "".join(postfijo.split()):
        if token.isalnum():
            pila.append(token)
        else:
            if token not in '+-*/^=' or len(pila) < 2:
                print("Expresion postfija no valida")
                return False
            derecho = pila.pop()
            izquierdo = pila.pop()

            if token == '=':
                if len(izquierdo) != 1 or not izquierdo.isalpha():
                    print("Se necesita una variable como destino para la asignacion")
                    return False
                cuartetos.append(('=', derecho, '-', izquierdo))
                pila.append(izquierdo)
            else:
                temporal = 'R' + str(numero)
                cuartetos.append((token, izquierdo, derecho, temporal))
                pila.append(temporal)
            numero = numero + 1

    if len(pila) != 1:
        print("Expresion postfija no valida")
        return False
    return cuartetos


if __name__ == "__main__":
    ejemplo = "X = A + B * C ^ D - E"
    ejemplo = "A+B*C^D"
    resultado = infijo_a_postfijo(ejemplo)
    print("Infijo:", ejemplo)
    print("Postfijo:", resultado)

    cuartetos = generar_cuartetos(resultado)
    if(cuartetos == False):
        print("No se pudo generar los cuartetos")
    else:
        print("Total de cuartetos:", len(cuartetos))
        print("(Operador, Operando 1, Operando 2, Resultado)")
        for cuarteto in cuartetos:
            print(cuarteto)
