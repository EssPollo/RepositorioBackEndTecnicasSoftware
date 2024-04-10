document.addEventListener('DOMContentLoaded', (event) => {
document.getElementById('registerButton').addEventListener('click', function(event) {
    event.preventDefault();
    var userData = {
        nombre: document.getElementById('nombre').value,
        apellidoP: document.getElementById('apellidoP').value,
        apellidoM: document.getElementById('apellidoM').value,
        correo: document.getElementById('correo').value,
        contrasena: document.getElementById('contrasena').value
    };

    // Imprime los datos del usuario en la consola
    console.log('Datos del usuario:', userData);

    fetch('/usuario_blueprint/api/usuario/guardar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en el registro');
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        // Redirige al usuario a index.html
        window.location.href = '/./templates/login.html';
    })
    .catch((error) => {
        console.error('Error:', error);
        // Aquí puedes manejar el error, mostrar un mensaje, etc.
    });
});
});
