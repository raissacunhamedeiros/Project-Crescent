from flask import redirect, render_template, Blueprint, url_for, request, session
from DAO.token_verificacao import verificar_integridade_token, verificar_session
from DAO.shows_request import show_especifico_quantidade_request

pagamento_interface = Blueprint('pagamento_interface', __name__)

@pagamento_interface.route('/pagamento/interface/<int:show_id>', methods = ['GET'])
def pagamento_interface_generator(show_id):
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
        
        quantidade = show_especifico_quantidade_request(show_id)

        print(quantidade)
        
    except Exception as ex:
        print(f"erro pagamento: {ex}")
        return redirect(url_for('login.login_generator'))
    
    return render_template('pagamento_tela.html', quantidade=quantidade)