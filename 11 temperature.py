T = float(input("Temperature: "))
scale0 = input("First scale: K (kelvin), C (Celsius): ")
scale1 = input("Second scale: K (kelvin), C (Celsius): ")

if scale0.upper == "C" and scale1.upper == "K":  #celsius to kelvin 
    RK = T + 273.15 
    if RK >= 0.15:
        print(RK)
    else:
        print("This temperature doesn't exist")
elif scale0.upper == "K" and scale1.upper == "C":
    RC = T - 273.15 
    if RC >= -273.15:
        print(RC)
    else:
        print("This temperature doesn't exist")
elif scale0.upper == "C" and scale1.upper == "C": #celsius to celsius 
    if T >= -273.15:
        print(T)
    else:
        print("This temperature doesn't exist")
elif scale0.upper == "K" and scale1.upper == "K": #kelvin to kelvin
    if T > -0.15:
        print(T)
    else:
        print("This temperature doesn't exist")




   






   
    

