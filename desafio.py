import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head()

# Crear una lista con los DataFrames y sus nombres
tiendas = [
    ('Tienda uno', tienda),
    ('Tienda dos', tienda2),
    ('Tienda tres', tienda3),
    ('Tienda cuatro', tienda4)
]

# Calcular y mostrar el total para cada tienda
for nombre, df in tiendas:
    total = df['Precio'].sum()
    print(f'El total de la {nombre} es: ${total:,.0f}')

    # Lista con los DataFrames de cada tienda y sus nombres
tiendas = [
    ('Tienda uno', tienda),
    ('Tienda dos', tienda2),
    ('Tienda tres', tienda3),
    ('Tienda cuatro', tienda4)
]

# Procesar cada tienda
for nombre, df in tiendas:
    print(f'\n{nombre}')

    # Agrupar por categoría y contar ventas
    ventas_por_categoria = df['Categoría del Producto'].value_counts()

    # Mostrar el total por categoría
    print(f'\n{ventas_por_categoria.to_string()}')

    # Categoría más popular
    categoria_top = ventas_por_categoria.idxmax()
    cantidad_top = ventas_por_categoria.max()

    print(f'\nCategoría más vendida: {categoria_top}')
    print(f'Cantidad: {cantidad_top:,}')

    # Lista con los DataFrames de cada tienda y sus nombres
tiendas = [
    ('Tienda uno', tienda),
    ('Tienda dos', tienda2),
    ('Tienda tres', tienda3),
    ('Tienda cuatro', tienda4)
]

# Procesar cada tienda
for nombre, df in tiendas:

    promedio_calificacion = df['Calificación'].mean()
    print(f'La calificacion promedio de la {nombre} es : {round(promedio_calificacion,2)}')



# Lista con los DataFrames de cada tienda y sus nombres
tiendas = [
    ('Tienda uno', tienda),
    ('Tienda dos', tienda2),
    ('Tienda tres', tienda3),
    ('Tienda cuatro', tienda4)
]

# Procesar cada tienda
for nombre, df in tiendas:
    print(f'\n{nombre}')

    #Contar productos
    productos = df['Producto'].value_counts()

    # Producto más popular
    producto_max = productos.idxmax()
    cantidad_max = productos.max()

    #Producto menos popular
    producto_min = productos.idxmin()
    cantidad_min = productos.min()

    print(f'\nProducto mas vendido: {producto_max}')
    print(f'Cantidad: {cantidad_max:,}')

    print(f'\nProducto menos vendido: {producto_min}')
    print(f'Cantidad: {cantidad_min:,}')

    
# Lista con los DataFrames de cada tienda y sus nombres
tiendas = [
    ('Tienda uno', tienda),
    ('Tienda dos', tienda2),
    ('Tienda tres', tienda3),
    ('Tienda cuatro', tienda4)
]

# Procesar cada tienda
for nombre, df in tiendas:

    promedio_envio = df['Costo de envío'].mean()
    print(f'El costo de envio promedio de la {nombre} es : ${promedio_envio:,.0f}')


# Lista con los DataFrames de cada tienda y sus nombres
tiendas = [
    ('Tienda uno', tienda),
    ('Tienda dos', tienda2),
    ('Tienda tres', tienda3),
    ('Tienda cuatro', tienda4)
]

for nombre, df in tiendas:
  plt.figure(figsize=(8, 5))
  ventas_por_categoria.plot(kind='bar')
  plt.title(f'Ventas por categoría - {nombre}')
  plt.xlabel('Categoría del Producto')
  plt.ylabel('Cantidad de ventas')
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

  # Lista de nombres y sus DataFrames
tiendas = [
    ('Tienda uno', tienda),
    ('Tienda dos', tienda2),
    ('Tienda tres', tienda3),
    ('Tienda cuatro', tienda4)
]

# Obtener promedios
nombres_tiendas = []
promedios = []

for nombre, df in tiendas:
    promedio = df['Calificación'].mean()
    nombres_tiendas.append(nombre)
    promedios.append(promedio)

# Crear gráfico de torta
plt.figure(figsize=(7,7))
plt.pie(promedios, labels=nombres_tiendas, autopct='%1.1f%%', startangle=140)
plt.title('Distribución del promedio de calificación por tienda')
plt.axis('equal')  # Para que el círculo sea perfecto
plt.show()



# Lista de tiendas y sus DataFrames
tiendas = [
    ('Tienda uno', tienda),
    ('Tienda dos', tienda2),
    ('Tienda tres', tienda3),
    ('Tienda cuatro', tienda4)
]

# Preparar datos
nombres_tiendas = []
ingresos = []

for nombre, df in tiendas:
    total = df['Precio'].sum()
    nombres_tiendas.append(nombre)
    ingresos.append(total)

# Crear gráfico de líneas
plt.figure(figsize=(8, 5))
plt.plot(nombres_tiendas, ingresos, marker='o', linestyle='-', color='teal')
plt.title('Ingresos Totales por Tienda')
plt.xlabel('Tienda')
plt.ylabel('Ingreso Total')
plt.grid(True)

# Mostrar valores
for i, valor in enumerate(ingresos):
    plt.text(i, valor + max(ingresos)*0.01, f'${valor:,.0f}', ha='center')

plt.tight_layout()
plt.show()


