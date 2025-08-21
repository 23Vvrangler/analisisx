from flask import Flask, render_template, request, redirect, url_for
from utils.statistics_utils import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = []
    table = None
    Q1 = Q2 = Q3 = rango = varianza = desviacion = None

    if request.method == "POST":
        data_str = request.form["data"]
        data = [int(x) for x in data_str.split(",") if x.strip().isdigit()]

        if data:
            table = calcular_tabla_frecuencias(data)
            Q1, Q2, Q3 = calcular_medidas_posicion(data)
            rango, varianza, desviacion = calcular_dispersion(data)

    return render_template("index.html", data=",".join(map(str, data)),
                           table=table, Q1=Q1, Q2=Q2, Q3=Q3,
                           rango=rango, varianza=varianza, desviacion=desviacion)

@app.route("/aleatorio")
def aleatorio():
    data = generar_datos_aleatorios()
    return redirect(url_for("index", data=",".join(map(str, data))))

if __name__ == "__main__":
    app.run(debug=True)

