from werkzeug.security import generate_password_hash, check_password_hash #Criar senha hash (Segurança)
from app.repositories.user_repository import create_user, check_login_user
from email_validator import validate_email, EmailNotValidError


def register_user(email:str, password: str):
    #senha hash (aleatoria), para privacidade e criptografia
        password_hash = generate_password_hash(password)
        create_user(email, password_hash)
        return True
    

def email_verification(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False
    
def login_user(email:str, password: str):
    pass_hash = check_login_user(email)
    return check_password_hash(pass_hash[0], password)
