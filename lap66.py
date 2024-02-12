import webbrowser

html_content = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>my personal page</title>
</head>
<body>
    <h1>[qusai mashagbeh]</h1>
    <p>
        <img src="123.jpg" alt="pic[qusai]" width="200px">
    </p>
    <p>
        
    </p>
    <p>
       
    </p>
</body>
</html>
"""

with open("my_page.html", "w") as f:
    f.write(html_content)

webbrowser.open("my_page.html")