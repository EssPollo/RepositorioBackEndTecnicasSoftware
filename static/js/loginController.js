document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('btnEntrar').addEventListener('click', function(event) {
        event.preventDefault();
        var userData = {
            correo: document.getElementById('correo').value,
            contrasena: document.getElementById('contrasena').value       
        };
    
        // Imprime los datos del usuario en la consola
        console.log('Datos del usuario:', userData);
    
        fetch('/usuario_blueprint/api/usuario/obtenerPorCorreoyContrasena', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Usuario no encontrado');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            // Redirige al usuario a index.html
            window.location.href = '/../templates/index.html';
        })
        .catch((error) => {
            console.error('Error:', error);
            console.log('Usuario no encontrado');
            // Aquí puedes manejar el error, mostrar un mensaje, etc.
            alert('Usuario no encontrado');
        });
    });
    });
    