import requests
import concurrent.futures

url = "http://localhost:8000/api/users/create-manager/"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    # "Authorization": "Bearer <tu_token_aquí>",  # Descomenta si usas JWT
}

data = {
    "username": "test_manager",
    "email": "manager@example.com",
    "password": "Password123!"
}

def attempt_create_manager(i):
    try:
        response = requests.post(url, json=data, headers=headers)
        status_code = response.status_code
        print(f"Intento {i}: Status {status_code}")
        
        try:
            json_data = response.json()
            if status_code == 429:
                print(f"[Intento {i}] 🚫 Bloqueado por rate limit: {json_data.get('detail')}")
            elif status_code == 201:
                print(f"[Intento {i}] ✅ Manager creado: {json_data.get('detail')}")
            elif status_code == 400:
                print(f"[Intento {i}] ⚠️ Error de validación: {json_data}")
            else:
                print(f"[Intento {i}] 📄 Respuesta: {json_data}")
        except ValueError:
            print(f"[Intento {i}] ❌ Respuesta no es JSON. Texto crudo:\n{response.text}")

    except Exception as e:
        print(f"[Intento {i}] ❌ Error de red o conexión: {e}")

if __name__ == "__main__":
    num_intentos = 10  # Supera el límite de 5/m para probar
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(attempt_create_manager, i + 1) for i in range(num_intentos)]
        concurrent.futures.wait(futures)
