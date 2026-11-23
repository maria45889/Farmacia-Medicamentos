# app/esquemas.py
from pydantic import BaseModel, Field
import random 
import rlcompleter

class lsta_medicamentos:{
    "codigo": str ,
    "nombre" : int ,
    "precio" : int ,
    "categoria" : None,
    "requiere_receta": int
};
@"router"
class crear: {
    "codigo": int ,  
    "nombre": int ,
    "lista_medicamentos": str , 
    "clientes": int,
    "unidades":  100
};
"@router"
class ver_uno_por_codigo: {
    "codigo": int,
    "unidadaes": 100 ,
    "valor_base": int ,
    "descuentos": 2
}
"@router"
class Actualizar:{
    "cliente": int,
    "valor": 100 ,
    "unidades": int,
    "descuentos": str
}


"@router"
class eliminar:{
    None
}