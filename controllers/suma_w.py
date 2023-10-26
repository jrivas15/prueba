from PySide6.QtWidgets import QWidget
from views.suma import Ui_Form


class SumaWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #SIGNAL
        self.buton_suma.clicked.connect(self.sumar)
        self.boton_borrar.clicked.connect(self.borrar)
        self.boton_cerrar.clicked.connect(self.cerrar_ventana)


    def sumar(self):
        numero1 = float(self.numero1_lineEdit.text())
        numero2 = float(self.numero2_lineEdit.text())

        resultado = numero1 + numero2

        self.resultado_label.setText('{:,.0f}'.format(resultado))


    def borrar(self):
        self.numero1_lineEdit.clear()
        self.numero2_lineEdit.clear()
        self.resultado_label.clear()
    
    def cerrar_ventana(self):
        self.close()