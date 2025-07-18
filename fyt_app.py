# -*- coding: utf-8 -*-

# Librerías necesarias
import streamlit as st
from supabase import create_client, Client
import requests
import datetime

# Configuración básica
SUPABASE_URL = "https://swsqgkccwviqfsixfmwi.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN3c3Fna2Njd3ZpcWZzaXhmbXdpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcwNjY1NzAsImV4cCI6MjA2MjY0MjU3MH0.9PcRFd6Q_i-mh8VCmvd9150PWAAaRr5f-VOrdrg6soM"
HEADERS = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"}

# Función auxiliar para insertar datos en Supabase
def insert_into_supabase(table, data):
    url = f"{SUPABASE_URL}/rest/v1/{table}"
    response = requests.post(url, headers=HEADERS, json=data)
    return response.status_code, response.text

# Navegación lateral
menu = st.sidebar.radio("Selecciona un formulario", [
    "Registro de Centro Deportivo",
    "Registro de Usuario Deportista",
    "Búsqueda de Actividades"])

# FORMULARIO 1: Centro Deportivo
if menu == "Registro de Centro Deportivo":
    st.header("Registro de Centro Deportivo")

    with st.form("venue_form"):
        name = st.text_input("Nombre comercial")
        vat = st.text_input("CIF o VAT")
        company = st.text_input("Nombre fiscal")
        address = st.text_input("Dirección")
        postal = st.text_input("Código postal")
        city = st.text_input("Ciudad")
        lat = st.number_input("Latitud", format="%.6f")
        lon = st.number_input("Longitud", format="%.6f")
        website = st.text_input("Web")
        insta = st.text_input("Instagram")
        fb = st.text_input("Facebook")
        tw = st.text_input("Twitter")
        tt = st.text_input("TikTok")
        phone = st.text_input("Teléfono")
        email = st.text_input("Email")
        venue_type = st.selectbox("Tipo", ["Club", "Tienda", "Otro"])
        accessible = st.checkbox("¿Accesibilidad física?")
        langs = st.text_input("Idiomas hablados")

        submitted = st.form_submit_button("Registrar")

        if submitted:
            venue_data = {
                "name": name,
                "vat_number": vat,
                "company_name": company,
                "address": address,
                "postal_code": postal,
                "city": city,
                "latitude": lat,
                "longitude": lon,
                "website": website,
                "instagram": insta,
                "facebook": fb,
                "twitter": tw,
                "tiktok": tt,
                "phone": phone,
                "email": email,
                "venue_type": venue_type,
                "accessibility": accessible,
                "languages_spoken": langs
            }
            code, result = insert_into_supabase("venues", venue_data)
            st.success("Centro registrado!" if code == 201 else f"Error: {result}")

# FORMULARIO 2: Usuario
elif menu == "Registro de Usuario Deportista":
    st.header("Registro de Usuario Deportista")

    with st.form("user_form"):
        full_name = st.text_input("Nombre completo")
        email = st.text_input("Email")
        age = st.number_input("Edad", min_value=10, max_value=100)
        sex = st.selectbox("Sexo", ["male", "female", "other"])
        disability = st.checkbox("¿Tienes alguna discapacidad física?")
        frequency = st.selectbox("Frecuencia deportiva", ["daily", "weekly", "occasional", "other"])
        goals = st.text_input("Objetivo deportivo")
        preferences = st.multiselect("Preferencias deportivas", ["Fútbol", "Yoga", "Running", "Pádel", "Tenis"])
        address = st.text_input("Dirección")
        postal_code = st.text_input("Código postal")
        transport = st.selectbox("Medio de transporte habitual", ["bike", "public transport", "car", "walk"])
        preferred_time = st.selectbox("Franja horaria preferida", ["morning", "afternoon", "evening"])
        experience = st.selectbox("Nivel de experiencia", ["beginner", "intermediate", "advanced"])
        phone = st.text_input("Teléfono")

        submit_user = st.form_submit_button("Registrar")

        if submit_user:
            user_data = {
                "full_name": full_name,
                "email": email,
                "age": age,
                "sex": sex,
                "disability": disability,
                "frequency": frequency,
                "training_goal": goals,
                "preferred_sports": preferences,
                "residence_address": address,
                "postal_code": postal_code,
                "transport_mode": transport,
                "preferred_time_of_day": preferred_time,
                "experience_level": experience,
                "phone": phone
            }
            code, result = insert_into_supabase("users", user_data)
            st.success("Usuario registrado!" if code == 201 else f"Error: {result}")

# FORMULARIO 3: Búsqueda
elif menu == "Búsqueda de Actividades":
    st.header("Búsqueda de Actividades Deportivas")

    with st.form("search_form"):
        sport = st.selectbox("Deporte", ["Fútbol", "Yoga", "Padel", "Running", "Otro"])
        weekday = st.selectbox("Día", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        time = st.time_input("Hora")
        price_range = st.slider("Rango de precio (€)", 0, 100, (10, 30))
        location = st.text_input("Zona o barrio")
        proximity = st.slider("Distancia máxima (km)", 1, 50, 10)
        use_gps = st.checkbox("Usar ubicación actual")
        modality = st.selectbox("Modalidad", ["online", "onsite"])
        kind = st.selectbox("Tipo", ["recreational", "federated", "professional"])
        category = st.text_input("Categoría")
        age_group = st.text_input("Rango de edad")
        sex = st.selectbox("Sexo", ["male", "female", "other"])

        submit_search = st.form_submit_button("Buscar")

        if submit_search:
            search_data = {
                "created_at": str(datetime.datetime.utcnow()),
                "sport": sport,
                "weekday": weekday,
                "time": str(time),
                "price_range": f"{price_range[0]}-{price_range[1]}",
                "location": location,
                "proximity_preference": proximity,
                "used_device_location": use_gps,
                "modality": modality,
                "type": kind,
                "category": category,
                "age_group": age_group,
                "sex": sex
            }
            code, result = insert_into_supabase("User_Searches", search_data)
            st.success("Búsqueda registrada!" if code == 201 else f"Error: {result}")

