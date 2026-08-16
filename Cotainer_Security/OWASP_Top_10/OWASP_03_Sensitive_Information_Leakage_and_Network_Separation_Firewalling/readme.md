# OWASP Docker Top 10 - #3 Sensitive Information Leakage & Network Separation

## Objective

This lab demonstrates how improper Docker networking can expose sensitive services and how network segmentation helps reduce the attack surface.

---

# What is Network Separation?

Network Separation is the practice of isolating Docker containers into different networks so that only authorized containers can communicate with each other.

Without proper isolation, an attacker who compromises one container may gain access to databases, internal APIs, or other sensitive services.

---

# Lab Overview

This lab contains two Docker Compose configurations:

- **docker-compose.insecure.yml**
- **docker-compose.secure.yml**

---

# Scenario 1 - Insecure Network

All containers are connected to the same Docker network.

```
Web
   │
   ├────────► API
   │
   └────────► Database
```

### Services

- Web
- API
- Database

All containers can communicate with each other.

---

## Start the Insecure Environment

```bash
docker compose -f docker-compose.insecure.yml up -d
```

---

## Verify Running Containers

```bash
docker ps
```

---

## Inspect the Network

```bash
docker network ls
```

```bash
docker network inspect <network_name>
```

---

## Test Connectivity

Access the web container:

```bash
docker exec -it web sh
```

Ping the API:

```bash
ping api
```

**Result**

✅ Success

Ping the Database:

```bash
ping database
```

**Result**

✅ Success

### Observation

All containers can communicate because they share the same Docker network.

---

# Scenario 2 - Secure Network

Containers are separated into two custom Docker networks.

```
Frontend Network

Web  <------>  API

Backend Network

API  <------> Database
```

The Web container is **not** connected to the backend network.

---

## Stop the Insecure Environment

```bash
docker compose -f docker-compose.insecure.yml down
```

---

## Start the Secure Environment

```bash
docker compose -f docker-compose.secure.yml up -d
```

---

## Inspect Networks

```bash
docker network inspect frontend
```

```bash
docker network inspect backend
```

---

## Test Connectivity

### From Web Container

```bash
docker exec -it web sh
```

Ping API

```bash
ping api
```

**Result**

✅ Success

Ping Database

```bash
ping database
```

**Result**

❌ Failed

---

### From API Container

```bash
docker exec -it api sh
```

Ping Database

```bash
ping database
```

**Result**

✅ Success

---

# Comparison

| Test | Insecure | Secure |
|------|----------|---------|
| Web → API | ✅ Allowed | ✅ Allowed |
| Web → Database | ✅ Allowed | ❌ Blocked |
| API → Database | ✅ Allowed | ✅ Allowed |
| Network Isolation | ❌ No | ✅ Yes |

---

# Security Benefits

- Reduces attack surface.
- Prevents unauthorized access to backend services.
- Limits lateral movement after container compromise.
- Improves network segmentation.
- Follows the principle of least privilege.

---

# Mitigation

- Create custom Docker networks.
- Separate frontend and backend services.
- Restrict container communication to only what is required.
- Avoid exposing internal services unnecessarily.
- Use firewall rules and network policies where applicable.

---

# Screenshots

## Insecure Network

![Insecure Network](Screenshots/insecure-network.png)

---

## Secure Frontend Network

![Frontend Network](Screenshots/frontend-network.png)

---

## Secure Backend Network

![Backend Network](Screenshots/backend-network.png)

---

## Web → API

![Web API](Screenshots/ping-api-success.png)

---

## Web → Database

![Web Database](Screenshots/ping-database-failed.png)

---

## API → Database

![API Database](Screenshots/ping-database-success.png)

---

# Conclusion

Using Docker's custom networking capabilities, we can isolate containers and restrict communication between services. Network separation minimizes the impact of a compromised container and is an important container security best practice.
