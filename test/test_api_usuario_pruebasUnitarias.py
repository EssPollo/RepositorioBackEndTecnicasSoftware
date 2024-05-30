#from models.configDataBase import db
#from models.usuario import Usuario
import requests
import pytest

@pytest.mark.parametrize("nombre, apellidoP, apellidoM, correo, contraseña, statusCode", [
    ( 'Luisa', 'Ramirez','alcantara','luisa@gmail','1234', 200),
    ('brad', 'Juarez','Moreno','brad@gmail','1234', 200),
    ('Maria', 'Sair','Navarro','maria@gmail','abc', 200),
    (None, 10,"Navarrete","alan@gmail","1234",400),
])

def test_create_user(nombre, apellidoP, apellidoM, correo, contraseña, statusCode):
    url= 'http://127.0.0.1:5000/usuario_blueprint/api/usuario/guardar'
    data = {'nombre': nombre, 'apellidoP': apellidoP, 'apellidoM': apellidoM, 'correo': correo, 'contraseña': contraseña}
    x= requests.post(url, json=data)
    print(x.text)
    assert x.status_code == statusCode
    # usuario = db.session.query(Usuario).filter_by(nombre=nombre).first()
    # assert usuario is not None
    # assert usuario.nombre == nombre
    # assert usuario.apellidoP == apellidoP
    # assert usuario.apellidoM == apellidoM
    # assert usuario.correo == correo