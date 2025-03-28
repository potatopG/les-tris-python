<?php
// Connexion à la base de données
$serveur = "localhost";
$utilisateur = "root";
$mot_de_passe = "";
$base_de_donnees = "test-ajout";
$connexion = mysqli_connect($serveur, $utilisateur, $mot_de_passe, $base_de_donnees);

// Vérification de la connexion
if (!$connexion) {
    die("La connexion à la base de données a échoué: " . mysqli_connect_error());
}

// Récupération des données du formulaire
$nom = $_POST['nom'];
$prenom = $_POST['prenom'];
$age = $_POST['age'];

// Requête SQL pour insérer la nouvelle personne
$sql = "INSERT INTO personnes (nom, prenom, age) VALUES ('$nom', '$prenom', '$age')";

// Exécution de la requête SQL
if (mysqli_query($connexion, $sql)) {
    echo "Nouvelle personne insérée avec succès";
} else {
    echo "Erreur d'insertion: " . mysqli_error($connexion);
}

// Fermeture de la connexion à la base de données
mysqli_close($connexion);
?>
