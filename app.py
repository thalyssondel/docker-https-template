from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meu Site Python</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f4f4f9; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Olá! Este é um servidor Flask rodando com HTTPS via Docker.</h1>
        <p>A configuração do Nginx + Let's Encrypt está funcionando corretamente!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Roda a aplicação (em produção usaremos o Gunicorn via Dockerfile)
    app.run(host='0.0.0.0', port=8080)