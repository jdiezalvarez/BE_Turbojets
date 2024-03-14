#Donnees numeriques
gamma = 1.4
Cp = 1.4
rho = 1
r = 287.05
M = 0.02897
Ma = 0.85
m_point_std_2 = 400






##Cruise conditions
#Altitude (km)
h = 10 
Tatm1 = 288.15-6.5*h
#print(round(Tatm1,3))
patm1 = 101325*(1-0.0225577*h)**(5.25588)
#print(round(patm1,3)) 

###Cruise Conditions####
print("\n\n*******Cruise Condition******** \n")


####Point 1
print("Point 1")
T_1 = Tatm1*(1+(gamma-1)/2*Ma**2)
print("T_1 =",round(T_1,3))
p_1 = (T_1/Tatm1)**(gamma/(gamma-1))*patm1
print("P_1 = ", round(p_1,3))
rho_1 = rho*(1+(gamma-1)/2*Ma**2)**(1/(gamma-1))
print("rho_1 = ", round(rho_1,3))


###Point 2
print("\n\nPoint 2")
p_2 = p_1*0.97
print("p_2 = " , round(p_2,3))

T_2 = T_1*(p_2/p_1)**((gamma-1)/gamma)
print("T_2 = ", round(T_2,3))

rho_2 = (T_2/T_1)**(1/(gamma-1)*rho_1)
print("rho_2 = ", round(rho_2,3))
##print(p_2/r/T_2) debería dar lo mismo pero no da no sé porque.






