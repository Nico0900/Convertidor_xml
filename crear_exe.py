#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script automatizado para crear ejecutable del Convertidor XML Adobe Illustrator
Compatible con Windows, macOS y Linux
Ejecutar: python crear_exe.py
"""

import subprocess
import sys
import os
import shutil
import platform
from pathlib import Path

def mostrar_banner():
    """Mostrar banner inicial"""
    sistema = platform.system()
    print("=" * 70)
    print("🚀 CREADOR DE EJECUTABLE - CONVERTIDOR XML ADOBE ILLUSTRATOR")
    print("=" * 70)
    print(f"💻 Sistema detectado: {sistema}")
    print("📁 Convierte tu aplicación Python en ejecutable")
    print("💼 Listo para distribuir sin instalar Python")
    print("=" * 70)
    print()

def verificar_python():
    """Verificar versión de Python"""
    version = sys.version_info
    print(f"🐍 Python detectado: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("✅ Versión de Python compatible")
        return True
    else:
        print("❌ Se requiere Python 3.7 o superior")
        return False

def instalar_dependencias():
    """Instalar todas las dependencias necesarias"""
    print("📦 Instalando dependencias necesarias...")
    
    dependencias = [
        "pyinstaller",
        "pandas", 
        "openpyxl",
        "pillow"  # Para crear iconos
    ]
    
    for dep in dependencias:
        try:
            print(f"   ⬇️ Instalando {dep}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", dep, "--upgrade"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   ✅ {dep} instalado")
        except subprocess.CalledProcessError:
            print(f"   ❌ Error instalando {dep}")
            return False
    
    print("✅ Todas las dependencias instaladas correctamente")
    return True

def verificar_archivos():
    """Verificar que existe el script principal"""
    archivos_necesarios = [
        "convertidor.py",           # Nombre más común
        "convertidor_xml.py",       # Alternativa
        "convertidor_universal.py", # Otra alternativa
        "main.py",                  # Genérico
        "app.py"                    # Otro genérico
    ]
    
    script_encontrado = None
    
    # Buscar el archivo principal
    archivos_en_directorio = [f for f in os.listdir(".") if f.endswith(".py")]
    print(f"📂 Archivos Python encontrados: {archivos_en_directorio}")
    
    for archivo in archivos_necesarios:
        if os.path.exists(archivo):
            script_encontrado = archivo
            break
    
    # Si no encuentra ningún archivo conocido, mostrar opciones
    if not script_encontrado:
        print("\n❓ No se encontró el archivo principal automáticamente")
        print("📋 Archivos Python disponibles:")
        
        archivos_python = [f for f in archivos_en_directorio if f != "crear_exe.py"]
        
        if not archivos_python:
            print("❌ No hay archivos Python en este directorio")
            return None
        
        for i, archivo in enumerate(archivos_python, 1):
            print(f"   {i}. {archivo}")
        
        while True:
            try:
                seleccion = input(f"\n🎯 Selecciona el archivo principal (1-{len(archivos_python)}): ")
                indice = int(seleccion) - 1
                if 0 <= indice < len(archivos_python):
                    script_encontrado = archivos_python[indice]
                    break
                else:
                    print("❌ Selección inválida")
            except (ValueError, KeyboardInterrupt):
                print("\n❌ Operación cancelada")
                return None
    
    print(f"✅ Archivo principal: {script_encontrado}")
    return script_encontrado

def crear_icono():
    """Crear un icono personalizado para la aplicación"""
    if os.path.exists("icono.ico"):
        print("✅ Icono personalizado encontrado: icono.ico")
        return True
    
    print("🎨 Creando icono personalizado...")
    
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Crear imagen 256x256
        size = 256
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))  # Transparente
        draw = ImageDraw.Draw(img)
        
        # Colores Adobe
        bg_color = (52, 152, 219)      # Azul Adobe
        text_color = (255, 255, 255)   # Blanco
        accent_color = (231, 76, 60)   # Rojo acento
        
        # Fondo circular
        margin = 20
        draw.ellipse([margin, margin, size-margin, size-margin], 
                    fill=bg_color, outline=accent_color, width=4)
        
        # Texto XML
        try:
            font_size = 48
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            try:
                font = ImageFont.load_default()
            except:
                font = None
        
        # Dibujar "XML"
        text = "XML"
        if font:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        else:
            text_width, text_height = 80, 20  # Estimación
        
        x = (size - text_width) // 2
        y = (size - text_height) // 2 - 10
        
        draw.text((x, y), text, fill=text_color, font=font)
        
        # Texto pequeño "AI"
        text_small = "AI"
        y_small = y + text_height + 5
        if font:
            font_small = ImageFont.truetype("arial.ttf", 24) if font else font
        else:
            font_small = font
        
        if font_small:
            bbox_small = draw.textbbox((0, 0), text_small, font=font_small)
            text_small_width = bbox_small[2] - bbox_small[0]
        else:
            text_small_width = 20
        
        x_small = (size - text_small_width) // 2
        draw.text((x_small, y_small), text_small, fill=accent_color, font=font_small)
        
        # Guardar en múltiples tamaños
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save('icono.ico', format='ICO', sizes=sizes)
        
        print("✅ Icono creado exitosamente: icono.ico")
        return True
        
    except ImportError:
        print("⚠️ PIL no disponible - creando icono básico")
        # Crear un archivo ICO básico (esto es complejo sin PIL)
        return False
    except Exception as e:
        print(f"⚠️ Error creando icono: {e}")
        return False

def limpiar_archivos_anteriores():
    """Limpiar archivos de compilaciones anteriores"""
    print("🧹 Limpiando archivos anteriores...")
    
    carpetas_limpiar = ["build", "dist", "__pycache__"]
    archivos_limpiar = []
    
    for carpeta in carpetas_limpiar:
        if os.path.exists(carpeta):
            try:
                shutil.rmtree(carpeta)
                print(f"   🗑️ Eliminado: {carpeta}/")
            except:
                print(f"   ⚠️ No se pudo eliminar: {carpeta}/")
    
    # Eliminar archivos .spec
    for archivo_spec in Path(".").glob("*.spec"):
        try:
            archivo_spec.unlink()
            print(f"   🗑️ Eliminado: {archivo_spec}")
        except:
            print(f"   ⚠️ No se pudo eliminar: {archivo_spec}")
    
    print("✅ Limpieza completada")

def crear_ejecutable(script_principal):
    """Crear el archivo ejecutable con configuración optimizada (multiplataforma)"""
    print("⚙️ Creando ejecutable...")

    # Detectar sistema operativo
    sistema = platform.system()
    nombre_base = "ConvertidorXML"

    # Ajustar nombre según plataforma
    if sistema == "Darwin":  # macOS
        nombre_exe = f"{nombre_base}_macOS"
        print("🍎 Creando aplicación para macOS")
    elif sistema == "Windows":
        nombre_exe = f"{nombre_base}_Windows"
        print("🪟 Creando ejecutable para Windows")
    else:  # Linux
        nombre_exe = f"{nombre_base}_Linux"
        print("🐧 Creando ejecutable para Linux")

    # Comando base de PyInstaller
    comando = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                    # Un solo archivo
        "--windowed",                   # Sin consola
        f"--name={nombre_exe}",         # Nombre del ejecutable
        "--clean",                      # Limpiar cache
        "--noconfirm",                  # No confirmar sobrescritura
        "--optimize=2",                 # Optimización máxima
    ]
    
    # Agregar icono si existe (solo Windows)
    if sistema == "Windows" and os.path.exists("icono.ico"):
        comando.extend(["--icon=icono.ico"])
        print("🎨 Icono personalizado agregado")
    elif sistema == "Darwin" and os.path.exists("icono.icns"):
        comando.extend(["--icon=icono.icns"])
        print("🎨 Icono personalizado agregado (macOS)")
    
    # Librerías específicas que pueden necesitar importación explícita
    librerias_ocultas = [
        "pandas",
        "openpyxl", 
        "tkinter",
        "tkinter.ttk",
        "tkinter.filedialog",
        "tkinter.messagebox",
        "json",
        "csv",
        "xml.etree.ElementTree",
        "xml.parsers.expat"
    ]
    
    for lib in librerias_ocultas:
        comando.extend(["--hidden-import", lib])
    
    # Datos adicionales si existen
    archivos_datos = ["config.ini", "readme.txt", "licencia.txt"]
    for archivo in archivos_datos:
        if os.path.exists(archivo):
            comando.extend(["--add-data", f"{archivo};."])
    
    # Script principal al final
    comando.append(script_principal)
    
    print(f"🔨 Ejecutando: {' '.join(comando[:8])}... [comando completo]")
    
    try:
        # Ejecutar PyInstaller con salida en tiempo real
        proceso = subprocess.Popen(
            comando,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        
        # Mostrar progreso
        while True:
            output = proceso.stdout.readline()
            if output == '' and proceso.poll() is not None:
                break
            if output and ("INFO" in output or "WARNING" in output):
                # Mostrar solo líneas importantes
                if "Analyzing" in output:
                    print("   📋 Analizando dependencias...")
                elif "Collecting" in output:
                    print("   📦 Recopilando archivos...")
                elif "Building" in output:
                    print("   🔨 Construyendo ejecutable...")
        
        proceso.wait()
        
        if proceso.returncode == 0:
            print("✅ ¡Ejecutable creado exitosamente!")
            return True
        else:
            print("❌ Error al crear ejecutable")
            return False
            
    except Exception as e:
        print(f"❌ Error en PyInstaller: {e}")
        return False

def verificar_ejecutable(nombre_base="ConvertidorXML"):
    """Verificar que el ejecutable se creó correctamente (multiplataforma)"""
    sistema = platform.system()

    # Determinar extensión según plataforma
    if sistema == "Windows":
        extension = ".exe"
        nombre_completo = f"{nombre_base}_Windows{extension}"
    elif sistema == "Darwin":
        extension = ".app"  # macOS crea .app o ejecutable sin extensión
        nombre_completo = f"{nombre_base}_macOS"
    else:  # Linux
        extension = ""
        nombre_completo = f"{nombre_base}_Linux"

    # Buscar el ejecutable
    ruta_exe = Path("dist") / nombre_completo

    if ruta_exe.exists():
        tamaño = ruta_exe.stat().st_size / (1024*1024)  # MB
        print(f"✅ Ejecutable creado: {ruta_exe.name}")
        print(f"📏 Tamaño: {tamaño:.1f} MB")
        print(f"📁 Ubicación: {ruta_exe.absolute()}")
        return True
    else:
        print("❌ No se encontró el ejecutable en dist/")
        # Buscar todos los archivos en dist/
        if Path("dist").exists():
            archivos = list(Path("dist").iterdir())
            if archivos:
                print(f"📁 Archivos encontrados en dist/: {[f.name for f in archivos]}")
        return False

def crear_documentacion():
    """Crear documentación para el usuario final"""
    readme_content = """# CONVERTIDOR UNIVERSAL XML - ADOBE ILLUSTRATOR

## 🎯 ¿Qué hace este programa?
Convierte datos desde Excel, CSV, JSON, TXT y otros formatos a archivos XML compatibles con las Variables de Adobe Illustrator.

## 📋 Formatos soportados:
- Excel (.xlsx, .xls)
- CSV (.csv) 
- TXT (.txt)
- JSON (.json)
- TSV (.tsv)
- RAW (.raw, .data)

## 🚀 Cómo usar:
1. Ejecuta ConvertidorXML_Adobe.exe
2. Haz clic en "Buscar" y selecciona tu archivo
3. El programa auto-detectará la columna con nombres/datos
4. Ajusta la configuración si es necesario
5. Haz clic en "GENERAR ARCHIVO XML"
6. Importa el XML en Adobe Illustrator

## 📁 En Adobe Illustrator:
1. Ve a Ventana > Variables
2. En el panel Variables, haz clic en "Importar"
3. Selecciona el archivo XML generado
4. ¡Listo! Tus variables estarán disponibles

## ⚙️ Configuración:
- **Variable XML**: Nombre de la variable en Illustrator (ej: NOMBRE2)
- **Binding name**: Nombre del conjunto de variables (ej: binding1)

## 🆘 Soporte:
Si tienes problemas, verifica que:
- Tu archivo tenga datos válidos
- La columna seleccionada contenga texto
- El nombre del archivo XML no tenga caracteres especiales

---
Convertidor Universal XML v1.0
Compatible con Adobe Illustrator CC/2024
"""
    
    try:
        with open("dist/LEEME.txt", "w", encoding="utf-8") as f:
            f.write(readme_content)
        print("✅ Documentación creada: dist/LEEME.txt")
    except:
        print("⚠️ No se pudo crear la documentación")

def crear_script_instalacion():
    """Crear script de instalación para Windows"""
    script_instalacion = """@echo off
title Instalador - Convertidor XML Adobe Illustrator
color 0B
echo.
echo ================================================================
echo                CONVERTIDOR XML ADOBE ILLUSTRATOR
echo                        Instalador v1.0
echo ================================================================
echo.

set "DESTINO=%USERPROFILE%\\Desktop\\ConvertidorXML"
set "MENU_INICIO=%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs"

echo 📁 Creando carpeta de instalacion...
if not exist "%DESTINO%" mkdir "%DESTINO%"

echo 📋 Copiando archivos...
copy "ConvertidorXML_Adobe.exe" "%DESTINO%\\" >nul
copy "LEEME.txt" "%DESTINO%\\" >nul 2>nul
copy "icono.ico" "%DESTINO%\\" >nul 2>nul

echo 🔗 Creando acceso directo en el escritorio...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Convertidor XML Adobe.lnk'); $Shortcut.TargetPath = '%DESTINO%\\ConvertidorXML_Adobe.exe'; $Shortcut.WorkingDirectory = '%DESTINO%'; $Shortcut.Description = 'Convertidor Universal XML para Adobe Illustrator'; $Shortcut.Save()" >nul 2>nul

echo 📋 Creando acceso en el menu inicio...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%MENU_INICIO%\\Convertidor XML Adobe.lnk'); $Shortcut.TargetPath = '%DESTINO%\\ConvertidorXML_Adobe.exe'; $Shortcut.WorkingDirectory = '%DESTINO%'; $Shortcut.Description = 'Convertidor Universal XML para Adobe Illustrator'; $Shortcut.Save()" >nul 2>nul

echo.
echo ✅ ¡INSTALACION COMPLETADA!
echo.
echo 📍 Ubicacion: %DESTINO%
echo 🖥️  Acceso directo creado en el escritorio
echo 📋 Tambien disponible en el menu inicio
echo.
echo 🚀 Para usar: Haz doble clic en "Convertidor XML Adobe" en el escritorio
echo.
pause
"""
    
    try:
        with open("dist/Instalar.bat", "w", encoding="utf-8") as f:
            f.write(script_instalacion)
        print("✅ Instalador creado: dist/Instalar.bat")
    except:
        print("⚠️ No se pudo crear el instalador")

def mostrar_resumen_final():
    """Mostrar resumen final y instrucciones (multiplataforma)"""
    sistema = platform.system()

    print("\n" + "=" * 70)
    print("🎉 ¡EJECUTABLE CREADO EXITOSAMENTE!")
    print("=" * 70)
    print()
    print("📦 ARCHIVOS GENERADOS:")

    if sistema == "Windows":
        print("   📁 dist/ConvertidorXML_Windows.exe  (Programa principal)")
        print("   📋 dist/LEEME.txt                   (Instrucciones)")
        print("   ⚙️  dist/Instalar.bat               (Instalador automático)")
        if os.path.exists("dist/icono.ico"):
            print("   🎨 dist/icono.ico                   (Icono personalizado)")
    elif sistema == "Darwin":
        print("   📁 dist/ConvertidorXML_macOS        (Aplicación macOS)")
        print("   📋 dist/LEEME.txt                   (Instrucciones)")
    else:  # Linux
        print("   📁 dist/ConvertidorXML_Linux        (Ejecutable Linux)")
        print("   📋 dist/LEEME.txt                   (Instrucciones)")

    print()
    print("🚀 PARA DISTRIBUIR:")
    print("   1. Comparte toda la carpeta 'dist'")
    print("   2. O solo el archivo ejecutable")

    if sistema == "Windows":
        print("   3. Los usuarios pueden ejecutar Instalar.bat para instalación automática")

    print()
    print("✅ CARACTERÍSTICAS:")
    print("   • No requiere instalar Python")
    print(f"   • Compatible con {sistema}")
    print("   • Interfaz gráfica intuitiva")
    print("   • Soporte para múltiples formatos")
    print("   • Optimizado para Adobe Illustrator")
    print("   • Multilenguaje (Español/Inglés)")
    print()
    print("🔧 PARA PROBAR:")
    print("   1. Ve a la carpeta 'dist'")

    if sistema == "Windows":
        print("   2. Ejecuta ConvertidorXML_Windows.exe")
    elif sistema == "Darwin":
        print("   2. Ejecuta ./ConvertidorXML_macOS")
        print("   3. O abre ConvertidorXML_macOS.app si se creó")
    else:
        print("   2. Ejecuta ./ConvertidorXML_Linux")
        print("   3. (Puede necesitar: chmod +x ConvertidorXML_Linux)")

    print("   4. Debería abrir la interfaz gráfica")
    print()

def main():
    """Función principal del creador de ejecutables"""
    mostrar_banner()
    
    try:
        # Paso 1: Verificar Python
        if not verificar_python():
            input("❌ Presiona Enter para salir...")
            return
        
        # Paso 2: Instalar dependencias
        if not instalar_dependencias():
            input("❌ Presiona Enter para salir...")
            return
        
        # Paso 3: Verificar archivo principal
        script_principal = verificar_archivos()
        if not script_principal:
            input("❌ Presiona Enter para salir...")
            return
        
        # Paso 4: Crear icono
        crear_icono()
        
        # Paso 5: Limpiar archivos anteriores
        limpiar_archivos_anteriores()
        
        # Paso 6: Crear ejecutable
        if crear_ejecutable(script_principal):
            # Paso 7: Verificar resultado
            if verificar_ejecutable():
                # Paso 8: Crear documentación y extras
                crear_documentacion()
                crear_script_instalacion()
                
                # Paso 9: Mostrar resumen
                mostrar_resumen_final()
            else:
                print("❌ Error: No se pudo verificar el ejecutable")
        else:
            print("❌ Error: No se pudo crear el ejecutable")
            
    except KeyboardInterrupt:
        print("\n❌ Proceso cancelado por el usuario")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    
    print("Presiona Enter para salir...")
    input()

if __name__ == "__main__":
    main()