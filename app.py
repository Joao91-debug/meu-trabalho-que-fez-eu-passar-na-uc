from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_feedback, get_all_feedbacks

app = Flask(__name__)

# Inicializa o banco de dados ao iniciar a aplicação
init_db()

def classificar_nota(nota):
    """
    Classifica a experiência com base na nota fornecida.
    """
    if nota >= 9:
        return "Excelente"
    elif 6 <= nota < 9:
        return "Bom"
    else:
        return "Ruim"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar_feedback', methods=['POST'])
def registrar_feedback():
    if request.method == 'POST':
        nome_atendente = request.form['nome_atendente']
        setor = request.form['setor']
        tipo_atendimento = request.form['tipo_atendimento']
        nota = float(request.form['nota']) # Converte a nota para float
        comentario = request.form['comentario']

        classificacao = classificar_nota(nota)

        add_feedback(nome_atendente, setor, tipo_atendimento, nota, classificacao, comentario)
        return redirect(url_for('feedbacks')) # Redireciona para a lista de feedbacks

@app.route('/feedbacks')
def feedbacks():
    todos_feedbacks = get_all_feedbacks()
    return render_template('feedbacks.html', feedbacks=todos_feedbacks)

if __name__ == '__main__':
    app.run(debug=True)