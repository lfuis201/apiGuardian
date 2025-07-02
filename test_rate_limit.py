import requests
import concurrent.futures

# Configuración del endpoint
url = "http://localhost:8000/api/auth/login/"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
data = {
    "username": "admin",
    "password": "contraseña_incorrecta"
}

# Función para un intento de login
def attempt_login(i):
    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"Intento {i}: {response.status_code}")
        try:
            print("Respuesta:", response.json())
        except Exception:
            print("Respuesta no es JSON.")
    except Exception as e:
        print(f"Error en el intento {i}: {e}")

# Ejecutar múltiples intentos en paralelo
if __name__ == "__main__":
    num_intentos = 10  # Supera el límite configurado en AXES_FAILURE_LIMIT

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(attempt_login, i + 1) for i in range(num_intentos)]
        concurrent.futures.wait(futures)
