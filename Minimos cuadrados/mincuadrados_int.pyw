import sys
from mincuadrados_ui import *
from PyQt5.QtWidgets import *
import numpy as np
import math
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class Ventana(QWidget):#se definen todas las funciones
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.numero_datos)#conecta el boton con la funcion numero_datos
        self.ui.comboBox.activated.connect(self.selector)#conecta el combobox con la funcion selector
        
    def numero_datos(self):#esta funcion lee el numero en el textbox y crea las corespondientes filas en la tabla 
        num_datos=self.ui.textEdit.toPlainText()#lee el numero que esta en edit text
        num_datos=int(num_datos)#conviete el string en entero
        self.ui.tableWidget.setRowCount(num_datos)#crea las filas correspondientes
        
    def selector(self):#funcion para calcular y graficar la curva de ajuste
        x=[]
        y=[]
        opcion=self.ui.comboBox.currentIndex()#lee en que posicion esta el combobox
        n=self.ui.textEdit.toPlainText()#lee el numero que esta en el edit text
        n=int(n)#conviete el string en entero
        i=0
        while(i<n):#el while lee todos los datos de la tabla
            t1=self.ui.tableWidget.item(i,0)#lee los datos en la columna x
            t2=self.ui.tableWidget.item(i,1)#lee los datos en la columna y
            t1=t1.text()#lo convierte en texto
            t2=t2.text()#lo convierte en texto
            print(t1)
            print(t2)
            x.append(float(t1))#guarda la variable en en un vector
            y.append(float(t2))#guarda la variable en en un vector
            i=i+1
        print(n)
        print(opcion)
        print(x)
        print(y)
        if opcion==0:#lineal
            xi=0
            yi=0
            x2=0
            xy=0
            i=0
            while(i<n):#hace las correspondientes sumatorias
                xi=xi+x[i]
                yi=yi+y[i]
                x2=x2+(x[i]*x[i])
                xy=xy+(x[i]*y[i])
                i=i+1
            i=0
            a = np.array([[n,xi],[xi,x2]])
            b = np.array([yi,xy])
            resultado=np.linalg.solve(a,b)
            self.ui.textEdit_3.setText("Y="+str(resultado[1])+"x+"+str(resultado[0]))
            xplot = np.linspace(x[0],x[n-1],20)#genera el vector para graficar
            yplot = resultado[1]*xplot+resultado[0]#genera el vector para graficar
            medx=xi/n
            medy=yi/n
            i=0
            finx=0
            covar=0
            varx=0
            vary=0
            while(i<n):
                covar=covar+((x[i]-medx)*(y[i]-medy))
                varx=varx+math.pow((x[i]-medx),2)
                vary=vary+math.pow((y[i]-medy),2)
                i=i+1
            finx=(covar)/(math.sqrt(varx*vary))
            self.ui.label_4.setText("R="+str(finx))
        elif opcion==1:#parabolica
            xi=0
            yi=0
            x2=0
            x3=0
            x4=0
            xy=0
            x2y=0
            i=0
            while(i<n):#hace las correspondientes sumatorias
                xi=xi+x[i]
                yi=yi+y[i]
                x2=x2+(x[i]*x[i])
                x3=x3+(x[i]*x[i]*x[i])
                x4=x4+(x[i]*x[i]*x[i]*x[i])
                xy=xy+(x[i]*y[i])
                x2y=x2y+(x[i]*x[i]*y[i])
                i=i+1
            a = np.array([[n,xi,x2],[xi,x2,x3],[x2,x3,x4]])
            b = np.array([yi,xy,x2y])
            resultado=np.linalg.solve(a,b)
            self.ui.textEdit_3.setText("Y="+str(resultado[2])+"x^2+"+str(resultado[1])+"x+"+str(resultado[1]))
            xplot = np.linspace(x[0],x[n-1],20)#genera el vector para graficar
            yplot = resultado[2]*np.power(xplot,2)+resultado[1]*xplot+resultado[0]#genera el vector para graficar
        elif opcion==2:#polinomica
            i=0
            ai=[]
            ri=[]
            yi=0
            m=self.ui.textEdit_2.toPlainText()#lee el numero que esta en edit text
            m=int(m)#conviete el string en entero
            texto_curva="Y="
            while(i<=m):#el while para el grado del polinomio
                xiy=0
                ai.append([])
                j=0
                while(j<=m):
                    xi=0
                    k=0
                    while(k<n):#hace las correspondientes sumatorias
                        xi=xi+math.pow(x[k],j+i)
                        k=k+1
                    ai[i].append(xi)
                    j=j+1
                l=0
                while(l<n):#hace las correspondientes sumatorias
                    xiy=xiy+(math.pow(x[l],i)*y[l])
                    l=l+1
                ri.append(xiy)
                i=i+1
            a = np.array(ai)
            b = np.array(ri)
            resultado=np.linalg.solve(a,b)
            i=m
            while(i>0):
                texto_curva=texto_curva+str(resultado[i])+"x^"+str(i)+" +"
                i=i-1
            texto_curva=texto_curva+str(resultado[0])
            self.ui.textEdit_3.setText(texto_curva)
            xplot = np.linspace(x[0],x[n-1],20)#genera el vector para graficar
            yplot=0
            yplot = resultado[m]*np.power(xplot,m)
            i=m-1
            while(i>=0):
                yplot =yplot+resultado[i]*np.power(xplot,i)#genera el vector para graficar
                i=i-1
            print(ai)
            print(ri)
        elif opcion==3:#exponencial
            xi=0
            yi=0
            x2=0
            xy=0
            yln=[]
            i=0
            mal=0
            while(i<n):#hace las correspondientes sumatorias
                if(y[i]<0):
                    self.ui.textEdit_3.setText("valor negativo perifique su tabla")
                    mal=1
                else:
                    yln.append(math.log(y[i],math.e))#linealiza la funcion
                    xi=xi+x[i]
                    yi=yi+yln[i]
                    x2=x2+(x[i]*x[i])
                    xy=xy+(x[i]*yln[i])
                i=i+1
            if(mal==0):
                a = np.array([[n,xi],[xi,x2]])
                b = np.array([yi,xy])
                resultado=np.linalg.solve(a,b)
                resultado[0]=math.exp(resultado[0])
                self.ui.textEdit_3.setText("Y="+str(resultado[0])+"*e^("+str(resultado[1])+"x)")
                xplot = np.linspace(x[0],x[n-1],20)#genera el vector para graficar
                yplot = resultado[0]*np.exp(resultado[0]*xplot)#genera el vector para graficar                
        elif opcion==4:#logaritmica
            xi=0
            yi=0
            x2=0
            xy=0
            xln=[]
            i=0
            mal=0
            while(i<n):#hace las correspondientes sumatorias
                if(x[i]<0):
                    self.ui.textEdit_3.setText("valor negativo perifique su tabla")
                    mal=1
                else:
                    xln.append(math.log(x[i],math.e))#linealiza la funcion
                    xi=xi+xln[i]
                    yi=yi+y[i]
                    x2=x2+(xln[i]*xln[i])
                    xy=xy+(xln[i]*y[i])
                i=i+1
            if(mal==0):
                a = np.array([[n,xi],[xi,x2]])
                b = np.array([yi,xy])
                resultado=np.linalg.solve(a,b)
                self.ui.textEdit_3.setText("Y="+str(resultado[1])+"*ln(x)"+str(resultado[0]))#escribe la curva caracteristica en el edit text
                xplot = np.linspace(x[0],x[n-1],20)#genera el vector para graficar
                yplot = resultado[1]*np.log(xplot)+resultado[0]#genera el vector para graficar
        plt.plot(x,y,'ro')#genera los punto en otra ventana
        plt.plot(xplot, yplot)#genera una grafica en otra ventana
        self.ui.MplWidget.canvas.axes.clear()#limpia el widget
        self.ui.MplWidget.canvas.axes.plot(x,y,'ro')#genera los puntos en la UI
        self.ui.MplWidget.canvas.axes.plot(xplot, yplot)#genera la grafica en la UI
        self.ui.MplWidget.canvas.axes.set_title('Grafica curva de ajuste')
        self.ui.MplWidget.canvas.draw()
        print(resultado)
        
        
if __name__ == "__main__":
        mi_aplicacion= QApplication(sys.argv)
        mi_app= Ventana()
        mi_app.show()
        sys.exit(mi_aplicacion.exec_())