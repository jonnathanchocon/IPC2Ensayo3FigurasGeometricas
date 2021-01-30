import figuras


def menu():  # muestra el menu de opciones
    print('Figuras Geométricas')
    print('1. Cuadrado')
    print('2. Rectángulo')
    print('3. Triángulo')
    print('4. Círculo')
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
            print(f'Área: {str(cuadrado.get_area())}')
            print(f'Perímetro: {str(cuadrado.get_perimetro())}')

            suma_area += cuadrado.get_area()
            suma_perimetro += cuadrado.get_perimetro()
            numero_figuras += 1

        elif opcion == 2:  # Rectangulo
            rectangulo = figuras.Rectangulo()
            rectangulo.definir_datos()
            print(f'Área: {str(rectangulo.get_area())}')
            print(f'Perímetro: {str(rectangulo.get_perimetro())}')

            suma_area += rectangulo.get_area()
            suma_perimetro += rectangulo.get_perimetro()
            numero_figuras += 1

        elif opcion == 3:  # Triangulo
            triangulo = figuras.Triangulo()
            triangulo.definir_datos()
            print(f'Área: {str(triangulo.get_area())}')
            print(f'Perímetro: {str(triangulo.get_perimetro())}')

            suma_area += triangulo.get_area()
            suma_perimetro += triangulo.get_perimetro()
            numero_figuras += 1

        elif opcion == 4:  # Circulo
            circulo = figuras.Circulo()
            circulo.definir_datos()
            print(f'Área: {str(circulo.get_area())}')
            print(f'Perímetro: {str(circulo.get_perimetro())}')

            suma_area += circulo.get_area()
            suma_perimetro += circulo.get_perimetro()
            numero_figuras += 1

        elif opcion == 5:
            if numero_figuras == 1:
                print(f'Se ingresó {str(numero_figuras)} figura')
                print(
                    'Sumatoria de áreas: ',
                    f'{str(round(suma_area, 2))}'
                )
                print(
                    'Sumatoria de perímetros: ',
                    f'{str(round(suma_perimetro, 2))}'
                )

            elif numero_figuras > 1:
                print(f'Se ingresaron {str(numero_figuras)} figuras')
                print(
                    'Sumatoria de áreas: ',
                    f'{str(round(suma_area, 2))}'
                )
                print(
                    'Sumatoria de perímetros: ',
                    f'{str(round(suma_perimetro, 2))}'
                )

            print('Aplicación Finalizada')

        print('')


main()
