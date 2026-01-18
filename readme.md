L-System Fractal Explorer
A high-performance L-System (Lindenmayer System) generator built using Python, Tkinter, and Turtle Graphics. This project was developed to demonstrate proficiency in formal grammars, parallel string rewriting, and GUI integration.

🚀 Key Features
Parallel Rewriting Engine: Implements a true simultaneous replacement logic where all symbols in a string are updated in a single pass, ensuring mathematical accuracy of the L-system.

Hybrid GUI Architecture: Uses turtle.RawTurtle to embed a high-performance drawing canvas directly into a Tkinter dashboard.

Recursive Branching (Push/Pop): Supports the [ and ] operators using a stack-based architecture to save and restore turtle states, enabling complex, organic tree structures.

Real-time Optimization: Utilizes turtle.tracer(0, 0) to handle massive strings (10,000+ characters) without UI lag or crashes.

Recursive Gradient: Dynamically shifts the pen color based on iteration progress to provide visual depth.

🛠️ Tech Stack
Language: Python 3.x

GUI Framework: Tkinter (Built-in)
Rendering Engine: Turtle Graphics (Built-in)
📋 How to Run
Ensure Python 3 is installed.
Clone or download main.py.
Run the script via terminal:
python main.py
Recommended test cases:
1. The Fractal Plant (Nature Simulation)
Axiom: X
Rules: X:F+[[X]-X]-F[-FX]+X, F:FF
Angle: 25
Iterations: 4 or 5
Step Length: 5
2. The Koch Snowflake (Symmetry & Loops)
Axiom: F--F--F
Rules: F:F+F--F+F
Angle: 60
Iterations: 3
Step Length: 5
3. The Dragon Curve (Complexity & Stress Test)
Axiom: FX
Rules: X:X+YF+, Y:-FX-Y
Angle: 90
Iterations: 10
Step Length: 4
4. The Binary Tree (Simple Branching)
Axiom: F
Rules: F:G[+F]-F, G:GG
Angle: 30
Iterations: 4
Step Length: 10
5. Rings (Geometric Pattern)
Axiom: F+F+F+F
Rules: F:FF+F+F+F+F+F-F
Angle: 90
Iterations: 2
Step Length: 10