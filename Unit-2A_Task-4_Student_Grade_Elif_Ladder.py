#Student Grade Analysis
marks=int(input("Enter total marks out of 100:"))
if marks >= 90:
 print(f"Grade:A (Mark={marks})")
elif marks >= 80 and marks<90:
 print(f"Grade:B (Marks={marks})")
elif marks >= 70 and marks<80:
 print(f"Grade:C (Marks={marks})")
else:
 print(f"Grade:D (Marks={marks})")