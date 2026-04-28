def login(username, password):
    if username == "admin" and password == "12345":
        return True
    return False

def logout():
    print("Вы вышли из системы")

def check_auth(token):
    return token is not None    if username == "admin" and password == "12345":
        return True
    return False
