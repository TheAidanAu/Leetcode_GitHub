# Queue/Stack
# Use Deque as a Queue

from collections import deque

printer_queue = deque()

#enque aka add item to the queue
printer_queue.append("taylortickets.pdf")
printer_queue.append("notes.pdf")
printer_queue.append("id.pdf")

# Use the popleft method to remove item from the front
while printer_queue:
    doc = printer_queue.popleft() #FIFO
    print(doc)

# Use list as a Stack
book_stack = []

book_stack.append("jack of hearts")
book_stack.append("2 of diamonds")
book_stack.append("10 of spades")

top_card = book_stack.pop()  # 10 of spades
print(top_card)

top_card = book_stack[-1]  # 2 of diamond
