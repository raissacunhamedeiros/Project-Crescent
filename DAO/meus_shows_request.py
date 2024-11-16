from flask import request
from database.database import db  # Certifique-se de que está usando o banco de dados correto
from database.database import meus_shows, Shows  # Importe os modelos corretamente

def PegarMeusShows(usuario_id, show_id):
    try:
        # Busca um registro específico com usuário e show relacionados
        meu_show = meus_shows.query.filter_by(usuario_id=usuario_id, show_id=show_id).first()
        return meu_show
    except Exception as ex:
        print(f"Erro ao buscar o show específico: {ex}")
        return None

def listar_shows_usuario(usuario_id):
    try:
        meus_show = meus_shows.query.filter_by(usuario_id=usuario_id).all()
        lista_shows = []

        for i in meus_show:
            show = Shows.query.get(i.show_id)
            lista_shows.append({
                'id': show.id,
                'title': show.title,
                'local': show.local,
                'description': show.description,
                'data': show.data,
                'quantidade_ingressos': i.quantidade_comprada
            })

        return lista_shows
    except Exception as ex:
        print(f"Erro ao listar os shows do usuário: {ex}")
        return []
