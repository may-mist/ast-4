from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
driver = webdriver.Chrome(options=options)

page = """
data:text/html,
<html>
<head>
<title>Login Test</title>

<script>
function login(){
    var u = document.getElementById("username").value;
    var p = document.getElementById("password").value;

    if(u=="administrator" && p=="1234"){
        document.getElementById("status").innerHTML="Login Successful";
        document.getElementById("loginDiv").style.display="none";
        document.getElementById("logoutDiv").style.display="block";
    }
    else{
        document.getElementById("status").innerHTML="Invalid Username or Password";
    }
}

function logout(){
    document.getElementById("status").innerHTML="Logged Out Successfully";
    document.getElementById("loginDiv").style.display="block";
    document.getElementById("logoutDiv").style.display="none";
}
</script>

</head>

<body>

<div id="loginDiv">

<h2>Login Form</h2>

<input id="username" type="text" placeholder="Username">
<br><br>

<input id="password" type="password" placeholder="Password">
<br><br>

<button class="login-btn" onclick="login()">Login</button>

</div>

<div id="logoutDiv" style="display:none">

<h2>Welcome Admin</h2>

<button id="logoutBtn" onclick="logout()">Logout</button>

</div>

<p id="status"></p>

</body>
</html>
"""

driver.get(page)

username = driver.find_element(By.ID, "username")
username.send_keys("administrator")

password = driver.find_element(By.ID, "password")
password.send_keys("1234")

login = driver.find_element(By.CLASS_NAME, "login-btn")
login.click()

time.sleep(2)

status = driver.find_element(By.ID, "status")
print("After Login :", status.text)

logout = driver.find_element(By.ID, "logoutBtn")
logout.click()

time.sleep(2)

status = driver.find_element(By.ID, "status")
print("After Logout :", status.text)

driver.quit()