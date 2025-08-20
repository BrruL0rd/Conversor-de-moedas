from flask import Flask, render_template, request

app = Flask(__name__)

# Valores de câmbio fixos (você pode atualizar depois com valores reais)
TAXAS_CAMBIO = {
    'USD': 5.20,   # Dólar → Real
    'EUR': 5.60    # Euro → Real
}

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        valor = float(request.form['valor'])
        moeda = request.form['moeda']
        taxa = TAXAS_CAMBIO.get(moeda, 1)
        resultado = valor * taxa

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
