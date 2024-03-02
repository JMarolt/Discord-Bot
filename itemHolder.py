

class ItemHolder:
    
    def __init__(self, name, prices, rarity, float_min, float_max, item_type, can_st):
        self.name = name
        self.prices = prices
        self.rarity = rarity
        self.float_min = float_min
        self.float_max = float_max
        self.item_type = item_type
        self.can_st = can_st

    def getName(self):
        return self.name

    def getRarity(self):
        return self.rarity

    def getPrice(self, float, st):
        if self.item_type == "Sticker":
            return self.prices[0]
        else:
            num = 0
            if float < 0.07:
                num = 1
            elif float < 0.15:
                num = 2
            elif float < 0.38:
                num = 3
            elif float < 0.45:
                num = 4
            else:
                num = 5
            if not self.item_type == "Souvenir":
                if not st:
                    num += 5
        return self.prices[num]
    
    def getFloatMin(self):
        return self.float_min
    
    def getFloatMax(self):
        return self.float_max
    
    def getItemType(self):
        return self.item_type
    
    def getST(self):
        return self.can_st
    
    
    
