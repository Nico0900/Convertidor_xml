# 📚 Manual de Usuario
## Convertidor Universal XML - Adobe Illustrator

---

## 📖 Índice

1. [🎯 Introducción](#-introducción)
2. [💻 Requisitos del Sistema](#-requisitos-del-sistema)
3. [📦 Instalación](#-instalación)
4. [🚀 Inicio Rápido](#-inicio-rápido)
5. [📋 Guía Detallada](#-guía-detallada)
6. [🎨 Usar en Adobe Illustrator](#-usar-en-adobe-illustrator)
7. [🔧 Solución de Problemas](#-solución-de-problemas)
8. [💡 Consejos y Trucos](#-consejos-y-trucos)
9. [📞 Soporte](#-soporte)

---

## 🎯 Introducción

El **Convertidor Universal XML** es una herramienta diseñada para automatizar la creación de archivos XML compatibles con las Variables de Adobe Illustrator. 

### ¿Qué hace?
- Convierte datos desde Excel, CSV, JSON y otros formatos
- Genera archivos XML con la estructura exacta que Adobe Illustrator requiere
- Automatiza un proceso que normalmente tomaría horas de trabajo manual

### ¿Para quién es?
- Diseñadores gráficos que usan Adobe Illustrator
- Profesionales que necesitan generar múltiples versiones de diseños
- Cualquier persona que trabaje con Variables de Adobe Illustrator

---

## 💻 Requisitos del Sistema

### Mínimos
- **Sistema Operativo**: Windows 10 (64-bit) o superior
- **RAM**: 4 GB
- **Espacio en disco**: 50 MB libres
- **Adobe Illustrator**: CS6 o superior

### Recomendados
- **Sistema Operativo**: Windows 11
- **RAM**: 8 GB o más
- **Adobe Illustrator**: CC 2020 o superior

### Formatos de archivo soportados
- **Excel**: `.xlsx`, `.xls`
- **CSV**: `.csv` (cualquier delimitador)
- **JSON**: `.json`
- **Texto**: `.txt`
- **TSV**: `.tsv`
- **RAW**: `.raw`, `.data`

---

## 📦 Instalación

### Opción 1: Instalación Automática (Recomendada)
1. Descarga el archivo `ConvertidorXML_Adobe_v1.0.zip`
2. Extrae todos los archivos en una carpeta
3. Ejecuta `Instalar.bat` como administrador
4. Sigue las instrucciones en pantalla

### Opción 2: Instalación Manual
1. Copia `ConvertidorXML_Adobe.exe` a tu ubicación deseada
2. Crea un acceso directo en el escritorio si lo deseas
3. ¡Listo para usar!

**Nota**: El programa no requiere instalación de Python ni otras dependencias.

---

## 🚀 Inicio Rápido

### En 5 pasos:
1. **Abre** el programa `ConvertidorXML_Adobe.exe`
2. **Haz clic** en "Buscar" y selecciona tu archivo de datos
3. **Verifica** que la columna correcta esté seleccionada
4. **Haz clic** en "GENERAR ARCHIVO XML"
5. **Importa** el XML en Adobe Illustrator

### Tu primer XML en 2 minutos:
1. Usa el archivo `samples/ejemplo.xlsx` incluido
2. Abre el Convertidor
3. Selecciona el archivo de ejemplo
4. Genera el XML
5. ¡Pruébalo en Illustrator!

---

## 📋 Guía Detallada

### 1. Interfaz Principal

Al abrir el programa verás:
- **Formatos Soportados**: Lista de tipos de archivo compatibles
- **Seleccionar Archivo**: Área para elegir tu archivo de datos
- **Configuración**: Opciones para personalizar la conversión
- **Estado y Mensajes**: Área donde se muestran los resultados

### 2. Seleccionar Archivo

1. **Haz clic en "Buscar"**
   - Se abrirá un diálogo de selección
   - Los archivos se filtran por tipo automáticamente

2. **Selecciona tu archivo**
   - Excel, CSV, JSON, TXT, etc.
   - El programa analizará automáticamente el contenido

3. **Análisis automático**
   - Se muestran las columnas encontradas
   - Se detecta automáticamente la mejor columna para usar

### 3. Configuración

#### Auto-detección de columnas
- **Automática**: El programa selecciona la mejor columna
- **Manual**: Puedes elegir una columna específica del menú desplegable

#### Configuración XML
- **Variable XML**: Nombre que tendrá la variable en Illustrator
  - Por defecto: `NOMBRE2`
  - Puedes cambiarlo por cualquier nombre sin espacios

- **Binding name**: Nombre del conjunto de variables
  - Por defecto: `binding1`
  - Útil si manejas múltiples conjuntos de variables

#### Archivo de salida
- **Nombre del XML**: Dónde se guardará el archivo generado
- **Por defecto**: `variables_illustrator.xml`

### 4. Generar XML

1. **Haz clic en "GENERAR ARCHIVO XML"**
2. **Espera la confirmación**
   - Verás el progreso en el área de mensajes
   - Se mostrará un mensaje de éxito cuando termine

3. **Ubicación del archivo**
   - Por defecto se guarda en la misma carpeta del programa
   - Puedes cambiar la ubicación antes de generar

### 5. Funciones Adicionales

#### Vista Previa
- **Haz clic en "Vista Previa"** para ver los primeros elementos
- Te ayuda a verificar que los datos son correctos antes de generar

#### Validar XML
- **Automática**: Se valida automáticamente al generar
- **Manual**: Haz clic en "Validar XML" para verificar un archivo existente

#### Abrir Carpeta
- **Haz clic en "Abrir Carpeta"** para ir directamente donde se guardó el XML

---

## 🎨 Usar en Adobe Illustrator

### Tutorial paso a paso:

#### 1. Preparar Adobe Illustrator
1. Abre Adobe Illustrator
2. Crea un nuevo documento o abre uno existente
3. Ve a `Ventana → Variables` para abrir el panel

#### 2. Importar Variables
1. En el panel Variables, haz clic en el **menú hamburguesa** (≡)
2. Selecciona **"Importar"**
3. Busca y selecciona tu archivo XML generado
4. Haz clic en **"Abrir"**

#### 3. Verificar la Importación
- Las variables aparecerán en el panel Variables
- Deberías ver tu variable (ej: `NOMBRE2`) listada
- Los datasets aparecerán numerados

#### 4. Vincular Elementos de Texto
1. **Crea un objeto de texto** en tu documento
2. **Selecciona el texto**
3. En el panel Variables, **haz clic en "Crear"**
4. Selecciona **"Texto"** y elige tu variable

#### 5. Probar los Datasets
1. En el panel Variables, selecciona diferentes datasets
2. El texto cambiará automáticamente
3. ¡Usa las flechas para navegar entre datasets!

#### 6. Generar Múltiples Versiones
1. Ve a `Archivo → Exportar → Exportar para pantallas`
2. O usa `Archivo → Automatizar → Lote de variables`
3. Se generarán versiones para cada dataset

### Casos de Uso Comunes

#### Certificados
1. Diseña un certificado base
2. Usa variables para el nombre del graduado
3. Genera automáticamente certificados para toda la clase

#### Tarjetas de Presentación
1. Diseña el template base
2. Variables para nombre, cargo, email, teléfono
3. Genera tarjetas para todo el equipo

#### Etiquetas de Productos
1. Template de etiqueta
2. Variables para nombre, precio, código
3. Genera etiquetas para todo el inventario

---

## 🔧 Solución de Problemas

### El programa no abre
**Posibles causas y soluciones:**

- **Antivirus bloqueando**
  - Agrega una excepción para el archivo .exe
  - Temporalmente desactiva el antivirus para probar

- **Windows bloqueando archivo desconocido**
  - Haz clic derecho → Propiedades → Desbloquear
  - O ejecuta como administrador

- **Archivo corrupto**
  - Descarga nuevamente el programa
  - Verifica la integridad del archivo

### Error al seleccionar archivo
**Posibles causas:**
- **Archivo muy grande**: Prueba con archivos menores a 100MB
- **Archivo corrupto**: Verifica que el archivo se abra correctamente en su programa original
- **Formato no soportado**: Usa uno de los formatos listados

### Error al generar XML
**Verificaciones:**
1. **Datos válidos**: Asegúrate de que la columna tenga texto, no solo números
2. **Permisos**: Verifica que puedas escribir en la carpeta de destino
3. **Espacio en disco**: Confirma que hay espacio suficiente

### El XML no importa en Illustrator
**Posibles soluciones:**
1. **Versión de Illustrator**: Asegúrate de usar CS6 o superior
2. **Validar XML**: Usa la función "Validar XML" del programa
3. **Caracteres especiales**: Algunos caracteres pueden causar problemas

### Problemas de rendimiento
- **Archivos grandes**: Para archivos con más de 10,000 filas, el proceso puede tomar varios minutos
- **Memoria insuficiente**: Cierra otros programas para liberar RAM
- **Disco lento**: Usa un SSD si está disponible

---

## 💡 Consejos y Trucos

### Preparar tus datos
1. **Limpia los datos antes**: Elimina filas vacías y caracteres extraños
2. **Una columna por variable**: Separa nombres, apellidos, etc. si necesitas variables independientes
3. **Evita saltos de línea**: En Excel, usa Alt+Enter con cuidado

### Optimizar el flujo de trabajo
1. **Nombres descriptivos**: Usa nombres claros para tus variables XML
2. **Organiza por proyectos**: Crea carpetas separadas para diferentes proyectos
3. **Respalda los XMLs**: Guarda copias de tus archivos XML generados

### Trabajar con Excel
- **Congela paneles**: Para archivos grandes, congela la primera fila
- **Filtros**: Usa filtros de Excel para preparar subconjuntos de datos
- **Formato de texto**: Asegúrate de que la columna esté formateada como texto

### Trabajar con CSV
- **Codificación UTF-8**: Guarda los CSV con codificación UTF-8 para caracteres especiales
- **Delimitadores**: El programa detecta automáticamente comas, puntos y comas, y tabs

### Adobe Illustrator
- **Variables múltiples**: Puedes tener varias variables por documento
- **Objetos dinámicos**: No solo texto, también imágenes pueden ser variables
- **Scripts de automatización**: Considera usar scripts para procesos repetitivos

---

## 📞 Soporte

### Antes de contactar soporte
1. **Verifica los requisitos del sistema**
2. **Prueba con los archivos de ejemplo incluidos**
3. **Revisa esta documentación**
4. **Anota el mensaje de error exacto**

### Información útil para soporte
- Versión del programa
- Sistema operativo y versión
- Tipo de archivo que causa problemas
- Mensaje de error completo
- Pasos para reproducir el problema

### Canales de soporte
- **Email**: [soporte@convertidorxml.com]
- **GitHub Issues**: [Reportar problema]
- **Documentación online**: [Wiki del proyecto]

### Tiempo de respuesta
- **Problemas críticos**: 24 horas
- **Consultas generales**: 2-3 días laborables
- **Mejoras y sugerencias**: Se evalúan mensualmente

---

## 📊 Registro de Cambios

### v1.0.0 (Fecha actual)
- Lanzamiento inicial
- Soporte para Excel, CSV, JSON, TXT
- Interfaz gráfica completa
- Auto-detección de columnas
- Validación automática de XML
- Generación de ejecutable portable

### Próximas versiones
- **v1.1**: Soporte para archivos de Google Sheets
- **v1.2**: Procesamiento por lotes
- **v1.3**: Interfaz en múltiples idiomas
- **v2.0**: Soporte para Mac y Linux

---

**© 2024 Convertidor Universal XML - Adobe Illustrator**  
*Manual de Usuario v1.0*

---

*¿Te fue útil este manual? ¡Compártelo con otros diseñadores!*