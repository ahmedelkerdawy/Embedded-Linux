# ------------------- string methods -----------------------#

#  capitalize()
name = "ahmed"
print(name.capitalize())
print("------------------------------------------------")

#  lower()
name = "AHMED" 
print(name.lower())
print("------------------------------------------------")

#  casefold()
name = "AHMED" 
print(name.casefold())
print("------------------------------------------------")

#  center()
name = "ahmed"
print(name.center(10))
print("------------------------------------------------")

#  count()
name = "ahmed"
print(name.count('a'))
print("------------------------------------------------")

#   encode()
name = "ahmed"
encoded_str = name.encode('utf-8')
print(encoded_str)
print("------------------------------------------------")

#   endswith()
name = "ahmed"
print(name.endswith("ahmed"))
print("------------------------------------------------")

#   expandtabs()
name = "a hmed"
print(name.expandtabs(2))
print("------------------------------------------------")

#   find()
name = "ahmed"
print(name.find("m"))
print("------------------------------------------------")

#   upper()
name = "ahmed"
print(name.upper())
print("------------------------------------------------")

#   index()
name = "ahmed"
print(name.index("e"))
print("------------------------------------------------")

#   isalnum()
name = "ahmed123"
print(name.isalnum())
print("------------------------------------------------")

#   isalpha()
name = "ahmed"
print(name.isalpha())
print("------------------------------------------------")

#   isascii()
name = "ahmed"
print(name.isascii())
print("------------------------------------------------")

#   isdecimal
name = "123"
print(name.isdecimal())
print("------------------------------------------------")

#   isidentifier()
name = "ahmed"
print(name.isidentifier())
print("------------------------------------------------")

#   join()
names = ("ahmed"  , "ismail" , " Elkerdawy") 
print(" ".join(names))
print("------------------------------------------------") 

#   zfill()
name = "50"
print(name.zfill(10))
print("------------------------------------------------")

#   swapcase()
names = ("ahmed ismail Elkerdawy") 
print(names.swapcase())
print("------------------------------------------------") 

#   strip()
name = "   ahmed   "
print(name.strip())
print("------------------------------------------------")
