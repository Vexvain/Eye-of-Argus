<?php

	/*
		ARGUS

		Author : VEXVAIN
		This project is released under the GPL 3 license. 	
	*/

	// If user is logged in
	if (isset($_SESSION['username'])) {
		header ('Location: shell.php');
	
	// if the database has not been installed yet
	} else if (!file_exists('database/config.php')) {
		header ('Location: install.php');
	
	} else {
		header ('Location: login.php');
	}
