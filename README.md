Aquí tienes la información estructurada de forma continua y simplificada, ideal para copiar y pegar directamente en un documento de Word o Google Docs sin interrupciones visuales.

---

**Guía de Ejecución y Análisis del Script de Fuerza Bruta**

**1. Cómo ejecutar el programa**
Para poner en marcha el código, debes tener Python instalado y usar la terminal o consola de comandos. Los comandos principales son:
*   **Ejecución simple:** Escribe `python nombre_del_archivo.py`. El programa intentará adivinar la palabra "gaming" por defecto.
*   **Probar una palabra propia:** Escribe `python nombre_del_archivo.py tuclave`. El programa buscará "tuclave" usando letras minúsculas.
*   **Probar con números:** Escribe `python nombre_del_archivo.py 12345 digits`. El programa cambiará su base de datos a números para encontrar el objetivo más rápido.

**2. Ejemplos de lo que verás en pantalla (Salida)**
Si el programa tiene éxito, mostrará tres datos clave:
*   **Encontrada:** La confirmación de la palabra que estabas buscando.
*   **Intentos:** El número total de combinaciones que el procesador tuvo que generar y comparar antes de acertar.
*   **Tiempo:** Los segundos exactos (con decimales) que tomó el proceso. 
Por ejemplo, para una palabra de 4 letras, podrías ver 456,976 intentos en menos de un segundo. Para una de 6 letras, los intentos suben a 308 millones y el tiempo puede pasar a varios minutos dependiendo de la potencia de tu PC.

http://googleusercontent.com/image_content/115



**3. Reflexión sobre contraseñas complejas (8+ caracteres)**
El código proporcionado utiliza un alfabeto de 26 letras minúsculas. Si intentaras usarlo contra una contraseña de 8 caracteres que combine mayúsculas, números y símbolos, el programa se volvería extremadamente lento por las siguientes razones:

*   **Aumento del alfabeto:** Pasar de 26 letras a 94 caracteres posibles (incluyendo símbolos como @, #, $) hace que el número de combinaciones crezca de forma explosiva.
*   **La escala del tiempo:** Mientras que una palabra de 6 letras minúsculas tiene 308 millones de combinaciones, una de 8 caracteres con símbolos tiene más de 6,000 billones de combinaciones. 
*   **Limitación técnica:** Este código corre en un solo "hilo" del procesador. En un escenario real, una contraseña robusta de más de 10 caracteres tardaría décadas o siglos en ser descifrada por este método, lo que demuestra por qué la longitud y la variedad de caracteres son la mejor defensa en ciberseguridad.

---

**¿Te gustaría que añada una tabla comparativa de tiempos para que la incluyas en tu documento?**
