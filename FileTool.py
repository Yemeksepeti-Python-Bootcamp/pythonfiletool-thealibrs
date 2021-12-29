import csv,json
from pathlib import Path

class FileTool:
    # List of exceptions message
    NO_FILE_EXCEPTION = "There is no file in the given path!"
    UNMATCHED_FILE_TYPE_EXCEPTION = "Unmatched file type!"

    def __init__(self, path, fields = []):
        self.path = path
        self.fields = fields


    def isFileExist(self):
        """
            - Helper method that checks the file exist or not
            - returns bool 
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

    def read_file_content(self):
        """
            This method is used to read all data from files.
        """
        with open(self.path, "r") as file:
            contents = file.read()
            print(contents)
    
    def json_operations(self):
        """
            This method is used to 
               [1] imports whole contents of json into txt file.
               [2] imports whole contents of txt into json file.
        """
        menu = "List of operations:\n\n[1] JSON to TXT \n[2] TXT to JSON\n"
        choice = input(menu)

        if choice == "1":
            if Path(self.path).suffix == ".json": # checks whether file is a json file or not
                if self.isFileExist(): # checks whether file exits
                    with open(self.path,"r") as json_file: # opens json file
                        json_content = json.load(json_file) # takes whole contents of json file

                    new_file_name = Path(self.path).stem+".txt" 
                    with open(new_file_name,"w+") as new_file:
                        new_file.write(str(json_content))

                    print("PROCESS COMPLETED!")
                else:
                    print(FileTool.NO_FILE_EXCEPTION)
            else:
                print(FileTool.UNMATCHED_FILE_TYPE_EXCEPTION)

        elif choice == "2":
            if Path(self.path).suffix == ".txt":
                if self.isFileExist():
                    pass
                else:
                    print(FileTool.NO_FILE_EXCEPTION)
            else:
                print(FileTool.UNMATCHED_FILE_TYPE_EXCEPTION)


    def file_operations(self):
        """
            This method is used to File Operations like 
            searching, reading, updating and deleting.
        """
        if self.isFileExist():
            menu = "List of operations:\n\n[1] Searching\n[2] Deleting\n[3] Adding\n[4] Updating\n"
            choice = input(menu)

            if choice == "1": # searching, if choice 1
                key = input("Enter a word that you want to search: ")
                with open(self.path) as file:
                    contents = file.readlines() # reads all lines
                found_lines = [ data for data in contents if key in data ] # creates a list that if matches that desired word with content

                if len(found_lines) != 0:
                    print(f"{key} found in {len(found_lines)} lines: \n", *found_lines)
                else:
                    print(f"Nothing matched with {key} in the content!")
            
            elif choice == "2": # deleting
                key = input("Enter a word that you want to delete from the file: ")
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

    file_path = 'lorem2.json'
    ft = FileTool(file_path)
    ft.json_operations()

