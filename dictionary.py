# a dictionary is a collection of key:value pairs ordered and changable . No duplictes

capitals = {"USA": "Washington DC",
            "India":"New Delhi",
            "Uganda":"Kampala"}

#print(dir(capitals))
#print(help(capitals))  to get help and get all the functions you can use with the dictionary 

#capitals.get("India")  to get the iteam connected to the key 
  
#if capitals.get("Uganda"):
#    print("That capital exists ")

#else:
#    print("that capital doesn't exist ")    
#capitals.update({"germerny ": "Berlin"})
#print(capitals)

keys =  capitals.keys()
print(keys)