# rabbitmq

## install

``` sh
python -m venv .venv
pip -r requirements.txt

docker-compose up -d

docker exec -it rabbitmq1 /bin/bash
rabbitmqctl join_cluster rabbit@rabbitmq2
exit

docker exec -it rabbitmq1 /bin/bash
rabbitmqctl join_cluster rabbit@rabbitmq2
exit


```