import unittest
import os
import sys

# Añade el directorio raíz del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import json
from models.configDataBase import db
from models.usuario import Usuario
from main import app

class UsuarioControllerTestCase(unittest.TestCase):
    def setUp(self):
        # Configuración del entorno de prueba
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Limpieza después de cada prueba
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        # Prueba de la creación de un nuevo usuario
        usuario_data = {
            'nombre': 'John',
            'apellidoP': 'Doe',
            'apellidoM': 'Smith',
            'correo': 'john.doe@example.com',
            'contrasena': 'password123'
        }
        response = self.app.post('/usuario_blueprint/api/usuario/guardar', data=json.dumps(usuario_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Usuario guardado exitosamente", response.data)

    def test_get_all_user(self):
        # Prueba para obtener todos los usuarios
        response = self.app.get('/usuario_blueprint/api/usuario/obtenerTodos')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id(self):
        # Prueba para obtener un usuario por ID
        usuario = Usuario(nombre='Jane', apellidoP='Doe', apellidoM='Smith', correo='jane.doe@example.com', contrasena='password123')
        with app.app_context():
            db.session.add(usuario)
            db.session.commit()

        response = self.app.get(f'/usuario_blueprint/api/usuario/obtenerPorId/{usuario.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jane', response.data)

    def test_update_user(self):
        # Prueba para actualizar un usuario existente
        usuario = Usuario(nombre='Jane', apellidoP='Doe', apellidoM='Smith', correo='jane.doe@example.com', contrasena='password123')
        with app.app_context():
            db.session.add(usuario)
            db.session.commit()

        updated_data = {
            'nombre': 'Janet',
            'apellidoP': 'Doe',
            'apellidoM': 'Smith',
            'correo': 'janet.doe@example.com',
            'contrasena': 'newpassword123'
        }
        response = self.app.put(f'/usuario_blueprint/api/usuario/actualizar/{usuario.id}', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Janet', response.data)

    def test_delete_user(self):
        # Prueba para eliminar un usuario
        usuario = Usuario(nombre='Jane', apellidoP='Doe', apellidoM='Smith', correo='jane.doe@example.com', contrasena='password123')
        with app.app_context():
            db.session.add(usuario)
            db.session.commit()

        response = self.app.delete(f'/usuario_blueprint/api/usuario/eliminar/{usuario.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Jane', response.data)

    def test_get_user_by_email_and_password(self):
        # Prueba para obtener un usuario por correo y contraseña
        usuario = Usuario(nombre='Jane', apellidoP='Doe', apellidoM='Smith', correo='jane.doe@example.com', contrasena='password123')
        with app.app_context():
            db.session.add(usuario)
            db.session.commit()

        data = {'correo': 'jane.doe@example.com', 'contrasena': 'password123'}
        response = self.app.post('/usuario_blueprint/api/usuario/obtenerPorCorreoyContrasena', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'usuario encontrado', response.data)

if __name__ == '__main__':
    unittest.main()
