#Лабораторная1.4

import math as math;
while True:
    try:
        n=int(input("Введите число N(N-кол-во раз с группой\nребят происходит ураган за 17 дней: "));
    except ValueError:
        print("Вы ввели не целое число");
        break;
    d=400;c=17;
    m=n/c*d;
    p=1/3;
    m=math.ceil(m);
    lam=d*p;
    try:
        res=math.pow(lam,m)*math.exp(-lam)/math.factorial(m)*100;
        print("Ураган случиться за 400 дней только с Катей с вероятностью в "+str(res)+"%");
        inc=input("Желаете повторить расчет для другого N?(да/нет)");
        if inc=="нет":
            break;
    except OverflowError:
        print("Введите более маленькое число N");
        
    

        

