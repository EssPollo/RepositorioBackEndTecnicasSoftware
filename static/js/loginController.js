document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('btnEntrar').addEventListener('click', function(event) {
        event.preventDefault();
        var userData = {
            correo: document.getElementById('correo').value,
            contrasena: document.getElementById('contrasena').value       
        };
    
        // Imprime los datos del usuario en la consola
        console.log('Datos del usuario:', userData);
    
        fetch('http://127.0.0.1:5000/usuario_blueprint/api/usuario/obtenerPorCorreoyContrasena', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        })
        .then(response => {
            console.log('Respuesta del servidor:', response);
            if (!response.ok) {
                throw new Error('Usuario no encontrado');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            // Redirige al usuario a index.html
            window.location.href = '/index';
        })
        .catch((error) => {
            // Aquí puedes manejar el error, mostrar un mensaje, etc.
            console.error('Error:', error);
            alert('Usuario no encontrado');
        });
    });
    });
    