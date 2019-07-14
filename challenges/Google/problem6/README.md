# XOR Linked List

![language](https://img.shields.io/badge/C++-17-blue.svg?cacheSeconds=2592000)

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding `next` and `prev` fields, it holds a field named `both`, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an `add(element)` which adds the `element` to the end, and a `get(index)` which returns the node at `index`.

If using a language that has no pointers (such as Python), you can assume you have access to `get_pointer` and `dereference_pointer` functions that converts between nodes and memory addresses.

## Specs

### Input

`add` - `element` to add to the end of the XOR linked list

`get` - `index` of an element within the linked list

### Output

`add` - no return value, adds `element` to XOR linked list

`get` - the node at `index`

## Timing

#### Start time: 2:08PM
<!--- Work happens here --->
#### End time: 3:55PM

## Runtime Complexity

<img src="https://latex.codecogs.com/gif.latex?add-O\left(1\right)" />

<img src="https://latex.codecogs.com/gif.latex?get-O\left(n\right)" />

## Thoughts

The problem itself was pretty interesting. Took me a while to really settle on the concept of a XOR linked list, but after a few minutes, I felt confident enough to write out the code necessary.

I started with the `Node` class, which was basically just `data` and `both`. I represented `data` with `void*` because for some reason g++ and gcc weren't recognizing the `<any>` header. Weird.

Anyways, then I made the `LinkedList` class itself, with a `head`, `tail`, and `length`. Basic linked list structure.

Now when it came to `add`, I had a couple realizations:
 1. At any given point in time, `head->both` is the xor of 0 and the address of the next node. This will always be equal to the address of the next node.
 2. Likewise, `tail->both` is the xor of 0 and the address of the previous node. This will always be equal to the address of the previous node.

And since we're only adding to the end, we would just need to make a new `Node` as `node`, update `tail->both`, set `node->both` to `tail`, and set `tail` to `node`.

But at what point does `head` matter? Well, if we want to search by index, it's much more intuitive to search from `head`, but that means we would have to add an edge case in `add` for it. Hence, if `length` is 0, set `head` as well.

Traversing the XOR linked list was pretty fun in `get`. Traversal requires reference to the previous element's address, in which case an xor would reveal the address. Logically speaking, `a xor b xor a = b`, and `a xor b xor b = a`. We use this logical equality to obtain the next address and update references as we traverse each element on the way to `index`.

Now you might be wondering, _why did you take so much time_? Well, I ran into a seg fault that resulted from not incrementing `idx` in my `get` function. Not having a debugger installed on this machine made finding that bug a train wreck.