#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Internacionalización (i18n) para Convertidor XML
Soporta español e inglés con detección automática del idioma del sistema
"""

import locale
import sys

class I18n:
    """Clase para manejar la internacionalización de la aplicación"""

    # Diccionario de traducciones
    TRANSLATIONS = {
        'es': {
            # Títulos principales
            'app_title': 'Convertidor Universal a XML - Adobe Illustrator',
            'app_subtitle': 'Para Variables de Adobe Illustrator',

            # Formatos soportados
            'supported_formats': 'Formatos Soportados',
            'formats_text': '''📁 Formatos de archivo compatibles:
• Excel (.xlsx, .xls) - Hojas de cálculo
• CSV (.csv) - Valores separados por comas
• TXT (.txt) - Archivos de texto plano (línea por línea)
• JSON (.json) - Archivos JSON con arrays o objetos
• TSV (.tsv) - Valores separados por tabulaciones
• RAW (.raw, .data) - Datos en texto plano''',

            # Sección de archivos
            'select_file': 'Seleccionar Archivo',
            'file_label': 'Archivo:',
            'browse': 'Buscar',

            # Configuración
            'configuration': 'Configuración',
            'data_column': 'Columna de datos:',
            'auto_detect': 'Auto-detectar',
            'xml_variable': 'Variable XML:',
            'binding_name': 'Binding name:',
            'xml_file': 'Archivo XML:',

            # Botones
            'generate_xml': '📄 GENERAR ARCHIVO XML',
            'preview': '👁 Vista Previa',
            'validate': '✓ Validar XML',
            'open_folder': '📁 Abrir Carpeta',

            # Estado y mensajes
            'status_messages': 'Estado y Mensajes',
            'app_started': '🚀 Convertidor Universal XML iniciado',
            'select_file_start': '📝 Selecciona un archivo para comenzar',
            'file_selected': '📁 Archivo seleccionado: {filename}',
            'analyzing_file': '🔍 Analizando archivo...',
            'columns_found': '📊 Columnas encontradas: {count}',
            'data_rows': '📝 Filas de datos: {count}',
            'analysis_error': '❌ No se pudo analizar la estructura del archivo',
            'error_analyzing': '❌ Error al analizar: {error}',
            'auto_detected': '🎯 Auto-detectado: \'{column}\' ({score:.1%} contenido textual)',
            'auto_detect_error': '❌ Error en auto-detección: {error}',

            # Conversión
            'starting_conversion': '🔄 Iniciando conversión...',
            'generating_xml': '🔄 Generando archivo XML...',
            'processing_elements': '📊 Procesando {count} elementos',
            'conversion_complete': '✅ ¡Conversión completada!',
            'file_saved': '💾 Archivo guardado: {path}',
            'datasets_created': '📈 Datasets creados: {count}',
            'xml_generated': '✅ ¡XML GENERADO EXITOSAMENTE! ({count} elementos)',
            'conversion_error': '❌ Error en conversión: {error}',
            'xml_generation_error': '❌ Error al generar XML',

            # Validación
            'xml_validated': '✅ XML validado correctamente',
            'xml_valid': '✅ El archivo XML es válido para Adobe Illustrator',
            'xml_validation_error': '❌ Error de validación XML: {error}',
            'xml_invalid': 'XML inválido:\n{error}',

            # Mensajes de diálogo
            'warning': 'Advertencia',
            'error': 'Error',
            'success': '¡Éxito!',
            'complete_all_fields': 'Completa todos los campos',
            'select_file_column': 'Selecciona archivo y columna primero',
            'no_xml_validate': 'No hay archivo XML para validar',
            'folder_not_exist': 'La carpeta no existe',
            'no_output_file': 'No hay archivo de salida especificado',
            'folder_opened': '📁 Carpeta abierta: {path}',

            # Vista previa
            'preview_title': 'Vista Previa',
            'preview_header': 'Vista previa (primeros 10 elementos):\n\n',
            'preview_more': '\n... y {count} elementos más',
            'preview_error': 'Error en vista previa: {error}',

            # Mensaje de éxito
            'success_message': '''¡Archivo XML generado correctamente!

📁 Archivo: {filename}
📊 Elementos: {count}
📍 Ubicación: {location}

¿Deseas abrir la carpeta donde se guardó?''',

            # Formato no soportado
            'unsupported_format': 'Formato de archivo no soportado: {ext}',
            'file_load_error': 'Error cargando archivo: {error}',
        },
        'en': {
            # Main titles
            'app_title': 'Universal XML Converter - Adobe Illustrator',
            'app_subtitle': 'For Adobe Illustrator Variables',

            # Supported formats
            'supported_formats': 'Supported Formats',
            'formats_text': '''📁 Compatible file formats:
• Excel (.xlsx, .xls) - Spreadsheets
• CSV (.csv) - Comma-separated values
• TXT (.txt) - Plain text files (line by line)
• JSON (.json) - JSON files with arrays or objects
• TSV (.tsv) - Tab-separated values
• RAW (.raw, .data) - Plain text data''',

            # File section
            'select_file': 'Select File',
            'file_label': 'File:',
            'browse': 'Browse',

            # Configuration
            'configuration': 'Configuration',
            'data_column': 'Data column:',
            'auto_detect': 'Auto-detect',
            'xml_variable': 'XML Variable:',
            'binding_name': 'Binding name:',
            'xml_file': 'XML File:',

            # Buttons
            'generate_xml': '📄 GENERATE XML FILE',
            'preview': '👁 Preview',
            'validate': '✓ Validate XML',
            'open_folder': '📁 Open Folder',

            # Status and messages
            'status_messages': 'Status and Messages',
            'app_started': '🚀 Universal XML Converter started',
            'select_file_start': '📝 Select a file to begin',
            'file_selected': '📁 File selected: {filename}',
            'analyzing_file': '🔍 Analyzing file...',
            'columns_found': '📊 Columns found: {count}',
            'data_rows': '📝 Data rows: {count}',
            'analysis_error': '❌ Could not analyze file structure',
            'error_analyzing': '❌ Error analyzing: {error}',
            'auto_detected': '🎯 Auto-detected: \'{column}\' ({score:.1%} text content)',
            'auto_detect_error': '❌ Auto-detection error: {error}',

            # Conversion
            'starting_conversion': '🔄 Starting conversion...',
            'generating_xml': '🔄 Generating XML file...',
            'processing_elements': '📊 Processing {count} elements',
            'conversion_complete': '✅ Conversion completed!',
            'file_saved': '💾 File saved: {path}',
            'datasets_created': '📈 Datasets created: {count}',
            'xml_generated': '✅ XML GENERATED SUCCESSFULLY! ({count} elements)',
            'conversion_error': '❌ Conversion error: {error}',
            'xml_generation_error': '❌ Error generating XML',

            # Validation
            'xml_validated': '✅ XML validated correctly',
            'xml_valid': '✅ The XML file is valid for Adobe Illustrator',
            'xml_validation_error': '❌ XML validation error: {error}',
            'xml_invalid': 'Invalid XML:\n{error}',

            # Dialog messages
            'warning': 'Warning',
            'error': 'Error',
            'success': 'Success!',
            'complete_all_fields': 'Complete all fields',
            'select_file_column': 'Select file and column first',
            'no_xml_validate': 'No XML file to validate',
            'folder_not_exist': 'Folder does not exist',
            'no_output_file': 'No output file specified',
            'folder_opened': '📁 Folder opened: {path}',

            # Preview
            'preview_title': 'Preview',
            'preview_header': 'Preview (first 10 elements):\n\n',
            'preview_more': '\n... and {count} more elements',
            'preview_error': 'Preview error: {error}',

            # Success message
            'success_message': '''XML file generated successfully!

📁 File: {filename}
📊 Elements: {count}
📍 Location: {location}

Do you want to open the folder where it was saved?''',

            # Unsupported format
            'unsupported_format': 'Unsupported file format: {ext}',
            'file_load_error': 'Error loading file: {error}',
        }
    }

    def __init__(self, language=None):
        """
        Inicializar el sistema i18n

        Args:
            language: Código de idioma ('es', 'en') o None para auto-detectar
        """
        if language is None:
            language = self.detect_system_language()

        self.current_language = language if language in self.TRANSLATIONS else 'en'

    @staticmethod
    def detect_system_language():
        """
        Detectar el idioma del sistema operativo

        Returns:
            str: Código de idioma ('es' o 'en')
        """
        try:
            # Obtener el locale del sistema
            system_locale, _ = locale.getdefaultlocale()

            if system_locale:
                # Extraer código de idioma (primeros 2 caracteres)
                lang_code = system_locale[:2].lower()

                # Si es español, retornar 'es'
                if lang_code == 'es':
                    return 'es'

                # Para cualquier otro idioma, usar inglés por defecto
                return 'en'

        except Exception as e:
            print(f"Warning: Could not detect system language: {e}")

        # Por defecto, usar inglés
        return 'en'

    def get(self, key, **kwargs):
        """
        Obtener una traducción

        Args:
            key: Clave de la traducción
            **kwargs: Parámetros para formatear el string

        Returns:
            str: Texto traducido y formateado
        """
        # Obtener el texto en el idioma actual
        text = self.TRANSLATIONS.get(self.current_language, {}).get(key, key)

        # Si hay parámetros, formatear el texto
        if kwargs:
            try:
                return text.format(**kwargs)
            except KeyError:
                return text

        return text

    def set_language(self, language):
        """
        Cambiar el idioma actual

        Args:
            language: Código de idioma ('es' o 'en')
        """
        if language in self.TRANSLATIONS:
            self.current_language = language
        else:
            print(f"Warning: Language '{language}' not supported. Using English.")
            self.current_language = 'en'

    def get_current_language(self):
        """
        Obtener el idioma actual

        Returns:
            str: Código del idioma actual
        """
        return self.current_language

    def get_available_languages(self):
        """
        Obtener lista de idiomas disponibles

        Returns:
            list: Lista de códigos de idioma disponibles
        """
        return list(self.TRANSLATIONS.keys())


# Crear instancia global
_i18n_instance = None

def get_i18n():
    """
    Obtener la instancia global de i18n (singleton)

    Returns:
        I18n: Instancia del sistema de internacionalización
    """
    global _i18n_instance
    if _i18n_instance is None:
        _i18n_instance = I18n()
    return _i18n_instance


def t(key, **kwargs):
    """
    Función de atajo para traducir texto

    Args:
        key: Clave de la traducción
        **kwargs: Parámetros para formatear

    Returns:
        str: Texto traducido
    """
    return get_i18n().get(key, **kwargs)


if __name__ == "__main__":
    # Pruebas del sistema de i18n
    print("Testing i18n system...")
    print("=" * 50)

    # Detectar idioma del sistema
    detected = I18n.detect_system_language()
    print(f"Detected system language: {detected}")
    print()

    # Probar en español
    i18n_es = I18n('es')
    print(f"Spanish test:")
    print(f"  Title: {i18n_es.get('app_title')}")
    print(f"  File selected: {i18n_es.get('file_selected', filename='test.xlsx')}")
    print()

    # Probar en inglés
    i18n_en = I18n('en')
    print(f"English test:")
    print(f"  Title: {i18n_en.get('app_title')}")
    print(f"  File selected: {i18n_en.get('file_selected', filename='test.xlsx')}")
    print()

    # Probar función de atajo
    print(f"Shortcut function test:")
    print(f"  {t('app_title')}")
