% include('header.tpl')
<body>
    <header>
        <h1>{{name}}</h1>
        <p>Phone: {{phone}} | Email: <a href="mailto:{{email}}">{{email}}</a> | Address: {{address}}</p>
        <p>LinkedIn: <a href="{{linkedin}}" target="_blank">{{linkedin}}</a></p>
    </header>
    % include('navbar.tpl')
    <div class="container">
        <section id="about" class="about">
            <h2>About Me</h2>
            <p>{{about}}</p>
        </section>
    </div>
    % include('footer.tpl')
</body>
</html>
