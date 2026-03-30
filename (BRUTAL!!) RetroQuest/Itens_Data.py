from Itens import item
#weapons
rustysword=item(name="Rusty sword", slot="Weapon",  bonus={"dex": 2, "atkdmgbonus": 3}, atkform="melee")
iron_sword = item(name="Iron Sword", slot="Weapon", bonus={"strg": 2, "atkdmgbonus": 3}, atkform="melee")
butchers_cleaver = item(name="Butcher's Cleaver", slot="Weapon", bonus={"vit": 3, "atkdmgbonus": 2}, atkform="melee")
crossbow=item(name="Crossbow", slot="Weapon", bonus={"atkdmgbonus": 5}, atkform="ranged")
throwknife=item(name="Throw Knife", slot="Weapon", bonus={"atkdmgbonus": 3, "dex": 2}, atkform="ranged")

# crossbow=item(name="", slot="Weapon", bonus={"":}, atkform="")
# crossbow=item(name="", slot="Weapon", bonus={"":}, atkform="")
#lista com todas as weapons
todasaarmas=[rustysword, iron_sword, butchers_cleaver, crossbow, throwknife]

#armors
torn_clothes = item("Torn Clothes", "Armor", bonus={"thorns": 3} )
leather_armor = item("Leather Armor", "Armor", bonus={"vit": 2} )
chainmail = item("Chainmail", "Armor", bonus={"armor": 3})

#lista com todas as armaduras
todasasarmors=[torn_clothes, leather_armor, chainmail]

#acsessories
old_ring = item("Old Ring", "Accessory",bonus={"strg": 2})
mana_pendant = item("Mana Pendant", "Accessory",bonus={"intel": 2} )
lucky_charm = item("Lucky Charm", "Accessory", bonus={"luck": 2})

#lista com todos
todososacesssorios=[old_ring, mana_pendant, lucky_charm]

#lista com todos os equipamentos
todososequipamentos = todasaarmas + todososacesssorios + todasasarmors