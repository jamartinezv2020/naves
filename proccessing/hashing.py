# Hash basado en la suma de los códigos ASCII
def hash1(lastname):
    return sum(ord(char) for char in lastname) % 5

# Hash combinando posición y código ASCII
def hash2(lastname):
    return sum((index + 1) * ord(char) for index, char in enumerate(lastname)) % 5

# Hash basado en la suma de los códigos ASCII del primer y segundo carácter del ID
def hash3(id):
    return (ord(id[0]) + ord(id[1]) * len(id)) % 5

lastname = "Martínez"
print(hash1(lastname))  # Salida: 4


lastname = "Valdés"
print(hash2(lastname))  # Salida: 4


id = "C.C.16885496"
print(hash3(id))  # Salida: 2

