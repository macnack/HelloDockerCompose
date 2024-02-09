# Docker compose hello world

Build and compose up example
```
docker-compose up --build
```
compose up with custom name
```
docker-compose -p myproject1 up
```
## Running Docker Compose in background
```
docker-compose up -d
```
## Stop and removing background Containers
```
docker-compose down
```
## Viewing logs
```
docker-compose logs
```
## Following in Real Time
```
docker-compose logs -f
```
## Viewing logs in specific services
```
docker-compose logs -f hello1
```
### See the last 10 lines
```
docker-compose logs --tail=10 -f hello1
```
## Display resource usage
```
docker stats
```
