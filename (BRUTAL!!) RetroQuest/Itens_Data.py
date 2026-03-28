from Itens import item
#weapons
rustysword=item(name="Rusty sword", slot="Weapon",  bonus={"dex": 2}, atkform="melee")
iron_sword = item(name="Iron Sword", slot="Weapon", bonus={"strg": 2}, atkform="melee")
butchers_cleaver = item(name="Butcher's Cleaver", slot="Weapon", bonus={"vit": 2}, atkform="melee")

#lista com todas as weapons
todasaarmas=[rustysword, iron_sword, butchers_cleaver]

#armors
torn_clothes = item("Torn Clothes", "Armor", bonus={"vit": 2} )
leather_armor = item("Leather Armor", "Armor", bonus={"vit": 2} )
chainmail = item("Chainmail", "Armor", bonus={"vit": 2})

#lista com todas as armaduras
todasasarmors=[torn_clothes, leather_armor, chainmail]

#acsessories
old_ring = item("Old Ring", "Accessory",bonus={"strg": 1})
mana_pendant = item("Mana Pendant", "Accessory",bonus={"intel": 2} )
lucky_charm = item("Lucky Charm", "Accessory", bonus={"luck": 2})

#lista com todos
todososacesssorios=[old_ring, mana_pendant, lucky_charm]

#lista com todos os equipamentos
todososequipamentos = todasaarmas + todososacesssorios + todasasarmors