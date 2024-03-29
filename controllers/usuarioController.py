from flask import Flask,request,jsonify,Blueprint
from models.usuario import Usuario
from dtos.usuarioDTO import UsuarioDTO
from configDataBase import db
  
usuario_blueprint = Blueprint('usuario', __name__)

@usuario_blueprint.route('/api/usuario/guardar', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        usuario_dto = UsuarioDTO(data['nombre'], data['apellidoP'], data['apellidoM'], data['correo'], data['contrasena'])
        usuario = Usuario(nombre=usuario_dto.nombre, apellidoP=usuario_dto.apellidoP, apellidoM=usuario_dto.apellidoM, correo=usuario_dto.correo, contrasena=usuario_dto.contrasena)
        db.session.add(usuario)
        db.session.commit()
                
        return jsonify(usuario.nombre)
    except Exception as e:
        return jsonify(error = str(e)),400
