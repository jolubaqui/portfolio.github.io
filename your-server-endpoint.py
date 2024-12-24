from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/your-server-endpoint', methods=['POST'])
def receive_data():
    data = request.get_json()
    # Procesa los datos aquí
    return jsonify({"message": "Datos recibidos correctamente", "data": data})

if __name__ == '__main__':
    app.run(debug=True)
    def send_email(data):
        sender_email = "your-email@example.com"
        receiver_email = "jolubaqui.developer@hotmail.com"
        password = "your-email-password"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Datos recibidos"
        message["From"] = sender_email
        message["To"] = receiver_email

        text = f"Datos recibidos:\n{data}"
        part = MIMEText(text, "plain")
        message.attach(part)

        with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    @app.route('/your-server-endpoint', methods=['POST'])
    def receive_data():
        data = request.get_json()
        send_email(data)
        return jsonify({"message": "Datos recibidos correctamente", "data": data})