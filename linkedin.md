# LinkedIn — texto para pegar y qué mueve la aguja

Actualizado: 2026-09-12. Basado en documentación oficial de LinkedIn (`/help/`,
`/blog/engineering/`, `business.linkedin.com`) y en un dataset de 571 vacantes vivas
de Get on Board. Cada afirmación marcada **(A)** tiene doc oficial o dato; **(B)** es
consenso profesional sin medición; **(C)** es mito.

---

## PARTE 1 — Dónde rinde tu tiempo

LinkedIn Recruiter indexa **exactamente cuatro zonas de texto**: tarjeta del perfil,
**About**, **Experiencia** (título, descripción y ubicación) y **Skills**. Banner,
sección Destacado y URL personalizada **no aparecen** en esa lista. **(A)**

| Acción | Impacto | Evidencia |
|---|---|---|
| Llenar la sección **Idiomas** | **Alto** — filtro booleano duro | (A) |
| Poner 20-30 **Skills** del catálogo | **Alto** — único filtro binario | (A) |
| Keywords en **headline / About / Experiencia** | Alto | (A) |
| Mantener **"Open to work · solo reclutadores"** | Medio | (A) |
| **Actualizar el perfil** y subir el CV | Medio — spotlight *Active talent* | (A) |
| Seguir e interactuar con **la empresa objetivo** | Medio — spotlight *Interested in your company* | (A) |
| Verificar el empleo con email corporativo | Bajo — spotlight *Verifications* | (A) |
| Foto profesional | Bajo pero gratis | (B) |
| **Postear contenido** | **Ninguno sobre sourcing** | (C) |
| Banner, Destacado, URL personalizada | **Ninguno sobre búsqueda** | (C) |

**Cambio importante:** desde enero 2026 la búsqueda de LinkedIn es **semántica (LLM)**,
no de coincidencia exacta. Repetir la misma keyword pierde valor; usar el vocabulario
natural del rol y sus variantes, gana. **(A)**

---

## PARTE 2 — Los dos campos que probablemente tenés vacíos o flojos

### 2.1 Idiomas — el más rentable y el que casi nadie llena

Es un **filtro booleano duro con nivel de competencia**. Vacío, desaparecés de toda
búsqueda filtrada por idioma — **incluidas las que buscan hispanohablantes nativos**,
que es justamente tu mercado. **(A)**

```
Español  →  Native or bilingual proficiency
Inglés   →  Limited working proficiency
```

Declarar el nivel honesto trabaja en las dos direcciones: te encuentra quien busca
español nativo, y quien exige inglés conversacional te descarta **antes** de quemarte
una entrevista. No te cierra puertas — te canaliza al pool donde podés competir.

### 2.2 Skills — el único filtro binario

Si la skill no está en el campo estructurado, **no pasás el filtro** por más que tu
experiencia la implique. Máximo 100 (el help dice 100, un blog de 2024 dice 50 —
LinkedIn se contradice). Poné **20-30 con el nombre exacto del catálogo**, reordená
para que las 3-5 primeras sean las del rol objetivo, y asociá cada una al puesto
donde la usaste.

Ordenadas por frecuencia real en vacantes de datos (dataset de 571 vacantes):

```
Python · SQL · ETL · Data Engineering · Data Warehousing · Data Modeling
PostgreSQL · Microsoft SQL Server · dbt · Docker · Git · CI/CD · Data Quality
Apache Airflow · Dagster · Power BI · Pandas · Terraform · Microsoft Azure
Amazon Web Services (AWS) · Model Context Protocol (MCP) · LLMs · Python Testing
```

**Sobre Airflow:** ponelo SOLO si lo tocaste. Si no, dejá Dagster. El dato crudo es
que Dagster tiene 23 avisos en UK contra 244 de Airflow, y el 100% de los que piden
Dagster también piden Airflow — pero mentir en una skill se cae en la primera
pregunta técnica.

---

## PARTE 3 — Texto para pegar

### Criterio de confidencialidad (se mantiene)

LinkedIn es público, permanente e indexado. **Nombrá la capacidad, no el cliente, ni
el volumen del negocio ajeno, ni el defecto que encontraste.**

### 3.1 Headline (máx. 220 · este usa ~140)

El título exacto va **adelante**: es lo que sobrevive al truncado en móvil y en la
tarjeta de resultados. "Data Engineer" es el mercado grande (2.033 avisos UK contra
867 de AI Engineer), así que va primero y la IA va de segundo bloque.

```
Data Engineer | Python · SQL · dbt · Dagster · ETL | Pipelines en producción con TDD | AI Engineer: servidores MCP y tooling de agentes
```

No metas "Open to work" ni "buscando oportunidades": ocupa espacio de keywords y el
spotlight ya cumple esa función.

### 3.2 About (máx. 2.600 · este usa ~1.100)

LinkedIn recomienda oficialmente **primera persona, keywords naturales y un CTA al
final** **(A)**. El gancho va en las primeras 2-3 líneas, porque ahí corta el "…ver más".

```
Soy Ingeniero en Sistemas y Data Engineer. Construyo pipelines de datos en producción y herramientas para que la IA opere infraestructura real.

Trabajo a diario con Python, SQL, Dagster y dbt sobre un data warehouse corporativo en SQL Server: procesos ETL, conciliaciones bancarias, integraciones REST, alertado propio y monitoreo autónomo. Todo con TDD estricto y desarrollo guiado por especificación — escribo los tests antes que el código, incluso cuando el código lo asiste un modelo.

También construyo y opero un fleet de 6 servidores MCP (Model Context Protocol) propios que permiten manejar orquestación, bases de datos y despliegues desde asistentes de IA, con validador read-only y confirmación de dos pasos para operaciones en producción.

Dos resultados que me representan: optimicé un forecast mensual de demanda de ~18 horas a ~61 minutos manteniendo el output byte-idéntico, y reduje un 94% los falsos positivos de un sistema de screening de cumplimiento sin perder un solo verdadero positivo.

Stack: Python · SQL · Dagster · dbt · PostgreSQL · SQL Server · Docker · Terraform · Azure · AWS · Rust · MCP

Trabajo en remoto para LATAM y mi idioma de trabajo es el español. Si tenés un equipo de datos que necesita pipelines confiables y no solo funcionales, escribime.
```

### 3.3 Experiencia — Grupo Farinter

**Título:** `Desarrollador RPA & Data Engineer`

**Nombre de empresa:** hoy figura como "Somos GF - Talento" y tu CV dice "Grupo
Farinter". Que coincidan, o un reclutador que cruce los dos ve empleadores distintos.

**Descripción** (~1.150 de 2.000 caracteres):

```
Data engineering y automatización sobre el data warehouse corporativo (SQL Server + Dagster), y construcción de herramientas MCP para operar producción desde asistentes de IA.

• Optimicé un forecast mensual de demanda (~23.000 series) de ~18 horas a ~61 minutos en producción, paralelizando con multiprocessing, con output byte-idéntico y determinista.

• Construí y opero un fleet de 6 servidores MCP (Model Context Protocol) propios que permiten manejar orquestación, consultas y despliegues desde asistentes de IA, con validador read-only y confirmación de dos pasos para operaciones en producción.

• Desarrollé un RPA de screening de cumplimiento contra listas restrictivas internacionales con matching difuso, reduciendo un 94% los falsos positivos sin perder verdaderos positivos.

• Construí pipelines ETL y de conciliación bancaria: integraciones REST autenticadas con OAuth2 y secretos en HashiCorp Vault, modelos dbt incrementales y asset checks de calidad de datos.

• Diseñé el sistema de alertado y observabilidad de los pipelines, con censo del workspace vía GraphQL y atribución de incidentes que redujo drásticamente el ruido de las alertas.
```

### 3.4 Analiza

Títulos que no coinciden: LinkedIn dice `Full Stack Engineer`, tu CV dice
`Software Developer`. Elegí uno y usalo en los dos lados.

```
Desarrollo de sistemas de producción para laboratorios clínicos en Honduras, Guatemala y El Salvador.

• Automaticé la integración entre el equipo de laboratorio y el CRM con FastAPI y protocolos médicos estándar (ASTM/HL7), en producción y bidireccional.

• Modelé catálogos clínicos complejos con SQLModel ORM, con relaciones entre encabezados y detalles de antibiogramas.

• Creé un proxy corporativo con Docker, Squid y OpenVPN reduciendo la gestión de 30+ equipos a un solo punto.
```

### 3.5 GuabaBIT

LinkedIn dice `System Engineering Intern`, tu CV dice `QA & Backend Developer`.

```
• Diseñé la documentación técnica de arquitectura para un sistema de pagos con servicios RESTful, NestJS, DynamoDB y AWS (S3, SNS).

• Implementé pruebas E2E con Playwright para flujos críticos y automaticé testing de API.
```

### 3.6 Educación — falta una entrada

```
Universidad Nacional Autónoma de Honduras
Licenciatura en Matemáticas (en curso)
2024 – Actualidad
```

---

## PARTE 4 — Configuración de "Open to Work"

**Dejalo en "Solo reclutadores". No actives el banner verde.** Tres razones con
documentación oficial y una de contexto:

1. Quien elige "solo reclutadores" **aparece igual en el spotlight Open to work**; lo
   único que no se muestra es el marco verde en la foto. El banner **no agrega nada
   del lado del reclutador**. **(A)**
2. LinkedIn precisó que la señal **privada** ya aporta ~2x del efecto; el banner
   público lleva a ~3x. El famoso "40% más InMails" es *banner vs. señal privada*,
   no *banner vs. nada*, y es de 2020. **(A)**
3. Estás **empleado**, y LinkedIn admite por escrito que con "solo reclutadores"
   *"no podemos garantizar privacidad completa"* — con el banner público ni lo intenta. **(A)**
4. Los reclutadores que lo leen como señal de desesperación se concentran en agencias
   y executive search; los sourcers in-house lo usan como herramienta. **(B)**

**Configuralo así:**
- Workplace type: **Remote** (Recruiter tiene filtro dedicado para esto)
- Locations: Honduras + los países LATAM donde aceptarías contrato
- Job titles: **en inglés y en español** (Data Engineer, Ingeniero de Datos, AI Engineer…)

⚠️ LinkedIn apaga el Open to Work si dejás de responder mensajes de reclutadores.
Revisalo cada tanto.

*Caveat honesto:* no existe ningún experimento controlado sobre el banner. El mejor
dato observacional (interviewing.io, n>10.000) muestra que **el signo del efecto se
invirtió con el ciclo del mercado**: en 2021 los del badge aprobaban 7 puntos menos;
en 2023, 5 puntos más. Es una decisión de riesgo, no un hecho.

---

## PARTE 5 — Mitos, para que no te los vendan

| Circula por todos lados | Realidad |
|---|---|
| "El ATS rechaza el 75% de los CV automáticamente" | Sale de un **argumento de venta de Preptel (2012)**, empresa que cerró en 2013 sin publicar metodología |
| "Harvard: 88% de rechazo automático" | Ese 88% es **percepción autodeclarada** en encuesta de **enero 2020**, y la causa que identifica el informe son filtros del empleador, no el formato del CV |
| "Los reclutadores miran tu CV 6 segundos" | Estudio de **Ladders**, una bolsa de empleo que vende optimización de CV. Sin muestra, sin metodología, nunca revisado por pares |
| "El headline pesa 5x en el índice" | El paper de LinkedIn sobre Talent Search **nunca menciona ponderación por campo** |
| "Postear te hace aparecer en búsquedas de reclutadores" | Confunde alcance de feed con ranking de sourcing. **No aparece en ninguna doc de LinkedIn** |
| "Estudio de LinkedIn: 14.5% vs 4.6% con Open to Work" | **No es de LinkedIn.** Es un reclutador independiente, n=487, marzo 2022 |
| "Update del algoritmo 2026: más peso a la densidad de keywords" | LinkedIn publicó lo **contrario** en enero 2026: búsqueda semántica |

**Trampa de fuentes:** las páginas bajo `linkedin.com/top-content/...` están en el
dominio de LinkedIn pero son contenido agregado, **no** investigación oficial.

---

## PARTE 6 — Orden de ejecución

1. **Idiomas** — 2 minutos, filtro duro, es lo que más te falta
2. **Skills** — 20-30 del catálogo, reordenadas. Donde más rinde tu tiempo
3. **Headline** — título exacto adelante
4. **About** — reponé los saltos de párrafo (LinkedIn los colapsa al pegar)
5. Nombre de empresa: que coincida con el CV
6. Títulos de Analiza y GuabaBIT: que coincidan con el CV
7. Licenciatura en Matemáticas
8. Verificar empleo con email corporativo
9. Subir el CV para compartir con reclutadores → spotlight *Active talent*

**Lo que NO vale tu tiempo:** postear para "el algoritmo", el banner personalizado,
la sección Destacado y la URL bonita como factores de búsqueda. Hacelos si querés
que se vea prolijo ante un humano que ya llegó — no esperes que te encuentren por eso.
