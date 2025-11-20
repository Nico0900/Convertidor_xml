# Changelog - Convertidor Universal XML

Todos los cambios notables en este proyecto serán documentados aquí.

## [2.0.0] - 2025-01-20

### 🎉 Nuevas Características

#### 🌍 Internacionalización (i18n)
- **Sistema de idiomas múltiples**: Soporte completo para Español e Inglés
- **Detección automática**: El sistema detecta el idioma del sistema operativo
- **Función de cambio de idioma**: Los usuarios pueden cambiar entre idiomas
- **Traducciones completas**: Toda la interfaz está traducida

#### 💻 Soporte Multiplataforma
- **Windows**: Compatibilidad completa con Windows 10/11
- **macOS**: Soporte nativo para macOS (Darwin)
- **Linux**: Funcionalidad completa en distribuciones Linux
- **Abrir carpetas**: Función multiplataforma para abrir carpetas del sistema
  - Windows: `os.startfile()`
  - macOS: `subprocess.run(["open", path])`
  - Linux: `subprocess.run(["xdg-open", path])`

#### 🧪 Suite de Tests Completa
- **15 tests de i18n**: Verifican sistema de internacionalización
- **30+ tests del convertidor**: Prueban toda la funcionalidad
- **Script de ejecución**: `run_tests.py` para ejecutar todos los tests
- **Cobertura completa**: Tests para carga de archivos, generación XML, escape de caracteres

### 🔧 Mejoras

#### Arquitectura del Código
- **Módulo i18n separado**: Sistema de internacionalización modular y reutilizable
- **Detección de plataforma**: Uso de `platform.system()` para compatibilidad
- **Código más limpio**: Refactorización para mejorar mantenibilidad

#### Generación de Ejecutables
- **Nombres específicos por plataforma**:
  - Windows: `ConvertidorXML_Windows.exe`
  - macOS: `ConvertidorXML_macOS`
  - Linux: `ConvertidorXML_Linux`
- **Iconos específicos**: Soporte para `.ico` (Windows) y `.icns` (macOS)
- **Documentación mejorada**: Instrucciones específicas por plataforma

#### Dependencias
- Agregado `pytest>=7.0.0` para testing
- Agregado `pytest-cov>=3.0.0` para cobertura de código
- Documentación mejorada en `requirements.txt`

### 📚 Documentación
- **CHANGELOG.md**: Nuevo archivo de cambios
- **Tests documentados**: Cada test tiene descripción clara
- **Comentarios mejorados**: Código mejor documentado

### 🐛 Correcciones
- Corregidos problemas de encoding en diferentes plataformas
- Mejorado manejo de rutas multiplataforma
- Corregido escape de caracteres XML

---

## [1.0.0] - 2024-XX-XX

### Características Iniciales
- Conversión de múltiples formatos a XML Adobe Illustrator
- Soporte para Excel, CSV, JSON, TXT, TSV, RAW
- Auto-detección de columnas con datos
- Generación de XML con arquitectura Adobe exacta
- Validación automática de XML
- Interfaz gráfica intuitiva
- Sistema de logging
- Vista previa de datos

### Formatos Soportados
- Excel (.xlsx, .xls)
- CSV (.csv)
- JSON (.json)
- TXT (.txt)
- TSV (.tsv)
- RAW (.raw, .data)

### Características XML
- DTD compatible con Adobe Illustrator
- Variables y bindings configurables
- Escape automático de caracteres especiales
- Múltiples datasets
- Validación con xml.parsers.expat
