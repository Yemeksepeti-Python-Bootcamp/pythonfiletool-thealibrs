import csv,json
from pathlib import Path

class FileTool:
    def __init__(self, path, fields = []):
        self.path = path
        self.fields = fields


    def isFileExist(self):
        """
            Helper method that checks the file exist or not
            returns bool 
        """
        return Path(self.path).exists()

    def create_new_file(self):
        """
            This method is used to create a new file 
        """
        file_name = input("Enter a file name: ")
        file_format = input("Write file format?\n- csv\n- json\n- txt\n")

        try:
            open(file_name+"."+file_format,"x")
        except:
            print("There is same file in given path")

    
    def read_file(self):
        """
            This method is used to read all data from files.
        """
        with open(self.path, "r") as file:
            contents = file.read()
            print(contents)
    
    def file_operations(self):
        """
            This method is used to File Operations like 
            searching, reading, updating and deleting.
        """
        if self.isFileExist():
            menu = "List of operations:\n\n[1] Searching\n[2] Deleting\n[3] Adding\n[4] Updating\n"
            choice = input(menu)

            if choice == "1": # searching if choice 1
                key = input("Enter a word that you want to search: ")
                with open(self.path) as file:
                    contents = file.readlines() # reads all lines
                found_lines = [ data for data in contents if key in data ] # creates a list that if matches that desired word with content

                if len(found_lines) != 0:
                    print(f"{key} found in {len(found_lines)} lines: \n", *found_lines)
                else:
                    print(f"Nothing matched with {key} in the content!")
            
            elif choice == "2": # deleting
                key = input("Enter a word that you want to delete: ")
                current_file = open(self.path)
                updated_file = open("updated_"+self.path,"w")
                
                for line in current_file:
                    if key in line:
                        updated_file.write(line.replace(key,""))
                    else:
                        print(f"No matching with {key}")
                        break
                current_file.close()
                updated_file.close()
                

            elif choice == "3":
                key = input("Enter anything that you want to add: ")
                with open(self.path, "a+") as file:
                    file.write(key)
                print(f"{key} added to your file!")
            
            elif choice == "4":
                pass
                



        else:
            print("There is no file in the given path!")



   
       





if __name__ == "__main__":

    file_path = 'demofile.txt'
    ft = FileTool(file_path)
    ft.file_operations()

