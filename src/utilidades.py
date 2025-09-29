# src/utilidades.py (fuente única para utilidades; sin duplicaciones)

def saludar_usuario(nombre: str) -> str:
    """Devuelve un saludo robusto."""
    return f"¡Hola, {nombre or 'Anónimo'}!"

def formatear_mensaje(datos: dict) -> str:
    """
    Crea un bloque de mensaje formateado a partir de un diccionario de estadísticas.
    Se mantiene en un solo lugar para evitar duplicación.
    """
    datos = datos or {}
    partes = ["== MENSAJE =="]

    usuario = datos.get("usuario") or "Anónimo"
    partes.append(f"Usuario: {usuario}")

    conteo = datos.get("conteo")
    total = datos.get("total")
    maximo = datos.get("max")
    minimo = datos.get("min")
    promedio = datos.get("promedio")

    partes.append(f"Conteo: {conteo if conteo is not None else 'N/A'}")
    partes.append(f"Total: {total if total is not None else 'N/A'}")
    partes.append(f"Máximo: {maximo if maximo is not None else 'N/A'}")
    partes.append(f"Mínimo: {minimo if minimo is not None else 'N/A'}")
    partes.append(f"Promedio: {promedio if promedio is not None else 'N/A'}")

    if conteo and total is not None:
        partes.append(f"Promedio calc: {total / conteo if conteo else 'N/A'}")
    else:
        partes.append("Promedio calc: N/A")

    partes.append("-- FIN --")
    return "\n".join(partes)
