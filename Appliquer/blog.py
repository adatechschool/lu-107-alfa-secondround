from enum import Enum

# Cette variable devra être alimentée des articles créés par les utilisateurs qui en ont le droit
articles = []

###############################################################################
# CODE À COMPLÉTER
###############################################################################

class User:
    def __init__(self, name: str):
        self.name = name

    def can(self, permission: "Permission") -> bool:
        """ Un utilisateur "lambda" ne peut que lire du contenu """
        return True if permission == Permission.READ else False

# TODO: Ajoute ici les autres classes nécessaires au programme

def get_user(name: str) -> User:
    """
    :param name: Nom de l'utilisateur pour lequel renvoyer une instance `User`
    :return: instance d'une classe `User` adaptée au niveau de droits de
             l'utilisateur passé en paramètre
    """
    # TODO: Compléter cette fonction pour qu'elle renvoie une instance adaptée
    #       au niveau de droits de l'utilisateur passé en paramètre, tel que
    #       renseigné dans la variable USER plus bas
    return User(name)

def display_article(article):
    """
    Affiche un article : son titre, son auteur, son texte

    TODO: cette fonction prend un supposé objet "article" en paramètre pour en faire l'affichage.
          Les concepts d'encapsulation et d'abstraction imposeraient une autre façon de faire.
          À vous de corriger !
    """
    print("")
    print("-" * 4 + article.title + "-" * 4)
    print(f"Auteur : {article.author.name}")
    print(f"\\n{article.text}\\n")
    print("-" * (len(article.title) + 8))
    print("")

def write_article():
    """
    Écriture et enregistrement d'un nouvel article
    """
    if not current_user.can(Permission.WRITE):
        return

    author = current_user

    print("Quel est le titre de l'article ?")
    title = input("> ")

    print("Quel est le contenu de l'article ?")
    text = input("> ")

    # TODO: créer un nouvel Article à partir des données collectées et l'ajouter à la variable `articles`

###############################################################################
# / FIN DU CODE À COMPLÉTER
###############################################################################

###############################################################################
# Définition des rôles & utilisateurs
###############################################################################

class UserRole(Enum):
    VISITOR = 'visitor'  # Peut consulter des articles
    WRITER = 'writer'  # Peut consulter des articles et en écrire
    ADMIN = 'admin'  # Peut consulter, écrire et supprimer des articles

class Permission(Enum):
    READ = 'read'
    WRITE = 'write'
    DELETE = 'delete'

# Fausse "base de données" des utilisateurs du système
USERS = {
    "chloe": UserRole.ADMIN,
    "alya": UserRole.WRITER,
    "visitor": UserRole.VISITOR
}

###############################################################################
# Actions du menu
###############################################################################
current_user = None

def list_articles(prompt, use_article_callback):
    while True:
        print("--- Articles disponibles ---")

        for idx, article in enumerate(articles):
            print(f"{idx + 1} -> {article.title}")

        print(f"{len(articles) + 1} -> Retour")

        print(prompt)
        article_idx = int(input("> ")) - 1

        # Sort de la fonction si le choix est "Retour"
        if article_idx == len(articles):
            return

        if 0 <= article_idx > len(articles):
            continue

        use_article_callback(articles[article_idx])

def display_articles():
    if not current_user.can(Permission.READ):
        return

    # Affiche les articles disponibles et affiche celui sélectionné
    list_articles("Quel article veux-tu lire ?", lambda article: display_article(article))

def delete_article(article):
    articles.remove(article)

def delete_articles():
    if not current_user.can(Permission.DELETE):
        return

    # Affiche les articles disponibles et supprime celui sélectionné
    list_articles("Quel article veux-tu supprimer ?", lambda article: delete_article(article))

ACTIONS = [
    {
        "label": "Lire un article",
        "permission": Permission.READ,
        "action": display_articles
    },
    {
        "label": "Écrire un article",
        "permission": Permission.WRITE,
        "action": write_article
    },
    {
        "label": "Supprimer un article",
        "permission": Permission.DELETE,
        "action": delete_articles
    },
    {
        "label": "Se déconnecter",
        "action": None
    }
]

###############################################################################
# Implémentation du menu
###############################################################################
if __name__ == '__main__':
    print("---- Bienvenue dans le Low-Tech Blog! ----")

    while True:
        print(f"Qui va là ?")
        print(f"({', '.join([f'{u}: {r.value}' for u, r in USERS.items()])} – autre chose pour quitter)")
        user_name = input("> ")

        if user_name not in USERS:
            print("Y a rien à voir ici, circulez !")
            exit(1)

        # Récupère la bonne instance de User pour le nom entré
        current_user = get_user(user_name)

        print(f"Salut, {current_user.name} ! Que veux-tu faire aujourd'hui ?")

        # Liste les actions disponibles pour l'utilisateur courant
        # -> celles qui ne nécessitent aucune permission et celles que `current_user` a le droit d'effectuer
        possible_actions = [a for a in ACTIONS if a.get("permission") is None or current_user.can(a["permission"])]

        while True:
            # Affiche les actions disponibles à l'utilisateur
            for idx, action in enumerate(possible_actions):
                print(f"{idx + 1} -> {action['label']}")

            # Récupère le choix de l'utilisateur et exécute la fonction liée au choix
            action_idx = int(input("> ")) - 1

            # On recommence si le choix est invalide
            if 0 <= action_idx >= len(possible_actions):
                continue

            # Récupère l'action de l'élément de menu choisi
            action = possible_actions[action_idx]["action"]

            # "Déconnexion" si aucune action : on retourne vers la boucle infinie de premier niveau
            if action is None:
                break

            # Exécute l'action choisie
            action()
