class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return (len(self.collection) + self.items_per_page - 1) // self.items_per_page

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        if page_index < self.page_count() - 1:
            return self.items_per_page
        return len(self.collection) % self.items_per_page or self.items_per_page

    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        return item_index // self.items_per_page

test = PaginationHelper([1, 2, 3, 4], 1)
print(test.page_item_count(3))