% include('header.tpl')
<body>
    <header>
        <h1>{{name}}</h1>
        <p>Phone: {{phone}} | Email: <a href="mailto:{{email}}">{{email}}</a> | Address: {{address}}</p>
        <p>LinkedIn: <a href="{{linkedin}}" target="_blank">{{linkedin}}</a></p>
    </header>
    % include('navbar.tpl')
    <div class="container">
        <section id="experience" class="experience">
            <h2>Experience</h2>
            % for job in experience:
            <div class="experience-item">
                <h3>{{job['position']}}</h3>
                <p><strong>{{job['company']}}</strong>, {{job['date']}}, {{job['location']}}</p>
                <ul>
                    % for detail in job['details']:
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
