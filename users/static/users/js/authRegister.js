// Función para obtener el token CSRF de las cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Comprueba si esta cookie comienza con el nombre dado
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

document.getElementById('registerForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const username = document.getElementById('regUsername').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('regPassword').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  // Validación de que las contraseñas coincidan
  if (password !== confirmPassword) {
      alert("Las contraseñas no coinciden");
      return;
  }

  // Obtener el token CSRF
  const csrftoken = getCookie('csrftoken');

  // Enviar la solicitud de registro
  fetch('http://127.0.0.1:8000/api/users/register/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,  // Incluir el token CSRF en las cabeceras
      },
      body: JSON.stringify({
          username: username,
          email: email,
          password: password
      }),
  })
  .then(response => response.json())
  .then(data => {
      if (data.username) {
          console.log('Registro exitoso:', data);
          alert('Usuario registrado exitosamente.');
          // Redirigir al login
          window.location.href = '/api/users/index/';
      } else {
          console.error('Error al registrar:', data);
          alert('Error al registrar el usuario.');
      }
  })
  .catch(error => console.error('Error:', error));
});
