Ce projet consiste à faire une applications Web qui a but pour aidez une entreprise à gérer ces 3 centres le projet
On a dans models les relations qu'on va utilisé comme produit clients fournisseur team (employé) centrepnv (les 3 centres de production et ventes) 
Views qui contient les vue que l'application a besoins pour exécuter les tâches comme select qui sert à faire sélect d'un objet en utilisant son id
qui va être envoyer automatiquement comme paramètre à la vue, add qui sert à ajouter des objets à la base de données.....
On a forms qui sert à créer les différents form qui seront afficher pour que l'utilisateur saisie des informations afin de créer ou modifier un objet 
chaque modèle ou relation à son form qui est construit à base des champs ou attributs de cette relation
On a les templates qui sont les page html qui vont êtres afficher sur l'écran 
Template achat-> sert à fournir les front utilisé dans la tâche achat
Template achat_confirmation-> sert à fournir le front utilisé dans la tâche de confirmé l'achat 
Template add-> sert à fournir le front utilisé dans la tâche d'ajout i.e fournir les forms pour que un objet prends ces informations 
Template adding_home-> sert à fournir le front utilisé dans la tâche d'ajout aussi mais ce template fait afficher une interface pour que l'utilisateur choisit de quel type d'objet il veut ajouter par exemple produit ou client...,cette opération permet d'envoyer à VIEW charger d'ajouter le type d'objet pour qu'elle puisse appelé son form spécifique 
Template home-> sert à fournir la première interface que le client voit et interagi avec 
Template index-> sert à fournir le front utilisé pour afficher tous les objet de la base de données en les groupant par type
Template règle_fournisseur-> sert à fournir le front utilisé dans la tâche de règlement du fournisseur en cas où l'entreprise n'as pas tous payé pour les matières premières 
Template achat_confirmation-> sert à fournir le front utilisé dans la tâche de
Template search -> sert à fournir le front utilisé dans la tâche d'affichage du résultat de recherche envoyer par index ou home et ce résultat est calculé par VIEW search 
Template select -> sert à fournir l'affichage de résultat d'un sélect d'un objet dans index et affiche les informations de l'objet et donne la main à modifier ces informations ou supprimer l'objet par des Views 
Template update-> sert à fournir le front utilisé dans la tâche update i.e afficher le form correspondant à cet objet pour que l'utilisateur peut modifier des informations 
