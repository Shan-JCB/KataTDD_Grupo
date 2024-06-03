# KataTDD_Grupo

# Calculadora de promedio ponderado

Esta es una calculadora simple de promedio ponderado implementada en Python. Permite calcular el promedio ponderado de un conjunto de datos dados sus valores y pesos correspondientes.

## Funcionalidades

- Calcula el promedio ponderado de un conjunto de datos y pesos.
- Maneja casos especiales como conjuntos vacíos o con un solo elemento.

## Uso

Para utilizar la calculadora, simplemente crea una instancia de la clase `Conjunto` con los datos y pesos correspondientes, y luego llama al método `promedio_ponderado()` para obtener el resultado.

Ejemplo de uso:

```python
datos = [10, 12, 14]
pesos = [3, 4, 2]
conjunto = Conjunto(datos, pesos)
resultado = conjunto.promedio_ponderado()
print(f"El promedio ponderado es: {resultado}")
