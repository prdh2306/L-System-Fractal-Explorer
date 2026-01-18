import tkinter as tk
from turtle import RawTurtle, TurtleScreen

class LSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("L-System Fractal Explorer")
        
        # --- UI Layout ---
        self.setup_ui()
        
        # --- Turtle Setup ---
        # We use RawTurtle to embed it into the Tkinter Canvas
        self.screen = TurtleScreen(self.canvas)
        self.screen.bgcolor("white")
        self.t = RawTurtle(self.screen)
        self.t.hideturtle()
        self.t.speed(0)

    def setup_ui(self):
        """Creates the Input Dashboard on the left and Canvas on the right."""
        control_panel = tk.Frame(self.root, padx=10, pady=10)
        control_panel.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="white")
        self.canvas.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Inputs
        tk.Label(control_panel, text="Axiom (e.g., F):").pack(anchor="w")
        self.entry_axiom = tk.Entry(control_panel)
        self.entry_axiom.insert(0, "F")
        self.entry_axiom.pack(fill="x", pady=5)

        tk.Label(control_panel, text="Rules (Symbol:Replacement, ...):").pack(anchor="w")
        self.entry_rules = tk.Entry(control_panel)
        self.entry_rules.insert(0, "F:F[+F]F[-F]F")
        self.entry_rules.pack(fill="x", pady=5)

        tk.Label(control_panel, text="Angle (Degrees):").pack(anchor="w")
        self.entry_angle = tk.Entry(control_panel)
        self.entry_angle.insert(0, "25")
        self.entry_angle.pack(fill="x", pady=5)

        tk.Label(control_panel, text="Iterations:").pack(anchor="w")
        self.entry_iterations = tk.Entry(control_panel)
        self.entry_iterations.insert(0, "4")
        self.entry_iterations.pack(fill="x", pady=5)

        tk.Label(control_panel, text="Step Length:").pack(anchor="w")
        self.entry_step = tk.Entry(control_panel)
        self.entry_step.insert(0, "5")
        self.entry_step.pack(fill="x", pady=5)

        # Generate Button
        self.btn_generate = tk.Button(control_panel, text="Generate Fractal", 
                                      command=self.generate, bg="#4CAF50", fg="white")
        self.btn_generate.pack(fill="x", pady=20)

        tk.Label(control_panel, text="Guide:\nF = Move Forward\n+ = Turn Right\n- = Turn Left\n[ = Save State\n] = Restore State", 
                 justify="left", fg="gray").pack(side="bottom")

    def expand_string(self, axiom, rules, n):
        """The Recursive Engine: Parallel replacement logic."""
        current_string = axiom
        for _ in range(n):
            next_string = ""
            for char in current_string:
                next_string += rules.get(char, char)
            current_string = next_string
        return current_string

    def parse_rules(self, raw_rules):
        """Converts user string 'F:FF, X:F+X' into a dictionary."""
        rule_dict = {}
        try:
            pairs = raw_rules.split(",")
            for pair in pairs:
                key, val = pair.strip().split(":")
                rule_dict[key.strip()] = val.strip()
        except:
            print("Error parsing rules. Use Format 'Symbol:Replacement'")
        return rule_dict

    def generate(self):
        # 1. Get User Input
        axiom = self.entry_axiom.get()
        rules = self.parse_rules(self.entry_rules.get())
        angle = float(self.entry_angle.get())
        iterations = int(self.entry_iterations.get())
        step = float(self.entry_step.get())

        # 2. Expand
        final_string = self.expand_string(axiom, rules, iterations)

        # 3. Render with Optimization
        self.render(final_string, angle, step)

    def render(self, instructions, angle, step):
        self.screen.tracer(0, 0) # Turn off animation for speed
        self.t.clear()
        self.t.penup()
        self.t.home()
        self.t.setheading(90) # Start pointing up
        self.t.pendown()
        
        stack = [] # For branching [ ]
        
        for i, char in enumerate(instructions):
            # Dynamic Color (Gradient Effect)
            # Shifts from green to brown based on progress
            color_val = int((i / len(instructions)) * 255)
            self.screen.colormode(255)
            self.t.pencolor(30, max(50, 255 - color_val), 30)

            if char == "F":
                self.t.forward(step)
            elif char == "+":
                self.t.right(angle)
            elif char == "-":
                self.t.left(angle)
            elif char == "[":
                stack.append((self.t.position(), self.t.heading()))
            elif char == "]":
                pos, head = stack.pop()
                self.t.penup()
                self.t.setposition(pos)
                self.t.setheading(head)
                self.t.pendown()

        self.screen.update() # Refresh canvas once at the end

if __name__ == "__main__":
    root = tk.Tk()
    app = LSystemApp(root)
    root.mainloop()