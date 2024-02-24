
item_dict = {"White": "Consumer Grade", "Light Blue": "Industrial Grade", "Blue": "Mil-Spec", "Purple": "Restricted", "Pink": "Classified", "Red": "Covert", "Yellow": "Extraordinary", "Gold": "Extraordinary", "Orange": "Contraband"}

def floatName(float):
    if float < 0.07:
        return "Factory New"
    elif float >= 0.07 and float < 0.15:
        return "Minimal Wear"
    elif float >= 0.15 and float < 0.38:
        return "Field-Tested"
    elif float >= 0.38 and float < 0.45:
        return "Well-Worn"
    else:
        return "Battle-Scarred"

class Item:
    
    def __init__(self, name, price, rarity, st, float, pattern, time_unboxed):
        self.name = name
        self.price = price
        self.rarity = rarity
        self.st = st
        self.float = float
        self.pattern = pattern
        self.time_unboxed = time_unboxed

    def __str__(self):
        global item_dict
        stattrak_str = "StatTrak™" if self.st else ""
        all_str = stattrak_str + " " + floatName(self.float)+ " " + self.name + ": " + item_dict[self.rarity] +  ", Float: " + self.float + " , Pattern: " + self.pattern + ", is currently worth: " + self.price + ". Unboxed at: " + self.time_unboxed
        return all_str
    
    
