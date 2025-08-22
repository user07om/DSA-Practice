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


console.log("-----------------------------------")

const fruits = new Set();

fruits.add("Mango");
fruits.add("Apple");
fruits.add("Cherry");

// search in here.
const is_it = fruits.has("Apple");
console.log(is_it)


// for (const fruit of fruits) {
  //console.log(fruit)
// }

// it won't work, map is an array function, you can use the forEach
// fruits.map(fruit => console.log(fruit))


fruits.forEach(fruit => {
 console.log(fruit)
});


// check for dublicates [2, 1, 2, 4]
const nums = [2, 1, 2, 4]
const remDubli = (arr) => {
  const seen = new Set();
  return arr.some(n => {
      if (seen.has(n)) {
        return true;
      }
      seen.add(n)
      return false
    })
}

console.log(remDubli(nums));

// ------------
// set operatiosn [union, intersection, differeces and symatric differences]
const num1 = new Set([1, 2, 3, 4])
const num2 = new Set([3, 4, 5, 6])

const union = new Set([...num1, ...num2])
const intersection = new Set([...num1].filter(x => num2.has(x)))
const differences = new Set([...num1].filter(x => !num2.has(x)))
const simatricDiff = new Set([...num1, ...num2].filter(x => (!num1.has(x) && num2.has(x))))

console.log(union)
console.log(intersection)
console.log(differences)
console.log(simatricDiff)
