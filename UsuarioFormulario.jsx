import React, { useState } from 'react';

function UsuarioFormulario() {
  // Definimos el estado para almacenar los valores del formulario
  const [usuario, setUsuario] = useState({
    id: '',
    nombre: '',
    apellidoP: '',
    apellidoM: '',
    correo: '',
    contrasena: ''
  });

  // Función para manejar cambios en los campos del formulario
  const handleChange = (event) => {
    const { name, value } = event.target;
    setUsuario({ ...usuario, [name]: value });
  };

  // Función para manejar el envío del formulario
  const handleSubmit = (event) => {
    event.preventDefault();
    // Aquí podrías hacer algo con los datos del usuario, como enviarlos a un servidor
    console.log(usuario);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        ID:
        <input type="number" name="id" value={usuario.id} onChange={handleChange} />
      </label>
      <br />
      <label>
        Nombre:
        <input type="text" name="nombre" value={usuario.nombre} onChange={handleChange} />
      </label>
      <br />
      <label>
        Apellido Paterno:
        <input type="text" name="apellidoP" value={usuario.apellidoP} onChange={handleChange} />
      </label>
      <br />
      <label>
        Apellido Materno:
        <input type="text" name="apellidoM" value={usuario.apellidoM} onChange={handleChange} />
      </label>
      <br />
      <label>
        Correo:
        <input type="email" name="correo" value={usuario.correo} onChange={handleChange} />
      </label>
      <br />
      <label>
        Contraseña:
        <input type="password" name="contrasena" value={usuario.contrasena} onChange={handleChange} />
      </label>
      <br />
      <button type="submit">Enviar</button>
    </form>
  );
}

export default UsuarioFormulario;
