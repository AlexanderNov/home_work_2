import unittest
from Item import Item
from Hub import Hub


class TestHub(unittest.TestCase):
    def setUp(self):
        self.hub = Hub()

    def test_hub_singleton(self):
        """Проверка того, что hub - синглтон"""  # небольшая документация к тесту
        self.assertTrue(Hub() is Hub())

    def test_len(self):
        """Проверка того, что при добавлении предметов меняется значение len(item)"""
        for i in range(5):
            self.hub.add_item(Item('name', 'description', 'dispatch_time', {1}), 'date')
        self.assertEqual(len(self.hub), 5)

    def test_hub_is_iterable(self):
        """Проверка того, что к предметам в hub теперь можно обращаться по hub[id]"""
        item = Item('name', 'description', 'dispatch_time', {1})
        self.hub.add_item(item, "2025-01-09")
        self.assertEqual(item, self.hub[0])

    def test_find_by_id_positive(self):
        """Проверка поиска предметов по id"""
        item = Item('name', 'description', 'dispatch_time', {"1"})
        self.hub.add_item(item, "2025-01-09")
        self.assertEqual((item._id, item), self.hub.find_by_id(item._id))

    def test_find_by_id_negative(self):
        """Проверка того, что вернется [-1, None], если ввести несуществующий id"""
        self.assertEqual([-1, None], self.hub.find_by_id(1000))

    def test_find_by_tags(self):
        """Проверка поиска предметов по тегам"""
        item = Item('name', 'description', 'dispatch_time', {"плохой"})
        self.hub.add_item(item, "2025-01-09")
        self.assertEqual([item], self.hub.find_by_tags({"плохой"}))

    def test_rm_by_id(self):
        """Проверка удаления предмета из hub по id"""
        item = Item('name', 'description', 'dispatch_time', {"плохой"})
        self.hub.add_item(item, "2025-01-09")
        before = len(self.hub)
        self.hub.rm_item(0)
        after = len(self.hub)
        self.assertTrue(after == before - 1)

    def test_rm_by_item(self):
        """Проверка удаления предмета из hub по item"""
        item = Item('name', 'description', 'dispatch_time', {"плохой"})
        self.hub.add_item(item, "2025-01-09")
        before = len(self.hub)
        self.hub.rm_item(item)
        after = len(self.hub)
        self.assertTrue(after == before - 1)

    def test_drop_items(self):
        """Проверка удаления предметов из hub по списку предметов"""
        item1 = Item('name', 'description', 'dispatch_time', {"плохой"})
        item2 = Item('name', 'description', 'dispatch_time', {"плохой"})
        item3 = Item('name', 'description', 'dispatch_time', {"плохой"})
        self.hub.add_item(item1, "2025-01-09")
        self.hub.add_item(item2, "2025-01-09")
        self.hub.add_item(item3, "2025-01-09")
        before = len(self.hub)
        items_to_drop = [item1, item3]
        self.hub.drop_items(items_to_drop)
        after = len(self.hub)
        self.assertTrue(after == before - 2)

    def test_clear_items(self):
        """Проверка того, что очищается hub от items"""
        item = Item('name', 'description', 'dispatch_time', {"плохой"})
        self.hub.add_item(item, "2025-01-09")
        self.hub.clear_items()
        self.assertEqual(0, len(self.hub))

    def test_set_date(self):
        """Проверка того, что устанавливается setter и возвращается getter дата"""
        self.hub.date = "2099-01-01"
        self.assertEqual("2099-01-01", self.hub.date)

    def test_find_by_date(self):
        """Проверка того, что по одной дате находится предмет с датой меньше или равной"""
        item = Item('name', 'description', '2025-01-15', {"плохой"})
        self.hub.add_item(item, "2025-01-09")
        self.assertEqual([item], self.hub.find_by_date('2025-01-15'))

    def test_find_by_two_date(self):
        """Проверка того, что по двум датам находится предмет с датой между или равной указанным датам"""
        item = Item('name', 'description', '2025-01-15', {"плохой"})
        self.hub.add_item(item, "2025-01-09")
        self.assertEqual([item], self.hub.find_by_date('2025-01-10', '2025-01-20'))

    def test_add_item_negative(self):
        """Проверка того, что возникает TypeError если добавлять в Hub item не класса Item"""
        itm = object
        with self.assertRaises(TypeError):
            self.hub.add_item(itm, "2025-01-09")

    def test_find_most_valuable(self):
        """Проверка поиска самого дорогого предмета в hub"""
        item1 = Item("Galaxy S101", "super puper smartphone", "2029-01-01", {"прелесть", "розовый"})
        item2 = Item("iPhone 42", "super puper iPhone", "2028-09-23", {"светящийся", "волшебный"})
        item1.cost = 60
        item2.cost = 90
        self.hub.add_item(item1, "2025-01-09")
        self.hub.add_item(item2, "2031-02-15")
        self.assertEqual([item2], self.hub.find_most_valuable())

    def test_find_most_valuable_2_items(self):
        """Проверка поиска двух самых дорогих предметов в hub"""
        item1 = Item("Galaxy S101", "super puper smartphone", "2029-01-01", {"прелесть", "розовый"})
        item2 = Item("iPhone 42", "super puper iPhone", "2028-09-23", {"светящийся", "волшебный"})
        item3 = Item("Xiaomi 77", "super puper Xiaomi", "2027-07-29", {"китайский", "надежный"})
        item1.cost = 60
        item2.cost = 90
        item3.cost = 130
        self.hub.add_item(item1, "2025-01-09")
        self.hub.add_item(item2, "2031-02-15")
        self.hub.add_item(item3, "2031-04-16")
        self.assertEqual([item3, item2], self.hub.find_most_valuable(2))


class TestItem(unittest.TestCase):
    # Реализуйте проверку того что у разных Items разные id
    def test_item_id(self):
        """Проверка того, что у разных Items разные id"""
        item1 = Item("Galaxy S101", "super puper smartphone", "2029-01-01", {"прелесть", "розовый"})
        item2 = Item("Galaxy S101", "super puper smartphone", "2029-01-01", {"прелесть", "розовый"})
        self.assertTrue(item1._id != item2._id)

    # Реализуйте проверку того что при добавлении тэгов меняется значение len(item)
    def test_len(self):
        """Проверка того, что при добавлении тэгов меняется значение len(item)"""
        item1 = Item("Galaxy S101", "super puper smartphone", "2029-01-01", {"прелесть", "розовый"})
        before = len(item1)
        item1.add_tag("красный")
        after = len(item1)
        self.assertTrue(after > before)

    # Реализуйте проверку того что если к предмету добавить два идентичных тега - их количество будет один
    def test_equal_tags(self):
        """Проверка того что если к предмету добавить два идентичных тега - их количество будет один"""
        item1 = Item("Galaxy S101", "super puper smartphone", "2029-01-01", {"красный"})
        before = len(item1)
        item1.add_tag({"красный"})
        after = len(item1)
        self.assertTrue(after == before)

    def test_set_cost(self):
        """Проверка того, что устанавливается цена"""
        item1 = Item('name', 'description', 'dispatch_time', {'0', '1', '2'})
        item1.cost = 500
        self.assertEqual(500, item1.cost)

    def test_lt(self):
        """Проверка того, что цена первого айтема меньше цены второго айтема"""
        item1 = Item('name', 'description', 'dispatch_time', {'0', '1', '2'})
        item2 = Item('name', 'description', 'dispatch_time', {'0', '1', '2'})
        item1.cost = 500
        item2.cost = 1000
        self.assertTrue(item1 < item2)

    def test_add_tags(self):
        """Проверка того, что можно добавить 2 тега"""
        item1 = Item('name', 'description', 'dispatch_time', {'0'})
        item1.add_tag({'1', '2'})
        self.assertEqual({'0', '1', '2'}, item1.get_tags())

    def test_rm_tags(self):
        """Проверка того, что можно удалить 2 тега"""
        item1 = Item('name', 'description', 'dispatch_time', {'0', '1', '2'})
        item1.rm_tag({'1', '2'})
        self.assertEqual({'0'}, item1.get_tags())

    def test_is_tagged_str(self):
        """Проверка того, что можно проверить наличие 1 тега"""
        item1 = Item('name', 'description', 'dispatch_time', {'0', '1', '2'})
        self.assertEqual(True, item1.is_tagged('1'))

    def test_is_tagged_container(self):
        """Проверка того, что можно проверить наличие сразу нескольких тегов"""
        item1 = Item('name', 'description', 'dispatch_time', {'0', '1', '2'})
        self.assertEqual(True, item1.is_tagged({'0', '1', '2'}))

    def test_copy(self):
        """Проверка того, что метод copy(self) возвращает новый item с таким же описанием, ценой и именем, но с другим id"""
        item1 = Item('name', 'description', 'dispatch_time', {'0', '1', '2'})
        item2 = item1.copy()
        self.assertEqual(item1.name, item2.name)
        self.assertEqual(item1.description, item2.description)
        self.assertEqual(item1.cost, item2.cost)
        self.assertTrue(item1._id != item2._id)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
