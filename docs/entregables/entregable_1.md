# Entregable 1: Plan de Implementacion y Diseno del Esquema NoSQL

**Asignatura:** Administracion de Bases de Datos
**Docente:** Andres Oswaldo Calderon Romero, Ph.D.
**Integrantes:** Carlos Andres Pinzon Caicedo, Alejandro Esteban Padilla Gaviria
**Institucion:** Pontificia Universidad Javeriana
**Fecha:** Octubre de 2026

---

## 1. Justificacion Tecnica del Stack NoSQL

El objetivo del proyecto es cuantificar el area de techos disponibles para energia solar en los 170 municipios PDET de Colombia.

### 1.1 Eleccion de MongoDB
* **Soporte GeoJSON Nativo:** Permite almacenar geometrias espaciales directamente en los documentos.
* **Indices Espaciales 2dsphere:** Ejecutan calculos sobre el elipsoide WGS84 (EPSG:4326), optimizando busquedas espaciales masivas.
* **Operadores Geograficos:** Uso de `$geoIntersects` para cruzar las huellas de las edificaciones con las fronteras de los municipios.

### 1.2 Justificacion de los Datasets
1. **DANE MGN (PDET):** Frontera administrativa oficial para delimitar el alcance geografico.
2. **Google Open Buildings:** Dataset principal con poligonos de edificaciones y metricas de confianza.
3. **Microsoft Building Footprints:** Dataset de validacion secundaria para contrastar densidad de infraestructura.

---

## 2. Plan de Implementacion

El flujo de trabajo se divide en tres fases de ejecucion:

**Fase 1 - Extraccion y Preparacion:**
* Uso de la libreria GeoPandas en Python para leer los limites municipales del DANE (Shapefile/GeoJSON).
* Filtrado de los 170 municipios catalogados como PDET.
* Reproyeccion estandarizada del sistema de coordenadas a EPSG:4326 (WGS84), requerimiento estricto de MongoDB.

**Fase 2 - Carga e Indexacion NoSQL:**
* Ingesta de las fronteras municipales en la coleccion `pdet_municipalities`.
* Descarga de huellas de edificaciones y carga distribuida por lotes (bulk write) hacia la coleccion `building_footprints` para optimizar operaciones de I/O.
* Creacion de indices espaciales `2dsphere` post-carga para habilitar las consultas geometricas.

**Fase 3 - Agregacion Espacial:**
* Ejecucion de un Aggregation Pipeline para mapear que edificaciones se encuentran dentro de las fronteras de cada municipio.
* Calculo acumulado del area total de techos utilizables por cada entidad territorial.

---

## 3. Diseno del Esquema NoSQL

El modelo de datos se compone de dos colecciones principales. MongoDB validara la estructura GeoJSON para habilitar la indexacion y el cruce espacial.

### 3.1 Coleccion: pdet_municipalities
Almacena los limites territoriales oficiales de cada municipio PDET.

**Estructura del Documento:**
{
  "_id": "ObjectId",
  "muni_code": "String (Codigo DANE de 5 digitos)",
  "muni_name": "String",
  "department": "String",
  "subregion_pdet": "String",
  "geometry": {
    "type": "String (Polygon o MultiPolygon)",
    "coordinates": "Array (Coordenadas longitudinales y latitudinales en EPSG:4326)"
  }
}

**Indices Definidos:**
* `{ "geometry": "2dsphere" }`: Indice espacial principal.
* `{ "muni_code": 1 }`: Indice unico para acelerar consultas por municipio.

### 3.2 Coleccion: building_footprints
Almacena las detecciones individuales de techos por satelite.

**Estructura del Documento:**
{
  "_id": "ObjectId",
  "dataset_source": "String (Ej. Google Open Buildings)",
  "confidence": "Double (Nivel de certeza de la prediccion de IA)",
  "area_m2": "Double (Superficie del techo calculada en metros cuadrados)",
  "geometry": {
    "type": "String (Polygon)",
    "coordinates": "Array (Coordenadas de los vertices del techo)"
  }
}

**Indices Definidos:**
* `{ "geometry": "2dsphere" }`: Indice espacial para evaluar intersecciones.
* `{ "dataset_source": 1 }`: Indice para filtrar y comparar resultados entre Google y Microsoft.

---

## 4. Pipeline de Consultas

Para calcular el area total disponible por municipio, se implementara un *Aggregation Pipeline* en MongoDB con las siguientes etapas:

1. **`$lookup` con pipeline personalizado:** Realiza un cruce espacial desde `building_footprints` hacia `pdet_municipalities` utilizando el operador `$geoIntersects` para identificar a que municipio pertenece cada techo.
2. **`$unwind`:** Desanida el arreglo resultante del cruce para aplanar los documentos.
3. **`$group`:** Agrupa los resultados usando el campo `muni_code` y utiliza el operador acumulador `$sum` sobre el campo `area_m2` para obtener los metros cuadrados totales utilizables por municipio.
4. **`$out`:** Exporta los resultados finales a una nueva coleccion estatica para visualizacion y exportacion.
