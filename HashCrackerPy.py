import hashlib
hash_file = "ff960cb55673958c594d0daaab1e368651c75c02f9687192a1811e7b180336a7"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")

with open(dic_file, 'r') as file:
    diccionario = [line.strip() for line in file]
    for password in diccionario:
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash_file:
            print("La contraseña original es: " + password)
            break
        else:
            print("La contraseña no se encuentra en el diccionario")

