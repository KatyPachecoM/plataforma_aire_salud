# Propuesta Completa: Plataforma de Datos Abiertos sobre Calidad del Aire y Salud Pública en el Valle de Aburrá

## Información del Estudiante
**Curso:** Analítica de Datos  
**Actividad:** Tarea 3 - Opción 2: Plataforma de datos abiertos con dashboards  
**Tecnología:** Python + Streamlit  
**Período de datos:** 2022-2025 (últimos 3 años)

---

## 1. RESUMEN EJECUTIVO

Este proyecto propone el desarrollo de una **plataforma de datos abiertos con dashboards interactivos** que integre información sobre calidad del aire y salud pública en el Valle de Aburrá (Medellín y municipios vecinos), con el objetivo de promover la transparencia, la participación ciudadana y la justicia ambiental.

La plataforma integrará datos de dos fuentes principales:
1. **Calidad del aire:** Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA)
2. **Salud pública:** Sistema de vigilancia epidemiológica (SIVIGILA) - enfermedades respiratorias

Los dashboards desarrollados en **Python con Streamlit** permitirán a las comunidades afectadas y a la industria de salud pública visualizar, analizar y comprender las relaciones entre contaminación atmosférica y enfermedades respiratorias, facilitando la toma de decisiones informadas y la exigencia de políticas públicas más efectivas.

---

## 2. JUSTIFICACIÓN DEL PROYECTO

### 2.1. Problema Identificado

El Valle de Aburrá enfrenta una crisis ambiental y de salud pública caracterizada por:

**Contaminación atmosférica crítica:**
- Material particulado (PM2.5 y PM10) excede normas nacionales e internacionales
- Más de 41 elementos químicos y compuestos orgánicos cancerígenos identificados en PM2.5
- Episodios recurrentes de contingencia ambiental
- Geomorfología del valle dificulta dispersión de contaminantes

**Impacto en salud pública:**
- Correlación directa entre niveles de PM y consultas por enfermedades respiratorias
- Daño genético (ADN) confirmado por estudios recientes (2025)
- Enfermedades asociadas: asma, bronquitis, infecciones respiratorias, rinitis, cáncer
- Trastornos del desarrollo neurológico en niños
- Complicaciones en embarazo y muerte fetal

**Desigualdades territoriales:**
- Desigualdades geográficas en mortalidad independientes de nivel socioeconómico
- Zonas con alta carga industrial especialmente afectadas
- Poblaciones vulnerables desproporcionadamente expuestas

**Limitaciones de políticas actuales:**
- Medidas como "pico y placa" tienen efectividad limitada y decreciente
- Falta de transparencia en datos ambientales y de salud
- Participación ciudadana limitada en decisiones sobre políticas ambientales

### 2.2. Necesidad de una Plataforma de Datos Abiertos

La evidencia científica recopilada demuestra que:

1. **Transparencia:** Las comunidades necesitan acceso a datos actualizados sobre calidad del aire y salud
2. **Participación:** La ciudadanía debe poder evaluar la efectividad de políticas públicas
3. **Justicia ambiental:** Se requiere visibilizar desigualdades en exposición a contaminación
4. **Toma de decisiones:** Autoridades de salud necesitan datos integrados para intervenciones focalizadas
5. **Rendición de cuentas:** La industria y el gobierno deben ser monitoreados por la ciudadanía

---

## 3. FUENTES DE DATOS

### 3.1. Fuente 1: Calidad del Aire - SIATA

**Nombre:** Sistema de Alerta Temprana de Medellín y el Valle de Aburrá (SIATA)  
**Entidad responsable:** Área Metropolitana del Valle de Aburrá (AMVA)  
**URL oficial:** https://siata.gov.co/sitio_web/index.php/calidad_aire  
**Tipo de datos:** Series temporales de mediciones de contaminantes atmosféricos  
**Período disponible:** 2022-2025 (datos históricos disponibles desde 2008)

**Variables disponibles:**
- **PM2.5:** Material particulado menor a 2.5 micrómetros (µg/m³)
- **PM10:** Material particulado menor a 10 micrómetros (µg/m³)
- **O3:** Ozono troposférico (µg/m³)
- **NO2:** Dióxido de nitrógeno (µg/m³)
- **SO2:** Dióxido de azufre (µg/m³)
- **CO:** Monóxido de carbono (mg/m³)

**Cobertura geográfica:**
- Red de estaciones de monitoreo distribuidas en el Valle de Aburrá
- Datos georreferenciados por estación
- Cobertura de Medellín y municipios vecinos

**Frecuencia de actualización:**
- Datos en tiempo real (cada hora)
- Promedios diarios, mensuales y anuales

**Acceso a datos:**
- Portal web del SIATA
- Datos históricos disponibles en formato CSV
- API disponible para consultas programáticas (por confirmar)
- Dataset en Kaggle: https://www.kaggle.com/datasets/sjessies/datos-siata-calidad-del-aire

**Estándares de referencia:**
- Normas nacionales colombianas (Resolución 2254 de 2017)
- Guías de calidad del aire de la OMS (2021)

### 3.2. Fuente 2: Salud Pública - SIVIGILA

**Nombre:** Sistema Nacional de Vigilancia en Salud Pública (SIVIGILA)  
**Entidad responsable:** Instituto Nacional de Salud (INS) y Secretaría de Salud de Medellín  
**Tipo de datos:** Registros de consultas y casos de enfermedades de notificación obligatoria  
**Período disponible:** 2022-2025

**Variables disponibles:**
- **Infecciones respiratorias agudas (IRA):** Número de consultas y hospitalizaciones
- **Enfermedad respiratoria aguda grave (IRAG):** Casos confirmados
- **Asma:** Consultas por urgencias
- **Bronquitis:** Consultas externas y urgencias
- **Neumonía:** Casos hospitalizados
- **Rinitis alérgica:** Consultas externas

**Desagregación:**
- Por edad (grupos etarios)
- Por sexo
- Por comuna/barrio (georreferenciado)
- Por fecha de consulta

**Acceso a datos:**
- Portal de datos abiertos del gobierno colombiano: https://www.datos.gov.co
- Secretaría de Salud de Medellín
- Solicitud formal a través de mecanismos de transparencia

**Nota sobre privacidad:**
- Datos agregados (sin información personal identificable)
- Cumplimiento de Ley de Protección de Datos Personales (Ley 1581 de 2012)

### 3.3. Fuentes Complementarias

**3.3.1. Datos demográficos y socioeconómicos**
- **Fuente:** DANE (Departamento Administrativo Nacional de Estadística)
- **Datos:** Población por comuna, Índice de Pobreza Multidimensional (MPI), estratificación socioeconómica
- **URL:** https://www.dane.gov.co

**3.3.2. Datos geográficos**
- **Fuente:** DANE Geoportal
- **Datos:** Cartografía de sectores censales, comunas, barrios
- **URL:** https://geoportal.dane.gov.co

**3.3.3. Datos meteorológicos**
- **Fuente:** SIATA
- **Datos:** Temperatura, humedad, precipitación, velocidad del viento
- **Uso:** Contextualizar variaciones en calidad del aire

---

## 4. ACTORES INVOLUCRADOS

### 4.1. Actor 1: Comunidades Afectadas por Contaminación Atmosférica

**Descripción:**
Residentes del Valle de Aburrá, especialmente aquellos que habitan en:
- Comunas con alta exposición a contaminación (ej. Comuna 1 Popular, Comuna 13 San Javier)
- Zonas cercanas a corredores viales principales
- Áreas con alta carga industrial
- Barrios con baja cobertura de espacio público verde

**Características:**
- Población diversa en términos socioeconómicos (estratos 1 a 6)
- Incluye poblaciones vulnerables: niños, adultos mayores, mujeres embarazadas
- Trabajadores expuestos ocupacionalmente (conductores, vendedores ambulantes)
- Personas con enfermedades respiratorias preexistentes

**Necesidades:**
- Acceso a información actualizada sobre calidad del aire en su zona
- Comprensión de riesgos para la salud asociados a contaminación
- Alertas tempranas en días de alta contaminación
- Evidencia para exigir políticas públicas más efectivas
- Participación informada en decisiones sobre medio ambiente

**Rol en la plataforma:**
- **Usuarios principales** de los dashboards
- **Generadores de demanda** de transparencia y rendición de cuentas
- **Promotores** de cambios en políticas públicas
- **Monitores ciudadanos** de calidad del aire

### 4.2. Actor 2: Industria de Salud Pública y Autoridades Sanitarias

**Descripción:**
Instituciones y profesionales del sector salud:
- Secretaría de Salud de Medellín
- Hospitales y centros de salud (ej. Metrosalud)
- Área Metropolitana del Valle de Aburrá (AMVA)
- Epidemiólogos y profesionales de salud pública
- Tomadores de decisiones en políticas de salud

**Características:**
- Responsables de vigilancia epidemiológica
- Gestores de programas de prevención y promoción de salud
- Planificadores de servicios de salud
- Investigadores en salud ambiental

**Necesidades:**
- Datos integrados de calidad del aire y salud para análisis epidemiológicos
- Identificación de patrones espaciales y temporales de enfermedades respiratorias
- Evidencia para priorizar intervenciones en zonas críticas
- Herramientas para comunicar riesgos a la población
- Monitoreo de efectividad de políticas de salud ambiental

**Rol en la plataforma:**
- **Usuarios avanzados** de análisis de datos
- **Generadores de políticas** basadas en evidencia
- **Comunicadores** de riesgos a la población
- **Evaluadores** de efectividad de intervenciones

---

## 5. ARQUITECTURA DE LA PLATAFORMA

### 5.1. Stack Tecnológico

**Lenguaje de programación:** Python 3.11+

**Framework web:** Streamlit
- Razón: Permite desarrollo rápido de dashboards interactivos
- Facilita visualizaciones dinámicas sin necesidad de JavaScript
- Ideal para prototipado y despliegue rápido

**Bibliotecas de análisis de datos:**
- **pandas:** Manipulación y análisis de datos tabulares
- **numpy:** Operaciones numéricas y estadísticas
- **scipy:** Análisis estadístico avanzado

**Bibliotecas de visualización:**
- **plotly:** Gráficos interactivos (series temporales, scatter plots, box plots)
- **folium:** Mapas interactivos georreferenciados
- **matplotlib/seaborn:** Visualizaciones estáticas complementarias

**Análisis espacial:**
- **geopandas:** Manipulación de datos geoespaciales
- **shapely:** Operaciones geométricas

**Base de datos:**
- **SQLite:** Para almacenamiento local de datos procesados
- **PostgreSQL con PostGIS:** Para despliegue en producción (opcional)

**Despliegue:**
- **Streamlit Cloud:** Hosting gratuito para prototipo
- **Docker:** Containerización para despliegue en servidor propio (opcional)

### 5.2. Arquitectura de Datos

```
[Fuentes de Datos]
    ├── SIATA (CSV/API)
    ├── SIVIGILA (CSV/Excel)
    ├── DANE (Shapefiles/CSV)
    └── SIATA Meteorología (CSV/API)
         ↓
[ETL Pipeline - Python]
    ├── Extracción de datos
    ├── Limpieza y validación
    ├── Transformación y agregación
    └── Carga a base de datos
         ↓
[Base de Datos]
    ├── Tabla: calidad_aire_diario
    ├── Tabla: salud_respiratoria
    ├── Tabla: demografia
    └── Tabla: geografia
         ↓
[Aplicación Streamlit]
    ├── Módulo: Dashboard Principal
    ├── Módulo: Análisis Temporal
    ├── Módulo: Análisis Espacial
    ├── Módulo: Correlaciones
    └── Módulo: Alertas y Recomendaciones
         ↓
[Usuario Final]
    └── Navegador web
```

### 5.3. Módulos de la Plataforma

**Módulo 1: Dashboard Principal**
- Vista general de indicadores clave
- Estado actual de calidad del aire
- Alertas activas
- Resumen de consultas por enfermedades respiratorias

**Módulo 2: Análisis Temporal**
- Series temporales de contaminantes (2022-2025)
- Series temporales de consultas por enfermedades respiratorias
- Identificación de tendencias y estacionalidad
- Comparación con normas nacionales e internacionales

**Módulo 3: Análisis Espacial**
- Mapas de calidad del aire por estación de monitoreo
- Mapas de consultas por enfermedades respiratorias por comuna
- Identificación de zonas críticas (hotspots)
- Análisis de equidad territorial

**Módulo 4: Correlaciones y Causalidad**
- Análisis de correlación entre PM2.5/PM10 y consultas por IRA
- Modelos de series temporales (lag analysis)
- Visualización de relaciones dosis-respuesta
- Análisis de impacto de políticas públicas

**Módulo 5: Alertas y Recomendaciones**
- Sistema de alertas basado en umbrales de OMS
- Recomendaciones de salud para la población
- Predicción de días críticos (opcional)
- Información sobre derechos y mecanismos de participación

---

## 6. DASHBOARDS ESPECÍFICOS

### 6.1. Dashboard 1: Calidad del Aire en Tiempo Real

**Objetivo:** Informar a la ciudadanía sobre el estado actual de la calidad del aire

**Componentes:**
1. **Mapa interactivo:**
   - Estaciones de monitoreo del SIATA georreferenciadas
   - Código de colores según índice de calidad del aire (ICA)
   - Tooltip con valores actuales de PM2.5, PM10, O3

2. **Indicadores clave (KPIs):**
   - PM2.5 promedio del día (µg/m³)
   - PM10 promedio del día (µg/m³)
   - Número de estaciones en alerta
   - Comparación con límites OMS

3. **Gráfico de tendencia (últimos 7 días):**
   - Serie temporal de PM2.5 y PM10
   - Líneas de referencia (límites OMS y norma colombiana)

4. **Alertas:**
   - Banner con nivel de alerta actual (Verde/Amarillo/Naranja/Rojo)
   - Recomendaciones de salud según nivel de alerta

**Interactividad:**
- Selección de estación de monitoreo
- Selección de contaminante a visualizar
- Filtro por rango de fechas

### 6.2. Dashboard 2: Impacto en Salud Respiratoria

**Objetivo:** Visualizar la relación entre contaminación y enfermedades respiratorias

**Componentes:**
1. **Serie temporal dual:**
   - Eje Y izquierdo: Concentración de PM2.5 (µg/m³)
   - Eje Y derecho: Número de consultas por IRA
   - Período: 2022-2025
   - Identificación visual de correlación

2. **Gráfico de dispersión:**
   - Eje X: PM2.5 promedio semanal
   - Eje Y: Consultas por IRA semanal
   - Línea de tendencia con R²
   - Tooltip con información detallada

3. **Análisis de lag (rezago):**
   - Correlación entre PM2.5 y consultas con diferentes rezagos (0-7 días)
   - Identificación del lag óptimo
   - Interpretación: "Las consultas aumentan X días después de alta contaminación"

4. **Desagregación por enfermedad:**
   - Gráfico de barras apiladas
   - Consultas por tipo: IRA, asma, bronquitis, neumonía
   - Comparación entre períodos de alta y baja contaminación

**Interactividad:**
- Selección de enfermedad específica
- Selección de contaminante (PM2.5, PM10, O3)
- Filtro por grupo etario (niños, adultos, adultos mayores)

### 6.3. Dashboard 3: Desigualdades Territoriales

**Objetivo:** Evidenciar desigualdades en exposición a contaminación y acceso a salud

**Componentes:**
1. **Mapa de equidad territorial:**
   - Capa 1: Concentración promedio de PM2.5 por comuna (2022-2025)
   - Capa 2: Tasa de consultas por IRA por 100.000 habitantes por comuna
   - Capa 3: Índice de Pobreza Multidimensional (MPI) por comuna
   - Superposición de capas para identificar inequidades

2. **Gráfico de correlación espacial:**
   - Scatter plot: MPI vs PM2.5 por comuna
   - Identificación de comunas con alta contaminación y alta pobreza
   - Identificación de comunas con alta contaminación y baja pobreza

3. **Ranking de comunas:**
   - Tabla interactiva con ranking por:
     - Mayor exposición a PM2.5
     - Mayor tasa de consultas por IRA
     - Mayor inequidad (alta contaminación + alta pobreza)

4. **Análisis de autocorrelación espacial:**
   - Índice de Moran para identificar clusters de alta contaminación
   - Mapa de clusters (High-High, Low-Low, High-Low, Low-High)

**Interactividad:**
- Selección de comuna para ver detalle
- Filtro por año (2022, 2023, 2024, 2025)
- Descarga de datos por comuna en CSV

### 6.4. Dashboard 4: Evaluación de Políticas Públicas

**Objetivo:** Monitorear la efectividad de políticas ambientales implementadas

**Componentes:**
1. **Línea de tiempo de políticas:**
   - Marcadores en serie temporal indicando implementación de políticas
   - Ej: "Pico y placa ambiental", "Día sin carro", "Restricción vehicular"

2. **Análisis antes-después:**
   - Comparación de PM2.5 promedio antes y después de política
   - Prueba estadística de significancia (t-test)
   - Visualización de cambio porcentual

3. **Análisis de efectividad temporal:**
   - Gráfico de efectividad de política en el tiempo
   - Identificación de degradación de efectividad (ej. pico y placa)

4. **Costo-beneficio en salud:**
   - Estimación de reducción en consultas por IRA atribuible a política
   - Cálculo de años de vida ajustados por discapacidad (AVAD) evitados
   - Comparación con costo de implementación (si disponible)

**Interactividad:**
- Selección de política específica
- Selección de período de análisis
- Comparación entre múltiples políticas

### 6.5. Dashboard 5: Participación Ciudadana

**Objetivo:** Facilitar la participación informada de la ciudadanía

**Componentes:**
1. **Mi barrio:**
   - Selección de barrio/comuna de residencia
   - Indicadores personalizados para el barrio
   - Comparación con promedio de la ciudad

2. **Calculadora de riesgo:**
   - Ingreso de características personales (edad, condiciones preexistentes)
   - Estimación de riesgo personal basado en exposición
   - Recomendaciones personalizadas

3. **Reportes ciudadanos:**
   - Formulario para reportar episodios de alta contaminación percibida
   - Mapa de reportes ciudadanos
   - Validación con datos oficiales del SIATA

4. **Recursos y acciones:**
   - Información sobre derechos ambientales
   - Mecanismos de participación (tutelas, derechos de petición)
   - Contactos de autoridades ambientales y de salud
   - Organizaciones ciudadanas trabajando en el tema

**Interactividad:**
- Personalización completa según ubicación y perfil
- Suscripción a alertas por correo/SMS
- Compartir datos en redes sociales

---

## 7. ANÁLISIS DE DATOS

### 7.1. Análisis Descriptivo

**Estadísticas descriptivas:**
- Media, mediana, desviación estándar de PM2.5 y PM10 por año
- Distribución de consultas por enfermedades respiratorias por mes
- Identificación de valores atípicos (outliers)

**Análisis de tendencias:**
- Tendencia temporal de contaminantes (2022-2025)
- Tendencia temporal de consultas por IRA (2022-2025)
- Identificación de estacionalidad (meses críticos)

**Análisis de distribución:**
- Histogramas de PM2.5 y PM10
- Box plots por año, mes, estación
- Identificación de días que exceden normas OMS

### 7.2. Análisis de Correlación

**Correlación temporal:**
- Correlación de Pearson entre PM2.5 y consultas por IRA
- Correlación con diferentes lags (0-7 días)
- Correlación entre diferentes contaminantes

**Correlación espacial:**
- Correlación entre PM2.5 por comuna y tasa de IRA por comuna
- Índice de Moran para autocorrelación espacial
- Identificación de clusters espaciales

### 7.3. Análisis de Series Temporales

**Descomposición de series:**
- Tendencia, estacionalidad y residuos
- Identificación de patrones recurrentes

**Análisis de lag (rezago):**
- Cross-correlation entre PM2.5 y consultas por IRA
- Identificación del lag óptimo
- Interpretación epidemiológica

**Modelos de series temporales:**
- ARIMA para predicción de PM2.5 (opcional)
- Modelos de regresión con lags para estimar impacto de contaminación en salud

### 7.4. Análisis Espacial

**Mapas de calor:**
- Interpolación espacial de PM2.5 (Kriging o IDW)
- Identificación de zonas de alta exposición

**Análisis de clusters:**
- Identificación de hotspots de contaminación
- Identificación de hotspots de enfermedades respiratorias
- Análisis de superposición

**Análisis de equidad:**
- Correlación entre MPI y exposición a PM2.5
- Identificación de inequidades ambientales
- Análisis de justicia ambiental

### 7.5. Análisis de Impacto

**Análisis antes-después de políticas:**
- Comparación de medias (t-test)
- Análisis de series interrumpidas
- Estimación de cambio atribuible a política

**Análisis de carga de enfermedad:**
- Fracción atribuible poblacional (FAP)
- Años de vida ajustados por discapacidad (AVAD)
- Estimación de consultas evitables con mejor calidad del aire

---

## 8. DIMENSIONES ÉTICAS Y SOCIALES

### 8.1. Justicia Ambiental

**Problema:**
La contaminación atmosférica afecta desproporcionadamente a poblaciones vulnerables:
- Comunas de bajos recursos con mayor exposición
- Trabajadores informales expuestos ocupacionalmente
- Niños y adultos mayores con mayor susceptibilidad

**Enfoque de la plataforma:**
- Visibilizar desigualdades en exposición a contaminación
- Evidenciar correlación entre pobreza y mala calidad del aire
- Proporcionar datos para exigir equidad en políticas ambientales

**Principio ético:**
> "Todas las personas tienen derecho a respirar aire limpio, independientemente de su nivel socioeconómico o ubicación geográfica"

### 8.2. Derecho a la Información

**Problema:**
Acceso limitado y fragmentado a datos ambientales y de salud:
- Datos dispersos en múltiples fuentes
- Lenguaje técnico poco accesible
- Falta de integración entre datos ambientales y de salud

**Enfoque de la plataforma:**
- Centralizar datos de múltiples fuentes
- Presentar información en lenguaje accesible
- Visualizaciones intuitivas para público no técnico
- Datos descargables para análisis independientes

**Principio ético:**
> "La ciudadanía tiene derecho a acceder a información clara, actualizada y comprensible sobre los factores ambientales que afectan su salud"

### 8.3. Participación Ciudadana

**Problema:**
Limitada participación de la ciudadanía en decisiones sobre políticas ambientales:
- Falta de información para participación informada
- Mecanismos de participación poco conocidos
- Asimetría de información entre ciudadanía y gobierno/industria

**Enfoque de la plataforma:**
- Empoderar a la ciudadanía con datos y análisis
- Facilitar monitoreo ciudadano de políticas públicas
- Proporcionar herramientas para exigir rendición de cuentas
- Información sobre mecanismos de participación

**Principio ético:**
> "La participación ciudadana informada es esencial para la democracia ambiental y la efectividad de políticas públicas"

### 8.4. Transparencia y Rendición de Cuentas

**Problema:**
Falta de transparencia en:
- Efectividad de políticas ambientales implementadas
- Cumplimiento de normas por parte de industrias
- Asignación de recursos para salud ambiental

**Enfoque de la plataforma:**
- Evaluación objetiva de efectividad de políticas
- Monitoreo de tendencias temporales de contaminación
- Evidencia de impacto en salud pública
- Datos abiertos para auditoría ciudadana

**Principio ético:**
> "Las autoridades y la industria deben rendir cuentas a la ciudadanía sobre el impacto ambiental y sanitario de sus decisiones y actividades"

### 8.5. Derecho a la Salud

**Problema:**
La contaminación atmosférica es una amenaza para el derecho fundamental a la salud:
- Daño genético (ADN) confirmado
- Enfermedades crónicas y agudas
- Efectos intergeneracionales (daño en desarrollo fetal)

**Enfoque de la plataforma:**
- Evidenciar relación causal entre contaminación y enfermedades
- Cuantificar carga de enfermedad atribuible a contaminación
- Fundamentar exigencia de políticas de salud ambiental
- Alertas tempranas para protección de poblaciones vulnerables

**Principio ético:**
> "El derecho a la salud incluye el derecho a un ambiente sano que no ponga en riesgo la vida y la integridad física de las personas"

---

## 9. CRONOGRAMA DE DESARROLLO

### Fase 1: Recopilación y Preparación de Datos (Semanas 1-2)
- Descarga de datos del SIATA (2022-2025)
- Solicitud de datos de SIVIGILA
- Descarga de datos demográficos y geográficos del DANE
- Limpieza y validación de datos
- Creación de base de datos

### Fase 2: Análisis Exploratorio (Semana 3)
- Estadísticas descriptivas
- Identificación de patrones temporales
- Análisis de correlaciones preliminares
- Identificación de datos faltantes o inconsistentes

### Fase 3: Desarrollo de Dashboards (Semanas 4-6)
- Configuración de entorno Streamlit
- Desarrollo de Dashboard 1: Calidad del Aire
- Desarrollo de Dashboard 2: Impacto en Salud
- Desarrollo de Dashboard 3: Desigualdades Territoriales
- Desarrollo de Dashboard 4: Evaluación de Políticas
- Desarrollo de Dashboard 5: Participación Ciudadana

### Fase 4: Análisis Avanzado (Semana 7)
- Análisis de series temporales
- Análisis espacial (clusters, autocorrelación)
- Análisis de impacto de políticas
- Cálculo de indicadores de equidad

### Fase 5: Documentación y Despliegue (Semana 8)
- Documentación técnica
- Guía de usuario
- Despliegue en Streamlit Cloud
- Pruebas de usabilidad
- Ajustes finales

---

## 10. ENTREGABLES

### 10.1. Código Fuente
- Repositorio en GitHub con código completo
- Scripts de ETL (extracción, transformación, carga)
- Scripts de análisis de datos
- Aplicación Streamlit con 5 dashboards
- Documentación de código

### 10.2. Datos Procesados
- Base de datos SQLite con datos integrados
- Archivos CSV con datos limpios y agregados
- Shapefiles con datos georreferenciados

### 10.3. Documentación
- **Informe técnico:** Metodología, análisis y resultados
- **Guía de usuario:** Cómo usar la plataforma
- **Documento de fuentes:** Referencias a las 6+ fuentes académicas
- **README:** Instrucciones de instalación y ejecución

### 10.4. Plataforma Web
- URL pública de la plataforma en Streamlit Cloud
- Dashboards interactivos funcionales
- Datos actualizados (2022-2025)

### 10.5. Presentación
- Presentación en PowerPoint/PDF
- Video demo de la plataforma (opcional)

---

## 11. REFERENCIAS ACADÉMICAS (6 FUENTES MÍNIMAS)

### Fuente 1: Justicia Ambiental y Desigualdad
**Título:** El color del aire: contaminación y desigualdad en Colombia  
**Fuente:** Universidad de los Andes  
**URL:** https://www.uniandes.edu.co/es/noticias/medio-ambiente/el-color-del-aire-contaminacion-y-desigualdad-en-colombia  
**Relevancia:** Marco conceptual de justicia ambiental y desigualdades en exposición a contaminación en Colombia

### Fuente 2: Contaminación y Enfermedades Respiratorias
**Título:** Contaminación por material particulado (PM2,5 y PM10) y consultas por enfermedades respiratorias en Medellín (2008-2009)  
**Autores:** Carlos F. Gaviria G., Paula C. Benavides C., Carolina A. Tangarife  
**Publicación:** Revista Facultad Nacional de Salud Pública, vol.29 no.3, 2011  
**URL:** http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0120-386X2011000300004  
**Relevancia:** Evidencia estadística de relación entre PM2.5/PM10 y consultas por enfermedades respiratorias en Medellín

### Fuente 3: Efectividad del Pico y Placa
**Título:** Análisis del "Pico y Placa" como restricción a la circulación vehicular en Medellín - Basado en volúmenes vehiculares  
**Autores:** John Jairo Posada Henao, Viviana Farbiarz Castro, Carlos Alberto González Calderón  
**Publicación:** DYNA rev.fac.nac.minas, vol.78 no.165, 2011  
**URL:** http://www.scielo.org.co/scielo.php?script=sci_arttext&pid=S0012-73532011000100011  
**Relevancia:** Evaluación de efectividad de políticas de restricción vehicular en Medellín, demuestra limitaciones de políticas actuales

### Fuente 4: Impacto Genético del PM2.5
**Título:** Entre el aire y el ADN: investigación evidencia el impacto invisible de las partículas PM2.5 en la salud genética del Valle de Aburrá  
**Institución:** Politécnico Colombiano Jaime Isaza Cadavid  
**Fecha:** 27 de mayo de 2025  
**URL:** https://www.politecnicojic.edu.co/comunicados-y-boletines/6143-entre-el-aire-y-el-adn-investigacion-evidencia-el-impacto-invisible-de-las-particulas-pm2-5-en-la-salud-genetica-del-valle-de-aburra  
**Relevancia:** Evidencia reciente (2025) de daño genético causado por PM2.5 en el Valle de Aburrá, más de 41 elementos químicos cancerígenos identificados

### Fuente 5: Equidad Territorial
**Título:** Equidad territorial en Medellín: espacio público, amenazas naturales y calidad del aire  
**Autores:** María Fernanda Cárdenas, Jhon Fredy Escobar, Katheryn Gutiérrez  
**Publicación:** Estudios Socioterritoriales. Revista de Geografía, núm. 27, 2020  
**DOI:** https://doi.org/10.37838/unicen/est.27-046  
**Relevancia:** Análisis de equidad territorial en Medellín integrando calidad del aire con nivel socioeconómico, metodología de análisis espacial

### Fuente 6: Desigualdades en Mortalidad
**Título:** Intraurban Geographic and Socioeconomic Inequalities of Mortality in Four Cities in Colombia  
**Autores:** Laura A Rodriguez-Villamizar, Diana Marín, et al.  
**Publicación:** International Journal of Environmental Research and Public Health, 20(2):992, 2023  
**DOI:** 10.3390/ijerph20020992  
**Relevancia:** Desigualdades geográficas y socioeconómicas en mortalidad dentro de Medellín, sugiere que factores ambientales impactan distribución espacial de mortalidad

---

## 12. CONCLUSIÓN

Este proyecto propone una plataforma de datos abiertos que integra información sobre calidad del aire y salud pública en el Valle de Aburrá, con el objetivo de promover la transparencia, la participación ciudadana y la justicia ambiental.

La plataforma desarrollada en **Python con Streamlit** proporcionará a las comunidades afectadas y a las autoridades de salud pública herramientas para:

1. **Visualizar** la relación entre contaminación atmosférica y enfermedades respiratorias
2. **Identificar** desigualdades territoriales en exposición a contaminación
3. **Evaluar** la efectividad de políticas públicas ambientales
4. **Participar** informadamente en decisiones sobre medio ambiente y salud
5. **Exigir** rendición de cuentas a autoridades e industria

La evidencia científica recopilada de 6 fuentes académicas demuestra que:
- El PM2.5 y PM10 en el Valle de Aburrá causan daño genético y enfermedades respiratorias
- Existen desigualdades territoriales en exposición a contaminación
- Las políticas actuales tienen efectividad limitada
- Se requiere transparencia y participación ciudadana para abordar el problema

Esta plataforma representa un paso hacia la **democracia ambiental** y la **justicia en salud pública**, empoderando a la ciudadanía con datos y análisis para exigir su derecho a respirar aire limpio.

---

**Fecha de elaboración:** Octubre 30, 2025  
**Tecnología:** Python + Streamlit  
**Período de datos:** 2022-2025  
**Fuentes académicas:** 6 (mínimo requerido cumplido)
