---
id: 20250522000000 # Example: New unique ID for this finalized lab note
title: "Lab Exegesis: Enhancing JavaScript Skills (Local Environment)"
date: 2025-05-22 # Example: Actual completion date of entire lab
tags:
  - javascript
  - browser-console
  - local-environment
  - problem-solving
  - algorithms
  - functions
  - loops
  - conditional-logic
  - data-structures
  - array-of-objects
  - string-formatting
  - regex
  - password-validation
  - stock-tracking
  - cognitiveclass
  - ibm-skills-network
  - hands-on-lab
  - sacred-tech
  - anacostia-vault-compliant
  - #script_discipline
status: completed # <<< CHANGED TO COMPLETED
course: IBM AI Developer Certificate
lab_reference: "Enhancing JavaScript Skills (CognitiveClass.ai) - Executed Locally"
lab_duration_estimate: "60 minutes" # Can add actual_duration if tracked
actual_engagement_focus:
  - algorithmic-thinking
  - data-manipulation
  - function-design
  - string-formatting-and-regex
  - debugging-in-browser-console
---

(Console Output: Total Sales Amount: 1850)

---

### Exercise 2: Generate an order receipt

(Content as previously finalized: Problem Statement, JS Code, Observed Output, Implementation Notes)

// Code for Exercise 2...
const orders = [ /* ... */ ];
function generateReceipt(orderList) { /* ... */ }
const fullReceipt = generateReceipt(orders);
console.log(fullReceipt);

(Console Output: Formatted Receipt...)

---

### Exercise 3: Validate passwords

(Content as previously finalized: Problem Statement, JS Code, Observed Output, Implementation Notes)

// Code for Exercise 3...
const samplePasswords = [ /* ... */ ];
function isValidPassword(password) { /* ... */ }
function validatePasswords(passwordsArray) { /* ... */ }
validatePasswords(samplePasswords);

(Console Output: List of passwords with Valid/Invalid status...)

---

### Exercise 4: Track product stock levels

**Problem Statement:** Write a JavaScript program that tracks the stock levels of various products. For each product, indicate if it is "In Stock" or "Out of Stock."

**1. Setup in Local Development Dojo (WSL - ANACOSTIA Terminal):**  
* **Development Path (WSL):** ~/projects_2025/ibm_ai_developer/labs/js_stock_checker_ex4/  
* Files: index.html (host), stock_checker.js (logic).  
* Execution: index.html opened via VS Code Live Server (from WSL), output observed in Windows browser's Developer Console.

**2. JavaScript Code (stock_checker.js):**

// #script_discipline: stock_checker.js - Tracks product stock levels.
// For IBM AI Developer Certificate - Enhancing JavaScript Skills Lab - Exercise 4

const products = [
    { product: "Anacostia Codex Scroll", stock: 15 },
    { product: "Tyrian Purple Ink Vial", stock: 0 },
    { product: "Scorpyun Stylus Prime", stock: 5 },
    { product: "Obsidian Data Crystal", stock: 0 },
    { product: "Lion's Mane Tassel", stock: 22 },
    { product: "Griot's Portable Lectern", stock: -1 } 
];

// #sacred_tech: Product names themed to align with the Anacostia Vault and digitalscorpyun ethos. 

function checkStockLevels(productArray) {
    console.log("--- ANACOSTIA Inventory Stock Check Ritual ---");
    productArray.forEach(currentProduct => {
        let stockStatus = "";
        let statusGlyph = "";
        let stockDisplay = "";

        if (typeof currentProduct.stock === 'number' && currentProduct.stock >= 0) {
            if (currentProduct.stock > 0) {
                stockStatus = "In Stock";
                statusGlyph = "🟢";
                stockDisplay = `(${currentProduct.stock} units)`;
            } else { 
                stockStatus = "Out of Stock";
                statusGlyph = "🔴";
            }
        } else {
            stockStatus = "Stock Unknown/Invalid";
            statusGlyph = "❓";
            if (typeof currentProduct.stock === 'number') {
                stockDisplay = `(Value: ${currentProduct.stock})`;
            }
        }
        console.log(
            `Product: ${currentProduct.product.padEnd(30)} | Status: ${statusGlyph} ${stockStatus.padEnd(20)} ${stockDisplay}`
        );
    });
    console.log("--- Stock Check Ritual Complete ---");
}

checkStockLevels(products);

**3. Observed Console Output:**

--- ANACOSTIA Inventory Stock Check Ritual ---
Product: Anacostia Codex Scroll         | Status: 🟢 In Stock              (15 units)
Product: Tyrian Purple Ink Vial        | Status: 🔴 Out of Stock          
Product: Scorpyun Stylus Prime         | Status: 🟢 In Stock              (5 units)
Product: Obsidian Data Crystal         | Status: 🔴 Out of Stock          
Product: Lion's Mane Tassel            | Status: 🟢 In Stock              (22 units)
Product: Griot's Portable Lectern      | Status: ❓ Stock Unknown/Invalid   (Value: -1)
--- Stock Check Ritual Complete ---

**4. Implementation Notes & Reflections (Exercise 4):**  
* Applied conditional logic (if/else) to determine stock status.  
* Included basic data validation for the stock property (checking for non-negative numbers).  
* Utilized string formatting (padEnd()) and thematic glyphs for clear, aligned console output.

## III. OD-COMPLY Critical Lessons & Anacostia Reflections (Overall Lab)

1. **Algorithm as Ritual:** Each exercise reinforced defining clear, step-by-step algorithms encapsulated in functions to solve specific problems.
    
2. **Data Structures as Foundation:** The effective use of arrays of objects was central to managing and iterating through collections of data (sales, orders, passwords, products).
    
3. **Local Environment (Dojo) for Sovereign Practice:** Conducting exercises locally (browser console/HTML files via WSL) provided direct interaction with the JavaScript engine, enhancing control and reducing friction compared to online IDEs for these types of logic-focused tasks.
    
4. **Importance of Output Formatting & String Manipulation:** The lab progressively required more attention to string construction for human-readable console output (template literals, newlines, padding, number formatting).
    
5. **Syntax Precision & Debugging:** JavaScript demands syntactic precision. Debugging syntax errors, sometimes reported on lines following the actual mistake, requires systematic investigation and understanding of parser behavior.
    
6. **Pedagogical Considerations:** Initial exercises requiring console use can be challenging for learners without prior experience in interpreting developer console errors or navigating its interface. Explicit guidance on common error types and debugging strategies is beneficial.
    
7. **Robustness through Validation:** Incorporating even basic input/data validation within functions (e.g., checking for empty tasks, valid numbers for stock) leads to more resilient and predictable code.
    

## IV. IBM Module Summary Integration

(This section incorporates the key learnings from the IBM module that this lab reinforced.)

The practical exercises in this lab solidified understanding of several core JavaScript concepts outlined in the broader IBM module:

- **JavaScript as a Scripting Language:** Directly applied for adding dynamic logic (though not DOM manipulation in this specific lab, the problem-solving is a precursor).
    
- **Variables (let, const):** Extensively used for storing data like arrays, loop counters, and accumulated totals.
    
- **Program Execution Control (If…Then…Else, For loops):** These were the primary tools for implementing the logic in all exercises (e.g., iterating through arrays, checking conditions for password validation or stock levels).
    
- **Functions (Blocks of Code):** Each exercise involved creating and calling functions to encapsulate specific tasks (calculateTotalSales, generateReceipt, isValidPassword, checkStockLevels).
    
- **Prototypes (Conceptual Link):** While not directly manipulating prototypes in this lab, understanding that methods like .toFixed() or .padEnd() are available on number and string primitives (via their respective object wrappers and prototype chains) is an implicit takeaway.
    
- **Client-Side Scripts & <script> Tag:** The local execution method (linking a .js file in index.html) directly demonstrates this.
    
- **DOM (Indirect Link):** Although this lab focused on console logic, the skills are foundational for DOM manipulation scripts that will eventually access and use data processed by such functions.
    

## V. Outcome & Integration into the Anacostia Vault

This "Enhancing JavaScript Skills" lab, adapted for execution within the ANACOSTIA Terminal's local dojo, successfully met its objectives. It provided rigorous practice in developing problem-solving skills, writing and debugging logical JavaScript programs, and implementing solutions using loops, functions, and conditional logic.

The exercises demonstrated the power of JavaScript for data processing and algorithmic thinking, even outside the immediate context of direct DOM manipulation. The shift to local execution reinforced principles of tool sovereignty and focused engagement. These inscribed rituals of problem-solving, along with the critical reflections on pedagogy and code robustness, significantly enrich the Anacostia Vault. The foundational JavaScript grammar and logical constructs practiced here are now more deeply integrated, ready to serve more complex conjurations in future web development and AI-related endeavors.