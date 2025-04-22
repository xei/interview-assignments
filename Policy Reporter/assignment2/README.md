# Assignment 2

## Overview
To demonstrate my skills in a language other than `Python`, and to build a reusable, extensible object-oriented architecture for a generic finite state machine (FSM), I chose `Java` due to its strong typing and interface-driven design.

## Project Structure
```bash
assignment2/
├── fsm/
│   ├── State.java          # Interface for FSM states
│   └── FSM.java            # FSM engine that holds the current state
│
├── mod3/
│   ├── Mod3State.java      # Mod-3 states
│   ├── Mod3FSM.java        # Process binary strings and compute the result of a modulo-3 FSM
│   └── Main.java           # Example main program
│
├── tests/
│   └── Mod3FSMTest.java    # Unit tests using JUnit 5
│
└── README.md               # Documentation
```

## Run the program
```bash
./gradle run
```

## Run Tests
```bash
./gradlew test
```

## [BONUS]: Another efficient solution by leveraging modulo arithmetic properties
 an elegant and memory-efficient way to implement the logic of the FSM without explicitly defining the states and transitions in a traditional FSM structure. It cleverly encodes the state transitions within the arithmetic operations.

```python
def binary_mod_3(binary_str: str) -> int:
    """
    Computes the remainder of a binary number (as string) divided by 3.
    Processes bits from LSB to MSB using modulo arithmetic.

    Args:
        binary_str (str): Binary string, e.g. "1111"

    Returns:
        int: Remainder (n % 3)
    """
    remainder = 0
    current_mod = 1  # 2^0 % 3
    mod3_cycle = [None, 2, 1]  # 2^k % 3 = 1, 2, 1, 2, ...

    for bit in reversed(binary_str):
        if bit == '1':
            remainder += current_mod
        current_mod = mod3_cycle[current_mod]

    return remainder % 3
```
```python
print(binary_mod_3("1111"))  # Output: 0
print(binary_mod_3("101"))   # Output: 2
```