---
title: "Chapter 1 Terms"
tags: [c_o_m_p_u_t_a_t_i_o_n_a_l_t_h_i_n_k_i_n_g, f_o_u_n_d_a_t_i_o_n_a_l_c_o_n_c_e_p_t_s, c_h_a_p_t_e_r_1, p_y_t_h_o_n_b_a_s_i_c_s]
created: 2025-04-16
aliases: []
cssclass: []
---
## 1. Declarative Knowledge

**Definition:**  
Declarative knowledge—often called "knowing that"—refers to factual information or propositions that one can state explicitly. For example, knowing that Paris is the capital of France is declarative knowledge. It is stored in memory as facts and can be communicated using declarative sentences.

**Visual Aid:**  
[Facts] │ ▼ "Paris is the capital of France"

**Sources:**  
– Wikipedia: [Declarative knowledge](https://en.wikipedia.org/wiki/Declarative_knowledge)  
– Merriam-Webster

---

## 2. Imperative Knowledge

**Definition:**  
Also known as procedural knowledge or "know-how," imperative knowledge is the practical usage or ability to execute a task. It involves the steps, techniques, or skills required to perform an action (for example, knowing how to ride a bicycle).

**Visual Aid:**  
[Know-How] ┌───────────────┐ │ Steps/Skills │ └───────────────┘ │ ▼ “How to ride a bike”

**Sources:**  
– Wikipedia: [Procedural knowledge](https://en.wikipedia.org/wiki/Procedural_knowledge)

---

## 3. Algorithm

**Definition:**  
An algorithm is a finite, ordered sequence of well-defined instructions for solving a problem or performing a computation. It is the backbone of problem-solving in both mathematics and computer science.

**Visual Aid:**  
[Input] → [Step 1] → [Step 2] → ... → [Step N] → [Output]

**Sources:**  
– Britannica  
– Wikipedia: [Algorithm](https://en.wikipedia.org/wiki/Algorithm)

---

## 4. Computation

**Definition:**  
Computation is the process of performing mathematical calculations or processing data according to a defined procedure—a key function carried out by computers and calculators.

**Visual Aid:**  
[Data/Input] │ ▼ [Computation/Calculation] │ ▼ [Result/Output]

**Sources:**  
– Merriam-Webster  
– Wikipedia: [Computation](https://en.wikipedia.org/wiki/Computation)

---

## 5. Fixed-Computer Program

**Definition:**  
A fixed (or fixed-program) computer is one whose set of instructions is hardware-wired or permanently defined. Such computers perform only a specific task, with no facility to change the program by loading new instructions into memory.

**Visual Aid:**  
Hardware with Embedded Instruction Set ┌─────────────────────────────┐ │ Fixed Program Computer │ │ (One specific task only) │ └─────────────────────────────┘

**Sources:**  
– History of Computing (Turing Archive)

---

## 6. Stored Program Computer

**Definition:**  
A stored program computer is built on the principle that both data and program instructions are stored together in a computer’s memory. This flexibility allows the same hardware to execute a variety of software applications.

   +----------------------+
   |  Memory              |
   |  ------------------  |
   |  [Instructions/Data] |
   +----------------------+
           ↑
           │
       [CPU executes]

**Sources:**  
– John von Neumann Architecture

---

## 7. Interpreter

**Definition:**  
An interpreter is a computer program that reads and executes code line by line. Unlike a compiler, which translates the entire source code into machine code before running, an interpreter directly executes the high-level instructions.

**Visual Aid:**  
[Source Code] │ ▼ [Interpreter] → Executes → [Runtime Behavior]

**Sources:**  
– Wikipedia: [Interpreter](https://en.wikipedia.org/wiki/Interpreter_(computing))

---

## 8. Program Counter

**Definition:**  
The program counter is a CPU register that holds the memory address of the next instruction to be fetched and executed. It is automatically updated (typically incremented) as instructions are read sequentially from memory.

**Visual Aid:**  
 ┌─────────────────────┐
 │     CPU             │
 │  ┌─────────────┐    │
 │  │ Program     │◄───┤
 │  │  Counter    │    │
 │  └─────────────┘    │
 └─────────────────────┘
      │       
      ▼
[Next Instruction Address]

**Sources:**  
– Modern CPU Architecture

---

## 9. Flow of Control

**Definition:**  
The flow of control (or control flow) in a program is the order in which individual statements, instructions, or function calls are executed. It is dictated by structures such as loops, conditionals, and jump statements.

**Visual Aid:**  
[Start] │ ▼ [Process A] │ ┌─────────┐ └→ [Decision]───Yes→ [Process B] │ └─No→ [Process C] │ ▼ [End]

**Sources:**  
– Programming textbooks, Python docs

---

## 10. Flowchart

**Definition:**  
A flowchart is a diagrammatic representation that illustrates a process, algorithm, or workflow using standardized symbols (such as rectangles for processes, diamonds for decisions) connected by arrows showing the sequence.

**Visual Aid:**  
[Start] │ ▼ [Process] │ ▼ [Decision?]──Yes→[Process] │ No │ ▼ [End]

**Sources:**  
– Visual Programming Guides

---

## 11. Programming Language

**Definition:**  
A programming language is a formal language comprising a set of instructions that produce various kinds of output. It is used to implement algorithms and interact with the hardware via an interpreter or compiler.

**Visual Aid:**  
   [Programmer]
        │
        ▼
[Programming Language Code] │ ▼ [Computer]

**Sources:**  
– CS50, Python.org

---

## 12. Universal Turing Machine

**Definition:**  
A Universal Turing Machine (UTM) is a theoretical model of computation that can simulate any other Turing machine. It lays the foundation for the modern stored-program computer by demonstrating that one machine can execute any algorithm when provided with a proper encoded program and input.

**Visual Aid:**  
  [Encoded Turing Machine Data]
           │
           ▼
┌───────────────────────────┐
│ Universal Turing Machine  │
└───────────────────────────┘
           │
           ▼
   [Simulated Computation]
  
**Sources:**  
– Alan Turing, Computability theory

---

## 13. Church-Turing Thesis

**Definition:**  
The Church-Turing thesis is a hypothesis stating that any function which would naturally be regarded as computable can be computed by a Turing machine. It bridges informal notions of "effective calculability" with formal models of computation.

**Visual Aid:**  
     Effective Calculability
              │
              ▼
     [Turing Computable]
     (Church-Turing Thesis)
    
**Sources:**  
– Stanford Encyclopedia of Philosophy

---

## 14. Turing Completeness

**Definition:**  
A system (such as a programming language or computational model) is said to be Turing complete if it can simulate any Turing machine. In practical terms, Turing-complete systems can be used to solve any problem that a Turing machine can, assuming unlimited memory and time.

**Visual Aid:**  
[System with Full Capability] can simulate [Universal Turing Machine] ⇒ Turing Complete

**Sources:**  
– Wikipedia: [Turing completeness](https://en.wikipedia.org/wiki/Turing_completeness)

---

## 15. Literals

**Definition:**  
Literals are fixed, explicit values (like numbers, characters, or strings) that appear directly in source code. They represent constant values that do not change at runtime.

**Visual Aid:**  
```python
int num = 42;    // 42 is a literal
String word = "Hello";  // "Hello" is a literal
**Sources:**  
– Python docs  
– Java Language Specification

---

## 16. Infix Operators

**Definition:**  
Infix operators sit between two operands. A common example is the addition operator (+), as in the expression `2 + 2`. This notation is widely used in mathematics and many programming languages.

**Visual Aid:**

```
   Operand1  Operator  Operand2
       2        +         2
```

**Sources:**  
– Wikipedia: [Infix notation](https://en.wikipedia.org/wiki/Infix_notation)

---

## 17. Syntax

**Definition:**  
Syntax is the set of rules that governs the structure and arrangement of symbols in expressions, statements, or programs. It defines the correct format and structure that must be followed for code (or language) to be considered well–formed.

**Visual Aid:**

```c
// Valid Syntax
if (x > 5) { doSomething(); }

// Invalid Syntax
if x > 5 doSomething(); 
```

**Sources:**  
– Programming Language References

---

## 18. Static Semantics

**Definition:**  
Static semantics refers to the set of rules that determine the meaning of syntactically valid programs _before_ they are executed (often at compile time). It includes checks such as data type compatibility and scope resolution.

**Visual Aid:**

```
  [Code Without Syntax Errors]
            │
            ▼
   [Static Semantic Checks]
            │
            ▼
  [Compiler Validates Meaning]
```

**Sources:**  
– Language Design Literature

---

## 19. Semantics

**Definition:**  
Semantics is the study of meaning. In programming, it concerns the behavior, results, and effects of executing syntactically correct code. Unlike static semantics (compile-time meaning), semantics also covers dynamic behavior at run time.

**Visual Aid:**

```
        [Source Code]
             │
             ▼
       [Program Execution]
             │
             ▼
   [Resulting Behavior/Outcome]
```

**Sources:**  
– Python.org  
– Compiler Design Texts

---

## 20. Not Provided

_No term was specified for number 20. You may wish to add another concept or delete this section._

---

### Final Notes

Each term is formatted for clarity and alignment with your Anacostia Vault's organizational logic. Let me know if you'd like a second YAML variant using `course_unit:`, `source_text:`, or if this file should be linked directly in `personal-development-digitalscorpyun` for review purposes.

