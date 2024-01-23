function [aproximacion]=polinomioTaylorFuncion(ecuacion,x,a,n)

%Funcion del calculo del polinomio de taylor para una determinada ecuacion
%No es ejecutable sin polinomioTaylor.m

%Copyright 2012-2013 Francisco Javier Bastante Flores, Ingeniería Química (UAM)

%Primer elemento sin derivada
temporal=inline(char(ecuacion));
aproximacion=temporal(a);

%Resto de elementos
for i=1:(n-1),
    if ecuacion==0,
       return;
    end;
    %Calculamos la derivada general (syms)
    ecuacion=diff(ecuacion);
    %Hallamos la derivada en a (inline)
    temporal=inline(char(ecuacion));
    %Hallamos el resto del sumando 
    sumando=(temporal(a))/(factorial(i))*((x-a)^i);
    aproximacion=aproximacion+sumando;
end;