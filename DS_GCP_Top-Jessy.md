# Liens

github : https://github.com/TopJessy/tp-gcp
Gcloud :

# Questions Ouvertes

## Décrivez les étapes pour créer un Service Account dans GCP. Quelles sont les bonnes pratiques à suivre en matière de gestion des clés et de sécurité ?

    - Aller dans GCP > IAM & Admin > Service Accounts.
    - Créer un compte avec un nom et des rôles adaptés.
    - Il faut appliquer le principe du moindre privilège.
    - Ne pas exposer les clés.

## Comment créer un bucket sur Google Cloud Storage ? Précisez les configurations importantes à définir (localisation, politique de conservation, etc.) et comment celles-ci impactent la sécurité et la performance. 


    - Aller dans GCP > Cloud Storage > "Créer un bucket".
    - Choisir un nom unique et une localisation.
    - Définir la classe de stockage (Standard).
    - Configurer la sécurité :
        Désactiver l’accès public.
        IAM : Restreindre les rôles d’accès.
    - Performance : Une région proche réduit la latence.
    - Sécurité : Restreindre les accès et utiliser des logs.




## En quoi consiste la gestion des identités et des accès (IAM) sur GCP ? Donnez un exemple concret de configuration des droits pour limiter l'accès à une ressource critique.


    - IAM contrôle qui accède à quoi via des rôles et politiques.
    - Il faut toujours appliquer le principe du moindre privilège.
    - Et configurer des alertes sur accès anormal.


## Expliquez comment configurer la facturation sur GCP. Quelles précautions recommanderiez-vous pour éviter des coûts imprévus lors du déploiement de projets ?

    - Aller dans GCP > Facturation.
    - Associer un compte de facturation au projet.
    - Créer un budget avec alertes pour éviter les dépassements.
    - Surveiller les coûts avec Cost Explorer et appliquer des étiquettes.
    - Limiter les quotas des services pour éviter une surconsommation.
    - Il faut désactiver les ressources inutilisées.
    - Il faut utiliser des VM préemptibles et des stockages adaptés.
    - Et faut activer les recommandations GCP pour optimiser les coûts.


## Quelle est la chose importante que l'on dit à la fin du cours en quittant la salle de TP ?

    - Dire aurevoir au professeur.
