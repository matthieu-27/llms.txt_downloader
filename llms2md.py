import argparse
import os
import re
from urllib.parse import urljoin, urlparse

import requests


def normalize_dirname(title):
    """Convertit un titre H1 en nom de dossier valide"""
    title = title.lstrip("#").strip()
    return re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")


def extract_md_links(text, base_url):
    """Extrait les liens Markdown et retourne les URLs absolues et leurs descriptions"""
    pattern = r"-\s*\[(.*?)\]\((.*?\.md)\):\s*(.*)"
    matches = re.findall(pattern, text)
    return [(name, urljoin(base_url, url.strip()), desc) for name, url, desc in matches]


def create_directory_structure(url, base_dir):
    """Crée l'arborescence de répertoires pour un fichier"""
    path = urlparse(url).path.lstrip("/")
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path


def download_md_files(input_url):
    """Télécharge et organise les fichiers .md selon la structure demandée"""
    try:
        # Télécharger le fichier source
        response = requests.get(input_url)
        response.raise_for_status()
        content = response.text

        # Extraire le titre H1
        first_line = content.split("\n")[0]
        if not first_line.startswith("# "):
            raise ValueError("Le fichier doit commencer par un titre H1")

        # Créer le dossier racine
        root_dir = normalize_dirname(first_line)
        os.makedirs(root_dir, exist_ok=True)
        print(f"Dossier racine créé: {root_dir}")

        # Extraire les liens et leurs descriptions
        base_url = input_url.rsplit("/", 1)[0] + "/"
        links = extract_md_links(content, base_url)

        # Télécharger chaque fichier .md
        for name, url, desc in links:
            try:
                # Créer l'arborescence de répertoires
                file_path = create_directory_structure(url, root_dir)

                # Télécharger le fichier
                file_response = requests.get(url)
                file_response.raise_for_status()

                # Sauvegarder le fichier
                with open(file_path, "wb") as f:
                    f.write(file_response.content)
                print(f"Téléchargé: {file_path}")

            except Exception as e:
                print(f"Erreur avec {url}: {e}")

        # Créer le fichier llms.txt local avec liens relatifs
        local_llms_path = os.path.join(root_dir, "llms.txt")
        with open(local_llms_path, "w", encoding="utf-8") as f:
            # Écrire le titre H1
            f.write(first_line + "\n\n")

            # Réécrire les liens avec chemins relatifs
            for name, url, desc in links:
                relative_path = os.path.relpath(
                    create_directory_structure(url, root_dir), root_dir
                )
                f.write(f"- [{name}]({relative_path}): {desc}\n")

        print(f"Fichier llms.txt local créé: {local_llms_path}")

    except Exception as e:
        print(f"Erreur globale: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Organise les fichiers .md depuis un llms.txt distant"
    )
    parser.add_argument("input_url", help="URL du fichier llms.txt source")
    args = parser.parse_args()

    download_md_files(args.input_url)
