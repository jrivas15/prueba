from PySide6.QtWidgets import QWidget, QTableWidgetItem
from views.suma import Ui_Form
from db.querys import consultar_alumnos, buscar_alumno
from db import querys


class SumaWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #SIGNAL
        self.buton_suma.clicked.connect(self.sumar)
        self.boton_borrar.clicked.connect(self.borrar)
        self.boton_cerrar.clicked.connect(self.cerrar_ventana)
        
        self.buscar_line.textChanged.connect(self.buscar)
        self.btn_actualizar.clicked.connect(self.actualizar_tabla)
        #SQL CONEXION
        data = consultar_alumnos()
        print(data)
        self.table_config()
        self.llenar_tabla(data)

    def sumar(self):
        numero1 = float(self.numero1_lineEdit.text())
        numero2 = float(self.numero2_lineEdit.text())

        resultado = numero1 + numero2

        self.resultado_label.setText('{:,.0f}'.format(resultado))


    def borrar(self):
        self.numero1_lineEdit.clear()
        self.numero2_lineEdit.clear()
        self.resultado_label.clear()
    
    #*-------------------------------------------

    def buscar(self):
        buscar = self.buscar_line.text()
        resultados = buscar_alumno(buscar)
        # print(f'Buscar : {buscar}')
        # print(f'Resultado : {resultados}')
        self.llenar_tabla(resultados)

    def actualizar_tabla(self):
        data = consultar_alumnos()
        self.llenar_tabla(data)

    def table_config(self):
        headers = ('ID', 'Nombre', 'Apellido', 'Asistió')
        self.alumnos_tableWidget.setHorizontalHeaderLabels(headers)
        self.alumnos_tableWidget.setRowCount(0)

    def llenar_tabla(self, data:list = [] ):
        self.alumnos_tableWidget.setRowCount(0) # Para limpiar la tabla 
        for i,registro in enumerate(data):
            # print(i, registro)
            self.alumnos_tableWidget.insertRow(i)
            for j, elemento in enumerate(registro):
                # print(elemento)
                celda = QTableWidgetItem(str(elemento))
                self.alumnos_tableWidget.setItem(i,j,celda)



    def cerrar_ventana(self):
        self.close()