function polinomioTaylorGrafica()

clear;
clc;

syms x
ecuacion=input('Introduzca la ecuación: ');
a=input('Introduzca el punto de aproximación: ');
n=input('Introduzca el número de sumandos (tolerancia): ');

%Primer elemento sin derivada
f=inline(char(ecuacion));
original=f;
aproximacion=f(a);
i=1;
i=representacion(i,original, aproximacion);
    
%Resto de elementos
for j=1:(n-1),
    if ecuacion==0,
       return;
    end;
    %Calculamos la derivada general (syms)
    ecuacion=diff(ecuacion);
    %Hallamos la derivada en a (inline)
    f=inline(char(ecuacion));
    %Hallamos el resto del sumando 
    sumando=(f(a))/(factorial(j))*((x-a)^j);
    aproximacion=aproximacion+sumando;
    i=representacion(i,original, aproximacion);
end;

function out=ispar(n)
if mod(n,2)==0,
   out=1;
elseif mod(n,2)==1,
   out=0;
else
   out=-1;
end;

function i=representacion(i,original, aproximacion)
numero=num2str(i);
eval(['figure' numero '=figure;'])
eval(['axes' numero ' = axes(' char(39) 'Parent' char(39) ',figure' numero ');'])
ezplot(original)
eval(['limitesOR=get(axes' numero ',' char(39) 'XLim' char(39) ');'])
if isa(aproximacion,'sym')==1,
   ap=inline(char(aproximacion));
else
   ap=inline(num2str(aproximacion));
end;
ezplot(ap)
eval(['limites=get(axes' numero ',' char(39) 'XLim' char(39) ');'])
x0=linspace(min(limitesOR(1),limites(1)),max(limitesOR(2),limites(2)),1000);
yOR=[];
y=[];
for j=1:1000,
    yOR=[yOR original(x0(j))];
    y=[y ap(x0(j))];
end;
%eval(['close(figure' numero ')'])
plot(x0,yOR,'r',x0,y)
legend('Ec. Original',['Polinomio Taylor (n=' numero ')'])
i=i+1;