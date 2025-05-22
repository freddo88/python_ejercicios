#programa que genera un token secreto
import secrets

token = secrets.token_hex(16)   
print(f"Token secreto: {token}")
# Este código genera un token secreto de 32 caracteres hexadecimales (128 bits) utilizando la biblioteca `secrets` de Python.
