#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para ejecutar todos los tests del proyecto
"""

import unittest
import sys
import os

# Agregar directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_all_tests():
    """Ejecutar todos los tests del proyecto"""

    print("=" * 70)
    print("🧪 EJECUTANDO TESTS DEL CONVERTIDOR XML")
    print("=" * 70)
    print()

    # Descubrir y ejecutar todos los tests
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')

    # Ejecutar con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Resumen
    print()
    print("=" * 70)
    print("📊 RESUMEN DE TESTS")
    print("=" * 70)
    print(f"✅ Tests ejecutados: {result.testsRun}")
    print(f"✅ Exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Fallos: {len(result.failures)}")
    print(f"⚠️  Errores: {len(result.errors)}")
    print("=" * 70)

    # Retornar código de salida
    if result.wasSuccessful():
        print("🎉 ¡TODOS LOS TESTS PASARON!")
        return 0
    else:
        print("❌ ALGUNOS TESTS FALLARON")
        return 1


if __name__ == '__main__':
    sys.exit(run_all_tests())
