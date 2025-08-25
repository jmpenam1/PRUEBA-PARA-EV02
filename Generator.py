# form_player.py
import streamlit as st
import pandas as pd

# Definir columnas del dataset
COLUMNS = [
    "Name", "Position", "Club", "Market Value", "Age", 
    "Primary Nationality", "Secondary Nationality", 
    "Matches Played", "Goals", "Assists", 
    "Yellow Cards", "Red Cards", 
    "Substituted In", "Substituted Out", 
    "Second Yellow Cards", "Own Goals"
]

st.title("Formulario de Registro de Jugadores ⚽")

# Crear formulario
with st.form("player_form"):
    name = st.text_input("Nombre del jugador")
    position = st.selectbox("Posición", [
        "Goalkeeper", "Defender", "Centre-Back", "Left-Back", "Right-Back",
        "Defensive Midfield", "Central Midfield", "Attacking Midfield",
        "Left Winger", "Right Winger", "Centre-Forward"
    ])
    club = st.text_input("Club")
    market_value = st.number_input("Valor de mercado (€)", min_value=0, step=1000000)
    age = st.number_input("Edad", min_value=15, max_value=50, step=1)
    nationality1 = st.text_input("Nacionalidad Principal")
    nationality2 = st.text_input("Nacionalidad Secundaria (opcional)", value="-")

    matches = st.number_input("Partidos Jugados", min_value=0, step=1)
    goals = st.number_input("Goles", min_value=0, step=1)
    assists = st.number_input("Asistencias", min_value=0, step=1)
    yellow = st.number_input("Tarjetas Amarillas", min_value=0, step=1)
    red = st.number_input("Tarjetas Rojas", min_value=0, step=1)
    sub_in = st.number_input("Veces ingresado", min_value=0, step=1)
    sub_out = st.number_input("Veces sustituido", min_value=0, step=1)
    second_yellow = st.number_input("Doble Amarilla", min_value=0, step=1)
    own_goals = st.number_input("Autogoles", min_value=0, step=1)

    submitted = st.form_submit_button("Guardar jugador")

# Guardar jugador en dataset temporal
if submitted:
    new_player = {
        "Name": name,
        "Position": position,
        "Club": club,
        "Market Value": market_value,
        "Age": age,
        "Primary Nationality": nationality1,
        "Secondary Nationality": nationality2,
        "Matches Played": matches,
        "Goals": goals,
        "Assists": assists,
        "Yellow Cards": yellow,
        "Red Cards": red,
        "Substituted In": sub_in,
        "Substituted Out": sub_out,
        "Second Yellow Cards": second_yellow,
        "Own Goals": own_goals,
    }

    # Si no existe el CSV, se crea
    try:
        df = pd.read_csv("players.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=COLUMNS)

    # Agregar fila nueva
    df = pd.concat([df, pd.DataFrame([new_player])], ignore_index=True)
    df.to_csv("players.csv", index=False)

    st.success(f"✅ Jugador {name} agregado correctamente al dataset.")
    st.dataframe(df.tail(5))
