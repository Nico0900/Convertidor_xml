# 🎨 Convertidor Universal XML - Adobe Illustrator

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![Adobe Illustrator](https://img.shields.io/badge/Adobe%20Illustrator-Compatible-orange.svg)](https://www.adobe.com/products/illustrator.html)

> **Convierte automáticamente datos desde Excel, CSV, JSON y otros formatos a archivos XML compatibles con Variables de Adobe Illustrator**

![Convertidor XML Demo](https://via.placeholder.com/800x400/52a3db/ffffff?text=Convertidor+Universal+XML+Demo)

## 🚀 Características Principales

- **📊 Múltiples Formatos**: Excel (.xlsx, .xls), CSV, JSON, TXT, TSV, RAW
- **🤖 Auto-Detección**: Identifica automáticamente columnas con datos de texto
- **🎯 100% Compatible**: Genera XML con arquitectura exacta de Adobe Illustrator
- **🖥️ Interfaz Intuitiva**: GUI moderna y fácil de usar
- **⚡ Validación Automática**: Verifica que el XML sea válido antes de guardar
- **📦 Ejecutable Portable**: No requiere instalar Python ni dependencias

## 📋 Tabla de Contenidos

- [🎨 Convertidor Universal XML - Adobe Illustrator](#-convertidor-universal-xml---adobe-illustrator)
  - [🚀 Características Principales](#-características-principales)
  - [📋 Tabla de Contenidos](#-tabla-de-contenidos)
  - [⚡ Inicio Rápido](#-inicio-rápido)
  - [📦 Instalación](#-instalación)
  - [🎯 Uso](#-uso)
  - [📁 Formatos Soportados](#-formatos-soportados)
  - [🖼️ Capturas de Pantalla](#️-capturas-de-pantalla)
  - [⚙️ Configuración](#️-configuración)
  - [🎨 Usar en Adobe Illustrator](#-usar-en-adobe-illustrator)
  - [🔧 Desarrollo](#-desarrollo)
  - [📊 Estructura del Proyecto](#-estructura-del-proyecto)
  - [🤝 Contribuir](#-contribuir)
  - [📄 Licencia](#-licencia)
  - [📞 Contacto](#-contacto)

## ⚡ Inicio Rápido

1. **Descarga** el ejecutable desde [Releases](../../releases)
2. **Ejecuta** `ConvertidorXML_Adobe.exe`
3. **Selecciona** tu archivo de datos (Excel, CSV, etc.)
4. **Genera** el XML con un click
5. **Importa** en Adobe Illustrator → Ventana → Variables

```bash
# O clona el repositorio para ejecutar desde código fuente
git clone https://github.com/tu-usuario/convertidor-xml-adobe.git
cd convertidor-xml-adobe
pip install -r requirements.txt
python convertidor.py
```

## 📦 Instalación

### 💻 Opción 1: Ejecutable (Recomendado)

1. Ve a [Releases](../../releases)
2. Descarga `ConvertidorXML_Adobe_v1.0.zip`
3. Extrae y ejecuta `ConvertidorXML_Adobe.exe`
4. ¡Listo! No necesita instalación

### 🐍 Opción 2: Desde Código Fuente

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/convertidor-xml-adobe.git
cd convertidor-xml-adobe

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python convertidor.py
```

**Dependencias:**
```txt
pandas>=1.3.0
openpyxl>=3.0.0
tkinter (incluido en Python)
```

## 🎯 Uso

### 📖 Guía Paso a Paso

1. **Abrir Programa**
   ```
   Doble click en ConvertidorXML_Adobe.exe
   ```

2. **Seleccionar Archivo**
   - Click en **"Buscar"**
   - Selecciona tu archivo de datos
   - El programa auto-detecta las columnas

3. **Configurar Variables**
   - **Variable XML**: Nombre en Illustrator (ej: `NOMBRE2`)
   - **Binding name**: Nombre del conjunto (ej: `binding1`)

4. **Generar XML**
   - Click en **"GENERAR ARCHIVO XML"**
   - Verifica la ubicación del archivo generado

5. **Usar en Adobe Illustrator**
   - Ve a `Ventana → Variables`
   - Click en `Importar`
   - Selecciona tu archivo XML

### 🎬 Demo Visual

```mermaid
graph LR
    A[📊 Archivo Excel] --> B[🔄 Convertidor]
    B --> C[📄 XML Adobe]
    C --> D[🎨 Illustrator]
    D --> E[✨ Variables Listas]
```

## 📁 Formatos Soportados

| Formato | Extensión | Descripción |
|---------|-----------|-------------|
| **Excel** | `.xlsx`, `.xls` | Hojas de cálculo de Microsoft Excel |
| **CSV** | `.csv` | Valores separados por comas (auto-detecta delimitadores) |
| **JSON** | `.json` | Archivos JSON con arrays u objetos |
| **Texto** | `.txt` | Archivos de texto plano (línea por línea) |
| **TSV** | `.tsv` | Valores separados por tabulaciones |
| **RAW** | `.raw`, `.data` | Datos en texto plano |

### 📋 Ejemplo de Archivo Excel

| Nombres |
|---------|
| Juan Pérez González |
| María García López |
| Carlos Rodríguez Silva |
| Ana Martínez Ruiz |

### 📄 XML Generado

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20001102//EN"...>
<svg>
<variableSets xmlns="&ns_vars;">
  <variableSet locked="none" varSetName="binding1">
    <variables>
      <variable varName="NOMBRE2" trait="textcontent" category="&ns_flows;"></variable>
    </variables>
    <v:sampleDataSets xmlns:v="&ns_vars;" xmlns="&ns_custom;">
      <v:sampleDataSet dataSetName="Data Set">
        <NOMBRE2>
          <p>Juan Pérez González</p>
        </NOMBRE2>
      </v:sampleDataSet>
      <!-- Más datasets... -->
    </v:sampleDataSets>
  </variableSet>
</variableSets>
</svg>
```

## 🖼️ Capturas de Pantalla

<details>
<summary>Ver capturas de pantalla</summary>

### Interfaz Principal
![Interfaz Principal](https://via.placeholder.com/600x400/f8f9fa/343a40?text=Interfaz+Principal)

### Selección de Archivos
![Selección de Archivos](https://via.placeholder.com/600x400/e3f2fd/1976d2?text=Selector+de+Archivos)

### Configuración
![Configuración](https://via.placeholder.com/600x400/f3e5f5/7b1fa2?text=Panel+de+Configuración)

### Generación Exitosa
![Generación Exitosa](https://via.placeholder.com/600x400/e8f5e8/388e3c?text=XML+Generado+Exitosamente)

</details>

## ⚙️ Configuración

### 🔧 Parámetros Configurables

| Parámetro | Descripción | Valor por Defecto |
|-----------|-------------|-------------------|
| **Variable XML** | Nombre de la variable en Illustrator | `NOMBRE2` |
| **Binding name** | Nombre del conjunto de variables | `binding1` |
| **Archivo de salida** | Nombre del archivo XML generado | `variables_illustrator.xml` |

### ⚡ Auto-Detección

El programa automáticamente:
- 🔍 **Analiza** todas las columnas del archivo
- 🎯 **Detecta** cuál contiene más contenido textual
- ✅ **Selecciona** la mejor columna para convertir
- ⚠️ **Ignora** columnas con solo números o fechas

## 🎨 Usar en Adobe Illustrator

### 📖 Tutorial Completo

1. **Crear Documento**
   - Abre Adobe Illustrator
   - Crea un nuevo documento

2. **Importar Variables**
   ```
   Ventana → Variables → Panel Variables → Importar
   ```

3. **Seleccionar XML**
   - Busca tu archivo XML generado
   - Click en "Abrir"

4. **Usar Variables**
   - Las variables aparecerán en el panel
   - Arrastra texto y vincula con variables
   - Usa los datasets para generar versiones

### 🎯 Casos de Uso

- **📜 Certificados**: Nombres de graduados
- **🏷️ Etiquetas**: Información de productos  
- **📇 Tarjetas**: Datos de contacto
- **📊 Reportes**: Datos variables por cliente
- **🎫 Tickets**: Información de eventos

## 🔧 Desarrollo

### 🏗️ Arquitectura

```python
# Estructura principal
convertidor.py          # Aplicación principal con GUI
├── XMLConverterApp     # Clase principal de la aplicación
├── load_file_data()    # Carga datos de diferentes formatos
├── generate_adobe_xml() # Genera XML compatible con Adobe
└── validate_xml()      # Valida estructura XML
```

### 🧪 Testing

```bash
# Ejecutar tests
python -m pytest tests/

# Generar ejecutable
python crear_exe.py

# Validar XML generado
python validate_xml.py samples/output.xml
```

### 🏃‍♂️ Ejecutar en Desarrollo

```bash
# Modo desarrollo (con consola para debug)
python convertidor.py

# Modo producción (sin consola)
pythonw convertidor.py
```

## 📊 Estructura del Proyecto

```
convertidor-xml/
├── 📄 README.md                    # Este archivo
├── 🐍 convertidor.py               # Aplicación principal
├── 🔧 crear_exe.py                 # Script para generar ejecutable
├── 📋 requirements.txt             # Dependencias Python
├── 🎨 icono.ico                    # Icono de la aplicación
├── 📁 samples/                     # Archivos de ejemplo
│   ├── ejemplo.xlsx
│   ├── ejemplo.csv
│   └── output.xml
├── 📁 docs/                        # Documentación adicional
│   ├── manual_usuario.pdf
│   └── guia_illustrator.md
├── 📁 dist/                        # Ejecutables generados
└── 📄 LICENSE                      # Licencia del proyecto
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! 🎉

### 🔀 Proceso

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### 🐛 Reportar Bugs

Si encuentras un bug, por favor [abre un issue](../../issues) con:

- **🖥️ Sistema operativo** y versión
- **🐍 Versión de Python** (si aplica)
- **📁 Tipo de archivo** que causó el problema
- **📝 Descripción detallada** del error
- **📋 Pasos para reproducir** el problema

### 💡 Solicitar Features

¿Tienes una idea genial? [Abre un issue](../../issues) con la etiqueta `enhancement`

### 🧪 Áreas de Mejora

- [ ] **🌐 Soporte para Mac/Linux**
- [ ] **📱 Interfaz responsiva**
- [ ] **🔄 Procesamiento por lotes**
- [ ] **☁️ Integración con servicios en la nube**
- [ ] **📊 Más formatos de archivo**
- [ ] **🎨 Temas personalizables**

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2024 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

## 📞 Contacto

**👨‍💻 Desarrollador**: [Tu Nombre]  
**📧 Email**: tu.email@ejemplo.com  
**🔗 LinkedIn**: [tu-linkedin](https://linkedin.com/in/tu-perfil)  
**🐦 Twitter**: [@tu-twitter](https://twitter.com/tu-usuario)

### 🌟 ¿Te gustó el proyecto?

Si este proyecto te resultó útil, ¡considera darle una ⭐ en GitHub!

### 📈 Estadísticas

![GitHub stars](https://img.shields.io/github/stars/tu-usuario/convertidor-xml-adobe?style=social)
![GitHub forks](https://img.shields.io/github/forks/tu-usuario/convertidor-xml-adobe?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/tu-usuario/convertidor-xml-adobe?style=social)

---

<div align="center">

**Hecho con ❤️ para la comunidad de diseñadores**

[⬆️ Volver arriba](#-convertidor-universal-xml---adobe-illustrator)

</div>