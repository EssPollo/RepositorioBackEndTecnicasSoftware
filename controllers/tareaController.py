from flask import Flask, request, jsonify, Blueprint
from models.tarea import Tarea
from dtos.tareasDTO import TareasDTO
from configDataBase import db

tarea_blueprint = Blueprint('tarea', __name__)

@tarea_blueprint.route('/api/tareas/guardar', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        tarea_dto = TareasDTO(data['titulo'], data['descripcion'], data['fecha_entrega'], data['prioridad'], data['tiempo'])
        tarea = Tarea(titulo=tarea_dto.titulo, descripcion=tarea_dto.descripcion, fecha_entrega=tarea_dto.fecha_entrega, prioridad=tarea_dto.prioridad, tiempo=tarea_dto.tiempo)
        db.session.add(tarea)
        db.session.commit()
        return jsonify(tarea.titulo)
    except Exception as e:
        return jsonify(error=str(e)), 400

@tarea_blueprint.route('/api/tarea/obtenerTodos', methods=['GET'])
def get_all_tasks():
    try:
        tareas = Tarea.query.all()
        return jsonify([tarea.obtenerTodos() for tarea in tareas])
    except Exception as e:
        return jsonify(error=str(e)), 400

@tarea_blueprint.route('/api/tarea/obtenerPorId/<int:id>', methods=['GET'])
def get_task_by_id(id):
    try:
        tarea = Tarea.query.get(id)
        if tarea is None:
            return jsonify(error="Tarea no encontrada"), 404
        return jsonify(tarea.obtenerPorId())
    except Exception as e:
        return jsonify(error=str(e)), 400

@tarea_blueprint.route('/api/tarea/actualizar/<int:id>', methods=['PUT'])
def update_task(id):
    try:
        data = request.get_json()
        tarea = Tarea.query.get(id)
        if tarea is None:
            return jsonify(error="Tarea no encontrada"), 404
        tarea.titulo = data['titulo']
        tarea.descripcion = data['descripcion']
        tarea.fecha_entrega = data['fecha_entrega']
        tarea.prioridad = data['prioridad']
        tarea.tiempo = data['tiempo']
        db.session.commit()
        return jsonify(tarea.titulo)
    except Exception as e:
        return jsonify(error=str(e)), 400

@tarea_blueprint.route('/api/tarea/eliminar/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        tarea = Tarea.query.get(id)
        if tarea is None:
            return jsonify(error="Tarea no encontrada"), 404
        db.session.delete(tarea)
        db.session.commit()
        return jsonify(tarea.titulo)
    except Exception as e:
        return jsonify(error=str(e)), 400
