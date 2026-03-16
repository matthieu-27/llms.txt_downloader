# LLMS.txt Downloader

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Un outil Python pour télécharger et organiser les fichiers Markdown référencés dans un fichier `llms.txt`, en créant une structure de répertoires miroir avec des liens relatifs selon le standard [llmstxt.org](https://llmstxt.org/).

## Fonctionnalités

- Télécharge tous les fichiers `.md` référencés dans un `llms.txt`
- Crée une arborescence de répertoires miroir selon la spécification llmstxt
- Génère un fichier `llms.txt` local avec des liens relatifs
- Normalise les noms de dossiers à partir du titre H1
- Gère les URLs relatives et absolues
- Structure conforme au standard `.ai_conf/`

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-utilisateur/llms-txt-downloader.git
cd llms-txt-downloader
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

```bash
python llms.txt_downloader/llms2md.py https://example.com/llms.txt
```

### Exemple de sortie

Pour un fichier `llms.txt` conforme à [llmstxt.org](https://llmstxt.org/) :

```bash
.ai_conf/
├── llms.txt
└── <project-name>/
    ├── SKILL.md
    └── docs/
        └── example.md
```

## Structure du projet

```
llms.txt_downloader
├── llms2md.py              # Script principal
├── README.md               # Ce fichier
├── LICENSE                 # License
└── requirements.txt        # Dépendances Python
```

## Contribution

Les contributions sont les bienvenues ! Voici comment participer :

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Bonnes pratiques

- Respectez le style de code PEP 8
- Ajoutez des tests unitaires pour les nouvelles fonctionnalités
- Documentez les changements dans le README
- Mettez à jour les exemples si nécessaire
- Utilisez des messages de commit clairs et descriptifs

## Licence

Distribué sous la licence MIT. Voir [LICENSE](LICENSE) pour plus d'informations.

## Contact

Votre Nom - [@votre_twitter](https://twitter.com/votre_twitter) - votre.email@example.com

Lien du projet : [https://github.com/matthieu-27/llms-txt-downloader](https://github.com/matthieu-27/llms-txt-downloader)