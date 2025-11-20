# 🪟 Convertidor XML - Windows

## 📦 Archivos Incluidos

- `convertidor.py` - Aplicación principal
- `i18n.py` - Sistema de internacionalización
- `requirements.txt` - Dependencias Python
- `build_windows.bat` - Script de compilación automática

## 🚀 Opción 1: Compilar el Ejecutable (Recomendado)

### Requisitos
- Windows 10/11
- Python 3.7 o superior ([Descargar](https://www.python.org/downloads/))

### Pasos

1. **Asegúrate de tener Python instalado**
   - Abre CMD y ejecuta: `python --version`
   - Debe mostrar Python 3.7 o superior

2. **Ejecuta el script de compilación**
   - Doble click en `build_windows.bat`
   - O desde CMD:
     ```cmd
     build_windows.bat
     ```

3. **Espera a que termine** (puede tardar 1-2 minutos)

4. **Encuentra tu ejecutable**
   - Se creará en: `dist\ConvertidorXML_Windows.exe`
   - Tamaño aproximado: 25-30 MB

5. **¡Listo!**
   - Doble click en `ConvertidorXML_Windows.exe`
   - No necesita Python para ejecutarse

## 🐍 Opción 2: Ejecutar desde Python

Si prefieres ejecutar directamente sin compilar:

```cmd
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python convertidor.py
```

## 📋 Características

- ✅ Interfaz gráfica en Español/Inglés (detección automática)
- ✅ Convierte Excel, CSV, JSON, TXT a XML
- ✅ Compatible con Adobe Illustrator Variables
- ✅ Validación automática de XML
- ✅ Sin dependencias externas una vez compilado

## 🔧 Compilación Manual (Avanzado)

Si el script automático no funciona, puedes compilar manualmente:

```cmd
# Instalar dependencias
pip install pandas openpyxl pyinstaller pillow

# Generar ejecutable
python -m PyInstaller --onefile --windowed --name=ConvertidorXML_Windows convertidor.py

# El ejecutable estará en: dist\ConvertidorXML_Windows.exe
```

## 🐛 Problemas Comunes

### "Python no está instalado"
**Solución:**
1. Descarga Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marca "Add Python to PATH"
3. Reinicia CMD y vuelve a intentar

### "pip no es reconocido"
**Solución:**
```cmd
python -m pip install --upgrade pip
```

### "Error al compilar"
**Solución:**
1. Asegúrate de tener permisos de administrador
2. Desactiva temporalmente el antivirus
3. Ejecuta CMD como administrador

### "El ejecutable no abre"
**Solución:**
1. Click derecho → Propiedades → Desbloquear
2. Agrega excepción en Windows Defender
3. Ejecuta como administrador

## 📊 Contenido del Ejecutable

El ejecutable incluye:
- ✅ Aplicación completa
- ✅ Sistema de internacionalización (ES/EN)
- ✅ Todas las librerías (pandas, openpyxl, etc.)
- ✅ Interfaz gráfica (tkinter)
- ✅ No requiere instalación

## 🎯 Uso del Programa

1. **Abrir la aplicación**
   - Doble click en el ejecutable

2. **Seleccionar archivo**
   - Click en "Buscar" (o "Browse" en inglés)
   - Elige tu archivo Excel, CSV, JSON o TXT

3. **Auto-detección**
   - El programa detecta automáticamente la mejor columna

4. **Generar XML**
   - Click en "GENERAR ARCHIVO XML"
   - El XML se guarda en la misma carpeta

5. **Usar en Adobe Illustrator**
   - Ve a: Ventana → Variables → Importar
   - Selecciona el XML generado

## 📁 Estructura de Archivos Después de Compilar

```
build_Windows/
├── convertidor.py
├── i18n.py
├── requirements.txt
├── build_windows.bat
├── README.md (este archivo)
├── build/                    # Archivos temporales
├── dist/
│   └── ConvertidorXML_Windows.exe  # 👈 TU EJECUTABLE
└── *.spec                    # Archivo de configuración PyInstaller
```

## 🔐 Seguridad

- **No es virus**: Algunos antivirus marcan ejecutables de PyInstaller como sospechosos
- **Solución**: Agrega excepción para el archivo en tu antivirus
- **Código fuente**: Todo el código está en `convertidor.py` e `i18n.py` (puedes revisarlo)

## 📞 Soporte

**Email**: nv0900nico@gmail.com

**Problemas o Bugs**: Abre un issue en GitHub

## 📝 Notas

- El ejecutable es portable (no necesita instalación)
- Funciona sin conexión a internet
- Compatible con Windows 10 y 11 (32 y 64 bits)
- El primer inicio puede tardar unos segundos

---

**Versión**: 2.0.0
**Plataforma**: Windows 10/11
**Fecha**: 2025-01-20
**Arquitectura**: Compatible con 32-bit y 64-bit
