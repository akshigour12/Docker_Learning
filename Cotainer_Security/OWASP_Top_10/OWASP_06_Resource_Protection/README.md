# OWASP Docker Top 10 #6 – Resource Protection

## Objective

This lab demonstrates how Docker resource limits prevent a container from consuming excessive CPU, memory, and system resources.

---

# What is Resource Protection?

Resource Protection limits the amount of CPU, memory, and processes available to a container.

Without limits, one compromised or malfunctioning container can consume all host resources.

---

# Lab Structure

```
OWASP_06_Resource_Protection/
│
├── Dockerfile
├── cpu_stress.py
├── README.md
└── Screenshots/
```

---

# Vulnerable Configuration

Run without limits.

```bash
docker run -d \
--name resource-unlimited \
owasp06:v1
```

---

# Secure Configuration

Run with resource constraints.

```bash
docker run -d \
--name resource-limited \
--cpus=0.5 \
--memory=128m \
--pids-limit=100 \
owasp06:v1
```

---

# Verification

Monitor container resources.

```bash
docker stats
```

Inspect limits.

```bash
docker inspect resource-limited
```

---

# Security Comparison

| Vulnerable | Secure |
|------------|--------|
| Unlimited CPU | CPU restricted |
| Unlimited memory | Memory limited |
| Unlimited processes | PID limit |
| High DoS risk | Protected |

---

# Screenshots

- docker stats (Unlimited)
- docker stats (Limited)
- docker inspect
- CPU comparison

---

# Best Practices

- Configure CPU limits.
- Configure memory limits.
- Configure PID limits.
- Monitor resource usage.
- Prevent Denial of Service attacks.

---

# Conclusion

Applying resource limits prevents a single container from exhausting host resources and improves overall platform stability.
