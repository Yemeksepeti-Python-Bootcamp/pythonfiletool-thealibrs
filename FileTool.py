import csv,json
from pathlib import Path

class FileTool:
    # List of exceptions message
    NO_FILE_EXCEPTION = "There is no file in the given path!"
    UNMATCHED_FILE_TYPE_EXCEPTION = "Unmatched file type!"
    INVALID_OPERATION_TYPE_EXCEPTION = "Invalid operation type!"

    # List of menu message
    JSON_OPERATIONS_MENU = "List of operations:\n\n[1] JSON to TXT \n[2] TXT to JSON\n"
    FILE_OPERATIONS_MENU = "List of operations:\n\n[1] Searching\n[2] Deleting\n[3] Adding\n[4] Updating\n"

    # List of input messages
    ASK_FOR_TXT_FILE_NAME = "Enter file name for txt file: "
    ASK_FOR_JSON_FILE_NAME = "Enter file name for json file: "
    ASK_FOR_DELETE = "Enter a word that you want to delete from the file: "
    ASK_FOR_SEARCH = "Enter a word that you want to search: "
    ASK_FOR_ADD = "Enter anything that you want to add: "

    # List of output messages
    SUCCESS_MESSAGE = "Operation Succes!"
    NO_MATCH_FOR_SEARCH = "Nothing matched in the content!"
    

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
        choice = input(FileTool.JSON_OPERATIONS_MENU)

        if choice == "1":
            if Path(self.path).suffix == ".json": # checks whether file is a json file or not
                if self.isFileExist(): # checks whether file exits
                    with open(self.path,"r") as json_file: # opens json file
                        json_content = json.load(json_file) # takes whole contents of json file

                    new_file_name = input(FileTool.ASK_FOR_TXT_FILE_NAME)
                    with open(new_file_name+".txt","w+") as new_file:
                        new_file.write(str(json_content))

                    print(FileTool.SUCCESS_MESSAGE)
                else:
                    print(FileTool.NO_FILE_EXCEPTION)
            else:
                print(FileTool.UNMATCHED_FILE_TYPE_EXCEPTION)

        elif choice == "2":
            if Path(self.path).suffix == ".txt":
                if self.isFileExist():
                    file_content = {}
                    with open(self.path) as file:
                        for line in file:
                            command, description = line.strip().split(None, 1)
                            file_content[command] = description.strip()
                        
                    new_file_name = input(FileTool.ASK_FOR_JSON_FILE_NAME)

                    with open(new_file_name+".json","w") as file:
                        json.dump(file_content,file,indent = 4, sort_keys = False)
                    print(FileTool.SUCCESS_MESSAGE)
                else:
                    print(FileTool.NO_FILE_EXCEPTION)
            else:
                print(FileTool.UNMATCHED_FILE_TYPE_EXCEPTION)
        else:
                print(FileTool.INVALID_OPERATION_TYPE_EXCEPTION)

    def file_operations(self):
        """
            This method is used to File Operations like 
            searching, reading, updating and deleting.
        """
        if self.isFileExist():
            choice = input(FileTool.FILE_OPERATIONS_MENU)

            if choice == "1": # searching, if choice 1
                key = input(FileTool.ASK_FOR_SEARCH)
                with open(self.path) as file:
                    contents = file.readlines() # reads all lines
                found_lines = [ data for data in contents if key in data ] # creates a list that if matches that desired word with content

                if len(found_lines) != 0:
                    print(f"{key} found in {len(found_lines)} lines: \n", *found_lines)
                else:
                    print(FileTool.NO_MATCH_FOR_SEARCH)
            
            elif choice == "2": # deleting
                key = input(FileTool.ASK_FOR_DELETE)
                current_file = open(self.path)
                updated_file = open("updated_"+self.path,"w")
                
                for line in current_file:
                    if key in line:
                        updated_file.write(line.replace(key,""))
                    else:
                        print(FileTool.NO_MATCH_FOR_SEARCH)
                        break
                current_file.close()
                updated_file.close()
                

            elif choice == "3":
                key = input(FileTool.ASK_FOR_ADD)
                with open(self.path, "a+") as file:
                    file.write(key)
                print(FileTool.SUCCESS_MESSAGE)
            
            elif choice == "4":
                pass
                
            else:
                print(FileTool.INVALID_OPERATION_TYPE_EXCEPTION)
        else:
            print(FileTool.NO_FILE_EXCEPTION)


if __name__ == "__main__":

    file_path = 'lorem.txt'
    ft = FileTool(file_path)
    ft.json_operations()

