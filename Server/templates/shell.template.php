<!-- 
		ARGUS

		Author : VEXVAIN
		This project is released under the GPL 3 license. 	
-->

<html>
	<head>
		<title>Argus</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

		<link rel="stylesheet" type="text/css" href="assets/css/shell_styles.css" />
		<link rel='shortcut icon' type='image/x-icon' href='assets/images/favicon.ico' />
		<script src="assets/jquery/jquery.min.js"></script>
		<script src="helpers/client/html.js"></script>
	</head>

	<body>
		<div id="output">
			<pre style="font-family:monospace; color:#e74c3c;">

 ▄▄▄       ██▀███    ▄████  █    ██   ██████ 
▒████▄    ▓██ ▒ ██▒ ██▒ ▀█▒ ██  ▓██▒▒██    ▒ 
▒██  ▀█▄  ▓██ ░▄█ ▒▒██░▄▄▄░▓██  ▒██░░ ▓██▄   
░██▄▄▄▄██ ▒██▀▀█▄  ░▓█  ██▓▓▓█  ░██░  ▒   ██▒
 ▓█   ▓██▒░██▓ ▒██▒░▒▓███▀▒▒▒█████▓ ▒██████▒▒
 ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ░▒   ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
  ▒   ▒▒ ░  ░▒ ░ ▒░  ░   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░
  ░   ▒     ░░   ░ ░ ░   ░  ░░░ ░ ░ ░  ░  ░  
      ░  ░   ░           ░    ░           ░  
                                              
			<span style="color:#27ae60">Coded by </span><span style="color:#2980b9">0blio</span>                                      
			</pre>
			
			<pre style="color:#bdc3c7; font-family:monaco">
:)
			</pre>
                                                  
			Type 'help' for a list of commands. <br/><br/>
		</div>

		<span id="software"><span style="color:#EF2929">Argus</span> <span style="color:#729FCF">» </span></span>
		<input id="input" type="text" name="command" autofocus contenteditable="true">
		<input id="csrf_token" style="display:none" value="<?php echo $_SESSION['csrf_token']; ?>">
		<span id="selected_target" style="display:none"></span>
		<span id="shell" style="display:none">false</span>

		<script src="controller-logic/clientside_controller.js"></script>
	</body>
</html>
