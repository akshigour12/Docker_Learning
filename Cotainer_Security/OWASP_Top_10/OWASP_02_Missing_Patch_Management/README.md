# OWASP Docker Top 10 - #2 Missing Patch Management

## Objective

This lab demonstrates **OWASP Docker Top 10 #2 – Missing Patch Management** using Docker Scout.

The purpose is to compare:

- An outdated Docker base image (`python:3.7`)
- A patched Docker base image (`python:3.12-slim`)

and observe the difference in security vulnerabilities.

---

# What is Missing Patch Management?

Missing Patch Management refers to the failure to regularly update:

- Docker Engine
- Base Images
- Operating System Packages
- Application Dependencies

Outdated software often contains publicly known vulnerabilities (CVEs) that attackers can exploit.

---

# Vulnerable Dockerfile

```dockerfile
FROM python:3.7

CMD ["python", "--version"]
```

Python 3.7 is End-of-Life (EOL) and contains numerous known vulnerabilities.

---

# Secure Dockerfile

```dockerfile
FROM python:3.12-slim

CMD ["python", "--version"]
```

Python 3.12 is a supported version that receives regular security updates.

---

# Build Vulnerable Image

```bash
docker build -t owasp02:v1 -f Dockerfile.vulnerable .
```

---

# Build Secure Image

```bash
docker build -t owasp02:v2 -f Dockerfile.secure .
```

---

# Scan Vulnerable Image

```bash
docker scout quickview owasp02:v1
```

Detailed CVEs

```bash
docker scout cves owasp02:v1
```

---

# Scan Secure Image

```bash
docker scout quickview owasp02:v2
```

Detailed CVEs

```bash
docker scout cves owasp02:v2
```

---

# Expected Result

The vulnerable image should report:

- More Critical Vulnerabilities
- More High Vulnerabilities
- Older Base Image

The secure image should report:

- Fewer Vulnerabilities
- Updated Base Image
- Better Security Score

---

# Screenshots




# Mitigation

- Use supported Docker base images.
- Regularly rebuild Docker images.
- Apply operating system security updates.
- Scan images using Docker Scout.
- Monitor newly published CVEs.

---

# OWASP Reference

OWASP Docker Top 10

Control #2: Missing Patch Management
