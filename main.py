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
hub.add_item(item5, "2027-09-01")


# Выбросите все объекты с названиями начинающиеся на "a" или "A", записав их в отдельный лист A
A = []
to_drop = []
for item in hub.get_all_items():
    if item.name.lower().startswith('a'):
        A.append(item)
        to_drop.append(item)

hub.drop_items(to_drop)
print(A)
print(hub)

# Выбросите все объекты с датой отправки раньше чем дата в hub, записав их в отдельный лист Outdated
hub.add_item(item1, "2025-01-09")
hub.add_item(item2, "2031-02-15")
hub.add_item(item3, "2031-04-16")
hub.add_item(item4, "2032-09-01")
hub.add_item(item5, "2027-09-01")
Outdated = []
to_drop = []
for item in hub.get_all_items():
    if item.dispatch_time < hub.date:
        Outdated.append(item)
        to_drop.append(item)

hub.drop_items(to_drop)
print(Outdated)
print(hub)

#Выбросите топ-3 объектов из hub, записав их в MostValuable Оставшиеся на складе объекты запишите в Others
item1 = Item("Galaxy S101", "super puper smartphone", "2029-01-01", {"прелесть", "розовый"})
item2 = Item("iPhone 42", "super puper iPhone", "2028-09-23", {"светящийся", "волшебный"})
item3 = Item("Xiaomi 77", "super puper Xiaomi", "2027-07-29", {"китайский", "надежный"})
item4 = Item("TVbox 2002", "color TV", "2025-05-30", {"японский", "устаревший"})
item5 = Item("Kettle 2000", "it is hot", "2020-09-07", {"японский", "огромный"})
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
hub.add_item(item5, "2027-03-11")

MostValuable = hub.find_most_valuable(3)
Others = []

for item in hub.get_all_items():
    if item not in hub.find_most_valuable(3):
        Others.append(item)

print(MostValuable)
print(Others)
