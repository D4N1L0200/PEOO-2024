# 4. Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores
# podem ser números reais. Mostrar o resultado com duas casas decimais.

import math

print("Digite a base e a altura do retângulo")

width = float(input())
height = float(input())

area = width * height
perimeter = (width + height) * 2
diagonal = math.sqrt(width ** 2 + height ** 2)

print(f"Área = {area} - Perímetro = {perimeter} - Diagonal = {diagonal}")
