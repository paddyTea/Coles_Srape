import re
from bs4 import BeautifulSoup


class Good:
    def __init__(self,name,price,price_per_100,nutritionInfo):
        self.name = name
        self.price = str_to_float(price)
        self.price_per_100 = str_to_float(price_per_100)
        self.weight_in_100s = self.price/self.price_per_100
        self.nutritionInfo = nutritionInfo

    def type_check(self):
        print("Price: ",type(self.price), self.price)
        print("Price Per 100: ", type(self.price_per_100), self.price_per_100)
        print("Weight Per 100: ", type(self.weight_in_100s), self.weight_in_100s)
        print("Nutrition Info: ",type(self.nutritionInfo))

    def protein(self):
        protein = self.nutritionInfo[0][1]
        numberlist = re.findall(r'\d+', protein)
        return str_to_float(protein)

    def calories(self):
        calories = self.nutritionInfo[2][1]
        numberlist = re.findall(r'\d+', calories)
        return str_to_float(calories)

    # def protein_per_dollar(self):
        
        



def str_to_float(string):
    numberList = re.findall(r'\d+', string)
    if len(numberList) == 3:
        num = float(numberList[0]) + float(numberList[1])/100
        return num/10
    elif len(numberList) == 2:
        return float(numberList[0]) + float(numberList[1])/10
    else :
        return float(numberList[0])
    

def is_food(soup):
    if "nutrition" in soup:
        return True
    else: return False