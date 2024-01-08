# Import the graphviz library for creating and rendering graphs.
import graphviz

# Define the source code which represents a simple program.
source = """
lire(a)                             # Read value for 'a'
lire(b)                             # Read value for 'b'
si a > b alors                      # If 'a' is greater than 'b'
    afficher("a est supérieur à b") # Print that 'a' is greater than 'b'
sinon                               # Otherwise
    afficher("a n'est pas supérieur à b")  # Print that 'a' is not greater than 'b'
finsi                               # End of if-else statement
"""

# Function to create a control flow graph from the source code.
def create_cfg_from_source(code):
    # Initialize the graph.
    dot = graphviz.Digraph(format='png')

    # Split the source code into lines and create nodes for each line.
    lines = code.strip().split('\n')
    nodes = {}

    for i, line in enumerate(lines):
        # Assign a unique node name for each line.
        node_name = chr(ord('A') + i)
        dot.node(node_name, line.strip())
        nodes[i] = node_name

    # Connect nodes to represent the flow of control.
    dot.edge(nodes[0], nodes[1], label='Read b')     # Connect 'lire(a)' to 'lire(b)'
    dot.edge(nodes[1], 'C', label='Evaluate')        # Connect 'lire(b)' to 'si a > b alors'

    # Connect the decision node 'C' to its outcomes.
    dot.edge('C', nodes[4], label='False')           # Connect 'si a > b alors' to 'a n'est pas supérieur à b'
    dot.edge('C', nodes[3], label='True')            # Connect 'si a > b alors' to 'a est supérieur à b'

    # Connect the end of the false condition to the 'finsi' (end of if-else).
    dot.edge(nodes[4], nodes[5], label='Do') 
    dot.edge(nodes[5], nodes[6], label='End') 

    return dot, nodes

# Function to render and save the control flow graph.
def render_and_save(dot, filename):
    dot.render(filename, view=True)

# Function to generate and save the control flow graph for the program.
def control_flow_graph_for_program(code):
    dot, nodes = create_cfg_from_source(code)
    render_and_save(dot, 'control_flow_graph_comparison_program')

# Generate and save the control flow graph for the provided source code.
control_flow_graph_for_program(source)
