# MultiAcqui

Le but de ce répertoire est de rassembler différentes acquisitions (Motion Capture, Vidéos, accéléromètre...) ainsi que leur traitement (Séries temporelles, tracking OpenPose, calcul de métriques...).

# Ajout d'une nouvelle acquisition

- copier le dossier 'template'
- renommer ce dossier de la façon suivante : JJMMAA_NomDuProjet_MotsClefs
- ouvrir et compléter le ficher readme.md permettant de décrire l'acquisition
- placer dans le dossier 'videos' les vidéos extraites d'OpenPose et de la GoPro
- placer dans le dossier 'OpenPose_skellington_capture/all_json' les json extraits avec OpenPose
- dans le dossier 'OpenPose_skellington_capture' créer un zip de 'all_json"
- coller le fichier csv extrait du Motion Capture dans le dossier 'template'
- ouvrir (après avoir ouvert jupyter notebook depuis Anaconda) le notebook charge_data.ipynb qui permet un premier chargement des données avec calcul de statistiques. ATTENTION, il faut remplacer les chemins dans le code et adapter les variables.

