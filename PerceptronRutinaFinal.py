import random
import math

class Perceptron():
    def __init__(self):
        self.__alfa = 0.05
        self.__umbrales = []
        self.llenarUmbrales()
        self.__pesos1 = []
        self.__pesos2 = []
        self.__pesos3 = []
        self.llenarPesos()
        self.__a = []
        self.__crearA()
        self.__entrenarPerceptron()
        

    def __escalamientoEntrada(self,input,vMin,vMax):
        return round((input-vMin)/(vMax-vMin),5)

    def __escalamientoSalida(self,output,vMin,vMax):
        return int(output*(vMax-vMin)+vMin)

    def llenarUmbrales(self):
        self.__umbrales.append([0]*1)
        self.__umbrales.append([0]*8)
        self.__umbrales.append([0]*6)
        self.__umbrales.append([0]*1)
        
        for i in range(len(self.__umbrales)):
            for j in range(len(self.__umbrales[i])):
                self.__umbrales[i][j] = round(random.random(),5)
                #self.__umbrales[i][j] = 1

        #self.printMatriz(self.__umbrales)

    def llenarPesos(self):
        self.__llenarPesosS(10,8,self.__pesos1)
        self.__llenarPesosS(8,6,self.__pesos2)
        self.__llenarPesosS(6,1,self.__pesos3)              
        
    def __llenarPesosS(self,filas,columnas,matriz):
        for i in range(filas):
            matriz.append([0]*columnas)

        for i in range(filas):
            for j in range(columnas):
                matriz[i][j] = round(random.random(),5)
                #matriz[i][j] = 1
    
    def __crearA(self):
        self.__a.append([0]*10)
        self.__a.append([0]*8)
        self.__a.append([0]*6)
        self.__a.append([0]*1)
        
        #print("a : ")
        #self.__printMatriz(self.__a)
    
    def __entrenarPerceptron(self):
        entrada = []
        entrada.append([0,1,2,0,4,5,6,7,0,9,1])
        entrada.append([1,1,2,1,4,5,6,7,1,9,1])
        entrada.append([2,1,2,2,4,5,6,7,2,9,1])
        entrada.append([3,1,2,3,4,5,6,7,3,9,1])
        entrada.append([4,1,2,4,4,5,6,7,4,9,1])
        entrada.append([5,1,2,5,4,5,6,7,5,9,1])
        entrada.append([6,1,2,6,4,5,6,7,6,9,1])
        entrada.append([7,1,2,7,4,5,6,7,7,9,1])
        entrada.append([8,1,2,8,4,5,6,7,8,9,1])
        entrada.append([9,1,2,9,4,5,6,7,9,9,1])
    
        print("Entrenamiento con las siguientes rutinas: ")
        print("------------------------------------------")
        self.__printMatrizRutina(entrada)
        
        print("--------------------------------------------------.----")
        print("Estado del perceptron antes de iniciar el aprendizaje :")
        print("-------------------------------------------------------")

        print("Pesos W1 : ")
        self.__printMatriz(self.__pesos1)
        print("Pesos W2 : ")
        self.__printMatriz(self.__pesos2)
        print("Pesos W3 : ")
        self.__printMatriz(self.__pesos3)
        print("Umbrales U1, U2, U3 : ")
        self.__printMatrizUmbrales(self.__umbrales)
        
        print("\n--------------------------------------------------------------------------------------")
        print("| Proceso visual de aprendizaje para todas las rutinas, omitido, ver ejemplo anterior |")
        print("--------------------------------------------------------------------------------------\n")

        for p in range(len(entrada)):
            correcto = False
            while(correcto == False ):
                #n = int(input())
                #if(n!=1):
                #    break

                #a1 -> 0
                for i in range(10):
                    self.__a[0][i] = round(self.__escalamientoEntrada(entrada[p][i],0,9),5)
                    #self.__a[0][i] = entrada[i]
                
                #a2 -> 1
                suma = 0 
                for i in range(8):
                    #print(self.__a[1][i],"=",self.__umbrales[1][i],"+",end=" ")               
                    suma = self.__umbrales[1][i] + self.__sumatoria1(i) 
                    self.__a[1][i] = round(self.__funcionSigmoide(suma),5)                  

                #a3 -> 2
                suma = 0 
                for i in range(6):
                    #print(self.__a[2][i],"=",self.__umbrales[2][i],"+",end=" ")   
                    suma = self.__umbrales[2][i] + self.__sumatoria2(i)
                    self.__a[2][i] = round(self.__funcionSigmoide(suma),5)

                #a4 -> 3
                suma = 0 
                for i in range(1):
                    #print(self.__a[3][i],"=",self.__umbrales[3][i],"+",end=" ")   
                    suma = round(self.__umbrales[3][i] + self.__sumatoria3(i),5)
                    self.__a[3][i] = self.__funcionSigmoide(suma)

                #self.__printTodo()
                #print("\n----------------------------------")
                
                #print("->",self.__a[3][0])
                #print("->",self.__escalamientoSalida(self.__a[3][0],0,24))

                if(self.__escalamientoSalida(self.__a[3][0],0,9) != entrada[p][10]):
                    error = -(0 - self.__a[3][0])
                    self.__modificarPesosW1(error)
                    self.__modificarPesosW2(error)
                    self.__modificarPesosW3(error)
                    self.__modificarUmbralesU1(error)
                    self.__modificarUmbralesU2(error)
                    self.__modificarUmbralesU3(error)
                else:
                    correcto = True 
                #correcto = True
                #self.__printTodo()
        
        print("----------------------------------------------------------")
        print("Estado del perceptron despues del proceso de aprendizaje :")
        print("----------------------------------------------------------")

        print("Pesos W1 : ")
        self.__printMatriz(self.__pesos1)
        print("Pesos W2 : ")
        self.__printMatriz(self.__pesos2)
        print("Pesos W3 : ")
        self.__printMatriz(self.__pesos3)
        print("Umbrales U1, U2, U3 : ")
        self.__printMatrizUmbrales(self.__umbrales)
        
        print("\n-----------------------------------------------------")
        print("Pruebas de rutinas con el perceptron ya entrenado : |")
        print("-----------------------------------------------------\n")
        n = int(input("1 para continuar 0 para parar : "))
        while (n==1):
            rutina = []
            print("ingrese una rutina:")
            for i in range(10):
                n = int(input())
                rutina.append(n)
            self.__probarPerceptron(rutina)
            
            #print("\nmatriz a")
            #self._Perceptron__printMatriz(self.__a)

            n = int(input("\n1 para continuar 0 para parar : "))
            

    def __probarPerceptron(self,rutina):
        #print("******************************************")
        #print("a1\n")
        for i in range(10):
            self.__a[0][i] = round(self.__escalamientoEntrada(rutina[i],0,9),5)
            #print(self.__a[0][i])
            
        #print("a2\n")    
        #a2 -> 1
        suma = 0 
        for i in range(8):
            #print(self.__a[1][i],"=",self.__umbrales[1][i],"+",end=" ")                         
            suma = self.__umbrales[1][i] + self.__sumatoria1(i) 
            self.__a[1][i] = round(self.__funcionSigmoide(suma),5)    
            #print(self.__a[1][i])              
        
        #print("a3\n")
        #a3 -> 2
        suma = 0 
        for i in range(6):
            #print(self.__a[2][i],"=",self.__umbrales[2][i],"+",end=" ")  
            suma = self.__umbrales[2][i] + self.__sumatoria2(i)
            self.__a[2][i] = round(self.__funcionSigmoide(suma),5)
            #print(self.__a[2][i])

        #print("a4\n")
        #a4 -> 3
        suma = 0 
        for i in range(1):
            #print(self.__a[3][i],"=",self.__umbrales[3][i],"+",end=" ")                  
            suma = self.__umbrales[3][i] + self.__sumatoria3(i)
            self.__a[3][i] = round(self.__funcionSigmoide(suma),5)
            #print(self.__a[3][i])

        
        #print("\n--->",self.__a[3][0])
        #print("---->",self.__escalamientoSalida(self.__a[3][0],0,9))
        #self.__printMatriz(self.__a)
        
        print("Salida para esta rutina : ",self.__escalamientoSalida(self.__a[3][0],0,9))
        #print("******************************************")

    def __sumatoria1(self,i):#sumatoria W1
        suma = 0
        for j in range(10):
            suma += self.__a[0][j] * self.__pesos1[j][i]
            #print(self.__a[0][j],"*",self.__pesos1[j][i],"+",end=" ")
        #print()
        return suma    
    
    def __sumatoria2(self,i): #sumatoria W2
        suma = 0
        for j in range(8):
            suma += self.__a[1][j] * self.__pesos2[j][i]
            #print(self.__a[1][j],"*",self.__pesos2[j][i],"+",end=" ")
        #print()
        return suma

    def __sumatoria3(self,i):#sumatoria W3
        suma = 0
        for j in range(6):
            suma += self.__a[2][j] * self.__pesos3[j][i]
            #print(self.__a[2][j],"*",self.__pesos3[j][i],"+",end=" ")
        #print()
        return suma

    def __modificarPesosW1(self,error): # modificar pesos W1   
        #W1        
        for i in range(10):
            for j in range(8):
               s1 = " ",self.__a[0][i], "*" ,self.__a[1][j],"*(", 1 ,"-", self.__a[1][j], ")"
               s2 = " ",self.__a[3][0],"*(",1,"-",self.__a[3][0],")"
               xi = self.__a[0][i] * (self.__a[1][j]*(1-self.__a[1][j]))
               yi = self.__a[3][0] * (1-self.__a[3][0])
               devParY1 = self.__sumatoria4(s1,s2,xi,yi,j)#s1,s2 es solo para imprimir
               devParErr = error - devParY1
               self.__pesos1[i][j] = round(self.__pesos1[i][j]-(self.__alfa * devParErr),5)
               #self.__a[0][i] * (self.__a[1][j]*(1-self.__a[1][j])) * self.__sumatoria4(j) * self.__a[3][0]

    def __sumatoria4(self,s1,s2,xi,yi,k):
        suma = 0
        for p in range(6):
            #print(s1,"*",self.__pesos2[k][p],"*", self.__a[2][p],"*(",1, "-", self.__a[2][p] ,") *", self.__pesos3[p][0],"*",s2)
            suma += xi * ( self.__pesos2[k][p] * (self.__a[2][p]*(1 - self.__a[2][p])) * self.__pesos3[p][0] ) * yi
        return suma
            
    def __modificarPesosW2(self,error): #modificar pesos W2
        for i in range(8):
            for j in range(6):
                yi = self.__a[3][0] * (1-self.__a[3][0])
                devPar = self.__a[1][i] * (self.__a[2][j] * (1 - self.__a[2][j])) * self.__pesos3[j][0] * yi
                devParErr = error - devPar
                self.__pesos2[i][j] = round(self.__pesos2[i][j] - (self.__alfa * devParErr),5)
    
    def __modificarPesosW3(self,error):# modificar pesos W3
        for i in range(6):
            for j in range(1):
                devPar = self.__a[2][j]* (self.__a[3][0] * (1 - self.__a[3][0]))
                devParErr = error - devPar
                self.__pesos3[i][j] = round(self.__pesos3[i][j] - (self.__alfa * devParErr),5)

    def __modificarUmbralesU1(self,error):
        for j in range(8):
            xi = (self.__a[1][j]*(1-self.__a[1][j]))
            yi = self.__a[3][0] * (1-self.__a[3][0])
            devParY1 = self.__sumatoria4(0,0,xi,yi,j)
            devParErr = error - devParY1
            self.__umbrales[1][j] = round(self.__umbrales[1][j]-(self.__alfa * devParErr),5)

    def __modificarUmbralesU2(self,error):
        for j in range(6):
            yi = self.__a[3][0] * (1-self.__a[3][0])
            devPar = (self.__a[2][j] * (1 - self.__a[2][j])) * self.__pesos3[j][0] * yi
            devParErr = error - devPar
            self.__umbrales[2][j] = round(self.__umbrales[2][j] - (self.__alfa * devParErr),5)

    def __modificarUmbralesU3(self,error):
        for j in range(1):
                devPar = (self.__a[3][0] * (1 - self.__a[3][0]))
                devParErr = error - devPar
                self.__umbrales[3][j] = round(self.__umbrales[3][j] - (self.__alfa * devParErr),5)

    #calculamos la funcion sigmoide
    def __funcionSigmoide(self,x):
        return round(1/( 1 + math.exp(-x)),5)
        
    #-------------------------------------------------
    def __printTodo(self):
        self.__printMatriz(self.__umbrales)
        self.__printMatriz(self.__pesos1)
        self.__printMatriz(self.__pesos2)
        self.__printMatriz(self.__pesos3)       
        self.__printMatriz(self.__a)

    def __printMatriz(self,mat):
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j],end=" ")
            print()
        print()

    def __printMatrizUmbrales(self,mat):
        for i in range(1,len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j],end=" ")
            print()
        print()
    
    def __printMatrizRutina(self,mat):
        for i in range(len(mat)):
            print("Rutina ",i," : ",end="")
            for j in range(len(mat[i])):
                print(mat[i][j],end=" ")
            print()
        print()

perceptron = Perceptron()

