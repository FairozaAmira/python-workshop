
class Text:
    
    def __init__(self, text):
        self.text = text
    
    def print_input(self):
        try:
            return print(self.text)
        except Exception as e:
            message = f"Exception in print_input: {str(e)}"
            print(message)
            raise Exception
    
