% include('header.tpl')
<body>
    <header>
        <h1>{{name}}</h1>
        <p>Phone: {{phone}} | Email: <a href="mailto:{{email}}">{{email}}</a> | Address: {{address}}</p>
        <p>LinkedIn: <a href="{{linkedin}}" target="_blank">{{linkedin}}</a></p>
    </header>
    % include('navbar.tpl')
    <div class="container">
        <section id="projects" class="projects">
            <h2>Projects</h2>
            % for project in projects:
            <div class="project-item">
                <h3>{{project['name']}}</h3>
                <p>{{project['date']}}</p>
                <ul>
                    % for detail in project['details']:
                    <li>{{detail}}</li>
                    % end
                </ul>
            </div>
            % end
        </section>
    </div>
    % include('footer.tpl')
</body>
</html>
