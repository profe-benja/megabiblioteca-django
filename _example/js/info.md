En JavaScript, puedes guardar el token de sesión de un usuario utilizando diferentes métodos, dependiendo de tus necesidades y del entorno en el que estés trabajando (por ejemplo, en un navegador web o en una aplicación móvil).

1. **Cookies**:

   Puedes almacenar el token como una cookie en el navegador del usuario. Esto te permitirá enviar automáticamente el token con cada solicitud HTTP.

   ```javascript
   // Establecer la cookie
   document.cookie = "token=valor_del_token; path=/";
   ```

   Para leer la cookie:

   ```javascript
   const token = document.cookie.replace(/(?:(?:^|.*;\s*)token\s*=\s*([^;]*).*$)|^.*$/, "$1");
   ```

2. **LocalStorage**:

   Puedes guardar el token en el `localStorage` del navegador. Ten en cuenta que el `localStorage` es persistente y no se elimina cuando se cierra el navegador.

   ```javascript
   // Guardar el token
   localStorage.setItem('token', 'valor_del_token');

   // Obtener el token
   const token = localStorage.getItem('token');
   ```

3. **SessionStorage**:

   Similar a `localStorage`, pero los datos en `sessionStorage` se eliminan cuando se cierra la ventana del navegador.

   ```javascript
   // Guardar el token
   sessionStorage.setItem('token', 'valor_del_token');

   // Obtener el token
   const token = sessionStorage.getItem('token');
   ```

Recuerda que, al trabajar con tokens de sesión, es importante asegurarse de utilizar prácticas seguras, como enviar el token a través de HTTPS y evitar la exposición a ataques de tipo XSS (Cross-Site Scripting).

Además, si estás construyendo una aplicación web, te recomiendo considerar el uso de bibliotecas o frameworks como React, Angular o Vue.js, que tienen herramientas y patrones específicos para la gestión de autenticación y tokens. También, si estás construyendo una API, asegúrate de manejar la autenticación de forma segura, por ejemplo, utilizando JWT (JSON Web Tokens) u otros métodos de autenticación segura.
