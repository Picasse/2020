
%Script del calculo del polinomio de taylor para una determinada ecuacion
%No es ejecutable sin polinomioTaylorFuncion.m

%Copyright 2012-2013 Francisco Javier Bastante Flores, Ingenier�a Qu�mica (UAM)

clear;
clc;
syms x

ecuacion=input('Introduzca la ecuaci�n: ');
a=input('Introduzca el punto de aproximaci�n: ');
n=input('Introduzca el n�mero de sumandos (tolerancia): ');

%Para cambiar el color de las gr�ficas se debe tener en cuenta que cada
%color es el porcentaje aplicado de la mezcla de tres colores b�sicos:
%rojo, verde y azul. La forma de acceder a ella es la siguiente:
% matriz = get(h(i),'Color')
%El color por defecto es azul, es decir, matriz = [0 0 1]
%El primer valor es la cantidad de rojo, el segundo verde y el tercero azul
%Si, por ejemplo, queremos poner la gr�fica de color rojo, ejecutamos:
% matriz = [1 0 0];
% set(h(i),'Color',matriz)
%Son m�ltiples las combinaciones de colores posibles. Aqu� se recogen
%algunas para implementarlas por defecto en el programa:
Colores=[0 0 0;  %Negro
         0 0 1;  %Azul oscuro
         0 1 0;  %Verde claro
         0 1 1;  %Azul claro
         1 0 0;  %Rojo
         1 0 1;  %Violeta
         1 1 0;  %Amarillo
         1 1 1]; %Blanco
%Representamos la ecuacion original
hold off
h(1)=ezplot(ecuacion);
hold on
%Ponemos la grafica en negro
set(h(1),'Color',Colores(1,:));

leyenda{1}='Ecuaci�n original';

%Representamos ahora las diversas aproximaciones
j=2;
for i=1:n,
    leyenda{i+1}=['n=' num2str(i)]; %A�adimos el sumando a la leyenda
    aproximacion=polinomioTaylorFuncion(ecuacion,x,a,i); %Calculamos el polinomio con n sumandos
    %Representacion
    if isa(aproximacion,'sym')==1,
       h(i+1)=ezplot(aproximacion);
    else
       h(i+1)=ezplot(num2str(aproximacion));
    end;
    set(h(i+1),'Color',Colores(j,:))
    j=j+1;
    %Si se acaban los colores vuelve a empezar
    if j==8,
       j=2;
    end;
end;

%Comandos de finalizacion del programa

title(char(ecuacion))
xlabel('')
legend(leyenda)

clc
aproximacion

clear x
clear ecuacion
clear a
clear n
clear i
clear j
clear Colores
clear h
clear leyenda