from Character import character
from Skill_Data import healing, fireball

Knight = character("Knight","She","her",5, 2, 5, 0, 3, 3, 0, 0, 0, 0, [healing], [], 0 )
Mage = character("Mage","he", "His", 3, 3, 3, 1, 5, 5, 0, 0, 0, 0, [fireball], [], 5)
Vampire= character("Vampire", "She", "her", 4, 2, 6, -1, 2, 2, 0, 20, 0, 0, [], [], 0 )
Penintent= character("Penitent", "He", "his", 2, 1, 8, -3, 1, 1, 0, 0, 5, 0, [], [], 0)
Bull=character("Bull", "She", "her", 4, 2, 6, 0, 1, 2, 0, 0, 0, 5, [], [], 0)
Huntress=character("Huntress", "She", "Her", 2, 6, 4, 4, 3, 3, 0, 0, 0, 0, [], [], 10 )
Jammy=character("Jammy", "He", "His", 3, 3, 3, 20, 6, 3, 0, 0, 0, 0, [], [], 15)

allcharacters=[Knight, Mage, Vampire, Penintent, Bull, Huntress, Jammy]