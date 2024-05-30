from flask import Flask,request,jsonify,Blueprint
from models.usuario import Usuario
from dtos.usuarioDTO import UsuarioDTO
from models.configDataBase import db
  
usuario_blueprint = Blueprint('usuario', __name__)

@usuario_blueprint.route('/api/usuario/guardar', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        usuario_dto = UsuarioDTO(data['nombre'], data['apellidoP'], data['apellidoM'], data['correo'], data['contrasena'])
        usuario = Usuario(nombre=usuario_dto.nombre, apellidoP=usuario_dto.apellidoP, apellidoM=usuario_dto.apellidoM, correo=usuario_dto.correo, contrasena=usuario_dto.contrasena)
        db.session.add(usuario)
        db.session.commit()  
        return jsonify("Usuario guardado exitosamente"),200
    except Exception as e:
        return jsonify("Error al guardar al usuario por el motivo: " + str(e)),400

@usuario_blueprint.route('/api/usuario/obtenerTodos', methods=['GET'])
def get_all_user():
    try:
        usuarios = Usuario.query.all()
        return jsonify([usuario.obtenerTodos() for usuario in usuarios]),200
    except Exception as e:
        return jsonify(error = str(e)),400

@usuario_blueprint.route('/api/usuario/obtenerPorId/<int:id>', methods=['GET'])
def get_user_id(id):
    try:
        usuario = Usuario.query.get(id)
        if usuario is None:
            return jsonify(error="Usuario no encontrado"), 404
        return jsonify(usuario.obtenerPorId())
    except Exception as e:
        return jsonify(error=str(e)), 400

@usuario_blueprint.route('/api/usuario/actualizar/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.get_json()
        usuario = Usuario.query.get(id)
        if usuario is None:
            return jsonify(error="Usuario no encontrado"), 404
        usuario.nombre = data['nombre']
        usuario.apellidoP = data['apellidoP']
        usuario.apellidoM = data['apellidoM']
        usuario.correo = data['correo']
        usuario.contrasena = data['contrasena']
        db.session.commit()
        return jsonify(usuario.nombre)
    except Exception as e:
        return jsonify(error=str(e)), 400
    
@usuario_blueprint.route('/api/usuario/eliminar/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        usuario = Usuario.query.get(id)
        if usuario is None:
            return jsonify(error="Usuario no encontrado"), 404
        db.session.delete(usuario)
        db.session.commit()
        return jsonify(usuario.nombre)
    except Exception as e:
        return jsonify(error=str(e)), 400 

@usuario_blueprint.route('/api/usuario/obtenerPorCorreoyContrasena', methods=['POST']) 
def get_user_correo_contrasena():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')

    try:
        usuario = Usuario.query.filter_by(correo=correo,contrasena=contrasena).first()
        if usuario is None:
            return jsonify(error="Usuario no encontrado"), 404
        return jsonify("usuario encontrado"),200
    except Exception as e:
        return jsonify(error=str(e)), 400  
    
