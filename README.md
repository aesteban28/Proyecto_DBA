# Evaluacion del Potencial Energetico Solar en Territorios PDET mediante NoSQL

**Asignatura:** Administracion de Bases de Datos  
**Docente:** Andres Oswaldo Calderon Romero, Ph.D.  
**Institucion:** Pontificia Universidad Javeriana - Facultad de Ciencias, Departamento de Matematicas  
**Fecha:** Octubre de 2026  

---

## 1. Descripcion del Proyecto

Este proyecto responde a la iniciativa estrategica de la Unidad de Planeacion Minero Energetica (UPME) de Colombia para evaluar la factibilidad de soluciones de energia solar en municipios priorizados bajo los Programas de Desarrollo con Enfoque Territorial (PDET).

El objetivo principal es disenar e implementar un flujo de trabajo geoespacial reproducible en una arquitectura de base de datos NoSQL (MongoDB). El sistema integra limites administrativos oficiales con datasets globales de huellas de edificaciones derivadas de imagenes satelitales, permitiendo cuantificar la cantidad y el area total de techos disponibles para la recoleccion de energia limpia en cada municipio PDET.

---

## 2. Tecnologias y Fuentes de Datos

### Stack Tecnologico
* Base de Datos NoSQL: MongoDB (Indexacion espacial 2dsphere, consultas geometricas $geoIntersects / $geoWithin, y Aggregation Pipelines).
* Lenguaje y Procesamiento: Python 3 (PyMongo, GeoPandas, Shapely).
* Control de Versiones: Git y GitHub.
* Documentacion: LaTeX / Markdown.

### Datasets Geoespaciales
1. Limites Municipales: Marco Geoestadistico Nacional (MGN) - DANE (Filtrado por municipios PDET).
2. Huellas de Edificaciones:
   * Google Open Buildings
   * Microsoft Building Footprints

---

## 3. Estructura del Repositorio

.
├── README.md               # Descripcion general del proyecto
├── .gitignore              # Filtro de archivos no rastreados por Git
├── docs/                   # Documentacion, diagramas y entregables semanales
│   └── entregables/        # Reportes en formato PDF (Entregables 1 a 4)
├── src/                    # Codigo fuente en Python
│   ├── ingest.py           # Scripts de carga e ingesta a MongoDB
│   └── spatial_queries.py  # Consultas de interseccion espacial y agregacion
└── data/                   # Datos locales de prueba (excluidos de Git)

---

## 4. Integrantes del Equipo

* Carlos Andres Pinzon Caicedo - Pontificia Universidad Javeriana
* Alejandro Esteban Padilla Gaviria - Pontificia Universidad Javeriana

---

## 5. Plan de Entregables

- [x] Semana 1: Plan de Implementacion y Diseno del Esquema NoSQL (MongoDB).
- [ ] Semana 2: Integracion e Indexacion Espacial de Territorios PDET (DANE/MGN).
- [ ] Semana 3: Carga, Indexacion Espacial y EDA de Huellas de Edificaciones.
- [ ] Semana 4: Flujo de Analisis Geoespacial Reproducible, Reporte Tecnico Final y Defensa.
