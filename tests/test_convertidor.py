#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitarios para el convertidor XML
"""

import unittest
import sys
import os
import tempfile
import pandas as pd
import json
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from convertidor import XMLConverterApp
import tkinter as tk


class TestXMLConverterApp(unittest.TestCase):
    """Tests para la clase XMLConverterApp"""

    @classmethod
    def setUpClass(cls):
        """Configuración inicial para todos los tests"""
        cls.root = tk.Tk()
        cls.root.withdraw()  # Ocultar ventana durante tests

    @classmethod
    def tearDownClass(cls):
        """Limpieza después de todos los tests"""
        cls.root.destroy()

    def setUp(self):
        """Configuración antes de cada test"""
        self.app = XMLConverterApp(self.root)
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Limpieza después de cada test"""
        # Limpiar archivos temporales
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def create_test_excel(self, filename='test.xlsx'):
        """Crear archivo Excel de prueba"""
        path = os.path.join(self.temp_dir, filename)
        df = pd.DataFrame({
            'Nombres': ['Juan Pérez', 'María García', 'Carlos López'],
            'Edad': [25, 30, 35],
            'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
        })
        df.to_excel(path, index=False)
        return path

    def create_test_csv(self, filename='test.csv'):
        """Crear archivo CSV de prueba"""
        path = os.path.join(self.temp_dir, filename)
        df = pd.DataFrame({
            'Nombres': ['Ana Martínez', 'Pedro Sánchez', 'Laura Gómez'],
            'Edad': [28, 32, 26]
        })
        df.to_csv(path, index=False)
        return path

    def create_test_json(self, filename='test.json'):
        """Crear archivo JSON de prueba"""
        path = os.path.join(self.temp_dir, filename)
        data = {
            'nombres': ['Miguel Torres', 'Carmen Ruiz', 'Francisco Vega']
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
        return path

    def create_test_txt(self, filename='test.txt'):
        """Crear archivo TXT de prueba"""
        path = os.path.join(self.temp_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write("Nombre Uno\n")
            f.write("Nombre Dos\n")
            f.write("Nombre Tres\n")
        return path

    # Tests de inicialización

    def test_app_initialization(self):
        """Test: inicialización correcta de la aplicación"""
        self.assertIsNotNone(self.app)
        self.assertIsNotNone(self.app.i18n)
        self.assertIsNotNone(self.app.root)

    def test_platform_detection(self):
        """Test: detección de plataforma"""
        self.assertIn(self.app.os_platform, ['Windows', 'Darwin', 'Linux'])

    def test_default_values(self):
        """Test: valores por defecto"""
        self.assertEqual(self.app.output_file.get(), "variables_illustrator.xml")
        self.assertEqual(self.app.var_name.get(), "NOMBRE2")
        self.assertEqual(self.app.binding_name.get(), "binding1")

    # Tests de carga de archivos

    def test_load_excel_file(self):
        """Test: cargar archivo Excel"""
        excel_path = self.create_test_excel()
        data = self.app.load_file_data(excel_path)

        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)
        self.assertIn('Nombres', data.columns)

    def test_load_csv_file(self):
        """Test: cargar archivo CSV"""
        csv_path = self.create_test_csv()
        data = self.app.load_file_data(csv_path)

        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)
        self.assertIn('Nombres', data.columns)

    def test_load_json_file(self):
        """Test: cargar archivo JSON"""
        json_path = self.create_test_json()
        data = self.app.load_file_data(json_path)

        self.assertIsInstance(data, pd.DataFrame)
        self.assertTrue(len(data) > 0)

    def test_load_txt_file(self):
        """Test: cargar archivo TXT"""
        txt_path = self.create_test_txt()
        data = self.app.load_file_data(txt_path)

        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 3)

    def test_load_unsupported_file(self):
        """Test: cargar archivo no soportado"""
        invalid_path = os.path.join(self.temp_dir, 'test.xyz')
        with open(invalid_path, 'w') as f:
            f.write("test")

        with self.assertRaises(Exception):
            self.app.load_file_data(invalid_path)

    # Tests de generación XML

    def test_generate_adobe_xml(self):
        """Test: generar XML con formato Adobe"""
        values = ['Nombre 1', 'Nombre 2', 'Nombre 3']
        xml_content = self.app.generate_adobe_xml(values, 'TEST_VAR', 'test_binding')

        self.assertIn('<?xml version="1.0" encoding="utf-8"?>', xml_content)
        self.assertIn('<svg>', xml_content)
        self.assertIn('TEST_VAR', xml_content)
        self.assertIn('test_binding', xml_content)
        self.assertIn('Nombre 1', xml_content)
        self.assertIn('Data Set', xml_content)

    def test_generate_xml_with_special_characters(self):
        """Test: generar XML con caracteres especiales"""
        values = ['Nombre & Apellido', 'Test < > "quotes"', "Test 'apostrophe'"]
        xml_content = self.app.generate_adobe_xml(values, 'VAR', 'binding')

        # Verificar que se escaparon los caracteres
        self.assertIn('&amp;', xml_content)
        self.assertIn('&lt;', xml_content)
        self.assertIn('&gt;', xml_content)
        self.assertIn('&quot;', xml_content)
        self.assertIn('&apos;', xml_content)

    def test_generate_xml_empty_values(self):
        """Test: generar XML con lista vacía"""
        values = []
        xml_content = self.app.generate_adobe_xml(values, 'VAR', 'binding')

        self.assertIn('<?xml version="1.0" encoding="utf-8"?>', xml_content)
        self.assertIn('<svg>', xml_content)

    def test_generate_xml_single_value(self):
        """Test: generar XML con un solo valor"""
        values = ['Único Nombre']
        xml_content = self.app.generate_adobe_xml(values, 'VAR', 'binding')

        self.assertIn('Único Nombre', xml_content)
        self.assertIn('Data Set', xml_content)

    # Tests de validación XML

    def test_validate_xml_valid_file(self):
        """Test: validar archivo XML válido"""
        values = ['Test 1', 'Test 2']
        xml_content = self.app.generate_adobe_xml(values, 'VAR', 'binding')

        xml_path = os.path.join(self.temp_dir, 'test_valid.xml')
        with open(xml_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)

        # Verificar que el XML es parseable
        from xml.parsers.expat import ParserCreate
        parser = ParserCreate()

        try:
            with open(xml_path, 'r', encoding='utf-8') as f:
                parser.Parse(f.read(), True)
            valid = True
        except:
            valid = False

        self.assertTrue(valid, "El XML generado debe ser válido")

    # Tests de escape de caracteres XML

    def test_xml_escape_ampersand(self):
        """Test: escapar &"""
        values = ['Test & Prueba']
        xml = self.app.generate_adobe_xml(values, 'V', 'b')
        self.assertIn('&amp;', xml)

    def test_xml_escape_less_than(self):
        """Test: escapar <"""
        values = ['Test < 5']
        xml = self.app.generate_adobe_xml(values, 'V', 'b')
        self.assertIn('&lt;', xml)

    def test_xml_escape_greater_than(self):
        """Test: escapar >"""
        values = ['Test > 5']
        xml = self.app.generate_adobe_xml(values, 'V', 'b')
        self.assertIn('&gt;', xml)

    # Tests de estructura XML

    def test_xml_structure_dtd(self):
        """Test: estructura DTD en XML"""
        xml = self.app.generate_adobe_xml(['Test'], 'V', 'b')
        self.assertIn('<!DOCTYPE svg PUBLIC', xml)
        self.assertIn('<!ENTITY ns_vars', xml)

    def test_xml_structure_variable_set(self):
        """Test: estructura variableSet en XML"""
        xml = self.app.generate_adobe_xml(['Test'], 'MY_VAR', 'my_binding')
        self.assertIn('<variableSet', xml)
        self.assertIn('varSetName="my_binding"', xml)


if __name__ == '__main__':
    unittest.main()
