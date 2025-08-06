class Stack {
  constructor() {
    this.stack = [];
  }

  push(value) {
    this.stack.push(value);
  }

  isEmpty() {
    return this.stack.length === 0;
  }

  pop() {
    return (this.isEmpty) ? this.stack.pop() : null;
  }

  peek() {
    return (this.isEmpty) ? this.stack[this.stack.length - 1] : null
  }
}


const s = new Stack();
s.push(4)
s.push(5)
console.log(s.stack)
console.log(s.peek())
console.log(s.pop())
console.log(s.isEmpty)
