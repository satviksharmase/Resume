from bottle import Bottle, run, template, static_file

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

@app.route('/')
def home():
    about_text = (
        "As a DevOps Engineer at Optus Enterprise with a Software Engineering Honours degree "
        "from Deakin University, I have a well-rounded experience in technology spanning from software "
        "development to customer service. My expertise includes Python, HTML, CSS, JavaScript, and C++ "
        "with hands-on experience in DevOps tools like Icinga, Grafana, AWS, Azure, Docker, and Kubernetes. "
        "I am skilled in both software development and design with a keen understanding of hardware-software "
        "integration for embedded systems. My background equips me to innovate and adapt in fast-paced tech environments."
    )
    return render_template('about', about=about_text)

@app.route('/education')
def education():
    education_info = [
        {
            'degree': 'Bachelor of Software Engineering (Honours)',
            'institution': 'Deakin University',
            'date': 'February 2019 – July 2023',
            'location': 'Burwood, Victoria',
            'details': [
                'Secured a 76% weighted average mark.',
                'Completed Honours research on “Financial Time Series Analysis with Machine Learning”.',
                'Participated in projects involving machine learning, full-stack and cloud development, cybersecurity, data structures, networking, UI/UX design, and embedded systems development.'
            ]
        }
    ]
    return render_template('education', education=education_info)

@app.route('/experience')
def experience():
    experience_info = [
        {
            'position': 'DevOps Engineer',
            'company': 'Optus Enterprise',
            'date': 'July 2023 – Present',
            'location': 'Melbourne, Victoria',
            'details': [
                'Currently a DevOps Engineer at Optus focusing on enhancing plugins, servers, web services, and devices for varied clientele.',
                'Utilizes expertise in Python, Bottle, Salt stack, SQL, Asciidoc, Linux, Icinga, Docker, Kubernetes, JavaScript, and Grafana to deliver superior services and solutions.'
            ]
        },
        {
            'position': 'eForms Developer',
            'company': 'Epworth HealthCare',
            'date': 'February 2023 – July 2023',
            'location': 'Richmond, Victoria',
            'details': [
                'Developed and maintained high-quality web forms using Altera Boss Net, HTML, CSS, and JavaScript ensuring consistency across all forms according to design guidelines.',
                'Conducted thorough testing of web forms to uphold high standards of functionality and user experience.'
            ]
        },
        {
            'position': 'Customer Service Officer',
            'company': 'Link Group',
            'date': 'June 2022 – February 2023',
            'location': 'Docklands, Victoria',
            'details': [
                'Specialized in managing investments, insurance, and superannuation account maintenance ensuring client needs are met effectively.',
                'Adapted services to individual client requirements for personalized financial management and support.'
            ]
        }
    ]
    return render_template('experience', experience=experience_info)

@app.route('/projects')
def projects():
    projects_info = [
        {
            'name': 'Financial Time Series Analysis with Machine Learning',
            'date': 'February 2022 – October 2022',
            'details': [
                'Wrote a research paper focusing on different algorithms used by companies for stock data predictions.',
                'Analyzed predictions for 1-year, 3-year, and 5-year intervals using machine learning and deep learning algorithms such as ARIMA, AR, SARIMAX, LSTM, GRU, ANN, and CNN.'
            ]
        }
    ]
    return render_template('projects', projects=projects_info)

@app.route('/skills')
def skills():
    skills_info = [
        'Programming Languages: C, C++, C#, Python, Java, SQL, Perl',
        'Web Development: HTML, CSS, JavaScript, NodeJS, React, Angular, PHP, Vue.js, Laravel, Kubernetes, Docker, Bottle',
        'DevOps: AWS, Microsoft Azure, IBM Cloud, Icinga, Grafana, RabbitMQ',
        'Embedded Systems: Arduino Uno, Raspberry Pi, Zumo Robot, Particle Argon',
        'Design Tools: Adobe Photoshop, Adobe After Effects, Adobe Premiere Pro, Adobe XD, Corel Draw, AutoCAD',
        'Software Knowledge: Microsoft Office Suite, Robotic Operating System, Linux, AWS, Salt Stack, Networks, AsBuilts'
    ]
    return render_template('skills', skills=skills_info)

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(app, host='localhost', port=8080, debug=True)
