
# 🛒 Análisis Comparativo de Tiendas

Este proyecto consiste en un análisis exploratorio de cuatro tiendas de comercio electrónico con el objetivo de recomendar al Sr. Juan la mejor plataforma para vender sus productos.

---

## 🎯 Propósito del Análisis

El objetivo de este análisis es comparar el rendimiento de cuatro tiendas en línea utilizando métricas clave como ingresos, calificaciones de clientes, categorías y productos más vendidos, así como costos logísticos. A partir de estos datos, se busca identificar la tienda más adecuada para que el Sr. Juan comercialice sus productos.

---

## 🗂️ Estructura del Proyecto

```
├── datos/               # Archivos de entrada (.csv o .xlsx) de cada tienda
├── graficos/            # Carpeta opcional para guardar imágenes generadas
├── notebooks/           # Análisis principal en Google Colab
├── src/                 # Scripts auxiliares (si los hay)
├── README.md            # Este archivo
```

---

## 📊 Ejemplos de Gráficos e Insights

Durante el análisis se generaron visualizaciones que permitieron descubrir:

- Gráficos de barras comparando ingresos por tienda.
- Gráficos de torta para visualizar calificaciones promedio.
- Gráficos de líneas y dispersión para evaluar ventas por producto.

**Insights destacados:**

- Todas las tiendas comparten “Muebles” como categoría más vendida.
- Tienda uno lidera en ingresos, pero tiene menor calificación que tienda dos.
- Tienda dos tiene un buen equilibrio entre ventas, calificación y costos.

---

## ▶️ Instrucciones para Ejecutar el Notebook

1. Abre el archivo `.ipynb` en [Google Colab](https://colab.research.google.com).
2. Asegúrate de subir los archivos de datos a la ruta correcta o cargar desde Google Drive.
3. Ejecuta las celdas paso a paso para generar:

   - Cálculos de ingresos y calificaciones.
   - Análisis de categorías y productos más vendidos.
   - Gráficos visuales con matplotlib.
   - Informe final con recomendación justificada.

4. (Opcional) Exporta los gráficos o el informe como PDF o Markdown.

---

## 📈 Informe Final: Recomendación Comercial

### **1. Ingresos totales por tienda**

| Tienda         | Ingreso Total      |
|----------------|--------------------|
| Tienda uno     | $1,150,880,400     |
| Tienda dos     | $1,116,343,500     |
| Tienda tres    | $1,098,019,600     |
| Tienda cuatro  | $1,038,375,700     |

### **2. Categoría más vendida**

| Tienda         | Categoría más vendida | Cantidad |
|----------------|------------------------|----------|
| Tienda uno     | Muebles                | 465      |
| Tienda dos     | Muebles                | 442      |
| Tienda tres    | Muebles                | 499      |
| Tienda cuatro  | Muebles                | 480      |

### **3. Calificación promedio**

| Tienda         | Calificación Promedio |
|----------------|------------------------|
| Tienda uno     | 3.98                   |
| Tienda dos     | 4.04                   |
| Tienda tres    | 4.05                   |
| Tienda cuatro  | 4.00                   |

### **4. Productos más y menos vendidos**

| Tienda         | Más vendido                  | Cantidad | Menos vendido             | Cantidad |
|----------------|-------------------------------|----------|---------------------------|----------|
| Tienda uno     | Microondas                    | 60       | Auriculares con micrófono | 33       |
| Tienda dos     | Iniciando en programación     | 65       | Juego de mesa             | 32       |
| Tienda tres    | Kit de bancas                 | 57       | Bloques de construcción   | 35       |
| Tienda cuatro  | Cama box                      | 62       | Guitarra eléctrica        | 33       |

### **5. Costo de envío promedio**

| Tienda         | Costo Envío Promedio |
|----------------|-----------------------|
| Tienda uno     | $26,019               |
| Tienda dos     | $25,216               |
| Tienda tres    | $24,806               |
| Tienda cuatro  | $23,459               |

---

## ✅ Conclusión y Recomendación

Tras evaluar los diferentes factores analizados, se recomienda que el **Sr. Juan venda sus productos en la _Tienda Dos_**. Esta tienda ofrece una combinación sólida de:

- Ingresos elevados (2° lugar, muy cerca del primero)
- Buena calificación promedio de los clientes (4.04)
- Producto más vendido con alta rotación
- Costo de envío competitivo

### ✔️ Fortalezas de Tienda Dos:
- Ingresos altos y constantes
- Calificación sólida
- Rotación de productos educativos
- Buen equilibrio entre ventas y costos operativos

> 📌 **Recomendación final:** Tienda Dos es la opción más equilibrada y estratégica para que el Sr. Juan comercialice sus productos de forma rentable y sostenible.

---

## 👤 Autor

**Cristian González**  
GitHub: [@tuusuario](https://github.com/tuusuario)

---

## 📃 Licencia

Este proyecto está bajo la licencia MIT.
