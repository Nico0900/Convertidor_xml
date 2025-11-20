#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitarios para el sistema de internacionalización (i18n)
"""

import unittest
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from i18n import I18n, get_i18n, t


class TestI18n(unittest.TestCase):
    """Tests para la clase I18n"""

    def test_detect_system_language(self):
        """Test: detectar idioma del sistema"""
        lang = I18n.detect_system_language()
        self.assertIn(lang, ['es', 'en'], "El idioma debe ser 'es' o 'en'")

    def test_initialize_with_spanish(self):
        """Test: inicializar con español"""
        i18n = I18n('es')
        self.assertEqual(i18n.get_current_language(), 'es')

    def test_initialize_with_english(self):
        """Test: inicializar con inglés"""
        i18n = I18n('en')
        self.assertEqual(i18n.get_current_language(), 'en')

    def test_initialize_with_invalid_language(self):
        """Test: inicializar con idioma inválido (debería usar inglés)"""
        i18n = I18n('fr')
        self.assertEqual(i18n.get_current_language(), 'en')

    def test_get_translation_spanish(self):
        """Test: obtener traducción en español"""
        i18n = I18n('es')
        text = i18n.get('app_title')
        self.assertIn('Convertidor Universal', text)
        self.assertIn('Adobe Illustrator', text)

    def test_get_translation_english(self):
        """Test: obtener traducción en inglés"""
        i18n = I18n('en')
        text = i18n.get('app_title')
        self.assertIn('Universal XML Converter', text)
        self.assertIn('Adobe Illustrator', text)

    def test_get_translation_with_parameters(self):
        """Test: obtener traducción con parámetros"""
        i18n = I18n('es')
        text = i18n.get('file_selected', filename='test.xlsx')
        self.assertIn('test.xlsx', text)

    def test_get_translation_nonexistent_key(self):
        """Test: obtener traducción con clave inexistente"""
        i18n = I18n('es')
        text = i18n.get('nonexistent_key')
        self.assertEqual(text, 'nonexistent_key')

    def test_set_language(self):
        """Test: cambiar idioma"""
        i18n = I18n('es')
        self.assertEqual(i18n.get_current_language(), 'es')

        i18n.set_language('en')
        self.assertEqual(i18n.get_current_language(), 'en')

    def test_get_available_languages(self):
        """Test: obtener idiomas disponibles"""
        i18n = I18n()
        languages = i18n.get_available_languages()
        self.assertIn('es', languages)
        self.assertIn('en', languages)
        self.assertEqual(len(languages), 2)

    def test_singleton_pattern(self):
        """Test: patrón singleton"""
        i18n1 = get_i18n()
        i18n2 = get_i18n()
        self.assertIs(i18n1, i18n2, "Debe ser la misma instancia")

    def test_shortcut_function(self):
        """Test: función de atajo t()"""
        text = t('app_title')
        self.assertIsInstance(text, str)
        self.assertTrue(len(text) > 0)

    def test_all_spanish_keys_exist(self):
        """Test: verificar que todas las claves existen en español"""
        i18n = I18n('es')
        required_keys = [
            'app_title', 'app_subtitle', 'supported_formats', 'select_file',
            'browse', 'configuration', 'generate_xml', 'preview', 'validate',
            'open_folder', 'warning', 'error', 'success'
        ]

        for key in required_keys:
            text = i18n.get(key)
            self.assertNotEqual(text, key, f"Clave '{key}' no existe en español")

    def test_all_english_keys_exist(self):
        """Test: verificar que todas las claves existen en inglés"""
        i18n = I18n('en')
        required_keys = [
            'app_title', 'app_subtitle', 'supported_formats', 'select_file',
            'browse', 'configuration', 'generate_xml', 'preview', 'validate',
            'open_folder', 'warning', 'error', 'success'
        ]

        for key in required_keys:
            text = i18n.get(key)
            self.assertNotEqual(text, key, f"Clave '{key}' no existe en inglés")

    def test_spanish_english_parity(self):
        """Test: verificar paridad entre español e inglés"""
        i18n_es = I18n('es')
        i18n_en = I18n('en')

        spanish_keys = set(I18n.TRANSLATIONS['es'].keys())
        english_keys = set(I18n.TRANSLATIONS['en'].keys())

        self.assertEqual(spanish_keys, english_keys,
                        "Las claves en español e inglés deben ser las mismas")


if __name__ == '__main__':
    unittest.main()
