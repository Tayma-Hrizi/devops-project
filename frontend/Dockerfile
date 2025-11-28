# frontend/Dockerfile
# Utiliser Nginx pour servir les fichiers statiques
FROM nginx:alpine

# Supprimer le contenu par défaut de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copier l'index.html dans le répertoire de service de Nginx
COPY index.html /usr/share/nginx/html/

# Nginx expose le port 80 par défaut
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]