# 🛠️ Guía para Desarrolladores - Convertidor XML

## Tabla de Contenidos
- [Configuración del Entorno](#configuración-del-entorno)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Sistema de Internacionalización](#sistema-de-internacionalización)
- [Tests](#tests)
- [Generar Ejecutables](#generar-ejecutables)
- [Contribuir](#contribuir)

---

## 📦 Configuración del Entorno

### Requisitos
- Python 3.7 o superior
- pip (gestor de paquetes)
- Sistema operativo: Windows, macOS, o Linux

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/convertidor-xml.git
cd convertidor-xml

# Crear entorno virtual (recomendado)
python3 -m venv venv

# Activar entorno virtual
# En macOS/Linux:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar la Aplicación

```bash
# Modo desarrollo
python3 convertidor.py

# Modo desarrollo con consola (útil para debugging)
python convertidor.py
```

---

## 🏗️ Arquitectura del Proyecto

### Estructura de Archivos

```
convertidor-xml/
├── convertidor.py          # Aplicación principal con GUI
├── i18n.py                 # Sistema de internacionalización
├── crear_exe.py            # Script para generar ejecutables
├── setup_proyecto.py       # Organizador del proyecto
├── run_tests.py            # Ejecutor de tests
├── requirements.txt        # Dependencias Python
├── CHANGELOG.md            # Historial de cambios
├── README.md               # Documentación usuario final
├── README_DEV.md           # Esta guía
├── tests/                  # Suite de tests
│   ├── __init__.py
│   ├── test_i18n.py       # Tests de internacionalización
│   └── test_convertidor.py # Tests del convertidor
├── samples/                # Archivos de ejemplo
├── docs/                   # Documentación adicional
└── dist/                   # Ejecutables generados
```

### Módulos Principales

#### 1. `convertidor.py`
**Clase Principal**: `XMLConverterApp`

**Responsabilidades**:
- Gestión de la interfaz gráfica (tkinter)
- Carga de archivos en múltiples formatos
- Auto-detección de columnas
- Generación de XML compatible con Adobe
- Validación de XML
- Integración con sistema i18n

**Métodos Clave**:
```python
load_file_data(file_path)           # Carga datos desde archivo
auto_detect_column()                 # Detecta mejor columna automáticamente
generate_adobe_xml(values, var, bind) # Genera XML con formato Adobe
validate_xml()                       # Valida estructura XML
open_output_folder()                 # Abre carpeta (multiplataforma)
```

#### 2. `i18n.py`
**Clase Principal**: `I18n`

**Responsabilidades**:
- Gestión de traducciones
- Detección automática de idioma del sistema
- Cambio dinámico de idioma
- Formateo de strings con parámetros

**API**:
```python
# Obtener instancia singleton
i18n = get_i18n()

# Obtener traducción
text = i18n.get('app_title')

# Traducción con parámetros
text = i18n.get('file_selected', filename='test.xlsx')

# Función de atajo
text = t('app_title')

# Cambiar idioma
i18n.set_language('es')  # 'es' o 'en'

# Detectar idioma del sistema
lang = I18n.detect_system_language()
```

#### 3. `crear_exe.py`
**Responsabilidades**:
- Detección de plataforma
- Configuración de PyInstaller
- Generación de ejecutables multiplataforma
- Creación de iconos personalizados
- Generación de documentación

**Plataformas Soportadas**:
- Windows → `ConvertidorXML_Windows.exe`
- macOS → `ConvertidorXML_macOS`
- Linux → `ConvertidorXML_Linux`

---

## 🌍 Sistema de Internacionalización

### Agregar Nuevo Idioma

1. **Editar `i18n.py`**:

```python
TRANSLATIONS = {
    'es': { ... },
    'en': { ... },
    'fr': {  # Nuevo idioma
        'app_title': 'Convertisseur XML Universel',
        'browse': 'Parcourir',
        # ... más traducciones
    }
}
```

2. **Asegúrate de mantener paridad** entre todos los idiomas (todas las claves deben existir)

3. **Ejecutar tests**:
```bash
python3 tests/test_i18n.py
```

### Agregar Nueva Traducción

1. Agrega la clave en **TODOS** los idiomas en `TRANSLATIONS`
2. Usa la clave en el código:

```python
self.i18n.get('nueva_clave')
# O con parámetros:
self.i18n.get('nueva_clave', param1='valor')
```

---

## 🧪 Tests

### Ejecutar Todos los Tests

```bash
# Ejecutar todos los tests
python3 run_tests.py

# O con pytest (más verboso)
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=. --cov-report=html
```

### Ejecutar Tests Específicos

```bash
# Solo tests de i18n
python3 tests/test_i18n.py

# Solo tests del convertidor (requiere GUI)
python3 tests/test_convertidor.py
```

### Crear Nuevos Tests

**Ejemplo de test unitario**:

```python
# tests/test_mi_modulo.py
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mi_modulo import MiClase

class TestMiClase(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.instancia = MiClase()

    def test_mi_funcionalidad(self):
        """Test: descripción de lo que prueba"""
        resultado = self.instancia.mi_metodo()
        self.assertEqual(resultado, 'esperado')

if __name__ == '__main__':
    unittest.main()
```

### Suite de Tests Actual

#### `test_i18n.py` (15 tests)
- ✅ Detección de idioma del sistema
- ✅ Inicialización con español/inglés
- ✅ Traducciones con/sin parámetros
- ✅ Cambio de idioma
- ✅ Patrón singleton
- ✅ Paridad entre idiomas

#### `test_convertidor.py` (30+ tests)
- ✅ Inicialización de la app
- ✅ Detección de plataforma
- ✅ Carga de archivos (Excel, CSV, JSON, TXT)
- ✅ Generación de XML
- ✅ Escape de caracteres especiales
- ✅ Validación de XML
- ✅ Estructura XML Adobe

---

## 🚀 Generar Ejecutables

### Generar para Tu Plataforma

```bash
# Instala dependencias si no lo has hecho
pip install -r requirements.txt

# Ejecuta el script
python3 crear_exe.py
```

El script:
1. Detecta tu plataforma automáticamente
2. Instala dependencias necesarias
3. Limpia builds anteriores
4. Crea icono personalizado (si es posible)
5. Ejecuta PyInstaller con configuración optimizada
6. Genera ejecutable en `dist/`

### Configuración Avanzada de PyInstaller

Para personalizar la generación, edita `crear_exe.py`:

```python
comando = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",                    # Un solo archivo
    "--windowed",                   # Sin consola
    f"--name={nombre_exe}",         # Nombre
    "--clean",                      # Limpiar cache
    "--noconfirm",                  # No confirmar
    "--optimize=2",                 # Optimización
    # Agregar más opciones aquí
]
```

### Iconos Personalizados

#### Windows
Coloca `icono.ico` en la raíz del proyecto

#### macOS
Coloca `icono.icns` en la raíz del proyecto

Para crear iconos:
```bash
# macOS (desde PNG)
sips -s format icns icono.png --out icono.icns

# O usando ImageMagick
convert icono.png -define icon:auto-resize=256,128,64,32,16 icono.ico
```

---

## 🤝 Contribuir

### Flujo de Trabajo

1. **Fork** el repositorio
2. **Crea** una rama para tu feature:
   ```bash
   git checkout -b feature/mi-nueva-feature
   ```
3. **Desarrolla** tu feature
4. **Escribe tests** para tu código
5. **Ejecuta tests** y asegúrate de que pasen:
   ```bash
   python3 run_tests.py
   ```
6. **Commit** tus cambios:
   ```bash
   git commit -m "Add: descripción de la feature"
   ```
7. **Push** a tu fork:
   ```bash
   git push origin feature/mi-nueva-feature
   ```
8. **Abre** un Pull Request

### Estándares de Código

#### Python
- **PEP 8**: Seguir guía de estilo de Python
- **Docstrings**: Documentar todas las funciones/clases
- **Type hints**: Usar anotaciones de tipo cuando sea posible
- **Nombres descriptivos**: Variables y funciones con nombres claros

**Ejemplo**:
```python
def load_file_data(self, file_path: str) -> pd.DataFrame:
    """
    Cargar datos según el tipo de archivo

    Args:
        file_path: Ruta absoluta al archivo

    Returns:
        DataFrame con los datos cargados

    Raises:
        ValueError: Si el formato no es soportado
        Exception: Si hay error al leer el archivo
    """
    # Implementación
```

#### Commits
Usar prefijos descriptivos:
- `Add:` - Nueva funcionalidad
- `Fix:` - Corrección de bugs
- `Update:` - Actualización de código existente
- `Refactor:` - Refactorización sin cambiar funcionalidad
- `Test:` - Agregar o modificar tests
- `Docs:` - Cambios en documentación

### Reportar Bugs

Incluye:
1. **Sistema operativo** y versión
2. **Versión de Python**
3. **Pasos para reproducir**
4. **Comportamiento esperado** vs **comportamiento actual**
5. **Screenshots** si aplica
6. **Logs de error** completos

---

## 📝 Notas Técnicas

### Compatibilidad de Plataformas

#### Abrir Carpetas
```python
if self.os_platform == "Windows":
    os.startfile(folder_path)
elif self.os_platform == "Darwin":  # macOS
    subprocess.run(["open", folder_path])
else:  # Linux
    subprocess.run(["xdg-open", folder_path])
```

#### Rutas de Archivos
Siempre usar `os.path` o `pathlib.Path` para compatibilidad:
```python
from pathlib import Path

# Bueno
path = Path("folder") / "file.txt"

# Evitar
path = "folder\\file.txt"  # Solo funciona en Windows
```

### Encoding
Siempre especificar UTF-8:
```python
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
```

### GUI y Tests
Los tests con GUI pueden fallar en sistemas sin display. Para tests de GUI:
```python
@classmethod
def setUpClass(cls):
    cls.root = tk.Tk()
    cls.root.withdraw()  # Ocultar ventana
```

---

## 🔗 Enlaces Útiles

- [Documentación Python](https://docs.python.org/3/)
- [Documentación tkinter](https://docs.python.org/3/library/tkinter.html)
- [Guía PyInstaller](https://pyinstaller.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Adobe Illustrator Variables](https://helpx.adobe.com/illustrator/using/data-driven-graphics-templates-variables.html)

---

## 📞 Soporte

Para preguntas o ayuda:
- **Issues**: [GitHub Issues](https://github.com/tu-usuario/convertidor-xml/issues)
- **Email**: nv0900nico@gmail.com

---

**Hecho con ❤️ para la comunidad de desarrolladores**
