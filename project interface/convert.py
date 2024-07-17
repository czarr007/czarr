import nbformat
from nbconvert import HTMLExporter

# Load the notebook file
notebook_filename = "/mnt/data/Untitled2.ipynb"
with open(notebook_filename) as f:
    notebook_content = nbformat.read(f, as_version=4)

# Convert the notebook to HTML
html_exporter = HTMLExporter()
(body, resources) = html_exporter.from_notebook_node(notebook_content)

# Save the HTML to a file
html_filename = "/mnt/data/converted_notebook.html"
with open(html_filename, "w") as f:
    f.write(body)

html_filename
