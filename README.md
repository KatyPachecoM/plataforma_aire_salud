# Plataforma de Análisis de Justicia Ambiental en el Valle de Aburrá

## Calidad del Aire y Salud Pública - Datos Reales

### 📋 Descripción del Proyecto

Plataforma interactiva de análisis de datos abiertos que integra información georreferenciada de **calidad del aire** y **salud pública** para estudiar la relación entre contaminación atmosférica y mortalidad en el Valle de Aburrá, Colombia.

### 🎯 Objetivos

1. Visualizar la distribución espacial de la contaminación atmosférica (PM2.5)
2. Analizar la evolución temporal de indicadores de salud pública
3. Identificar correlaciones entre calidad del aire y mortalidad
4. Promover la justicia ambiental mediante datos transparentes

---

## 📊 Fuentes de Datos Reales

### Fuente 1: SIATA (Sistema de Alerta Temprana de Medellín y el Valle de Aburrá)

**Entidad:** Área Metropolitana del Valle de Aburrá  
**URL:** https://datosabiertos.metropol.gov.co/node/99  
**Descripción:** Mediciones horarias de Material Particulado PM2.5

**Características:**
- **Registros:** 160,883 mediciones válidas
- **Estaciones:** 21 estaciones georreferenciadas
- **Período:** Octubre 2021 - Octubre 2022
- **Municipios:** Medellín, Itagüí, Envigado, Bello, Sabaneta, La Estrella, Caldas, Copacabana, Barbosa, Girardota

### Fuente 2: Ministerio de Salud y Protección Social

**Entidad:** Dirección de Epidemiología y Demografía  
**URL:** https://www.datos.gov.co/Salud-y-Protecci-n-Social/Indicadores-mortalidad-y-morbilidad-seg-n-departam/4e4i-ua65  
**Descripción:** Indicadores de mortalidad y morbilidad por municipio

**Características:**
- **Registros:** 386 registros del Valle de Aburrá
- **Municipios:** 9 municipios
- **Período:** 2005-2020
- **Indicadores:**
  - Tasa de mortalidad general
  - Tasa de mortalidad por IRA (Infección Respiratoria Aguda)
  - Tasa de mortalidad infantil
  - Tasa de mortalidad neonatal

---

## 👥 Actores Involucrados

### Actor 1: Comunidades del Valle de Aburrá
Población residente expuesta a contaminación atmosférica, especialmente grupos vulnerables (niños, adultos mayores, personas con enfermedades respiratorias).

### Actor 2: Autoridades Ambientales y de Salud Pública
- Área Metropolitana del Valle de Aburrá (AMVA)
- SIATA
- Secretarías de Salud municipales
- Ministerio de Salud y Protección Social

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.11**
- **Streamlit** - Framework de dashboards interactivos
- **Pandas** - Procesamiento y análisis de datos
- **Plotly** - Visualizaciones interactivas
- **Folium** - Mapas geográficos interactivos
- **NumPy** - Cálculos numéricos

---

## 📁 Estructura del Proyecto

```
plataforma_aire_salud/
├── app.py                              # Aplicación principal de Streamlit
├── data/                               # Datos procesados
│   ├── pm25_siata_real.json           # Datos crudos PM2.5 del SIATA
│   ├── mediciones_pm25_siata.csv      # Mediciones procesadas
│   ├── estaciones_siata.csv           # Información de estaciones
│   ├── estaciones_siata_con_municipio.csv  # Estaciones con municipio asignado
│   ├── mortalidad_morbilidad_colombia.csv  # Datos nacionales de salud
│   ├── salud_valle_aburra_procesado.csv    # Datos de salud filtrados
│   └── resumen_salud_municipios.csv   # Resumen por municipio
├── fuentes_academicas/                 # 6 fuentes académicas recopiladas
│   ├── fuente_1_uniandes_justicia_ambiental.md
│   ├── fuente_2_scielo_pm_enfermedades_respiratorias.md
│   ├── fuente_3_pico_y_placa_medellin.md
│   ├── fuente_4_pm25_salud_genetica_valle_aburra.md
│   ├── fuente_5_equidad_territorial_medellin.md
│   └── fuente_6_desigualdades_mortalidad_ciudades_colombia.md
├── FUENTES_DATOS_REALES.md            # Documentación detallada de fuentes
├── README.md                           # Este archivo
└── requirements.txt                    # Dependencias de Python
```

---

## 🚀 Instalación y Uso

### Requisitos Previos

- Python 3.11 o superior
- pip3

### Instalación de Dependencias

```bash
cd plataforma_aire_salud
pip3 install -r requirements.txt
```

### Ejecutar la Aplicación

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📊 Funcionalidades de la Plataforma

### 1. 🏠 Página de Inicio
- Resumen del proyecto y objetivos
- Estadísticas generales (estaciones, mediciones, promedios)
- Información sobre fuentes de datos y actores

### 2. 🗺️ Mapa Interactivo
- Visualización geográfica de las 21 estaciones de monitoreo
- Marcadores con código de colores según nivel de PM2.5
- Información detallada al hacer clic en cada estación
- Leyenda de calidad del aire (OMS)

### 3. 📈 Análisis Temporal
- **Calidad del Aire:** Serie temporal de PM2.5 por estación
- **Salud Pública:** Evolución de indicadores de mortalidad 2005-2020
- Gráficos interactivos con filtros por estación y municipio
- Estadísticas descriptivas (promedio, máximo, mínimo)

### 4. 📊 Análisis por Municipio
- Comparación de PM2.5 promedio entre municipios
- Comparación de indicadores de salud entre municipios
- Gráficos de barras con escala de colores
- Tablas comparativas con estadísticas detalladas

### 5. ℹ️ Acerca de
- Información del proyecto
- Referencias académicas (6 fuentes)
- Tecnologías utilizadas
- Créditos y fecha

---

## 📖 Referencias Académicas

1. **Uniandes** - El color del aire: contaminación y desigualdad en Colombia  
   https://www.uniandes.edu.co/es/noticias/medio-ambiente/el-color-del-aire-contaminacion-y-desigualdad-en-colombia

2. **Scielo** - Contaminación por material particulado (PM2.5 y PM10) y consultas por enfermedades respiratorias en Medellín (2008-2009)  
   http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0120-386X2011000300004

3. **Bioética** - Pico y placa en Medellín: análisis de una política pública  
   http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0012-73532011000100011

4. **Politécnico JIC** - Entre el aire y el ADN: investigación evidencia el impacto invisible de las partículas PM2.5 en la salud genética del Valle de Aburrá  
   https://www.politecnicojic.edu.co/comunicados-y-boletines/6143

5. **Amelica** - Equidad territorial en Medellín  
   https://portal.amelica.org/ameli/journal/32/325355008/html/

6. **PMC/NCBI** - Desigualdades intraurbanas en mortalidad en ciudades colombianas  
   https://pmc.ncbi.nlm.nih.gov/articles/PMC9859133/

---

## 📈 Indicadores Clave

### Calidad del Aire
- **PM2.5:** Material Particulado < 2.5 micras (µg/m³)
- **Límites OMS:**
  - Bueno: 0-12 µg/m³
  - Moderado: 12-35 µg/m³
  - Dañino para grupos sensibles: 35-55 µg/m³
  - Dañino: >55 µg/m³

### Salud Pública
- **Tasa de mortalidad general** (por 1,000 habitantes)
- **Tasa de mortalidad por IRA** en menores de 5 años
- **Tasa de mortalidad infantil** (menores de 1 año)
- **Tasa de mortalidad neonatal**

---

## 🔬 Metodología

1. **Recopilación de datos:** Descarga de datasets oficiales de SIATA y MinSalud
2. **Procesamiento:** Limpieza, filtrado y transformación de datos con Pandas
3. **Integración:** Asignación de municipios a estaciones, cruce de datos temporales
4. **Visualización:** Desarrollo de dashboards interactivos con Streamlit
5. **Análisis:** Identificación de patrones espaciales y temporales

---

## ✅ Cumplimiento de Requisitos Académicos

- ✅ **Mínimo 2 fuentes de datos:** SIATA + MinSalud
- ✅ **Mínimo 2 actores:** Comunidades + Autoridades
- ✅ **Datos de los últimos 3 años:** 2021-2022 (aire) + 2018-2020 (salud)
- ✅ **Mínimo 6 fuentes académicas:** 6 estudios recopilados
- ✅ **Datos georreferenciados:** Estaciones con lat/long + municipios
- ✅ **Datos 100% reales:** Todas las fuentes son oficiales

---

## 👨‍💻 Desarrollo

**Proyecto académico** desarrollado con datos abiertos oficiales para análisis de justicia ambiental.

**Fecha:** Octubre 2025

---

## 📧 Contacto

Para más información sobre las fuentes de datos:
- **SIATA:** https://siata.gov.co/
- **Área Metropolitana:** https://www.metropol.gov.co/
- **Datos Abiertos Colombia:** https://www.datos.gov.co/

---

## 📄 Licencia

Los datos utilizados son de dominio público (datos abiertos gubernamentales).  
El código de la aplicación está disponible para fines académicos.

---

**🌍 Plataforma de Análisis de Justicia Ambiental - Valle de Aburrá | 2025**
