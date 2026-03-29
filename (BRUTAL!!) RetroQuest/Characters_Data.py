from Character import character
from Skill_Data import healing, fireball

Knight = character("Knight","she","her",5, 2, 5, 0, 3, 3, 0, 0, 0, 0, [healing],[],[],"melee", 0)
Mage = character("Mage","he", "his", 3, 3, 3, 1, 5, 5, 0, 0, 0, 0, [fireball], [], [],"melee", 5)
Vampire = character("Vampire", "she", "her", 4, 2, 6, -1, 2, 2, 0, 20, 0, 0, [], [], [],"melee", 10 )
Penintent = character("Penitent", "He", "his", 2, 1, 8, -3, 1, 1, 0, 0, 5, 0, [], [], [],"melee", 15)
Bull = character("Bull", "She", "her", 4, 2, 6, 0, 1, 2, 0, 0, 0, 5, [], [],[],"melee",0)
Huntress = character("Huntress", "she", "Her", 2, 6, 4, 4, 3, 3, 0, 0, 0, 0, [], [],[],"melee",0)
Jammy = character("Jammy", "He", "she", 3, 3, 3, 7, 6, 3, 0, 0, 0, 0, [], [], [],"melee", 10)
# Dennis = character("Dennis", "He", "his", )

allcharacters=[Knight, Mage, Vampire, Penintent, Bull, Huntress, Jammy]