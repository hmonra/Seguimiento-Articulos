#  Seguimiento de productos personalizado

¿Cansado de buscar ese componente que siempre está agotado? ¡Este bot de Telegram te salvará la vida! 

## ✨ Funcionalidades ✨

*   **Búsqueda Inteligente:** Ingresa el enlace del producto y el bot lo rastreará por ti.
*   **Alertas Personalizadas:** Recibe notificaciones directamente en Telegram cuando el producto vuelva a estar en stock.
*   **Tipos de Producto:** Elige entre "Seminuevo" o "Reacondicionado" para afinar tu búsqueda.
*   **Fácil de Usar:** Comandos sencillos y una interfaz intuitiva para que no pierdas tiempo.

## ⚙️ Instalación ⚙️

1.  **Clona el repositorio:**

    ```bash
    git clone [https://github.com/hmonra/Seguimiento-Articulos.git](https://github.com/hmonra/Seguimiento-Articulos.git)
    ```

2.  **Entorno Virtual (Recomendado):**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3.  **Dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuración:**

    *   Modifica el archivo `config.py` y añade tu token de Telegram:

        ```python
        telegram_token = "TU_TOKEN_DE_TELEGRAM"
        ```
	*   Modifica el archivo `config.py` y añade tu id de Telegram:

        ```python
        id_canal = "TU_ID"
        ```

5.  **¡A correr!:**

    ```bash
    python main.py
    ```

##  Uso 

1.  Busca el bot en Telegram y únete a él.
2.  `/start`: Inicia el bot.
3.  `/alta`: Da de alta un producto para seguimiento.
4.  `/avisos`: Consulta tus avisos activos.

##  Contribución 

¡Nos encantaría recibir tus ideas y mejoras! Abre un "issue" o envía un "pull request" si quieres colaborar.

##  Licencia 

Este proyecto está bajo la licencia MIT.

## ❓ Preguntas Frecuentes ❓

*   **¿Cómo obtengo mi token de Telegram?**

    *   Habla con BotFather en Telegram y sigue sus instrucciones.

*   **¿Qué hago si el bot no encuentra el producto?**

    *   Asegúrate de que el enlace sea correcto y que el producto exista en PC Componentes.

*   **¿Puedo usar el bot para otros sitios web?**

    *   No, este bot está diseñado específicamente para PC Componentes.

##  ¡Empieza a rastrear tus productos favoritos!