#лабораторная 2 по ПО

import random,gspread,sys,os;
import numpy as np;
from numpy import linalg as lin;
from matplotlib import pyplot as plt;
from oauth2client.service_account import ServiceAccountCredentials

n=27;#количество интерполяционных узлов
X=[];Y=[];k=1.5;m=1.2#k:угловой коэффициент прямой,m:смещение прямой по ординате
lowboarder=float(input("Введите нижний предел диапазона: "));
hightboarder=float(input("Введите верхний предел диапозана: "));
X.append(lowboarder);
Y.append(k*lowboarder+m);
currentx=lowboarder;
dx=(hightboarder-lowboarder)/(n-1);#определение шага дискретизации данных
for i in range(1,n):
    currentx=currentx+dx;
    X.append(currentx);
    Y.append(k*currentx+m+random.random());
#здесь должно быть соединение с гугл таблицей
scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive'];
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope);
client = gspread.authorize(creds);
sheet = client.open("project").sheet1;
sheet.insert_row(X, 1);
sheet.insert_row(Y, 2);
#МНК
Y=np.array(Y);
Atr=np.array([[1.0 for i in range(1,n+1)],X]);
A=np.transpose(Atr);#матрица регрессеров
A1=np.dot(Atr,A);
A1=lin.inv(A1);
A2=np.dot(A1,Atr);
K=np.dot(A2,Y);#искомые значения параметров линейной функции
f=plt.figure();
plt.grid();
x=np.arange(lowboarder,hightboarder,dx);
y=K[0]+K[1]*x;
plt.plot(x,y);
plt.scatter(X,Y,color="red");
plt.title("Аппроксимация по МНК");
plt.show();


