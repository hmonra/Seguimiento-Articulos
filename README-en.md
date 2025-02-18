# Personalized Product Tracking

Tired of searching for that component that is always out of stock? This Telegram bot will save your life!

## ✨ Features ✨

*   **Smart Search:** Enter the product link and the bot will track it for you.
*   **Personalized Alerts:** Receive notifications directly in Telegram when the product is back in stock.
*   **Product Types:** Choose between "Used" or "Refurbished" to refine your search.
*   **Easy to Use:** Simple commands and an intuitive interface so you don't waste time.

## ⚙️ Installation ⚙️

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/hmonra/Seguimiento-Articulos.git](https://github.com/hmonra/Seguimiento-Articulos.git)
    ```

2. **Virtual Environment (Recommended):**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```

3. **Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configuration:**

    * Modify the `config.py` file and add your Telegram token:

        ```python
        telegram_token = "YOUR_TELEGRAM_TOKEN"
        ```
    * Modify the `config.py` file and add your Telegram ID:

        ```python
        id_canal = "YOUR_ID"
        ```

5. **Let's run!:**

    ```bash
    python main.py
    ```

## Usage

1. Search for the bot on Telegram and join it.
2. `/start`: Start the bot.
3. `/alta`: Register a product for tracking.
4. `/avisos`: Check your active alerts.

## Contribution

We would love to receive your ideas and improvements! Open an "issue" or send a "pull request" if you want to collaborate.

## License

This project is under the MIT license.

## ❓ Frequently Asked Questions ❓

*   **How do I get my Telegram token?**

    * Talk to BotFather on Telegram and follow his instructions.

*   **What if the bot doesn't find the product?**

    * Make sure the link is correct and the product exists on PC Componentes.

*   **Can I use the bot for other websites?**

    * No, this bot is specifically designed for PC Componentes.

## Start tracking your favorite products!