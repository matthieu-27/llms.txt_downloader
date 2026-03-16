# LLMS.txt Downloader

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

Un outil Python pour télécharger et organiser les fichiers Markdown référencés dans un fichier `llms.txt`, en créant une structure de répertoires miroir avec des liens relatifs.

## Fonctionnalités

- Télécharge tous les fichiers `.md` référencés dans un `llms.txt`
- Crée une arborescence de répertoires miroir
- Génère un fichier `llms.txt` local avec des liens relatifs
- Normalise les noms de dossiers à partir du titre H1
- Gère les URLs relatives et absolues

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
python download_md_files.py https://example.com/llms.txt
```

### Exemple

Pour un fichier `llms.txt` avec un structure standardisé: [llmstxt.org](https://llmstxt.org/)

Le script créera :
```
.ai_conf/
├── llms.txt
├── <project-name>/
│   ├── SKILL.md
│   └── docs/
│       └── example.md
```

```

## Structure du projet

```
py_utils/
├── llms2md.py              # Script principal
├── README.md               # Ce fichier
├── requirements.txt        # Dépendances Python

```

## Contribution

Les contributions sont les bienvenues ! Voici comment participer :

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Bonnes pratiques

- Respectez le style de code existant
- Ajoutez des tests pour les nouvelles fonctionnalités
- Documentez les changements dans le README
- Mettez à jour les exemples si nécessaire

## Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

## Contact

Votre Nom - [@votre_twitter](https://twitter.com/votre_twitter) - votre.email@example.com

Lien du projet : [https://github.com/votre-utilisateur/llms-txt-downloader](https://github.com/votre-utilisateur/llms-txt-downloader)
```

---

### Fichiers complémentaires à créer :

1. **LICENSE** (Licence MIT) :
```text LICENSE
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

2. **requirements.txt** :
```text requirements.txt
requests>=2.28.1
```

3. **ISSUE_TEMPLATE.md** (dans `.github/`) :
```markdown .github/ISSUE_TEMPLATE.md
---
name: Bug Report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment (please complete the following information):**
 - OS: [e.g. iOS]
 - Python version: [e.g. 3.8]
 - Version [e.g. 1.0.0]

**Additional context**
Add any other context about the problem here.
```

4. **PULL_REQUEST_TEMPLATE.md** (dans `.github/`) :
```markdown .github/PULL_REQUEST_TEMPLATE.md
## Description

Please include a summary of the change and which issue is fixed. Please also include relevant motivation and context.

Fixes # (issue)

## Type of change

Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] This change requires a documentation update

## How Has This Been Tested?

Please describe the tests that you ran to verify your changes. Provide instructions so we can reproduce.

- [ ] Test A
- [ ] Test B

## Checklist:

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes