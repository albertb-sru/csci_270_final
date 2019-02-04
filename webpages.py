#!/usr/bin/env python3
# Made by Albert Brandt
# webpage.py


html = """
<!DOCTYPE html>
<html>
<head>
<title>BirthTest</title>
<style>
  #main {
    background-color: #D3D3D3;
    width: 80%;
    height: 700px;
    margin-left:10%;
    margin-right:10%;
  }

  p {
    margin-left: 5px;
	margin-right: 5px;
  }
  
  .top {
    width:100%;
    height: 40px;
    background-color: black;
    color:white;
    text-align: center;
  }

  .biorhythm {
    list-style-type: none;
	margin: 0;
	padding: 0;
	overflow: hidden;
	background-color: #D3D3D3;
	align-items: center;
  }
  
  li {
	float: left;
	display: block;
	padding: 8px;
	background-color: #D3D3D3;
  }
  
</style>

</head>
<body>
<div id="main">
  <div class="top">
    <h1>Birth Test</h1>
  </div>

  <h1 style="margin-left: 5px;">Hello there %firstname%!</h1>
  <p>You have been alive %days_alive% days</p>
  <p>Your Chinese Year: %chyr%</p>
  <p>Your personality paragraph: %personality%</p>
  <p>Your zodiac sign: %zodiac% <a href='%z_url%' target='_blank'>Click here to learn more</a></p>
  <p>Your biorhythm calculations:</p>
  <ul class="biorhythm">
	<li style="color:blue;">Physical: %bio_phys%%</li>
	<li style="color:red;">Emotional %bio_emot%%</li>
	<li style="color:green;">Intellectual %bio_inte%%</li>
  <ul>
</div>
</body>
</html>
"""

def getHTML():
    return html
