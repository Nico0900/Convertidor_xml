@echo off
REM ============================================================================
REM Script para generar ejecutable de Windows
REM Convertidor Universal XML v2.0 - Adobe Illustrator
REM ============================================================================
REM Ejecutar en Windows con Python 3.7+ instalado
REM Este script genera ConvertidorXML_Windows.exe (portable, no requiere instalacion)
REM ============================================================================

echo.
echo ========================================
echo   Convertidor XML - Build para Windows
echo ========================================
echo   Version: 2.0.0
echo   Autor: Nicolas Vargas Canon
echo ========================================
echo.

REM Verificar que Python esta instalado
echo [CHECK] Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado
    echo.
    echo Por favor instala Python 3.7 o superior desde:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANTE: Durante la instalacion marca:
    echo   [X] Add Python to PATH
    echo.
    pause
    exit /b 1
)

python --version
echo [OK] Python instalado correctamente
echo.

echo [1/5] Instalando dependencias...
echo Este proceso puede tardar 1-2 minutos...
pip install pandas openpyxl pyinstaller pillow --quiet --upgrade
if %errorlevel% neq 0 (
    echo [ERROR] No se pudieron instalar las dependencias
    echo.
    echo Intenta ejecutar manualmente:
    echo   pip install --upgrade pip
    echo   pip install pandas openpyxl pyinstaller pillow
    echo.
    pause
    exit /b 1
)
echo [OK] Dependencias instaladas
echo.

echo [2/5] Limpiando builds anteriores...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist *.spec del /q *.spec
echo [OK] Limpieza completada
echo.

echo [3/5] Generando ejecutable para Windows...
echo Este proceso puede tardar 2-3 minutos...
echo Por favor espera...
python -m PyInstaller ^
    --onefile ^
    --windowed ^
    --name=ConvertidorXML_Windows ^
    --clean ^
    --noconfirm ^
    --optimize=2 ^
    --hidden-import=pandas ^
    --hidden-import=openpyxl ^
    --hidden-import=tkinter ^
    --hidden-import=tkinter.ttk ^
    --hidden-import=tkinter.filedialog ^
    --hidden-import=tkinter.messagebox ^
    --hidden-import=json ^
    --hidden-import=csv ^
    --hidden-import=xml.etree.ElementTree ^
    --hidden-import=xml.parsers.expat ^
    --hidden-import=i18n ^
    convertidor.py

if %errorlevel% neq 0 (
    echo ERROR: Fallo al crear el ejecutable
    pause
    exit /b 1
)

echo [4/5] Verificando resultado...
if exist dist\ConvertidorXML_Windows.exe (
    echo [OK] Ejecutable creado exitosamente
    echo.

    REM Obtener tamano del archivo
    for %%A in (dist\ConvertidorXML_Windows.exe) do set size=%%~zA

    echo.
    echo ========================================
    echo   ^!EXITO^! Ejecutable generado
    echo ========================================
    echo.
    echo   Archivo: dist\ConvertidorXML_Windows.exe
    echo   Tamano: %size% bytes
    echo.
    echo   El ejecutable es PORTABLE:
    echo   - No requiere instalacion
    echo   - No requiere Python
    echo   - Funciona en Windows 10/11
    echo.
    echo ========================================
    echo.
) else (
    echo [ERROR] No se encontro el ejecutable
    echo Revisa los mensajes de error anteriores
    pause
    exit /b 1
)

echo [5/5] Limpiando archivos temporales...
if exist build rmdir /s /q build
if exist *.spec del /q *.spec
echo [OK] Limpieza completada
echo.

echo ========================================
echo   PROCESO COMPLETADO
echo ========================================
echo.
echo Para usar el programa:
echo   1. Ve a la carpeta: dist\
echo   2. Ejecuta: ConvertidorXML_Windows.exe
echo   3. ^!Listo^!
echo.
echo Para distribuir:
echo   - Comparte solo el archivo .exe
echo   - Los usuarios NO necesitan Python
echo.
pause
