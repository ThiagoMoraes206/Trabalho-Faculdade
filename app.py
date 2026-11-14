from flask import Flask, request, jsonify, render_template
import operacoes  # importa funções do arquivo separado

# Como executar:
# 1. Certifique-se de ter o Flask instalado: pip install flask
# 2. Execute este arquivo: python app.py
# python.exe -m pip install --upgrade pip

app = Flask(__name__)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")


# Página de soma
@app.route("/soma")
def soma_page():
    return render_template("soma.html")


@app.route("/api/soma", methods=["POST"])
def soma():
    return calcular("soma")


# Página de subtração
@app.route("/subtracao")
def subtracao_page():
    return render_template("subtracao.html")


@app.route("/api/subtracao", methods=["POST"])
def subtracao():
    return calcular("subtracao")


# Página de multiplicação
@app.route("/multiplicacao")
def multiplicacao_page():
    return render_template("multiplicacao.html")


@app.route("/api/multiplicacao", methods=["POST"])
def multiplicacao():
    return calcular("multiplicacao")


# Página de divisão
@app.route("/divisao")
def divisao_page():
    return render_template("divisao.html")


@app.route("/api/divisao", methods=["POST"])
def divisao():
    return calcular("divisao")


# Função responsável pelos cálculos
def calcular(operacao):
    dados = request.get_json(silent=True) or {}

    try:
        valor1 = float(dados["valor1"])
        valor2 = float(dados["valor2"])

        funcoes = {
            "soma": operacoes.calcular_soma,
            "subtracao": operacoes.calcular_subtracao,
            "multiplicacao": operacoes.calcular_multiplicacao,
            "divisao": operacoes.calcular_divisao
        }

        resultado = funcoes[operacao](valor1, valor2)

        return jsonify({"resultado": resultado})

    except KeyError:
        return jsonify({"erro": "Informe os dois valores."}), 400

    except (TypeError, ValueError):
        return jsonify({"erro": "Digite valores numéricos válidos."}), 400

    except ZeroDivisionError as erro:
        return jsonify({"erro": str(erro)}), 400


if __name__ == "__main__":
    app.run(debug=True)