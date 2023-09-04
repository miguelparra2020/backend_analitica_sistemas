import httpx
import asyncio

# Lista de objetos a enviar por POST
objetos = [
   




    # Agrega más objetos aquí si los tienes
]

# URL de la endpoint donde enviar los objetos
url = "https://backend-analitica-sistemas.onrender.com/estadistica/"

# Función asincrónica para enviar objetos
async def enviar_objetos():
    async with httpx.AsyncClient() as client:
        for objeto in objetos:
            try:
                response = await client.post(url, json=objeto)
                response.raise_for_status()  # Verifica si hay errores en la solicitud
                print(f"Objeto enviado con éxito: {objeto}")
            except httpx.HTTPError as e:
                print(f"Error al enviar objeto: {e}")

# Ejecutar la función asincrónica
if __name__ == "__main__":
    asyncio.run(enviar_objetos())
