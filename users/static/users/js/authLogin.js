// Función para obtener el token CSRF de las cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Obtener el token CSRF
  const csrftoken = getCookie('csrftoken');

  fetch('http://127.0.0.1:8000/api/users/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-CSRFToken': csrftoken,  // Incluir el token CSRF en las cabeceras
    },
    body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`,
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Login failed');
    }
    return response.json();
  })
  .then(data => {
    if (data.token) {
      console.log('Login successful, token:', data.token);

      // Guarda el token en el localStorage o cookie para futuras peticiones
      localStorage.setItem('token', data.token);
    
      // Redirigir al Workspace después del login exitoso
      window.location.href = '/api/users/workspace/';
    } else {
      console.error('Error al iniciar sesión:', data);
      alert('Error al iniciar sesión. Verifica tus credenciales.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('Error al iniciar sesión. Verifica tus credenciales.');
  });
});
