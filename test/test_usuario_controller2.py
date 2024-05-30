import unittest
import os
import sys
from parameterized import parameterized

# Añade el directorio raíz del proyecto a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import json
from models.configDataBase import db
from models.usuario import Usuario
from dtos.usuarioDTO import UsuarioDTO
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

    @parameterized.expand([
        ('John', 'Doe', 'Smith', 'john.doe@example.com', 'password123'),
        ('Alice', 'Brown', 'Johnson', 'alice.brown@example.com', 'securepass'),
        ('Bob', 'White', 'Davis', 'bob.white@example.com', 'anotherpass')
    ])
    def test_create_user(self, nombre, apellidoP, apellidoM, correo, contrasena):
        # Prueba de la creación de un nuevo usuario
        usuario_data = {
            'nombre': nombre,
            'apellidoP': apellidoP,
            'apellidoM': apellidoM,
            'correo': correo,
            'contrasena': contrasena
        }
        response = self.app.post('/usuario_blueprint/api/usuario/guardar', data=json.dumps(usuario_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Usuario guardado exitosamente", response.data)



    #--------------------------------------------
    @parameterized.expand([
        ('Jane', 'Doe', 'Smith', 'jane.doe@example.com', 'password123'),
        ('Tom', 'Clark', 'Evans', 'tom.clark@example.com', 'tomspass')
    ])

    
    def test_get_user_by_id(self, nombre, apellidoP, apellidoM, correo, contrasena):
        # Prueba para obtener un usuario por ID
        usuario = Usuario(nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, correo=correo, contrasena=contrasena)
        with app.app_context():
            db.session.add(usuario)
            db.session.commit()

            response = self.app.get(f'/usuario_blueprint/api/usuario/obtenerPorId/{usuario.id}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(nombre.encode(), response.data)
    #--------------------------------------------

    @parameterized.expand([
        ('Jane', 'Doe', 'Smith', 'jane.doe@example.com', 'password123', 'Janet', 'Doe', 'Smith', 'janet.doe@example.com', 'newpassword123'),
        ('Tom', 'Clark', 'Evans', 'tom.clark@example.com', 'tomspass', 'Tommy', 'Clark', 'Evans', 'tommy.clark@example.com', 'newtompass')
    ])
    def test_update_user(self, nombre, apellidoP, apellidoM, correo, contrasena, updated_nombre, updated_apellidoP, updated_apellidoM, updated_correo, updated_contrasena):
        # Prueba para actualizar un usuario existente
        usuario = Usuario(nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, correo=correo, contrasena=contrasena)
        with app.app_context():
            db.session.add(usuario)
            db.session.commit()

            updated_data = {
                'nombre': updated_nombre,
                'apellidoP': updated_apellidoP,
                'apellidoM': updated_apellidoM,
                'correo': updated_correo,
                'contrasena': updated_contrasena
            }
            response = self.app.put(f'/usuario_blueprint/api/usuario/actualizar/{usuario.id}', data=json.dumps(updated_data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertIn(updated_nombre.encode(), response.data)


    #--------------------------------------------------------------------------------------------

    @parameterized.expand([
        ('Jane', 'Doe', 'Smith', 'jane.doe@example.com', 'password123'),
        ('Tom', 'Clark', 'Evans', 'tom.clark@example.com', 'tomspass')
    ])
    def test_delete_user(self, nombre, apellidoP, apellidoM, correo, contrasena):
        # Prueba para eliminar un usuario
       # usuario = Usuario(nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, correo=correo, contrasena=contrasena)
        with app.app_context():
            usuario_dto = UsuarioDTO(nombre, apellidoP, apellidoM, correo, contrasena)
            usuario = Usuario(nombre=usuario_dto.nombre, apellidoP=usuario_dto.apellidoP, apellidoM=usuario_dto.apellidoM, correo=usuario_dto.correo, contrasena=usuario_dto.contrasena)
            print("nombre DTO: ", usuario_dto.nombre)
            print("nombre: ", usuario.nombre)         
            db.session.add(usuario)
            db.session.commit()
            print("usuario ID: ", usuario.id)
            response = self.app.delete(f'/usuario_blueprint/api/usuario/eliminar/{usuario.id}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(nombre.encode(), response.data)

    
    #--------------------------------------------

    @parameterized.expand([
        ('jane.doe@example.com', 'password123'),
        ('tom.clark@example.com', 'tomspass')
    ])
    def test_get_user_by_email_and_password(self, correo, contrasena):
        # Prueba para obtener un usuario por correo y contraseña
        usuario = Usuario(nombre='Jane', apellidoP='Doe', apellidoM='Smith', correo=correo, contrasena=contrasena)
        with app.app_context():
            db.session.add(usuario)
            db.session.commit()

        data = {'correo': correo, 'contrasena': contrasena}
        response = self.app.post('/usuario_blueprint/api/usuario/obtenerPorCorreoyContrasena', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'usuario encontrado', response.data)

    def test_get_all_user(self):
        # Prueba para obtener todos los usuarios
        response = self.app.get('/usuario_blueprint/api/usuario/obtenerTodos')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
