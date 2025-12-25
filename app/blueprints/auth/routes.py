from flask import Blueprint, request, jsonify, render_template
from app.services.auth_service import register_user, email_verification
import psycopg

#Conjunto de rotas para flask
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


#rota do blueprint para enviar os dados de registro de novo usuario
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("")
    
    data = request.json
    email = data.get("email")
    password = data.get("password")
    

    if not email or not password:
        return jsonify({"error": "email e password obrigatórios"}), 400
    

    if not email_verification(email=email):
        return jsonify({"error": "Email Invalido"})
    

    #cria/valida user
    try:
        register_user(email=email, password=password)
        return jsonify({"message": "Usuário criado com sucesso"})
    except psycopg.errors.UniqueViolation:
        return jsonify({"error": "Usuário já existe"}), 409





@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "email e password obrigatórios"}), 400

    #busca a senha do usuario para validacao
    
    user = login_user(email)
    

    if not user:
        return jsonify({"error": "Credenciais inválidas"}), 401

    #faz a checagem do hash para validar
    if not check_password_hash(user[0], password):
        return jsonify({"error": "Credenciais inválidas"}), 401

    return jsonify({"message": "Login realizado com sucesso"}), 200