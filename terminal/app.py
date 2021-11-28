from flask import Flask
app = Flask(__name__)

@app.route("/")
def options():
    return '''<head>
    <style>body {
    background-color: #191414;
    font-family: 'Courier New', monospace;
    font-weight: normal;
}


ul.center{
    padding-left: 0%;
}



h1, h2, h3 {
    color: #1DB954;
    text-align: center;
    font-family: 'Courier New', monospace;
    font-weight: normal;
    
}

ul{
    list-style-type: none;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 20px 28px;
  text-decoration: none;
}

li a:hover {
  background-color: #4dd13f
}

.center {
    text-align: center;
}

  /* Fade animation styling below. */

.fade {
    margin-top: 75px;

    -webkit-animation: fadein 2s; /* Safari, Chrome and Opera > 12.1 */
    -moz-animation: fadein 2s; /* Firefox < 16 */
    -ms-animation: fadein 2s; /* Internet Explorer */
    -o-animation: fadein 2s; /* Opera < 12.1 */
    animation: fadein 2s;
}

@keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
}

/* Firefox < 16 */
@-moz-keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
}

/* Safari, Chrome and Opera > 12.1 */
@-webkit-keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
}

/* Internet Explorer */
@-ms-keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
}

/* Opera < 12.1 */
@-o-keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
}
</style>
  </head>
<body class='fade'>
<h1>Select an Application</h1>
<ul>
<li><a href='http://localhost:8888/'> Jupyter Notebook </a></li>
<li><a href='http://localhost:8080/'> Apache Spark </a></li>
<li><a href='http://localhost:9870/'> Apache Hadoop </a></li>
<li><a href='http://localhost:9000/'> SonarQube and SonarScanner </a></li>
</ul>
</body>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')