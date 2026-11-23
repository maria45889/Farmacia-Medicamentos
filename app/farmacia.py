@router.get("", response_model=list[farmacia])
def lista_medicamentos {
    "codigo": str ,
    "nombre" : int ,
    "precio" : int ,
    "categoria" : None,
    "requiere_receta": int
};

@router.post("", response_model=Medicamneto, status_code=status.HTTP_201_CREATED)
def crear {
    "codigo": int ,  
    "nombre": int ,
    "lista_medicamentos": str , 
    "clientes": int,
    "unidades":  100
};
    

@router.get("/{codigo}", response_model= farmacia)
def ver_uno_por_codigo {
    "codigo": int,
    "unidadaes": 100 ,
    "valor_base": int ,
    "descuentos": 2
}


@router.put("/{codigo}", response_model=farmacia)
def Actualizar {
    "cliente": int,
    "valor": 100 ,
    "unidades": int,
    "descuentos": str
    }

@router.delete("/{codigo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_medicamento(Farmaica: eliminar_medicamento) -> None:
    Farmaica.remove(eliminar_medicamento) 