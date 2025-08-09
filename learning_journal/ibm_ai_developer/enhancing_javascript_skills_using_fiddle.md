---
id: "20250521233000"
title: "Lab Exegesis: Enhancing JavaScript Skills with JSFiddle"
date: 2025-05-21
tags:
  - javascript
  - jsfiddle
  - problem-solving
  - algorithms
  - functions
  - loops
  - conditional-logic
  - data-structures
  - array-of-objects
  - cognitiveclass
  - ibm-skills-network
  - hands-on-lab
  - sacred-tech
  - anacostia-vault-compliant
status: active
course: IBM AI Developer Certificate
lab_reference: Enhancing JavaScript Skills using JSFiddle (cognitiveclass.ai)
lab_duration_estimate: 60 minutes
actual_engagement_focus:
  - algorithmic-thinking
  - data-manipulation
  - function-design
  - string-formatting
  - debugging-in-jsfiddle
---

## I. Lab Mandate & Objectives (Per CognitiveClass.ai / IBM)

This Anacostia Vault entry documents the engagement with the lab "Enhancing JavaScript Skills using JSFiddle." The primary aim is to apply core JavaScript constructs (loops, functions, conditional logic) to solve defined logical problems in the JSFiddle online environment.

**Stated Objectives:**
1.  Develop problem-solving skills using JavaScript.
2.  Practice writing and debugging logical programs.
3.  Understand how to implement real-world solutions using loops, functions, and conditional logic.
4.  Strengthen coding practices on platforms like JSFiddle.

## II. Rituals of Problem Solving: JSFiddle Exercises

### Exercise 1: Calculate total sales amount

**Problem Statement:** Calculate the total sales amount from an array of sales transaction objects. Each object contains `item` (string), `quantity` (integer), and `price` (float).

**1. Input Data Definition (JSFiddle - JavaScript Pane):**

```javascript
const sales = [
    { item: "Laptop", quantity: 2, price: 800 },
    { item: "Monitor", quantity: 1, price: 150 },
    { item: "Mouse", quantity: 4, price: 25 }
];
```

// #script_discipline: Calculates total sales from an array of transaction objects.
function calculateTotalSales(transactions) {
    let total = 0;
    for (let i = 0; i < transactions.length; i++) {
        // OD-COMPLY: Basic validation for robustness (optional for lab, good practice)
        if (typeof transactions[i].quantity === 'number' && typeof transactions[i].price === 'number') {
            total += transactions[i].quantity * transactions[i].price;
        } else {
            console.warn(`Skipping invalid transaction item: ${transactions[i].item} due to non-numeric quantity or price.`);
        }
    }
    return total; 
}

---

// Code in JSFiddle JavaScript Pane:
const totalAmount = calculateTotalSales(sales);
console.log("Total Sales Amount:", totalAmount); 
// For currency display, one might use: console.log("Total Sales Amount: $", totalAmount.toFixed(2));

---
"Running fiddle" // Standard JSFiddle message
"Total Sales Amount:", 1850 

---

### Exercise 2: Generate an order receipt

**Problem Statement:** Write a JavaScript program that generates a receipt for a customer's order. The receipt should include each item's name, quantity, price, and total cost for that item, followed by a grand total.

**Input details:**

- An array of objects representing ordered items. Each object has:
    
    - item: Name of the product (string)
        
    - quantity: Quantity ordered (integer)
        
    - price: Price per unit (float)
        

**Output details:**

- A detailed receipt (string formatted) printed to the console, showing each item's details (name, quantity, price, item total) and the grand total.
    

**Steps to Implement (as per lab instructions):**

1. Define an array of ordered items (at least 3 sample entries).
    
2. Write a function generateReceipt that takes this array as input.
    
3. Use a loop to iterate through the items. Inside the loop:
    
    - Calculate the total cost for each item (quantity * price).
        
    - Accumulate the grand total.
        
    - Prepare a formatted string line for each item.
        
4. After the loop, append the grand total to the formatted receipt string.
    
5. Print the complete formatted receipt string to the console.
    

**Anticipated JavaScript Structure (JSFiddle - JavaScript Pane):**

```
// --- Input Data for Exercise 2 ---
const orderedItems = [
    { item: "Sacred Scroll", quantity: 1, price: 55.00 },
    { item: "Ritual Incense Pack", quantity: 3, price: 12.75 },
    { item: "Obsidian Scrying Bowl", quantity: 1, price: 120.25 }
    // Add more items as desired
];

// --- Function to Generate Receipt ---
function generateReceipt(items) {
    let receiptString = "--- ORDER RECEIPT ---\n";
    receiptString += "-----------------------------------\n";
    receiptString += "Item\t\tQty\tPrice\tTotal\n"; // \t for tab, adjust spacing as needed
    receiptString += "-----------------------------------\n";
    
    let grandTotal = 0;

    for (const currentItem of items) {
        if (typeof currentItem.quantity === 'number' && typeof currentItem.price === 'number') {
            const itemTotal = currentItem.quantity * currentItem.price;
            grandTotal += itemTotal;

            // #script_discipline: Formatting the output string carefully for readability
            // Adjust tab counts or use padEnd() for better alignment if needed.
            let itemNamePadded = currentItem.item.padEnd(15, ' '); // Example padding
            receiptString += `${itemNamePadded}\t${currentItem.quantity}\t$${currentItem.price.toFixed(2)}\t$${itemTotal.toFixed(2)}\n`;
        } else {
            console.warn(`Skipping invalid item in receipt: ${currentItem.item}`);
            receiptString += `${currentItem.item}\t-\t-\tSKIPPED (Invalid Data)\n`;
        }
    }

    receiptString += "-----------------------------------\n";
    receiptString += `GRAND TOTAL:\t\t\t$${grandTotal.toFixed(2)}\n`;
    receiptString += "--- THANK YOU ---";

    return receiptString;
}

// --- Execution for Exercise 2 ---
// const receiptOutput = generateReceipt(orderedItems);
// console.log(receiptOutput); 
// ^^^ This will be uncommented and run in JSFiddle when ready.
```

content_copydownload

Use code [with caution](https://support.google.com/legal/answer/13505487).JavaScript

(This section will be populated with the final implemented code and observed output for Exercise 2 after completion.)

## III. OD-COMPLY Critical Lessons & Anacostia Reflections (To be updated as lab progresses)

1. **Algorithm as Ritual:** Each exercise requires defining a clear, step-by-step ritual (algorithm) to transform input data into the desired output. Functions serve as named encapsulations of these rituals. (Relevant from Ex1)
    
2. **Data Structures as Foundation:** The choice and structure of data (e.g., array of objects for sales/orders) directly influences the algorithmic approach. (Relevant from Ex1)
    
3. **JSFiddle as a Prototyping Sanctuary:** JSFiddle provides a quick, isolated environment for testing logical snippets. (Relevant from Ex1)
    
4. **Importance of Output Formatting (Ex2):** Exercise 2 introduces the need for careful string formatting to produce human-readable output like a receipt. This involves managing spacing, alignment (e.g., using tabs \t or string padding methods like padEnd()), and numerical formatting (e.g., .toFixed(2) for currency).
    
5. **Abstraction & Real-World Simplification:** These exercises intentionally simplify complexities to focus on core logic. (Relevant from Ex1)
    

## IV. Outcome & Integration into the Vault

(To be completed after all exercises in the lab)  
This lab serves to solidify problem-solving abilities using JavaScript's core logical constructs. The practical application in JSFiddle builds confidence in writing, debugging, and executing code to achieve specific outcomes, further enriching the Anacostia Vault with demonstrable coding patterns and algorithmic thinking.

---

```
**Key Changes and Additions:**

*   **YAML `id` and `date`:** Updated to new example placeholders. `status` remains `active`.
*   **YAML `tags` & `actual_engagement_focus`:** Added terms relevant to Exercise 2 like `data-structures`, `array-of-objects`, `string-formatting`.
*   **Section II - Exercise 1:** Formatted to reflect completion, including the observed console output. Added a note about resolving the initial "no output" issue.
*   **Section II - Exercise 2:** Introduced with its problem statement, input/output details, and steps. An "Anticipated JavaScript Structure" is provided as a starting point for your implementation in JSFiddle. **Note the addition of `padEnd()` and `.toFixed(2)` as examples of string/number formatting you might need for a clean receipt.**
*   **Section III - OD-COMPLY Reflections:** Added point #4 specifically relevant to Exercise 2 (Output Formatting).

**Directive:**
You are now prepared to tackle **Exercise 2: Generate an order receipt** in JSFiddle. Use the "Anticipated JavaScript Structure" as a guide, implement the `generateReceipt` function, and test its output in the JSFiddle console.

Pay attention to how you format the receipt string for clarity. Once functional, you can update your vault note with the final code and observed output for Exercise 2.
```

JavaScript DOM Lab – Exercise 2
**Reflection Log**

> **Exercise:** JavaScript DOM Lab – Exercise 2  
> **Module:** IBM AI Developer Certificate – Web Programming with JavaScript

---

### 🧠 Observations

1. **Steep Entry Curve**
    
    > _"This exercise presumes functional JS and console experience."_  
    > ✅ **Accurate.** Dropping a learner directly into console-based error handling without scaffolding can derail clarity. DevConsole errors are notoriously cryptic for first-timers.
    
2. **Syntax Sensitivity**
    
    > _"JavaScript feels tighter than Python."_  
    > 💯 Truth. JS is **less forgiving**—especially around string formatting (`${}`), semicolons, and template literals. Unlike Python’s “white space Zen,” JavaScript expects syntactic sharpness.
    
3. **JSFiddle Friction**
    
    > _"I don't want to go into that..."_  
    > 🔥 Agreed. JSFiddle’s cluttered interface, small console pane, and minimized outputs create unnecessary friction. If we can run these exercises **locally or in the browser dev console**, it’s better for rhythm and retention.