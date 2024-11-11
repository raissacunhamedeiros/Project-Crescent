from flask import request
from database.database import MeusShows, sh

def PegarMeusShows(show_id):
    MeuShow = MeusShows.query.get(show_id)
    return MeuShow