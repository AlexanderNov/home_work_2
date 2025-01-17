from datetime import datetime
from Item import Item


class Hub:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Hub, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._items = []
        self._date = ""

    def add_item(self, item, date):
        self._date = date
        """Добавляет новый Item в список, если он является экземпляром Item или его наследников."""
        if isinstance(item, Item):
            self._items.append(item)
        else:
            raise TypeError('Элемент должен быть экземпляром класса Item или его наследниками.')

    def get_all_items(self):
        return self._items

    def get_item_by_id(self, id):
        for item in self._items:
            if item._id == id:
                return item
        return None

    def __str__(self):
        return f'Все предметы на складе items={self._items}, date="{self._date}"'

    def __repr__(self):
        first_three_items = ', '.join(
            str(item) for item in self._items[:3])  # поставил str(item) чтобы не выводились теги
        return f'Первые 3 предмета на складе items=[{first_three_items}]'

    def __len__(self):
        return len(self._items)

    def __getitem__(self, i):
        return self._items[i]

    def find_by_id(self, i):
        """
        Возвращает предмет по указанному id. Если не найден, то вернет [-1, None]
        """
        for item in self._items:
            if item._id == i:
                return i, item
        return [-1, None]

    def find_by_tags(self, tags):
        """
        Возвращает список предметов, содержащих все указанные теги.
        """
        matching_items = []
        for item in self._items:
            if all(item.is_tagged(tag) for tag in tags):
                matching_items.append(item)
        return matching_items

    def rm_item(self, i):
        """Удаляет предмет по номеру (i - int) или самому предмету (i - Item)."""
        if isinstance(i, int):
            del self._items[i]
        elif isinstance(i, Item):
            if i in self._items:
                self._items.remove(i)
        else:
            raise ValueError('Неверный тип аргумента.')

    def drop_items(self, items_to_drop):
        """Удаляет все предметы из items_to_drop, если они существуют в хранилище."""
        for item in items_to_drop:
            if item in self._items:
                self._items.remove(item)

    def clear_items(self):
        self._items = []

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def find_by_date(self, *dates):
        """Ищет предметы по одной дате (dispatch_time <= date) или двум датам(start_date <= dispatch_time <= end_date)."""
        if len(dates) == 1:
            end_date = datetime.strptime(dates[0], '%Y-%m-%d')
            return [item for item in self._items if datetime.strptime(item.dispatch_time, '%Y-%m-%d') <= end_date]
        elif len(dates) == 2:
            start_date, end_date = dates
            return [item for item in self._items if
                    datetime.strptime(start_date, '%Y-%m-%d') <= datetime.strptime(item.dispatch_time,
                                                                                   '%Y-%m-%d') <= datetime.strptime(
                        end_date, '%Y-%m-%d')]
        else:
            raise ValueError('Передано неправильное количество аргументов.')

    def find_most_valuable(self, amount=1):
        """Находит первые amount самых дорогих предметов на складе. Если предметов на складе меньше чем amount, то возвращает все"""
        sorted_items = sorted(self._items, key=lambda x: x.cost, reverse=True)
        return sorted_items[:amount]
