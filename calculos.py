import pandas as pd
import psycopg2
from datetime import datetime

 
def mostrar_total(formatear_monto):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    df = pd.read_sql("SELECT * FROM movimientos", conn)
    df["fecha"] = pd.to_datetime(df["fecha"])

    # filtrado = df[(df["fecha"] == datetime.now().strftime("%Y-%m-%d"))]
    filtrado = df[df["fecha"].dt.date == datetime.now().date()]
    filtrado = df[df["fecha"].dt.date == datetime.now().date()]


    # filtrado = filtrado[filtrado["proveedor"]== "cliente"]
    total = filtrado["monto"].sum()
    return f"📊 Ganancia de hoy: ${formatear_monto(total)}"


def calcular_total(texto_usuario, extraer_info_consulta, formatear_monto):
    info = extraer_info_consulta(texto_usuario)

    if "fecha_inicio" not in info or "fecha_fin" not in info:
        return "❌ No pude entender la fecha. Probá de nuevo."

    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    df = pd.read_sql("SELECT * FROM movimientos", conn)
    df["fecha"] = pd.to_datetime(df["fecha"])

    desde = pd.to_datetime(info["fecha_inicio"])
    hasta = pd.to_datetime(info["fecha_fin"])
    tipo = info["tipo"]
    filtrado = df[(df["fecha"] >= desde) & (df["fecha"] <= hasta)]

    filtrado = filtrado[filtrado["proveedor"]== "cliente"]
    total = filtrado["monto"].sum()
    return f"📊 Total de {tipo} entre {desde.date()} y {hasta.date()}: ${formatear_monto(total)}"
