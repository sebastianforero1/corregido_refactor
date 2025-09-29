# tests/test_todo.py (pruebas ampliadas para aumentar cobertura)
import pytest
from src.calculadora import dividir_seguro, calcular_estadisticas, generar_resumen
from src.utilidades import saludar_usuario, formatear_mensaje


def test_saludar_usuario():
    assert saludar_usuario("Sebas") == "¡Hola, Sebas!"
    assert saludar_usuario("") == "¡Hola, Anónimo!"


def test_dividir_seguro_exitoso():
    assert dividir_seguro(10, 2) == 5


def test_dividir_seguro_error_division_cero():
    with pytest.raises(ValueError):
        dividir_seguro(10, 0)


def test_calcular_estadisticas_tipico():
    est = calcular_estadisticas([1, 2, 3, "x"])
    assert est["conteo"] == 3
    assert est["total"] == 6
    assert est["max"] == 3
    assert est["min"] == 1
    assert est["promedio"] == 2


def test_calcular_estadisticas_vacio():
    est = calcular_estadisticas([])
    assert est["conteo"] == 0
    assert est["total"] == 0
    assert est["max"] is None
    assert est["min"] is None
    assert est["promedio"] == 0.0


def test_generar_resumen():
    est = {"conteo": 3, "total": 6, "max": 3, "min": 1, "promedio": 2}
    s = generar_resumen(est)
    assert "Conteo 3" in s and "Prom 2" in s


def test_formatear_mensaje():
    est = {"usuario": "Sebas", "conteo": 3, "total": 6, "max": 3, "min": 1, "promedio": 2}
    mensaje = formatear_mensaje(est)
    assert "== MENSAJE ==" in mensaje
    assert "Usuario: Sebas" in mensaje
    assert "Conteo: 3" in mensaje
    assert "Promedio calc: 2.0" in mensaje
