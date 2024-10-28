from flask import redirect, render_template, Blueprint, url_for, request, session
from DAO.token_verificacao import verificar_integridade_token, verificar_session
from DAO.shows_request import show_especifico_quantidade_request, show_especifico_request
from database.database import db

pagamento_interface = Blueprint('pagamento_interface', __name__)

@pagamento_interface.route('/pagamento/interface/<int:show_id>', methods = ['GET'])
def pagamento_interface_generator(show_id):
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
        
        show = show_especifico_request(show_id)

    except Exception as ex:
        print(f"erro pagamento: {ex}")
        return redirect(url_for('login.login_generator'))
    
    return render_template('pagamento_tela.html', show=show)

@pagamento_interface.route('/pagamento/interface<int:show_id>', methods = ['POST'])
def pagamento_interface_send(show_id):
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
        
        quantidade_ingresso = request.form.get('quantidade_ingresso')
        #pode ser melhorado a logica
        quantidade = show_especifico_quantidade_request(show_id)
        if quantidade > 0:
            quantidade = (quantidade - 1)
            show = show_especifico_request(show_id)
            show.quantidade = quantidade
            db.session.commit()

        #------------

    except Exception as ex:
        print(f"erro pagamento: {ex}")
        return redirect(url_for('login.login_generator'))

    return redirect(url_for('index_usuario.index_usuario_generator'))