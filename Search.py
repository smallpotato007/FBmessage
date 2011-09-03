#!D:/usr/Python27/python.exe -u 
import time
print "Content-Type: text/html"

print '''
<html>
<head><title></title></head>
<body>
    <form action="ReturnResults.py" name="SearchForm">
        To <input type="text" name="searchstr" value="'''+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'''"><br/>
        <input type="submit" value="Search" >
    </form>
</body>
</html>
'''