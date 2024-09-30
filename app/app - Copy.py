from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.list_templates()  # This will show all available templates
