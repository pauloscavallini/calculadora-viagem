from flask import Flask, render_template, request
app = Flask(__name__)

def validar_dados(velocidade, distancia):
    if velocidade <= 0 and distancia <= 0:
        raise Exception("Insira um valor válido")
    return velocidade, distancia

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_viagem', methods=['POST'])
def calcular_imc():
    try:
        vel = int(request.form.get('velocidade'))
        dist = int(request.form.get('dist'))

        velocidade, distancia = validar_dados(vel, dist)

        tempo = distancia / velocidade

        return render_template('index.html', resultado=tempo)
    except Exception as e:
        return render_template('index.html', erro="Insira um valor válido")

if __name__ == '__main__':
    app.run()