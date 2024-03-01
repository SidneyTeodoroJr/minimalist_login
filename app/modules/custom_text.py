from flet import UserControl, colors, Text

class title(UserControl):
    def __init__(self, value=str, color=colors.WHITE, size=25):
        super().__init__()
        
        self.value= value
        self.color= color
        self.size= size

    def build(self):
        return Text(   
            value= self.value,
            color= self.color,
            size= self.size
        )
    
class subtitle(UserControl):
    def __init__(self, value=str, color=colors.WHITE54, size=15):
        super().__init__()

        self.value= value
        self.color= color
        self.size= size

    def build(self):
        return Text(
            value= self.value,
            color= self.color,
            size= self.size
        )
    
class link(UserControl):
    def __init__(self, value=str, color=colors.BLUE_400, size=13):
        super().__init__()

        self.value= value
        self.color= color
        self.size= size
    
    def build(self):
        return Text(
            value= self.value,
            color= self.color,
            size= self.size
        )
    