from Item import Item
from Hub import Hub

item1 = Item("Galaxy S101", "super puper smartphone", "2029-01-01", {"прелесть", "розовый"})
item2 = Item("iPhone 42", "super puper iPhone", "2028-09-23", {"светящийся", "волшебный"})
item3 = Item("Xiaomi 77", "super puper Xiaomi", "2027-07-29", {"китайский", "надежный"})
item4 = Item("TVbox 2002", "color TV", "2025-05-30", {"японский", "устаревший"})
item5 = Item("Kettle 2000", "it is hot", "2020-09-07", {"японский", "огромный"})

item1.add_tag({"красный", "легкий"})
item1.add_tag({"хрупкий"})
item1.rm_tag({"голубой"})

item1.cost = 60
item2.cost = 20
item3.cost = 30
item4.cost = 40
item5.cost = 50


hub = Hub()
hub.add_item(item1, "2025-01-09")
hub.add_item(item2, "2031-02-15")
hub.add_item(item3, "2031-04-16")
hub.add_item(item4, "2032-09-01")
hub.add_item(item5, "2032-09-01")


print (hub.find_most_valuable(3))

#print (hub.find_by_date("2020-09-24", "2028-10-07"))
"""
print(hub.find_by_id(1))

for x in range(5):
    print(hub[x])

#hub.rm_item(item3)

items_to_drop = [item1, item3, item5]
hub.drop_items(items_to_drop)

for x in range(2):
    print(hub[x])
"""

#print(hub.get_item_by_id(1))
#print(hub.get_all_items())
#print(item2)
#print(len(item1))
#print(hub)
#hub.clear_items()
#print(hub)
#print(len(hub))
#print(hub.__str__())
#print(hub.__repr__())