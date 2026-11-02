# Evaluacion del Potencial Energetico Solar en Territorios PDET mediante NoSQL

**Asignatura:** Administracion de Bases de Datos  
**Docente:** Andres Oswaldo Calderon Romero, Ph.D.  
**Institucion:** Pontificia Universidad Javeriana - Facultad de Ciencias, Departamento de Matematicas  
**Fecha:** Octubre de 2026  

---

## 1. Descripcion del Proyecto

Este proyecto evalua la factibilidad de soluciones de energia solar fotovoltaica en los 170 municipios de Colombia priorizados bajo los Programas de Desarrollo con Enfoque Territorial (PDET), mediante el procesamiento de datos geoespaciales masivos en una arquitectura NoSQL (MongoDB).

---

## 2. Tecnologias y Fuentes de Datos

### Stack Tecnologico
* Base de Datos NoSQL: MongoDB (Indexacion espacial 2dsphere, consultas geometricas $geoIntersects / $geoWithin y Aggregation Pipelines).
* Lenguaje y Procesamiento: Python 3 (PyMongo, GeoPandas, Shapely).
* Control de Versiones: Git y GitHub.

### Datasets Geoespaciales
1. Limites Municipales: Marco Geoestadistico Nacional (MGN) - DANE (Filtrado por los 170 municipios PDET).
2. Huellas de Edificaciones (Satelital AI):
   * Google Open Buildings (Poligonos de edificacion con metricas de confianza).
   * Microsoft Building Footprints (Dataset vectorial comparativo de infraestructura).

---

## 3. Estructura del Repositorio

.
├── README.md               # Descripcion general del proyecto
├── .gitignore              # Filtro de archivos no rastreados por Git
├── requirements.txt        # Dependencias de librerias Python
├── docs/                   # Documentacion y entregables semanales
│   └── entregables/        # Reportes tecnicos (Entregables 1 a 4)
├── src/                    # Codigo fuente en Python
│   └── config.py           # Parametros de conexion y colecciones MongoDB
└── data/                   # Datos locales excluidos de Git

---

## 4. Integrantes del Equipo

* Carlos Andres Pinzon Caicedo - Pontificia Universidad Javeriana
* Alejandro Esteban Padilla Gaviria - Pontificia Universidad Javeriana

---

## 5. Plan de Entregables

- [/] Semana 1: Plan de Implementacion y Diseno del Esquema NoSQL (Completado - 100%).
- [ ] Semana 2: Integracion e Indexacion Espacial de Territorios PDET (DANE/MGN).
- [ ] Semana 3: Carga, Indexacion Espacial y EDA de Huellas de Edificaciones.
- [ ] Semana 4: Flujo de Analisis Geoespacial Reproducible, Reporte Tecnico Final y Defensa.
