#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para organizar automáticamente el proyecto Convertidor XML
Ejecutar: python setup_proyecto.py
"""

import os
import shutil
from pathlib import Path

def crear_estructura_carpetas():
    """Crear estructura de carpetas del proyecto"""
    carpetas = [
        'samples',
        'docs', 
        'dist',
        'screenshots'  # Para futuras capturas de pantalla
    ]
    
    print("📁 Creando estructura de carpetas...")
    for carpeta in carpetas:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
            print(f"   ✅ Carpeta '{carpeta}' creada")
        else:
            print(f"   ✅ Carpeta '{carpeta}' ya existe")

def crear_archivo_requirements():
    """Crear archivo requirements.txt"""
    requirements_content = """# Convertidor Universal XML - Adobe Illustrator
# Dependencias necesarias para ejecutar la aplicación

# Interfaz gráfica (incluida en Python estándar)
# tkinter - GUI framework (incluido por defecto)

# Manipulación de datos
pandas>=1.3.0
openpyxl>=3.0.0

# Para crear el ejecutable (desarrollo)
pyinstaller>=4.5

# Para crear iconos personalizados (opcional)
Pillow>=8.0.0

# Librerías estándar utilizadas (incluidas en Python)
# json - Manejo de archivos JSON
# csv - Manejo de archivos CSV  
# xml.etree.ElementTree - Parser XML
# xml.parsers.expat - Validación XML
# os - Operaciones del sistema
# sys - Funciones del sistema
# pathlib - Manipulación de rutas"""

    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write(requirements_content)
    print("✅ Archivo 'requirements.txt' creado")

def crear_archivo_license():
    """Crear archivo LICENSE"""
    license_content = """MIT License

Copyright (c) 2024 Convertidor Universal XML

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

    with open('LICENSE', 'w', encoding='utf-8') as f:
        f.write(license_content)
    print("✅ Archivo 'LICENSE' creado")

def crear_archivo_gitignore():
    """Crear archivo .gitignore"""
    gitignore_content = """# Archivos compilados de Python
__pycache__/
*.py[cod]
*$py.class

# Distribución / empaquetado
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Entornos virtuales
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# Sistema operativo
.DS_Store
Thumbs.db

# Archivos temporales
*.tmp
*.log
*.bak

# Archivos de prueba
test_*.xlsx
test_*.csv
prueba.*

# Archivos generados
variables_illustrator.xml
output*.xml"""

    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    print("✅ Archivo '.gitignore' creado")

def crear_archivos_documentacion():
    """Crear archivos de documentación en la carpeta docs"""
    
    # Manual de usuario
    manual_content = """# 📚 Manual de Usuario - Convertidor Universal XML

Consulta el manual completo en: [manual_usuario.md](docs/manual_usuario.md)

## 🚀 Inicio Rápido
1. Ejecuta `ConvertidorXML_Adobe.exe`
2. Selecciona tu archivo de datos
3. Genera el XML
4. Importa en Adobe Illustrator

Ver documentación completa para detalles avanzados."""

    with open('docs/README.md', 'w', encoding='utf-8') as f:
        f.write(manual_content)
    print("✅ Archivo 'docs/README.md' creado")

def verificar_archivos_principales():
    """Verificar que existen los archivos principales"""
    archivos_principales = ['convertidor.py', 'crear_exe.py']
    archivos_faltantes = []
    
    for archivo in archivos_principales:
        if not os.path.exists(archivo):
            archivos_faltantes.append(archivo)
    
    if archivos_faltantes:
        print("⚠️ Archivos faltantes detectados:")
        for archivo in archivos_faltantes:
            print(f"   ❌ {archivo}")
        print("\n💡 Asegúrate de tener estos archivos en la carpeta raíz")
        return False
    else:
        print("✅ Archivos principales detectados correctamente")
        return True

def mostrar_estructura_final():
    """Mostrar la estructura final del proyecto"""
    print("\n" + "="*60)
    print("📊 ESTRUCTURA FINAL DEL PROYECTO")
    print("="*60)
    
    estructura = """
convertidor-xml/
├── 📄 README.md                    # Documentación principal
├── 🐍 convertidor.py               # Aplicación principal  
├── 🔧 crear_exe.py                 # Script para generar ejecutable
├── ⚙️ setup_proyecto.py            # Este script organizador
├── 📋 requirements.txt             # Dependencias Python
├── 📄 LICENSE                      # Licencia MIT
├── 🙈 .gitignore                  # Archivos ignorados por Git
├── 📁 samples/                     # Archivos de ejemplo
│   ├── ejemplo.xlsx               # (Se crearán con crear_ejemplos.py)
│   ├── ejemplo.csv
│   ├── ejemplo.json
│   ├── ejemplo.txt
│   └── output.xml
├── 📁 docs/                        # Documentación adicional
│   ├── README.md                  # Índice de documentación
│   ├── manual_usuario.md          # Manual completo
│   └── guia_illustrator.md        # Guía de Adobe Illustrator
├── 📁 dist/                        # Ejecutables generados
│   └── (archivos .exe después de compilar)
└── 📁 screenshots/                 # Para capturas de pantalla
    └── (imágenes para documentación)
    """
    
    print(estructura)

def crear_script_ejemplos():
    """Crear script para generar archivos de ejemplo"""
    ejemplos_script = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear archivos de ejemplo
Ejecutar: python crear_ejemplos.py
"""

import pandas as pd
import json
import os

def crear_ejemplos():
    """Crear todos los archivos de ejemplo"""
    print("🎯 Creando archivos de ejemplo...")
    
    # Datos de ejemplo
    nombres_data = {
        'Nombres': [
            'Juan Pérez González', 'María García López', 'Carlos Rodríguez Silva',
            'Ana Martínez Ruiz', 'Pedro Sánchez Torres', 'Laura Jiménez Castro',
            'Miguel Hernández Vega', 'Carmen López Morales', 'Francisco Gómez Ruiz'
        ]
    }
    
    # Excel
    df = pd.DataFrame(nombres_data)
    df.to_excel('samples/ejemplo.xlsx', index=False)
    print("✅ ejemplo.xlsx creado")
    
    # CSV
    df.to_csv('samples/ejemplo.csv', index=False, encoding='utf-8')
    print("✅ ejemplo.csv creado")
    
    # JSON
    with open('samples/ejemplo.json', 'w', encoding='utf-8') as f:
        json.dump({'nombres': nombres_data['Nombres']}, f, ensure_ascii=False, indent=2)
    print("✅ ejemplo.json creado")
    
    # TXT
    with open('samples/ejemplo.txt', 'w', encoding='utf-8') as f:
        for nombre in nombres_data['Nombres']:
            f.write(nombre + '\\n')
    print("✅ ejemplo.txt creado")
    
    print("🎉 ¡Archivos de ejemplo creados exitosamente!")

if __name__ == "__main__":
    crear_ejemplos()
'''

    with open('crear_ejemplos.py', 'w', encoding='utf-8') as f:
        f.write(ejemplos_script)
    print("✅ Script 'crear_ejemplos.py' creado")

def main():
    """Función principal del organizador"""
    print("🚀 ORGANIZADOR AUTOMÁTICO DEL PROYECTO")
    print("=====================================")
    print("Configurando estructura completa del Convertidor XML\n")
    
    # Verificar archivos principales
    if not verificar_archivos_principales():
        input("\n❌ Presiona Enter para continuar de todas formas...")
    
    # Crear estructura
    crear_estructura_carpetas()
    print()
    
    # Crear archivos base
    print("📄 Creando archivos base...")
    crear_archivo_requirements()
    crear_archivo_license() 
    crear_archivo_gitignore()
    crear_script_ejemplos()
    print()
    
    # Crear documentación
    print("📚 Creando documentación...")
    crear_archivos_documentacion()
    print()
    
    # Mostrar resultado
    mostrar_estructura_final()
    
    print("✅ ¡PROYECTO ORGANIZADO EXITOSAMENTE!")
    print()
    print("🚀 PRÓXIMOS PASOS:")
    print("   1. Ejecuta: python crear_ejemplos.py")
    print("   2. Prueba tu convertidor con los ejemplos")
    print("   3. Ejecuta: python crear_exe.py (para generar ejecutable)")
    print("   4. ¡Comparte tu proyecto en GitHub!")
    print()
    print("📚 DOCUMENTACIÓN:")
    print("   • Manual de usuario: docs/manual_usuario.md")
    print("   • Guía Illustrator: docs/guia_illustrator.md")
    print("   • README principal: README.md")

if __name__ == "__main__":
    main()