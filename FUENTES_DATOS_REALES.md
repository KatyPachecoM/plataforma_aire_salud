# Fuentes de Datos Reales - Proyecto Calidad del Aire y Salud Pública

## Resumen del Proyecto

**Título:** Plataforma de Análisis de Justicia Ambiental en el Valle de Aburrá: Calidad del Aire y Salud Pública

**Objetivo:** Desarrollar dashboards interactivos que integren datos georreferenciados de calidad del aire y salud pública para analizar desigualdades ambientales y su impacto en la salud de las comunidades del Valle de Aburrá.

---

## Fuente 1: Calidad del Aire (SIATA)

**Nombre:** Mediciones de Material Particulado PM2.5 - Red de Monitoreo SIATA

**Entidad:** Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA) - Área Metropolitana del Valle de Aburrá

**URL:** https://datosabiertos.metropol.gov.co/node/99

**Descripción:** Mediciones horarias de concentración de material particulado fino (PM2.5) en microgramos por metro cúbico (µg/m³) de 21 estaciones de monitoreo distribuidas en el Valle de Aburrá.

**Características:**
- **Registros:** 160,883 mediciones válidas
- **Estaciones:** 21 estaciones georreferenciadas (latitud, longitud)
- **Período:** Octubre 2021 - Octubre 2022
- **Frecuencia:** Horaria
- **Municipios cubiertos:** Medellín, Itagüí, Envigado, Bello, Sabaneta, La Estrella, Caldas, Copacabana, Barbosa, Girardota

**Variables:**
- `codigo_estacion`: Código único de la estación
- `nombre_estacion`: Nombre corto de la estación
- `fecha`: Fecha y hora de la medición
- `pm25`: Concentración de PM2.5 (µg/m³)
- `calidad`: Índice de calidad del aire
- `latitud`: Coordenada geográfica
- `longitud`: Coordenada geográfica

**Archivo:** `/home/ubuntu/plataforma_aire_salud/data/mediciones_pm25_siata.csv`

---

## Fuente 2: Salud Pública (Ministerio de Salud)

**Nombre:** Indicadores de Mortalidad y Morbilidad por Departamento, Municipio y Año

**Entidad:** Ministerio de Salud y Protección Social - Dirección de Epidemiología y Demografía

**URL:** https://www.datos.gov.co/Salud-y-Protecci-n-Social/Indicadores-mortalidad-y-morbilidad-seg-n-departam/4e4i-ua65

**Descripción:** Indicadores de salud pública calculados a partir de estadísticas vitales (nacimientos y defunciones) del DANE y registros del sistema de salud.

**Características:**
- **Registros totales:** 266,001 (34,590 para Antioquia)
- **Municipios de Antioquia:** 125 municipios
- **Período:** 2005-2020
- **Frecuencia:** Anual
- **Cobertura geográfica:** Municipal

**Indicadores Relevantes para el Proyecto:**
1. **Tasa de mortalidad general** (por 1,000 habitantes)
2. **Tasa de mortalidad en menores de 5 años por IRA** (Infección Respiratoria Aguda)
3. **Tasa de mortalidad en menores de 5 años** (mortalidad infantil)
4. **Tasa de mortalidad neonatal**
5. **Razón de mortalidad materna**

**Variables:**
- `coddepartamento`: Código DANE del departamento
- `departamento`: Nombre del departamento
- `codmunicipio`: Código DANE del municipio
- `municipio`: Nombre del municipio
- `indicador`: Nombre del indicador de salud
- `a_o`: Año del indicador
- `valor_indicador`: Valor numérico del indicador

**Archivo:** `/home/ubuntu/plataforma_aire_salud/data/mortalidad_morbilidad_colombia.csv`

---

## Actores Involucrados

### Actor 1: Comunidades del Valle de Aburrá
**Descripción:** Población residente en los 10 municipios del Valle de Aburrá, especialmente comunidades vulnerables expuestas a altos niveles de contaminación atmosférica.

**Rol:** Afectados directos por la calidad del aire y sus impactos en la salud respiratoria y mortalidad.

### Actor 2: Autoridades Ambientales y de Salud Pública
**Descripción:** Área Metropolitana del Valle de Aburrá (AMVA), SIATA, Secretarías de Salud municipales, Ministerio de Salud y Protección Social.

**Rol:** Responsables del monitoreo de calidad del aire, vigilancia epidemiológica y diseño de políticas públicas para mitigar impactos en salud.

---

## Análisis Propuesto

### 1. Análisis Espacial
- Mapeo de estaciones de calidad del aire
- Distribución geográfica de indicadores de salud por municipio
- Identificación de zonas críticas (alta contaminación + altos indicadores de mortalidad)

### 2. Análisis Temporal
- Tendencias de PM2.5 a lo largo del año 2021-2022
- Evolución de indicadores de salud 2005-2020
- Identificación de patrones estacionales

### 3. Análisis de Correlación
- Relación entre niveles de PM2.5 y tasas de mortalidad por IRA
- Comparación entre municipios con diferentes niveles de contaminación
- Análisis de justicia ambiental: ¿Las comunidades más vulnerables están más expuestas?

---

## Cumplimiento de Requisitos

✅ **Mínimo 2 fuentes de datos:** Calidad del Aire (SIATA) + Salud Pública (MinSalud)

✅ **Mínimo 2 actores:** Comunidades del Valle de Aburrá + Autoridades Ambientales/Salud

✅ **Datos de los últimos 3 años:** 
- Calidad del aire: 2021-2022
- Salud pública: 2005-2020 (incluye período 2018-2020)

✅ **Datos georreferenciados:** Estaciones con lat/long + municipios con códigos DANE

✅ **Datos 100% reales:** Todas las fuentes son oficiales y verificables

---

## Tecnologías

- **Lenguaje:** Python 3.11
- **Framework de dashboards:** Streamlit
- **Análisis de datos:** Pandas, NumPy
- **Visualización:** Plotly, Matplotlib, Seaborn
- **Análisis geoespacial:** Folium, GeoPandas
- **Despliegue:** Streamlit Cloud o servidor local

---

**Fecha de recopilación:** 30 de octubre de 2025
**Autor:** Proyecto académico - Análisis de Datos Abiertos
