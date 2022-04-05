from modules.dataManager import *

mir4 = MIR4()

# TESTs:
mir4.createClan('Sócria')
mir4.createClan('RedReaper')
for clan in mir4.clans:
    print(clan.name)
print('----------------', len(mir4.clans))
mir4.removeClan(mir4.clans[1])
for clan in mir4.clans:
    print(clan.name)
print('----------------', len(mir4.clans))

'''
app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
'''
