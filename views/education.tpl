% include('header.tpl')
<body>
    <header>
        <h1>{{name}}</h1>
        <p>Phone: {{phone}} | Email: <a href="mailto:{{email}}">{{email}}</a> | Address: {{address}}</p>
        <p>LinkedIn: <a href="{{linkedin}}" target="_blank">{{linkedin}}</a></p>
    </header>
    % include('navbar.tpl')
    <div class="container">
        <section id="education" class="education">
            <h2>Education</h2>
            % for edu in education:
            <div class="education-item">
                <h3>{{edu['degree']}}</h3>
                <p><strong>{{edu['institution']}}</strong>, {{edu['date']}}, {{edu['location']}}</p>
                <ul>
                    % for detail in edu['details']:
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
