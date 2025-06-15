from pydantic import BaseModel
from typing import Optional

def factorial(n:int):
    if n <= 1:
        return 1
    return n*factorial(n-1)

def cammelCase(variable:str):
    palabrasSeparadas = variable.split()
    if not palabrasSeparadas:
        return ''
    
    primeraPalabra = palabrasSeparadas[0].lower()
    restoPalabras = [palabra.capitalize() for palabra in palabrasSeparadas[1:]]
    
    textoCamelCase = primeraPalabra + ''.join(restoPalabras)
    return textoCamelCase 

class Execution(BaseModel):
    order: str 
    x: Optional[str] = None
    y: Optional[str] = None
    timeCountDown: int 

def order(order: Execution):
    if order.order.lower() == "execute order 66" or order.order.lower() == "order 66" or order.order.lower() == "66":
        return {"message":"All troopers, Execute order 66"}
    elif order.x and order.y and "nuke" in order.order: 
        return {"message":"Nuclear luch detected"}
    elif order.timeCountDown == 10:
        return {"message":f"10  9  8  7  6  5  4  3  2  1 Executing {order.order}"}
    
    coords = ""
    if order.x and order.y:
        coords = "at coords [{order.x},{order.y}] "

    return {"message": f"Order[{order.order}] executing {coords} in {order.timeCountDown} seconds"}
