class KeywordNotFoundError(Exception):
    """Custom exception raised when a keyword is not found in the file."""
    def __init__(self, keyword):
        super().__init__(f"Keyword '{keyword}' not found in the file.")

class File_helper:
    def __init__(self,path):
        self.content = ""
        self.path = path

    def read_file(self,path):
        with open(path, 'r') as file:
            self.content = file.read()
        return self.content
        
    def find_file_with_keyword(self,keyword) -> String:
        with open(self.path, 'r') as file:
            for line in file:
                if keyword in line:
                    return line
        raise KeywordNotFoundError(keyword)







    pass