#Лабораторная1 Задание2

inp=input("Введите любое количество чисел\nразделяя их запятыми без пробела между ними\n(i-мнимая единица,sqrt()-форма записи иррациональных чисел): ");
def isint(s):
    try:
        int(s)
        return 1
    except ValueError:
        return 0
def trans(s):
	res="";
	j=0;
	for i in s:
		if j==0:
			res=res+s[j];	
		elif j!=len(s)-1:
			res=res+' '+s[j]+",";
		else:
			res=res+" "+s[j];
		j=j+1;
	print(res);
s=inp.split(",");
l1=["Натуральные числа:"];l2=["Целые числа:"];l3=["Рациональные числа:"];
l4=["Комплексные числа:"];l5=["Четные числа:"];l6=["Нечетные числа:"];
l7=["Простые числа:"];l8=["Иррациональные числа:"];
for i in s:
    i.strip();k=1;
    if (isint(i)==1):
        if (i.isdigit()==True and int(i)!=0):
            l1.append(i);
            l2.append(i);
            l3.append(i);
            l4.append(i);
            if ((int(i)%2)==0):
                l5.append(i);
            else:
                l6.append(i);
            while k<(int(i)+1):
                if (((int(i)%k)==0) and (int(i)==k)):
                    l7.append(i);
                    break;
                elif ((int(i)%k)==0 and k!=1):
                    break;
                k=k+1;        
        else:
            l2.append(i);
            l4.append(i);
            l3.append(i);
            if ((int(i)%2)==0):
                l5.append(i);
            else:
                l6.append(i);
    else:
        try:
            l4.append(i);
            i.index("i");
        except ValueError:
            try:
                i.index("sqrt");
                l8.append(i);
            except ValueError:
                l3.append(i);
trans(l1);
trans(l2);
trans(l3);
trans(l4);
trans(l5);
trans(l6);
trans(l7);
trans(l8);
input();
        
    
