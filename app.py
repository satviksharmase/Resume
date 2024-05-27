from bottle import Bottle, run, template, static_file
import json

app = Bottle()

def get_common_vars():
    return {
        'name': "Satvik Sharma",
        'phone': "+61439626419",
        'email': "satvik0207@gmail.com",
        'address': "18 Japonica Way, Point Cook 3030, Victoria",
        'linkedin': "https://www.linkedin.com/in/satvik-sharma-80487319b/"
    }

def render_template(template_name, **kwargs):
    vars = get_common_vars()
    vars.update(kwargs)
    return template(template_name, **vars)

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/')
def home():
    about_data = load_data('./data/about.json')
    return render_template('about', about=about_data)

@app.route('/education')
def education():
    education_data = load_data('./data/education.json')
    return render_template('education', education=education_data)

@app.route('/experience')
def experience():
    experience_data = load_data('./data/experience.json')
    return render_template('experience', experience=experience_data)

@app.route('/projects')
def projects():
    projects_data = load_data('./data/projects.json')
    return render_template('projects', projects=projects_data)

@app.route('/skills')
def skills():
    skills_data = load_data('./data/skills.json')
    return render_template('skills', skills=skills_data)

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(app, host='localhost', port=8080, debug=True)
