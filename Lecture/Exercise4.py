"""
Foundation English = FE
General Business = GB
Introduction to Computer Systems = ICS
Computer Programming = CP
"""
print("-----------------------------------------------------------")
FE = float(input("Your Foundation English score : "))
GB = float(input("Your General Business score : "))
ICS = float(input("Your Introduction score : "))
CP = float(input("Your Computer System score : "))
print("-----------------------------------------------------------")
print("Your scores")
print("Foundation English score is:", FE)
print("General Business score is:", GB)
print("Introduction score is:", ICS)
print("Computer System score is:", CP)
print("--------------------------------------------------------------")
print("Summary :", (FE+GB+ICS+CP)/4)
