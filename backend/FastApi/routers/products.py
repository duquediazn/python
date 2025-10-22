from fastapi import APIRouter

# Si definimos "prefix" con "/products", no hará falta indicarlo en la ruta en la definición de las rutas.
# Si definimos "responses", podemos indicar la respuesta por defecto en caso de error. 
router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404:{"message":"No encontrado"}}) 

product_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
    return product_list

@router.get("/{id}")
async def products(id: int):
    return  product_list[id]
