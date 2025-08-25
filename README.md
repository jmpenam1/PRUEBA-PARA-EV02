````markdown
# ⚽ Formulario de Registro de Jugadores

Este proyecto es una aplicación web interactiva construida con **Streamlit** que permite registrar información de jugadores de fútbol y almacenarla en un archivo CSV (`players.csv`).  

Los datos incluyen información general, estadísticas de partidos y detalles disciplinarios, facilitando la construcción de un dataset estructurado para análisis posteriores.

---

## 🛠️ Requisitos

- Python 3.9 o superior  
- Librerías listadas en `requirements.txt`

Instalar dependencias con:

```bash
pip install -r requirements.txt
````

---

## 🚀 Ejecución de la aplicación

Para ejecutar la app, usa el siguiente comando en la terminal:

```bash
streamlit run form_player.py
```

Esto abrirá la aplicación en tu navegador predeterminado en la dirección:

```
http://localhost:8501
```

---

## 📋 Campos del formulario

* **Información del jugador**

  * Nombre
  * Posición
  * Club
  * Valor de mercado (€)
  * Edad
  * Nacionalidad principal
  * Nacionalidad secundaria

* **Estadísticas de rendimiento**

  * Partidos jugados
  * Goles
  * Asistencias
  * Sustituciones (entrada y salida)
  * Autogoles

* **Disciplina**

  * Tarjetas amarillas
  * Doble amarilla
  * Tarjetas rojas

---

## 📂 Salida

Cada registro de jugador se guarda en el archivo `players.csv`.
Si el archivo no existe, se crea automáticamente con las columnas definidas en el proyecto.
