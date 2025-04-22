class MinStack:
#Minimum Stack
#Design a stack class that supports the push, pop, top, and getMin operations.
#MinStack() initializes the stack object.
#void push(int val) pushes the element val onto the stack.
#void pop() removes the element on the top of the stack.
#int top() gets the top element of the stack.
#int getMin() retrieves the minimum element in the stack.
#Each function should run in O(1) time.
    def __init__(self):
      self.stack = []
      self.minStack = []

    def push(self, val: int) -> None:
      self.stack.append(val) #Append to main stack
      
      if not self.minStack: #If minStack empty
          self.minStack.append(val)
      else:
        if val <= self.minStack[-1]:
          self.minStack.append(val)

    def pop(self) -> None:
      if self.stack:
        val = self.stack.pop()
        
        if self.minStack[-1] == val: #If element popped from main stack was the current minimum.
            self.minStack.pop()

    def top(self) -> int:
      if self.stack:
        return self.stack[-1]  

    def getMin(self) -> int:
      if self.minStack:
        return self.minStack[-1]

def main():
    actions = {
        "1": lambda: push_with_validation(),
        "2": myStack.pop,
        "3": lambda: print(f"Top element: {myStack.top()}"),
        "4": lambda: print(f"Minimum element: {myStack.getMin()}"),
        "5": lambda: quit_program()
    }
    while True:
      action = input("Input: 1 to push, 2 to pop, 3 for top, 4 to get min, 5 to quit: ")

      if action in actions:
        actions[action]()
      else:
        print("Invalid input. Please try again.")

def push_with_validation():
    try:
        val = int(input("Enter a number to push: "))
        myStack.push(val)
    except ValueError:
        print("Invalid input! Please enter a number.")

def quit_program():
  print("Bye!")
  exit()
  
if __name__ == "__main__":
  myStack = MinStack()
  main()