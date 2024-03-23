import math

#Donnees numeriques
gamma = 1.4
Cp = 1.4
rho = 1
R = 8.314
M = 0.02897
r = R/M
m_point_std_2 = 400
p_std = 101325 #Pa
T_std = 288.15 #K
n_fan_is = 0.97 
n_IPC_is = 0.82

points = []




##Cruise conditions
#Altitude (km)
h = 10
#Mach number
Ma = 0.85 
Tatm1 = 288.15-6.5*h
#print(round(Tatm1,3))
patm1 = 101325*(1-0.0225577*h)**(5.25588)
#print(round(patm1,3)) 

###Cruise Conditions####
print("\n\n*******Cruise Condition******** \n")


####Point 1
point_1 = {}

T_1 = Tatm1*(1+(gamma-1)/2*Ma**2) #isentropic transformation

p_1 = (T_1/Tatm1)**(gamma/(gamma-1))*patm1 

rho_1 = rho*(1+(gamma-1)/2*Ma**2)**(1/(gamma-1))

v_1 = Ma*math.sqrt(gamma*r*Tatm1) #static temperature en vez de total


point_1['p'] = round(p_1,3)
point_1['T'] = round(T_1,3)
point_1['rho'] = round(rho_1,3)
point_1['v'] = round(v_1,3)


###Point 2 (et point 1)

point_2 = {}

p_2 = p_1*0.97
T_2 = T_1  #no es insentrópico porque hay pérdidas en la presión
#Lo que pasa aquí es que no hay intercambio de calor en el proceso, pero sí tenemos pérdidas de presión. Esto hace que el proceso no sea
#isentrópico y no podamos usar la fórmula con las gammas. Lo que pasa aquí es nuestro fluido pierde velocidad a pesar de que su temperatura sea la misma.

rho_2 = p_2/r/T_2

#The fluid is not supersonic so we can use (Ma<0.3).....

m_point_2 = m_point_std_2 * math.sqrt(T_std/T_2) * (p_2/p_std)


point_2['p'] = round(p_2,3)
point_2['T'] = round(T_2,3)
point_2['rho'] = round(rho_2,3)
point_2['m_point'] =  round(m_point_2,3)

m_point_1 = m_point_2
point_1['m_point'] =  round(m_point_1,3)



###Point 21
point_21 = {}
p_21 = 1.52 * p_2
#The transformation is isentropic so:
T_21_is = T_2* (p_21/p_2)**((gamma-1)/gamma)
T_21 = (T_21_is-T_2)/n_fan_is + T_2 

#Perfect gas
rho_21 = p_21/r/T_21

point_21['p'] = round(p_21,3)
point_21['T'] = round(T_21,3)
point_21['rho'] = round(rho_21,3)

#By conservation of mass (we are in stationary conditions)
m_point_21 = m_point_2/7.4 
point_21['m_point'] =  round(m_point_21,3)

###Point 13

point_13 = {}

m_point_13 = 6.4*m_point_21
p_13 = p_21
T_13 = T_21
rho_13 = p_13/r/T_13

point_13['p'] = round(p_13,3)
point_13['T'] = round(T_13,3)
point_13['rho'] = round(rho_13,3)
point_13['m_point'] =  round(m_point_13,3)

# Point 24
point_24 = {}
# There is a Low Pressure Comressor (Intermediate Pressure Compressor - IPC), also called Booster
p_24 = 1.41*p_21
#The transformation is isentropic so:
T_24_is = T_21*(p_24/p_21)**((gamma-1)/gamma)
#Then we use the isentropic efficiency of the booster
T_24 = (T_24_is-T_21)/n_IPC_is + T_21 
#Perfect gas
rho_24 = p_24/r/T_24

m_point_24 = m_point_21

point_24['p'] = round(p_24,3)
point_24['T'] = round(T_24,3)
point_24['rho'] = round(rho_24,3)
point_24['m_point'] =  round(m_point_24,3)

# Point 25
point_25 = {}

p_25 = p_24*0.98
T_25 = T_24
rho_25 = p_25/r/T_25
m_point_25 = m_point_24

point_25['p'] = round(p_25,3)
point_25['T'] = round(T_25,3)
point_25['rho'] = round(rho_25,3)
point_25['m_point'] =  round(m_point_25,3)






print("Point 1", point_1)
print("point_2", point_2)
print("Point 13", point_13)
print("Point_21", point_21)
print("Point_24", point_24)
print("Point_25", point_25)