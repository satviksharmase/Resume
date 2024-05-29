% include('header.tpl')
<body>
    % include('common_desc.tpl')
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
