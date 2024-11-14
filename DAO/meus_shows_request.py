from flask import request
from database.database import Meus_shows

def PegarMeusShows(usuario_id, show_id):
    MeuShow = Meus_shows.query.filter_by(usuario_id=usuario_id, show_id=show_id).first()
    return MeuShow

def meus_shows(usuario_id):
    meus_shows =   Meus_shows.query.filter_by(usuario_id=usuario_id).all()
    return meus_shows