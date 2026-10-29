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

## 2. Plan de Implementacion (En Desarrollo)

*Pendiente: Definir en equipo las fases exactas de extraccion, transformacion y carga (ETL), asi como el flujo de procesamiento espacial en la base de datos.*

---

## 3. Diseno del Esquema NoSQL (En Desarrollo)

*Pendiente: Definir con el equipo la estructura final del JSON para las colecciones (tipos de datos e indices compuestos).*

---

## 4. Pipeline de Consultas (En Desarrollo)

*Pendiente: Estructurar la sintaxis del Aggregation Pipeline usando los operadores espaciales.*
