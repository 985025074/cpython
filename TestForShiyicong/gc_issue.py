class BaseNode:
    def __del__(self):
        print("next", BaseNode.next)
        print("del", self)


BaseNode.next = BaseNode()
BaseNode.next.next = BaseNode()