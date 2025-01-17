class Item:
    _unique_id = 0

    def __init__(self, name: str, description: str, dispatch_time: str, tags: set):
        self._id = Item._unique_id
        Item._unique_id += 1
        self.name = name
        self.description = description
        self.dispatch_time = dispatch_time
        self._tags = tags
        self._cost = 10

    def add_tag(self, tg):
        for tag in tg:
            if len(tag.strip()) > 0:
                self._tags.add(tag)

    def rm_tag(self, tg):
        for tag in tg:
            if tag in self._tags:
                self._tags.remove(tag)

    def get_tags(self):
        return self._tags

    def __str__(self):
        return f'(id={self._id}, name="{self.name}", dispatch_time="{self.dispatch_time}")'

    def __repr__(self):
        first_three_tags = ', '.join(list(self._tags)[:3])
        return f'(id={self._id}, name="{self.name}", dispatch_time="{self.dispatch_time}", первые три tags=[{first_three_tags}])'

    def __len__(self):
        return len(self._tags)

    def is_tagged(self, tags):
        if isinstance(tags, str):
            return tags in self._tags
        else:
            return all(tag in self._tags for tag in tags)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    def __lt__(self, other):
        return self.cost < other.cost

    def copy(self):
        return Item(
            name=self.name,
            description=self.description,
            dispatch_time=self.dispatch_time,
            tags=set(self._tags)
        )
