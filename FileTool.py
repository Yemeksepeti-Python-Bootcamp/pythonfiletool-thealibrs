import csv,json

class FileTool:
    def __init__(self, path, fields = []):
        self.path = path
        self.fields = fields


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
        menu = "List of operations:\n\n[1] Searching\n[2] Deleting\n[3] Adding\n[4] Updating\n"
        choice = input(menu)

        # searching if choice 1
        if choice == "1":
            key = input("Enter a word that you want to search: ")
            with open(self.path) as file:
                # reads all lines
                contents = file.readlines()
            
            # creates a list that if matches that desired word with content
            found_lines = [ data for data in contents if key in data ]

            print(f"{key} found in {len(found_lines)} lines: \n", *found_lines)


       






ft = FileTool('C:\\Users\\BarisAyten\\Desktop\\pythonfiletool-thealibrs\\lorem.txt')

ft.file_operations()

