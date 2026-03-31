from Character import character
from Skill_Data import magicspark, block, bloodfeast, bite, teleport
# from Passive_Data import
Knight = character("Knight","she","her", 7, 2, 7, 0, 3, 4, 0, 0, 0, 0, [block],[],[], 5 ,"melee", 0)
Mage = character("Mage","he", "his", 3, 1, 3, 1, 7, 7, 0, 0, 0, 0, [magicspark], [], [], 0,"melee", 5)
Vampire = character("Vampire", "she", "her", 3, 2, 5, 0, 2, 5, 0, 30, 0, 0, [bite], [], [], 0,"melee", 10 )
Penintent = character("Penitent", "He", "his", 3, 1, 8, -3, 2, 2, 0, 0, 5, 0, [], [], [], 0,"melee", 15)
Bull = character("Bull", "She", "her", 4, 2, 7, 0, 1, 2, 0, 0, 0, 5, [teleport], [],[], 0, "melee",0)
Huntress = character("Huntress", "she", "Her", 2, 7, 3, 7, 2, 3, 0, 0, 0, 0, [], [],[], 0,"melee",0)
Jammy = character("Jammy", "He", "his", 3, 3, 3, 9, 5, 3, 0, 0, 0, 0, [], [], [], 0,"melee", 10)
Mama= character("Vampire`s Mommy", "she", "her", 8, 4, 4, -4, 3, 4, 0, 20, 0, 0, [bloodfeast], [], [], 0, "melee", 20)
# Dennis = character("Dennis", "He", "his", )

allcharacters=[Knight, Mage, Vampire, Penintent, Bull, Huntress, Jammy, Mama]