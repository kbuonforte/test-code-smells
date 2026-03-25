# Code Smells — Python Examples

A reference collection of common code smells with concrete Python examples, plus clean refactored counterparts.

## What Is a Code Smell?

A code smell is a surface-level indicator that something in the code may be poorly designed — not necessarily broken, but harder to read, maintain, or extend than it should be. The term was popularized by Martin Fowler in *Refactoring*.

## Examples

| File | Smell | Description |
|------|-------|-------------|
| `python/god_class.py` | **God Class** | One class that owns all state and behavior for an entire application |
| `python/long_method.py` | **Long Method** | A single function that validates, calculates, formats, and sends — doing too many things |
| `python/duplicate_code.py` | **Duplicate Code** | The same validation or logic copy-pasted across multiple functions |
| `python/deep_nesting.py` | **Deep Nesting** | Heavily indented conditionals that make control flow hard to follow |
| `python/feature_envy.py` | **Feature Envy** | A method that is more interested in another class's data than its own |
| `python/data_clumps.py` | **Data Clumps** | Groups of variables that always travel together but were never given a proper type |
| `python/primitive_obsession.py` | **Primitive Obsession** | Using raw strings/ints for domain concepts like money, status, or identity |
| `python/switch_statements.py` | **Switch Statements** | Long if/elif chains on a type field that should be replaced with polymorphism |
| `python/dead_code.py` | **Dead Code** | Unreachable branches, unused variables, and commented-out logic left in the codebase |
| `python/shotgun_surgery.py` | **Shotgun Surgery** | A single change requires edits scattered across many unrelated files or classes |
| `python/inappropriate_intimacy.py` | **Inappropriate Intimacy** | Two classes that reach into each other's internals, creating tight coupling |

## Clean Counterparts

| File | Description |
|------|-------------|
| `python/clean_order_processing.py` | Refactored order processing using dataclasses, enums, and single-responsibility functions |
| `python/clean_payment.py` | Refactored payment handling with clear types and separated concerns |

## Further Reading

- *Refactoring: Improving the Design of Existing Code* — Martin Fowler
- *Clean Code* — Robert C. Martin
- [Refactoring Guru — Code Smells](https://refactoring.guru/refactoring/smells)
