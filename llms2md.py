import argparse
import os
import re
from urllib.parse import urljoin, urlparse

import requests  # type: ignore


def normalize_dirname(title):
    """Convertit un titre H1 en nom de dossier valide"""
    title = title.lstrip("#").strip()
    return re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")


def extract_md_links(text, base_url):
    """Extrait les liens Markdown et retourne les URLs absolues et leurs descriptions"""
    pattern = r"-\s*\[(.*?)\]\((.*?)\):\s*(.*)"
    matches = re.findall(pattern, text)
    results = []
    for name, url, desc in matches:
        # Ajoute .md si absent dans l'URL
        if not url.lower().endswith('.md'):
            url = url + '.md'
        results.append((name, urljoin(base_url, url.strip()), desc))
    return results


def create_directory_structure(url, base_dir):
    """Crée l'arborescence de répertoires pour un fichier"""
    path = urlparse(url).path.lstrip("/")
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path


def try_download_url(url, max_retries=2):
    """Tente de télécharger une URL avec plusieurs stratégies"""
    strategies = [
        # Stratégie 1: URL directe
        lambda u: u,

        # Stratégie 2: URL avec .md ajouté
        lambda u: u if u.lower().endswith('.md') else u + '.md',

        # Stratégie 3: URL avec /docs/overview.md ajouté
        lambda u: u.rstrip('/') + '/docs/overview.md',
    ]

    for attempt in range(max_retries):
        for strategy in strategies:
            try:
                current_url = strategy(url)
                response = requests.get(current_url, timeout=10)
                if response.status_code == 200:
                    return response, current_url
            except requests.RequestException:
                continue

    return None, url


def download_md_files(input_path, output_dir=".llms2md"):
    """Télécharge et organise les fichiers .md depuis une URL ou un fichier local"""
    try:
        # Lire le contenu depuis une URL ou un fichier local
        if input_path.startswith(('http://', 'https://')):
            response = requests.get(input_path)
            response.raise_for_status()
            content = response.text
            base_url = input_path.rsplit("/", 1)[0] + "/"
        else:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            base_url = os.path.dirname(os.path.abspath(input_path)) + "/"

        # Extraire le titre H1
        first_line = content.split("\n")[0]
        if not first_line.startswith("# "):
            raise ValueError("Le fichier doit commencer par un titre H1")

        # Créer le dossier racine (output_dir)
        os.makedirs(output_dir, exist_ok=True)
        print(f"Dossier racine créé: {output_dir}")
        os.chdir(output_dir)

        created_dir = normalize_dirname(first_line)
        os.makedirs(created_dir, exist_ok=True)
        print(f"Dossier racine créé: {created_dir}")

        # Sites avec conventions spéciales (à étendre si nécessaire)
        SPECIAL_SITES = {
            'github.com': {
                'url_transform': lambda u: u.replace('/blob/', '/raw/')
            }
        }

        # Extraire les liens et leurs descriptions
        links = extract_md_links(content, base_url)
        processed_links = []

        # Télécharger chaque fichier .md
        for name, url, desc in links:
            try:
                # Appliquer les transformations spécifiques au site
                parsed_url = urlparse(url)
                if parsed_url.netloc in SPECIAL_SITES:
                    url = SPECIAL_SITES[parsed_url.netloc]['url_transform'](
                        url)

                # Télécharger avec stratégie de fallback
                response, final_url = try_download_url(url)

                if response:
                    # Créer l'arborescence de répertoires
                    file_path = create_directory_structure(
                        final_url, created_dir)

                    # Sauvegarder le fichier
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"Téléchargé: {file_path}")

                    # Conserver le lien traité
                    processed_links.append((name, final_url, desc))
                else:
                    print(f"Échec du téléchargement: {url}")
            except Exception as e:
                print(f"Erreur avec {url}: {e}")

        # Créer le fichier llms.txt local avec liens relatifs
        local_llms_path = os.path.join(created_dir, "llms.txt")
        with open(local_llms_path, "w", encoding="utf-8") as f:
            # Écrire le titre H1
            f.write(first_line + "\n\n")

            # Réécrire les liens avec chemins relatifs
            for name, url, desc in processed_links:
                relative_path = os.path.relpath(
                    create_directory_structure(url, created_dir), created_dir)
                # Supprime .md si présent dans le chemin relatif pour le fichier local
                if relative_path.lower().endswith('.md'):
                    relative_path = relative_path[:-3]
                f.write(f"- [{name}]({relative_path}): {desc}\n")

        print(f"Fichier llms.txt local créé: {local_llms_path}")

    except Exception as e:
        print(f"Erreur globale: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=
        "Organise les fichiers .md depuis un llms.txt (URL ou fichier local)")
    parser.add_argument("input_path",
                        help="URL ou chemin du fichier llms.txt source")
    parser.add_argument(
        "-o",
        "--output",
        help="Répertoire de sortie (par défaut: .llms2md)",
        default=".llms2md",
    )
    args = parser.parse_args()

    download_md_files(args.input_path, args.output)
