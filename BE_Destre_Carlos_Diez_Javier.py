#Donnees numeriques
gamma = 1.4
Cp = 1.4
Density = 1
R = 8.314
M = 0.02897
Ma = 0.85
m_point_std_2 = 400






##Cruise conditions
#Altitude (km)
h = 10 
Tatm1 = 288.15-6.5*h
#print(round(Tatm1,3))
Patm1 = 101325*(1-0.0225577*h)**(5.25588)

#print(round(Patm1,3))

####Point 1
print("*******Cruise Condition********")
print("Point 1")
T_1 = Tatm1*(1+(gamma-1)/2*Ma**2)
print("T_1 =",round(T_1,3))
P_1 = (T_1/Tatm1)**(gamma/(gamma-1))*Patm1
print("P_1 = ", round(P_1,3))







