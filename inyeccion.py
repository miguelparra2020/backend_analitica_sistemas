import httpx
import asyncio

# Lista de objetos a enviar por POST
objetos = [
{"id":	1	,"nombre":"	Producto 1	","descripcion":"	Descripción 1	","precio":"	60000	"}	,
{"id":	2	,"nombre":"	Producto 2	","descripcion":"	Descripción 2	","precio":"	60001	"}	,
{"id":	3	,"nombre":"	Producto 3	","descripcion":"	Descripción 3	","precio":"	60002	"}	,
{"id":	4	,"nombre":"	Producto 4	","descripcion":"	Descripción 4	","precio":"	60003	"}	,
{"id":	5	,"nombre":"	Producto 5	","descripcion":"	Descripción 5	","precio":"	60004	"}	,
{"id":	6	,"nombre":"	Producto 6	","descripcion":"	Descripción 6	","precio":"	60005	"}	,
{"id":	7	,"nombre":"	Producto 7	","descripcion":"	Descripción 7	","precio":"	60006	"}	,
{"id":	8	,"nombre":"	Producto 8	","descripcion":"	Descripción 8	","precio":"	60007	"}	,
{"id":	9	,"nombre":"	Producto 9	","descripcion":"	Descripción 9	","precio":"	60008	"}	,
{"id":	10	,"nombre":"	Producto 10	","descripcion":"	Descripción 10	","precio":"	60009	"}	,
{"id":	11	,"nombre":"	Producto 11	","descripcion":"	Descripción 11	","precio":"	60010	"}	,
{"id":	12	,"nombre":"	Producto 12	","descripcion":"	Descripción 12	","precio":"	60011	"}	,
{"id":	13	,"nombre":"	Producto 13	","descripcion":"	Descripción 13	","precio":"	60012	"}	,
{"id":	14	,"nombre":"	Producto 14	","descripcion":"	Descripción 14	","precio":"	60013	"}	,
{"id":	15	,"nombre":"	Producto 15	","descripcion":"	Descripción 15	","precio":"	60014	"}	,
{"id":	16	,"nombre":"	Producto 16	","descripcion":"	Descripción 16	","precio":"	60015	"}	,
{"id":	17	,"nombre":"	Producto 17	","descripcion":"	Descripción 17	","precio":"	60016	"}	,
{"id":	18	,"nombre":"	Producto 18	","descripcion":"	Descripción 18	","precio":"	60017	"}	,
{"id":	19	,"nombre":"	Producto 19	","descripcion":"	Descripción 19	","precio":"	60018	"}	,
{"id":	20	,"nombre":"	Producto 20	","descripcion":"	Descripción 20	","precio":"	60019	"}	,
{"id":	21	,"nombre":"	Producto 21	","descripcion":"	Descripción 21	","precio":"	60020	"}	,
{"id":	22	,"nombre":"	Producto 22	","descripcion":"	Descripción 22	","precio":"	60021	"}	,
{"id":	23	,"nombre":"	Producto 23	","descripcion":"	Descripción 23	","precio":"	60022	"}	,
{"id":	24	,"nombre":"	Producto 24	","descripcion":"	Descripción 24	","precio":"	60023	"}	,
{"id":	25	,"nombre":"	Producto 25	","descripcion":"	Descripción 25	","precio":"	60024	"}	,
{"id":	26	,"nombre":"	Producto 26	","descripcion":"	Descripción 26	","precio":"	60025	"}	,
{"id":	27	,"nombre":"	Producto 27	","descripcion":"	Descripción 27	","precio":"	60026	"}	,
{"id":	28	,"nombre":"	Producto 28	","descripcion":"	Descripción 28	","precio":"	60027	"}	,
{"id":	29	,"nombre":"	Producto 29	","descripcion":"	Descripción 29	","precio":"	60028	"}	,
{"id":	30	,"nombre":"	Producto 30	","descripcion":"	Descripción 30	","precio":"	60029	"}	,
{"id":	31	,"nombre":"	Producto 31	","descripcion":"	Descripción 31	","precio":"	60030	"}	,
{"id":	32	,"nombre":"	Producto 32	","descripcion":"	Descripción 32	","precio":"	60031	"}	,
{"id":	33	,"nombre":"	Producto 33	","descripcion":"	Descripción 33	","precio":"	60032	"}	,
{"id":	34	,"nombre":"	Producto 34	","descripcion":"	Descripción 34	","precio":"	60033	"}	,
{"id":	35	,"nombre":"	Producto 35	","descripcion":"	Descripción 35	","precio":"	60034	"}	,
{"id":	36	,"nombre":"	Producto 36	","descripcion":"	Descripción 36	","precio":"	60035	"}	,
{"id":	37	,"nombre":"	Producto 37	","descripcion":"	Descripción 37	","precio":"	60036	"}	,
{"id":	38	,"nombre":"	Producto 38	","descripcion":"	Descripción 38	","precio":"	60037	"}	,
{"id":	39	,"nombre":"	Producto 39	","descripcion":"	Descripción 39	","precio":"	60038	"}	,
{"id":	40	,"nombre":"	Producto 40	","descripcion":"	Descripción 40	","precio":"	60039	"}	,
{"id":	41	,"nombre":"	Producto 41	","descripcion":"	Descripción 41	","precio":"	60040	"}	,
{"id":	42	,"nombre":"	Producto 42	","descripcion":"	Descripción 42	","precio":"	60041	"}	,
{"id":	43	,"nombre":"	Producto 43	","descripcion":"	Descripción 43	","precio":"	60042	"}	,
{"id":	44	,"nombre":"	Producto 44	","descripcion":"	Descripción 44	","precio":"	60043	"}	,
{"id":	45	,"nombre":"	Producto 45	","descripcion":"	Descripción 45	","precio":"	60044	"}	,
{"id":	46	,"nombre":"	Producto 46	","descripcion":"	Descripción 46	","precio":"	60045	"}	,
{"id":	47	,"nombre":"	Producto 47	","descripcion":"	Descripción 47	","precio":"	60046	"}	,
{"id":	48	,"nombre":"	Producto 48	","descripcion":"	Descripción 48	","precio":"	60047	"}	,
{"id":	49	,"nombre":"	Producto 49	","descripcion":"	Descripción 49	","precio":"	60048	"}	,
{"id":	50	,"nombre":"	Producto 50	","descripcion":"	Descripción 50	","precio":"	60049	"}	,


    # Agrega más objetos aquí si los tienes
]

# URL de la endpoint donde enviar los objetos
url = "https://backend-github-8thk.onrender.com/productos/"

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
