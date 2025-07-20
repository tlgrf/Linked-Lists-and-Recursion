# Linked Lists and Recursion Lab
A simple employee roster manager using a singly linked list and recursion.  We’ll insert ids, sum them recursively, search for a specific id, and reverse the list in-place.

## Table of contents  
- [Setup](#setup)  
- [Testing](#testing)  
- [Features](#features)    
- [Endpoints & Methods](#endpoints--methods)  

---

## Setup  
1. Fork & clone the repo  
2. Create & activate  virtual environment
   `python3 -m venv .venv`
   `source .venv/bin/activate` (MAC, Linux)
   `.\.venv\Scripts\Activate.ps1` (Windows)
3. Install pytest: `pip install pytest`

---

## Testing
To run the test suite: `pytest`

---

## Features
	•	insert_at_front(data)
insert a new node at the head of the list in O(1) time
	•	insert_at_end(data)
traverse to the tail and append a new node in O(n) time
	•	recursive_sum()
return the sum of all node data via recursion
	•	recursive_search(target)
return True if target exists in the list, else False
	•	recursive_reverse()
reverse the list in-place using a tail-recursive helper

---

## Endpoints & Methods

Method: insert_at_front | Signature: insert_at_front(data: int)| Desc: add a node to the front
Method: insert_at_end | Signature: insert_at_end(data: int)| Desc: add a node to the end

Method: recursive_sum | Signature: recursive_sum() -> int| Desc: sum all node values


Method: recursive_search | Signature: recursive_search(target) -> bool | Desc: check if target is in the list


Method: recursive_reverse | recursive_reverse()| Desc: reverse the list in-place
Method: display | Signature: display()| Desc: print the list for debugging
