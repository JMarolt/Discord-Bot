class Player:
#add inventory later when I add unique cases

    def __init__(self, id):
        self.id = id
        self.inventory = []
        self.stats = {"Balance": 197.5, "Total Cases Opened": 0, "Total Winnings": 0, "Blue": 0, "Purple": 0, "Pink": 0, "Red": 0, "Yellow": 0}

    def getBalance(self):
        return self.stats["Balance"]
    
    def getMemberID(self):
        return self.id
    
    def setBalance(self, newBalance):
        self.stats["Balance"] = newBalance

    def getStats(self):
        return self.stats
    
    def setStats(self, new_stats):
        self.stats = new_stats

    def printInventory(self, page):
        start_index = page * 10
        temp_inv = self.inventory[start_index:start_index + 10]
        for item in temp_inv:
            print(item)

    # def opened_case(self, rarity, amount_won, item):
    #     self.stats["Total Cases Opened"] += 1
    #     self.stats[rarity] += 1
    #     self.stats["Total Winnings"] += amount_won
    #     self.inventory.append(item)

    def opened_case(self, rarity, amount_won):
        self.stats["Total Cases Opened"] += 1
        self.stats[rarity] += 1
        self.stats["Total Winnings"] += amount_won

    def get_stats(self, nick):
        return """{}'s lifetime statistics 
        Current Balance: {}
        Total Cases Opened: {}
        Total Amount Spent: {}
        Total Winnings: {}
        Net gain: {}
        Blues Spun: {}
        Purples Spun: {}
        Pinks Spun: {}
        Reds Spun: {}
        Golds Spun: {}
        """.format(nick, self.stats["Balance"], self.stats["Total Cases Opened"], round(self.stats["Total Cases Opened"] * 2.5, 2), round(self.stats["Total Winnings"], 2), round((self.stats["Total Winnings"]), 2) - round(self.stats["Total Cases Opened"] * 2.5, 2), self.stats["Blue"], self.stats["Purple"], self.stats["Pink"], self.stats["Red"], self.stats["Yellow"])

def load_from_file(filename):
    temp_players = []
    delimiter = '\n'
    with open(filename, 'r') as file:
        if file.readable() and len(file.read()) > 0:
            file.seek(0)
            new_player = None
            stats = {}
            for line in file:
                line = line.rstrip('\n')
                if not ':' in line:
                    if not new_player == None:
                        new_player.setStats(stats)
                        temp_players.append(new_player)
                    new_player = Player(int(line))
                    stats = {}
                else:
                    key, value = line.strip().split(': ', 1)
                    key = str(key)
                    value = float(value)
                    stats[key] = value
            new_player.setStats(stats)
            temp_players.append(new_player)
            return temp_players
        else:
            print("File is empty. No data to load.")
            return []
        
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for item in data:
            id = str(item.getMemberID())
            file.write(id + "\n")
            for key, value in item.getStats().items():
                file.write(str(key) + ": " + str(value) + "\n")