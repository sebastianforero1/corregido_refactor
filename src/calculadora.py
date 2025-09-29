# src/calculadora.py (CORREGIDO / REFACTORIZADO)
from .utilidades import saludar_usuario, formatear_mensaje  # reutilización, sin duplicaciones
from typing import Iterable, Dict, Any, List


def dividir_seguro(a: float, b: float) -> float:
    """
    Confiabilidad: valida divisor y lanza ValueError con mensaje claro,
    evitando ZeroDivisionError silencioso.
    """
    if b == 0:
        raise ValueError("No se permite división por cero.")
    return a / b


def _solo_numeros(numeros: Iterable[Any]) -> List[float]:
    """Filtra únicamente valores numéricos (int/float)."""
    return [x for x in (numeros or []) if isinstance(x, (int, float))]


def calcular_estadisticas(numeros: Iterable[Any]) -> Dict[str, Any]:
    """
    Retorna un diccionario con: conteo, total, max, min y promedio.
    Mejora de mantenibilidad: funciones pequeñas, nombres claros, sin side-effects.
    """
    items = _solo_numeros(numeros)
    if not items:
        return {"conteo": 0, "total": 0, "max": None, "min": None, "promedio": 0.0}

    total = sum(items)
    conteo = len(items)
    return {
        "conteo": conteo,
        "total": total,
        "max": max(items),
        "min": min(items),
        "promedio": total / conteo,
    }


def generar_resumen(estadisticas: Dict[str, Any]) -> str:
    """
    Construye un resumen compacto (separado del formateo largo).
    """
    e = estadisticas
    return (
        f"Conteo {e['conteo']} | Total {e['total']} | "
        f"Máx {e['max']} | Mín {e['min']} | Prom {e['promedio']}"
    )
