# Docker SDK for Python Commands

## Connect

```python
import docker

client = docker.from_env()
```

---

## Containers

### List

```python
client.containers.list(all=True)
```

### Run

```python
client.containers.run("ubuntu", "sleep 300", detach=True)
```

### Get

```python
container = client.containers.get("container-name")
```

### Stop

```python
container.stop()
```

### Start

```python
container.start()
```

### Restart

```python
container.restart()
```

### Remove

```python
container.remove(force=True)
```

### Logs

```python
container.logs().decode()
```

### Execute Command

```python
container.exec_run("ls /")
```

### Inspect

```python
container.attrs
```

### Statistics

```python
container.stats(stream=False)
```

---

## Images

### List Images

```python
client.images.list()
```

### Pull Image

```python
client.images.pull("ubuntu")
```

### Remove Image

```python
client.images.remove("ubuntu")
```

### Build Image

```python
client.images.build(path=".", tag="my-image")
```

---

## Docker CLI vs Docker SDK

| Docker CLI | Docker SDK |
|------------|------------|
| docker ps -a | client.containers.list(all=True) |
| docker run | client.containers.run() |
| docker stop | container.stop() |
| docker start | container.start() |
| docker restart | container.restart() |
| docker rm | container.remove() |
| docker logs | container.logs() |
| docker exec | container.exec_run() |
| docker images | client.images.list() |
| docker pull | client.images.pull() |
| docker rmi | client.images.remove() |
| docker build | client.images.build() |
