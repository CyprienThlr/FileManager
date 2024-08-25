import os
import shutil
import sys

class FileManager:

    def __init__(self, path):
        self.path = path

    def listing(self):
        files = os.listdir(self.path)
        return files

    def renaming(self, new_name):
        if not os.path.exists(self.path):
            print("Ce dossier/fichier n'existe pas.")
        else:
            repertory = os.path.dirname(self.path)
            new_path = os.path.join(repertory, new_name)
            try:
                os.rename(self.path, new_path)
                self.path = new_path
                return f"Renommé en {new_name}."
            except PermissionError:
                print("Accès refusé.")
            except FileNotFoundError:
                print("Le dossier/fichier est introuvable.")  

    def create(self, folder_name):
        try:
            os.mkdir(os.path.join(self.path, folder_name))
            return f"Repertoir {folder_name} créé."   
        except FileExistsError:
            print("Ce dossier existe deja.")
        except PermissionError:
            print("Accès refusé.")
        except Exception as e:
            return f'Erreur : {e}'
        
    def deleting(self):
        if os.path.isfile(self.path):
            os.remove(self.path)
        elif os.path.isdir(self.path):
            shutil.rmtree(self.path)
        return f"Dossier supprimé."

def main():
    print("Commands :")
    print("1 - Lister le contenu d'un dossier")
    print("2 - Renommer un fichier ou un dossier")
    print("3 - Créer un nouveau dossier")
    print("4 - Supprimer un dossier ou un fichier")
    print("5 - Exit")

    chose = input("Saisissez le nuléro de la commande à exécuter : ")
    if int(chose) != 5:
        path = input("Saisissez le chemin du dossier/fichier : ")

    manager = FileManager(path)

    if int(chose) == 1 :
        print(manager.listing())
        main()

    elif int(chose) == 2 :
        new_name = input("Saisissez le nouveau nom du dossier/fichier : ")
        print(manager.renaming(new_name))
        main()

    elif int(chose) == 3 :
        folder_name = input("Entrez le nom du fichier à créer : ")
        print(manager.create(folder_name))
        main()

    elif int(chose) == 4 :
        print(manager.deleting())
        main()

    elif int(chose) == 5 :
        sys.exit

if __name__ == "__main__":
    main()
