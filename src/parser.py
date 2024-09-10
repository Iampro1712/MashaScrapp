import re
from src.custom import custom_keywords

class Parser:

    def __init__(self, message):
        try:
            upper_text = message.upper()
        except AttributeError:
            upper_text = ''
        self.message = upper_text
        self.keywords = re.compile('|'.join(custom_keywords), re.IGNORECASE)

    def find_keyword(self):
        if any(keyword in self.message for keyword in custom_keywords) == True:
            return True
        else:
            return False
        
    def parse(self):
        return self.keywords.search(self.message).group(0)
    
    def formated_keyword(self):
        return "✅ " + self.parse()