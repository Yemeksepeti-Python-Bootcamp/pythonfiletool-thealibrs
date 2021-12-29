from os import path


def delete(file_path):
    key = input("Enter a word that you want to delete: ")
    current_file = open(file_path)
    updated_file = open("updated_"+file_path,"w")
    
    for line in current_file:
        updated_file.write(line.replace(key,""))
    current_file.close()
    updated_file.close()

file_path = 'lorem2.txt'
delete(file_path)