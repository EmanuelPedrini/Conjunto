from Skills import skill

#skills
fireball=skill("Fireball", "You cast a giant fireball to destroy your enemies!", 14, 0, 9,target="allenemies")
healing= skill("Healing", "You heal your wounds", 0, 5, 4,target="self")
satorogojonaooooo= skill("Deep Purple", "GOJO NOOOO", 15, 0, 12,target="enemy")
# manaflow=skill("Mana Flow", f"you use all your actual mana (0) and heal a equivalent amount.", 0, 0, 0, target="self")
lightning=skill("Lightning", "Balls", 8, 0, 5,target="allenemies")
magicspark=skill("Magic Spark", "A simple spell that every mage needs to know!", 4, 0, 3,target="enemy")
donothing=skill("Do nothing!", "You do nothing.", 0, 0, 2, target="self")
block =skill("Block", "You receive shield", 0, 0, 3, 2, target="self")
bite=skill("Toe Bite", "You bite your enemy with the strength of a lion!", 3, 0, 0, 2, target="enemy")
bloodfeast=skill("Blood Feast", "You drink the blood of your enemies!", 6, 0, 0, 7, target="allenemies")
# =skill("", "", 0, 0, 0, target="")

#lista de todas as skills
todasskills=[fireball,healing,satorogojonaooooo, lightning, magicspark, donothing]