class Python:
    
    def __init__(self):
        self.name = "python"
        
    def lang(self):
        return self.name + "Language"
    
    def difficulty(self):
        self.level = "hard"
        return self.level
    

user = Python()
print(user.lang())