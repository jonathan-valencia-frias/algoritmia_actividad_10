from _particula import Particula
import json

class Lista_Particulas:
    lt_particula=list()
    
    def insertar_inicio(self,p):
        self.lt_particula.insert(0,p)
        
    def insertar_final(self,p):
        self.lt_particula.append(p)
        
    def mostrar(self):
        for i in range(len(self.lt_particula)):
            print(str(self.lt_particula[i]))
            
    def __str__(self) -> str:
        return "".join(
        str(i)+"\n" for i in self.lt_particula
        )
        
    def __len__(self):
        return len(self.lt_particula)
    
    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.lt_particula):
            particula = self.lt_particula[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
        
    def Guardar(self,ubicacion):
        try:
            with open(ubicacion,"w") as archivo:
                lista = [particula.to_dict() for particula in self.lt_particula]
                json.dump(lista,archivo,indent=5)
            return 1
        except:
            return 0
        
    def Abrir(self,ubicacion):
        try:
            with open(ubicacion,"r") as archivo:
                lista = json.load(archivo)
                self.lt_particula = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0