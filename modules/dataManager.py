if __name__ == '__main__':
    import sqlite3

class Player:
    def __init__(self, name):
        self.name = name
        self.occupation = None
        self.level = 0
        self.power = 0
        self.position = None

class Week:
    def __init__(self):
        pass

class Clan:
    def __init__(self, name):
        self.name = name
        self.lider = []
        self.elders = []
        self.members = []
        self.newMembers = []
        self.weeks = []

    def createWeek(self):
        pass

class MIR4:
    def __init__(self):
        self.clans = []
        self.noClanPlayers = []

    def saveData(self):
        # SALVAR ESSE OBJETO "SELF".
        pass

    def loadData(self):
        # CARREGAR ESSE OBJETO "SELF".
        pass
    
    def createClan(self, name):
        '''Create a clan'''
        clan = Clan(name)
        self.clans.append(clan) # DEPOIS POR VERIFICAÇÃO SE JÁ EXISTE NA LISTA.
    
    def removeClan(self, clan):
        self.clans.remove(clan)
    
    def addNoClanPlayer(self, player):
        self.noClanPlayers.append(player)
    
    def removeNoClanPlayer(self, player):
        self.noClanPlayers.remove(player)

# ------> EDITAR, APAGAR
# class clan
'''
    name (ex Sócria)
    players
    lider
    elders
    playersNumber (ex 50)
    weekResources
'''
# class week
'''
    number (ex 1)
    firstDay (ex 2022-03-13)
    players
    playersNumber (ex 50)
    gold
    fund
    darksteel
    energy
'''
def verDepois():
    database = sqlite3.connect('database.db')
    clanName = 'Sócria'
    database.cursor().execute('CREATE TABLE ' + clanName + ' (week text, gold integer, fund integer, darksteel integer, energy integer)')

# week01-2022-03-13 (name text, gold integer, fund integer, darksteel integer, energy integer)
# week02-2022-03-20
# week03-2022-03-27
