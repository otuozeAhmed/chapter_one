class Python:
    
    def __init__(self):
        self.name = "python"
        
    def lang(self):
        return self.name + "Language"
    

user = Python()
print(user.lang())