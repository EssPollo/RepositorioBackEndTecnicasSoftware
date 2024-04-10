#get_all_user, get_user_id, update_user, delete_user, get_user_correo_contrasena
import requests
import pytest

@pytest.mark.parametrize("nombre, apellidoP, apellidoM, correo, contraseña, mensaje", [
    ( 'Luisa', 'Ramirez','alcantara','luisa@gmail','1234', 'Usuario guardado exitosamente'),
    ('brad', 'Juarez','Moreno','brad@gmail','1234', 'Usuario guardado exitosamente'),
    ('Maria', 'Sair','Navarro','maria@gmail','abc', 'Usuario guardado exitosamente'),
    (None, 10,"Navarrete","alan@gmail","1234", "Error al guardar al usuario"),
])

def test_create_user(nombre, apellidoP, apellidoM, correo, contraseña, mensaje):
    url= 'http://127.0.0.1:5000/usuario_blueprint/api/usuario/guardar'
    data = {'nombre': nombre, 'apellidoP': apellidoP, 'apellidoM': apellidoM, 'correo': correo, 'contraseña': contraseña}
    x= requests.post(url, json=data)
    print(x.text)
    assert x.status_code == 400

    #Primero debo crear un armado de un post
    #create post en pyhton