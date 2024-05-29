% include('header.tpl')
<body>
    % include('common_desc.tpl')
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
