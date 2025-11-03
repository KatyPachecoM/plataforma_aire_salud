"""
Plataforma de Análisis de Justicia Ambiental en el Valle de Aburrá
Calidad del Aire y Salud Pública - DATOS REALES (OPTIMIZADO)

Fuentes:
- SIATA: Mediciones PM2.5 (2021-2022)
- MinSalud: Indicadores de Mortalidad (2005-2020)
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium

# Configuración
st.set_page_config(
    page_title="Calidad del Aire y Salud - Valle de Aburrá",
    page_icon="🌍",
    layout="wide"
)

# Título
st.title("🌍 Plataforma de Análisis de Justicia Ambiental")
st.subheader("Calidad del Aire y Salud Pública en el Valle de Aburrá")

# Sidebar
st.sidebar.header("📊 Navegación")
pagina = st.sidebar.radio(
    "Selecciona una sección:",
    ["🏠 Inicio", "🗺️ Mapa Interactivo", "📈 Análisis Temporal", "📊 Análisis por Municipio", "ℹ️ Acerca de"]
)

# Cargar datos (OPTIMIZADO)
@st.cache_data(ttl=3600)
def cargar_datos():
    try:
        estaciones = pd.read_csv('data/estaciones_siata_con_municipio.csv')
        # Usar archivo optimizado (promedios diarios en lugar de horarios)
        mediciones = pd.read_csv('data/mediciones_pm25_siata_optimizado.csv')
        mediciones['fecha'] = pd.to_datetime(mediciones['fecha'])
        salud = pd.read_csv('data/salud_valle_aburra_procesado.csv')
        resumen_salud = pd.read_csv('data/resumen_salud_municipios.csv')
        return estaciones, mediciones, salud, resumen_salud
    except Exception as e:
        st.error(f"Error cargando datos: {e}")
        return None, None, None, None

# Mostrar spinner mientras carga
with st.spinner('Cargando datos...'):
    estaciones, mediciones, salud, resumen_salud = cargar_datos()

if estaciones is None:
    st.error("No se pudieron cargar los datos. Por favor, verifica que los archivos estén en la carpeta 'data/'.")
    st.stop()

# PÁGINA: INICIO
if pagina == "🏠 Inicio":
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Objetivo del Proyecto")
        st.write("""
        Esta plataforma integra datos abiertos de **calidad del aire** y **salud pública** 
        para analizar la relación entre contaminación atmosférica y mortalidad en el 
        Valle de Aburrá, con enfoque en justicia ambiental.
        """)
        
        st.markdown("### 📊 Fuentes de Datos Reales")
        st.write("""
        **Fuente 1: SIATA**
        - 160,883 mediciones de PM2.5
        - 21 estaciones georreferenciadas
        - Período: Oct 2021 - Oct 2022
        
        **Fuente 2: Ministerio de Salud**
        - 386 registros de mortalidad
        - 9 municipios del Valle de Aburrá
        - Período: 2005-2020
        """)
    
    with col2:
        st.markdown("### 👥 Actores Involucrados")
        st.write("""
        **Actor 1: Comunidades del Valle de Aburrá**
        - Población expuesta a contaminación
        - Afectados en salud respiratoria
        
        **Actor 2: Autoridades Ambientales y de Salud**
        - Área Metropolitana (AMVA)
        - SIATA
        - Secretarías de Salud
        """)
        
        st.markdown("### 🔬 Indicadores Clave")
        st.write("""
        - PM2.5: Material Particulado < 2.5 micras
        - Tasa de mortalidad general
        - Mortalidad por IRA
        - Mortalidad infantil
        """)
    
    st.markdown("---")
    st.markdown("### 📈 Estadísticas Generales")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Estaciones", f"{len(estaciones)}")
    with col2:
        st.metric("Días de Medición", f"{len(mediciones):,}")
    with col3:
        st.metric("PM2.5 Promedio", f"{mediciones['pm25'].mean():.1f} µg/m³")
    with col4:
        st.metric("Municipios", "9")

# PÁGINA: MAPA INTERACTIVO
elif pagina == "🗺️ Mapa Interactivo":
    st.markdown("---")
    st.markdown("### 🗺️ Distribución Geográfica de Estaciones")
    
    pm25_por_estacion = mediciones.groupby('codigo_estacion')['pm25'].mean().reset_index()
    pm25_por_estacion.columns = ['codigo', 'pm25_promedio']
    estaciones_con_pm25 = estaciones.merge(pm25_por_estacion, on='codigo', how='left')
    
    m = folium.Map(location=[6.25, -75.57], zoom_start=11)
    
    for idx, row in estaciones_con_pm25.iterrows():
        pm25_val = row['pm25_promedio'] if pd.notna(row['pm25_promedio']) else 0
        
        if pm25_val < 12:
            color = 'green'
            nivel = 'Bueno'
        elif pm25_val < 35:
            color = 'yellow'
            nivel = 'Moderado'
        elif pm25_val < 55:
            color = 'orange'
            nivel = 'Dañino para grupos sensibles'
        else:
            color = 'red'
            nivel = 'Dañino'
        
        popup_text = f"""
        <b>{row['nombre_corto']}</b><br>
        Municipio: {row['municipio']}<br>
        PM2.5: {pm25_val:.1f} µg/m³<br>
        Nivel: {nivel}
        """
        
        folium.CircleMarker(
            location=[row['latitud'], row['longitud']],
            radius=8,
            popup=folium.Popup(popup_text, max_width=250),
            color=color,
            fill=True,
            fillColor=color,
            fillOpacity=0.7
        ).add_to(m)
    
    st_folium(m, width=1200, height=600)
    
    st.markdown("""
    **Leyenda:**
    - 🟢 Bueno (0-12 µg/m³)
    - 🟡 Moderado (12-35 µg/m³)
    - 🟠 Dañino para grupos sensibles (35-55 µg/m³)
    - 🔴 Dañino (>55 µg/m³)
    """)

# PÁGINA: ANÁLISIS TEMPORAL
elif pagina == "📈 Análisis Temporal":
    st.markdown("---")
    st.markdown("### 📈 Evolución Temporal de PM2.5")
    
    estaciones_disponibles = sorted(mediciones['nombre_estacion'].unique())
    estacion_seleccionada = st.selectbox("Selecciona una estación:", estaciones_disponibles)
    
    datos_estacion = mediciones[mediciones['nombre_estacion'] == estacion_seleccionada].copy()
    
    fig = px.line(
        datos_estacion,
        x='fecha',
        y='pm25',
        title=f'Evolución de PM2.5 - {estacion_seleccionada} (Promedios Diarios)',
        labels={'fecha': 'Fecha', 'pm25': 'PM2.5 (µg/m³)'}
    )
    
    fig.add_hline(y=12, line_dash="dash", line_color="green", annotation_text="Límite Bueno (12)")
    fig.add_hline(y=35, line_dash="dash", line_color="orange", annotation_text="Límite Moderado (35)")
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("PM2.5 Promedio", f"{datos_estacion['pm25'].mean():.1f} µg/m³")
    with col2:
        st.metric("PM2.5 Máximo", f"{datos_estacion['pm25'].max():.1f} µg/m³")
    with col3:
        st.metric("PM2.5 Mínimo", f"{datos_estacion['pm25'].min():.1f} µg/m³")
    
    st.markdown("---")
    st.markdown("### 📊 Evolución de Indicadores de Salud (2005-2020)")
    
    indicadores_disponibles = sorted(salud['indicador'].unique())
    indicador_seleccionado = st.selectbox("Selecciona un indicador:", indicadores_disponibles)
    
    datos_indicador = salud[salud['indicador'] == indicador_seleccionado].copy()
    datos_por_año = datos_indicador.groupby(['a_o', 'municipio'])['valor_indicador'].mean().reset_index()
    
    fig = px.line(
        datos_por_año,
        x='a_o',
        y='valor_indicador',
        color='municipio',
        title=f'{indicador_seleccionado} por Municipio',
        labels={'a_o': 'Año', 'valor_indicador': 'Valor', 'municipio': 'Municipio'}
    )
    
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

# PÁGINA: ANÁLISIS POR MUNICIPIO
elif pagina == "📊 Análisis por Municipio":
    st.markdown("---")
    st.markdown("### 📊 Comparación entre Municipios")
    
    pm25_por_municipio = mediciones.merge(
        estaciones[['codigo', 'municipio']], 
        left_on='codigo_estacion', 
        right_on='codigo'
    ).groupby('municipio')['pm25'].mean().reset_index()
    pm25_por_municipio.columns = ['municipio', 'pm25_promedio']
    
    fig1 = px.bar(
        pm25_por_municipio.sort_values('pm25_promedio', ascending=False),
        x='municipio',
        y='pm25_promedio',
        title='PM2.5 Promedio por Municipio (2021-2022)',
        labels={'municipio': 'Municipio', 'pm25_promedio': 'PM2.5 (µg/m³)'},
        color='pm25_promedio',
        color_continuous_scale='Reds'
    )
    fig1.update_layout(height=400)
    st.plotly_chart(fig1, use_container_width=True)
    
    st.markdown("### 🏥 Indicadores de Salud por Municipio")
    
    indicador_salud = st.selectbox(
        "Selecciona indicador de salud:",
        resumen_salud['indicador'].unique()
    )
    
    datos_indicador = resumen_salud[resumen_salud['indicador'] == indicador_salud].copy()
    
    fig2 = px.bar(
        datos_indicador.sort_values('promedio', ascending=False),
        x='municipio',
        y='promedio',
        title=f'{indicador_salud} - Promedio 2005-2020',
        labels={'municipio': 'Municipio', 'promedio': 'Valor Promedio'},
        color='promedio',
        color_continuous_scale='Blues'
    )
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("### 📋 Tabla Comparativa")
    st.dataframe(datos_indicador[['municipio', 'promedio', 'minimo', 'maximo', 'num_años']], use_container_width=True)

# PÁGINA: ACERCA DE
elif pagina == "ℹ️ Acerca de":
    st.markdown("---")
    st.markdown("### ℹ️ Acerca de este Proyecto")
    
    st.write("""
    ## Plataforma de Análisis de Justicia Ambiental
    
    ### 📚 Fuentes de Datos
    
    **1. SIATA**
    - URL: https://datosabiertos.metropol.gov.co/
    - Datos: Mediciones PM2.5 de 21 estaciones
    - Período: Oct 2021 - Oct 2022
    
    **2. Ministerio de Salud**
    - URL: https://www.datos.gov.co/
    - Datos: Indicadores de mortalidad
    - Período: 2005-2020
    
    ### 📖 Referencias Académicas
    
    1. Uniandes - Contaminación y desigualdad en Colombia
    2. Scielo - PM y enfermedades respiratorias en Medellín
    3. Politécnico JIC - Impacto de PM2.5 en salud genética
    4. Amelica - Equidad territorial en Medellín
    5. PMC/NCBI - Desigualdades en mortalidad
    6. Bioética - Pico y placa en Medellín
    
    ### 🛠️ Tecnologías
    - Python 3.11
    - Streamlit
    - Pandas, Plotly, Folium
    
    ### 📅 Fecha
    Noviembre 2025
    """)

st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>📊 Plataforma de Datos Abiertos - Valle de Aburrá | 2025</p>
    <p>Datos: SIATA & Ministerio de Salud</p>
</div>
""", unsafe_allow_html=True)
