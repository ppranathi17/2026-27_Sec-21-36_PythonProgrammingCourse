#To check whether the triangle is valiod or not valid
angle1_in_degress=float(input("Enter first angle in degress:"))
angle2_in_degress=float(input("Enter second angle in degress:"))
angle3_in_degress=float(input("Enter third angle in degress:"))
if angle1_in_degress>0 and angle2_in_degress>0 and angle3_in_degress>0 and angle1_in_degress+angle2_in_degress+angle3_in_degress==180:
 print(f"The triangle with angles {angle1_in_degress},{angle2_in_degress},and {angle3_in_degress} is valid")
else: 
 print(f"The triangle with angles {angle1_in_degress},{angle2_in_degress},and {angle3_in_degress} is valid")