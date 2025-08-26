from config import db


class Tecnico:

    def get_percentagem_tecnico(id_tecnico):
        
        data = db.child("users").child(id_tecnico).child("porcentagem").get().val()
        
        return data