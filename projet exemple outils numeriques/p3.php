<?php
	if (isset($_POST['nombre1']) && isset($_POST['nombre2'])) {
		$nombre1 = $_POST['nombre1'];
		$nombre2 = $_POST['nombre2'];
		$somme = $nombre1 + $nombre2;
		echo "La somme de $nombre1 et $nombre2 est : $somme";
	}
?>