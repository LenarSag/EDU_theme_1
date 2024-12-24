from typing import Optional


class ObjList:
    def __init__(self, data) -> None:
        self.__data = data
        self.__prev: Optional["ObjList"] = None
        self.__next: Optional["ObjList"] = None

    def get_data(self):
        return self.__data

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next

    def set_data(self, data):
        self.__data = data

    def set_prev(self, obj: Optional["ObjList"]):
        self.__prev = obj

    def set_next(self, obj: Optional["ObjList"]):
        self.__next = obj


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[ObjList] = None
        self.tail: Optional[ObjList] = None

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head = self.tail = obj
            return

        self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj

    def remove_obj(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.tail = self.tail.get_prev()
        if self.tail:
            self.tail.set_next(None)

    def get_data(self):
        current = self.head
        nodes_list = []
        while current:
            nodes_list.append(current.get_data())
            current = current.get_next()

        return nodes_list


# lst = LinkedList()

# lst.add_obj(ObjList("1"))
# lst.add_obj(ObjList("2"))
# lst.add_obj(ObjList("3"))
# res = lst.get_data()

# print("check add obj", res)

# lst.remove_obj()
# res = lst.get_data()

# print("check remove obj once", res)

# lst.remove_obj()
# lst.remove_obj()
# lst.remove_obj()
# res = lst.get_data()

# print("check remove all objs", res)
