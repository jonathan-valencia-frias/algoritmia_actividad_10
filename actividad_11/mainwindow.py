from wsgiref import headers
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen,QColor,QTransform
from PySide2.QtWidgets import QMainWindow,QFileDialog,QMessageBox,QTableWidgetItem,QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from lista_particulas import Lista_Particulas
from _particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.lista_particulas = Lista_Particulas()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_inicio.clicked.connect(self.click_agregar_inicio)
        self.ui.btn_enviar_final.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_datos.clicked.connect(self.mostrar_datos)
        self.ui.actionAbrir.triggered.connect(self.accion_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.accion_guardar_archivo)
        self.ui.buscar_button.clicked.connect(self.buscar_particula)
        self.ui.mostrar_button.clicked.connect(self.mostrar_lista)
        self.ui.Btn_ordenarid.clicked.connect(self.sort_ID)
        self.ui.Btn_ordenardis.clicked.connect(self.sort_distancia)
        self.ui.Btn_ordenarvel.clicked.connect(self.sort_velocidad)
        self.ui.Dibujar.clicked.connect(self.dibujar)
        #self.ui.Limpiar.clicked.connect(self.mostrar_lista)
        self.scene = QGraphicsScene()
        self.ui.Escena_2.setScene(self.scene)
        
    
    @Slot()
    def sort_ID(self):
        sorted(self.lista_particulas,key=lambda particula: particula.id)
    
    @Slot()
    def sort_distancia(self):
        sorted(self.lista_particulas,key=lambda particula: particula.distancia)
    
    @Slot()
    def sort_velocidad(self):
        sorted(self.lista_particulas,key=lambda particula: particula.velocidad)
        
    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)
        
        for particula in self.lista_particulas:
            r = particula.red
            g = particula.green
            b = particula.blue
            color = QColor(r,g,b)
            pen.setColor(color)
            self.scene.addEllipse(particula.origen_x,particula.origen_y,3,3,pen)
            self.scene.addEllipse(particula.destino_x,particula.destino_y,3,3,pen)
            self.scene.addLine(particula.origen_x+3,particula.origen_y+3,particula.destino_x,particula.destino_y,pen)
            
            
    
    @Slot()
    def Limpiar(self):
        self.scene.clear()
        
                
    @Slot()
    def buscar_particula(self):
        id = self.ui.buscar_text.text()
        encontrado = False
        self.ui.tabla_datos.setColumnCount(10)
        headers = ["Id","origen_x","origen_y","destino_x","destino_y","velocidad","red","green","blue","distancia"]
        self.ui.tabla_datos.setHorizontalHeaderLabels(headers)
        
        self.ui.tabla_datos.setRowCount(1)
        for particula in self.lista_particulas:
            if id == str(particula.id):
                self.ui.tabla_datos.clear()
                
                self.ui.tabla_datos.setColumnCount(10)
                headers = ["Id","origen_x","origen_y","destino_x","destino_y","velocidad","red","green","blue","distancia"]
                self.ui.tabla_datos.setHorizontalHeaderLabels(headers)
                self.ui.tabla_datos.setRowCount(1)
                
                id_widget = QTableWidgetItem(str(particula.id))
                origenx_widget = QTableWidgetItem(str(particula.origen_x))
                origeny_widget = QTableWidgetItem(str(particula.origen_y))
                destinox_widget = QTableWidgetItem(str(particula.destino_x))
                destinoy_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                
                self.ui.tabla_datos.setItem(0,0,id_widget)
                self.ui.tabla_datos.setItem(0,1,origenx_widget)
                self.ui.tabla_datos.setItem(0,2,origeny_widget)
                self.ui.tabla_datos.setItem(0,3,destinox_widget)
                self.ui.tabla_datos.setItem(0,4,destinoy_widget)
                self.ui.tabla_datos.setItem(0,5,velocidad_widget)
                self.ui.tabla_datos.setItem(0,6,red_widget)
                self.ui.tabla_datos.setItem(0,7,green_widget)
                self.ui.tabla_datos.setItem(0,8,blue_widget)
                self.ui.tabla_datos.setItem(0,9,distancia_widget)
                
                encontrado = True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                "libro no encontrado"
            )
                
    
    @Slot()
    def accion_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Abrir Archivo",
            ".",
            "JSON (*.json)",              
        )[0]
        if self.lista_particulas.Abrir(ubicacion)==0:
            QMessageBox.information(
                self,
                "fallo",
                "fallo al intentar Abrir"+ubicacion
            )
        
        
    @Slot()
    def accion_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar Archivo",
            ".",
            "JSON (*.json)",              
        )[0]
        if self.lista_particulas.Guardar(ubicacion)==0:
            QMessageBox.information(
                self,
                "fallo",
                "fallo al intentar guardar"+ubicacion
            )
    
    @Slot()
    def mostrar_datos(self):
        self.ui.Canvas_mostar.insertPlainText(str(self.lista_particulas))
    @Slot()
    def click_agregar_inicio(self):
        id=int(self.ui.input_id.text())
        origen_x=int(self.ui.input_origenx.text())
        origen_y=int(self.ui.input_origeny.text())
        destino_x=int(self.ui.input_destinox.text())
        destino_y=int(self.ui.input_destinoy.text())
        velocidad=int(self.ui.input_velocidad.text())
        red=int(self.ui.input_red.text())
        green=int(self.ui.input_green.text())
        blue=int(self.ui.input_blue.text())
        
        particula=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista_particulas.insertar_inicio(particula)
        
    @Slot()
    def click_agregar_final(self):
        id=int(self.ui.input_id.text())
        origen_x=int(self.ui.input_origenx.text())
        origen_y=int(self.ui.input_origeny.text())
        destino_x=int(self.ui.input_destinox.text())
        destino_y=int(self.ui.input_destinoy.text())
        velocidad=int(self.ui.input_velocidad.text())
        red=int(self.ui.input_red.text())
        green=int(self.ui.input_green.text())
        blue=int(self.ui.input_blue.text())
        
        particula=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.lista_particulas.insertar_final(particula)
        
    @Slot()
    def mostrar_lista(self):
        self.ui.tabla_datos.setColumnCount(10)
        headers = ["Id","origen_x","origen_y","destino_x","destino_y","velocidad","red","green","blue","distancia"]
        self.ui.tabla_datos.setHorizontalHeaderLabels(headers)
        
        self.ui.tabla_datos.setRowCount(len(self.lista_particulas))
        
        row=0
        for particula in self.lista_particulas:
            id_widget = QTableWidgetItem(str(particula.id))
            origenx_widget = QTableWidgetItem(str(particula.origen_x))
            origeny_widget = QTableWidgetItem(str(particula.origen_y))
            destinox_widget = QTableWidgetItem(str(particula.destino_x))
            destinoy_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))
            
            self.ui.tabla_datos.setItem(row,0,id_widget)
            self.ui.tabla_datos.setItem(row,1,origenx_widget)
            self.ui.tabla_datos.setItem(row,2,origeny_widget)
            self.ui.tabla_datos.setItem(row,3,destinox_widget)
            self.ui.tabla_datos.setItem(row,4,destinoy_widget)
            self.ui.tabla_datos.setItem(row,5,velocidad_widget)
            self.ui.tabla_datos.setItem(row,6,red_widget)
            self.ui.tabla_datos.setItem(row,7,green_widget)
            self.ui.tabla_datos.setItem(row,8,blue_widget)
            self.ui.tabla_datos.setItem(row,9,distancia_widget)
            row = row + 1