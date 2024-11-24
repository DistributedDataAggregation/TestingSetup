sudo docker run --env-file .env \
    -p 8080:8080 -p 8081:8081 -p 3000:3000 \
    -v /home/data:/data \
    -it node-image:latest