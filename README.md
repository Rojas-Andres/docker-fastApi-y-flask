# docker-fastApi-y-flask

La pagina web es desarrollada con flask y esta lo que hace es hacer peticiones a fastapi .

Correr:

docker-compose build
docker-compose up

Ver la pagina web:

http://localhost:5000/


Subir a aws con docker swarm (Ubuntu)

- En cada maquina ejecutar los siguientes comandos 
    - sudo apt-get update
    - sudo apt-get -y install docker.io
    - sudo usermod -aG docker ubuntu
- Luego de eso salirse de cada maquina y volver a entrar para que podamos ejecutar los comandos de docker
    - probar en cada maquina docker --version

- Definir un manager de las 3 maquinas y ejecutar.
    - sudo docker swarm init --advertise-addr <ip-interna-de-la-maquina>
    - Eso entregara un docker swarm join --token <token> ... Eso que entrega pegarlo en los workers.
- Ejecutar en el manager.
    - docker service ls
    - docker node ls