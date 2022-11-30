from algoritmos import distancia_euclidiana

class Particula:
    id=0
    origen_x=0
    origen_y=0
    destino_x=0
    destino_y=0
    velocidad=0
    red=0
    green=0
    blue=0
    distancia=0.0
    
    def __init__(self,id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue):
        self.id=id
        self.origen_x=origen_x
        self.origen_y=origen_y
        self.destino_x=destino_x
        self.destino_y=destino_y
        self.velocidad=velocidad
        self.red=red
        self.green=green
        self.blue=blue
        self.distancia=distancia_euclidiana(origen_x,destino_x,origen_y,destino_y)
    
    def __str__(self) -> str:
        return (
        "ID:"+str(self.id)+"\n"+
        "Origen x:"+str(self.origen_x)+"\n"+
        "Origen y:"+str(self.origen_y)+"\n"+
        "Destino x:"+str(self.destino_x)+"\n"+
        "Destino y:"+str(self.destino_y)+"\n"+
        "Velocidad:"+str(self.velocidad)+"\n"+
        "Red:"+str(self.red)+"\n"+
        "Green:"+str(self.green)+"\n"+
        "Blue:"+str(self.blue)+"\n"+
        "Distancia:"+str(self.distancia)+"\n"
        )
        
    def to_dict(self):
        return{
            "id":self.id,
            "origen_x":self.origen_x,
            "origen_y":self.origen_y,
            "destino_x":self.destino_x,
            "destino_y":self.destino_y,
            "velocidad":self.velocidad,
            "red":self.red,
            "green":self.green,
            "blue":self.blue,
        }