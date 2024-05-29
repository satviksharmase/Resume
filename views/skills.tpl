% include('header.tpl')
<body>
    % include('common_desc.tpl')
    % include('navbar.tpl')
    <div class="container">
        <section id="skills" class="skills">
            <h2>Skills</h2>
            <ul>
                % for skill in skills:
                <li>{{skill}}</li>
                % end
            </ul>
        </section>
    </div>
    % include('footer.tpl')
</body>
</html>
