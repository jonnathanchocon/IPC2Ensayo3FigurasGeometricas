import figuras


def menu():  # muestra el menu de opciones
    print('Figuras Geométricas')
    print('1. Cuadrado')
    print('2. Rectangulo')
    print('3. Triangulo')
    print('4. Circulo')
    print('5. Salir')
    print('Elija una opción')


def main():  # metodo principal
    opcion = -1
    suma_area = 0
    suma_perimetro = 0
    numero_figuras = 0

    while opcion != 5:
        opcion = -1
        menu()
        try:
            opcion = int(input(''))
        except Exception:
            print('opción no disponible')

        if opcion == 1:  # Cuadrado
            cuadrado = figuras.Cuadrado()
            cuadrado.definir_datos()
            print(f'Área: {str(cuadrado.getArea())}')
            print(f'Perímetro: {str(cuadrado.getPerimetro())}')

            suma_area += cuadrado.getArea()
            suma_perimetro += cuadrado.getPerimetro()
            numero_figuras += 1

        elif opcion == 2:  # Rectangulo
            rectangulo = figuras.Rectangulo()
            rectangulo.definir_datos()
            print(f'Área: {str(rectangulo.getArea())}')
            print(f'Perímetro: {str(rectangulo.getPerimetro())}')

            suma_area += rectangulo.getArea()
            suma_perimetro += rectangulo.getPerimetro()
            numero_figuras += 1

        elif opcion == 3:  # Triangulo
            triangulo = figuras.Triangulo()
            triangulo.definir_datos()
            print(f'Área: {str(triangulo.getArea())}')
            print(f'Perímetro: {str(triangulo.getPerimetro())}')

            suma_area += triangulo.getArea()
            suma_perimetro += triangulo.getPerimetro()
            numero_figuras += 1

        elif opcion == 4:  # Circulo
            circulo = figuras.Circulo()
            circulo.definir_datos()
            print(f'Área: {str(circulo.getArea())}')
            print(f'Perímetro: {str(circulo.getPerimetro())}')

            suma_area += circulo.getArea()
            suma_perimetro += circulo.getPerimetro()
            numero_figuras += 1

        elif opcion == 5:
            if numero_figuras == 1:
                print(f'Se ingresaron {str(numero_figuras)} figura')
                print(
                    'Promedio de áreas: ',
                    f'{str(round(suma_area/numero_figuras, 2))}'
                )
                print(
                    'Promedio de perímetros: ',
                    f'{str(round(suma_perimetro/numero_figuras, 2))}'
                )

            elif numero_figuras > 1:
                print(f'Se ingresaron {str(numero_figuras)} figuras')
                print(
                    'Promedio de áreas: ',
                    f'{str(round(suma_area / numero_figuras, 2))}'
                )
                print(
                    'Promedio de perímetros: ',
                    f'{str(round(suma_perimetro / numero_figuras, 2))}'
                )

            print('Aplicación Finalizada')

        print('')


main()
