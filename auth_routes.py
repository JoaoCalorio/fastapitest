from fastapi import APIRouter  

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@auth_router.get("/")
async def autenticar():
    """
    Autenticação bem-sucedida!
    """
    return {"message": "Autenticação bem-sucedida!","autenticado": False}