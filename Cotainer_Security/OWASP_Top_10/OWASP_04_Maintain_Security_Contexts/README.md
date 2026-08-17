# OWASP Docker Top 10 #4 – Maintain Security Contexts

## Objective

This lab demonstrates how to secure Docker containers by maintaining proper security contexts. It compares an insecure container running with excessive privileges against a secure container following the Principle of Least Privilege.

---

# What are Security Contexts?

A security context defines the permissions and privileges of a container, including:

- User identity (root or non-root)
- Linux capabilities
- Privileged mode
- Read-only filesystem
- Privilege escalation settings

Maintaining proper security contexts reduces the attack surface and limits the impact of a compromised container.

---

# Lab Structure

```
OWASP_04_Maintain_Security_Contexts/
│
├── Dockerfile.vulnerable
├── Dockerfile.secure
├── README.md
└── Screenshots/
```

---

# Vulnerable Configuration

The vulnerable container:

- Runs as the **root** user.
- Is started using the `--privileged` flag.
- Has a writable root filesystem.
- Has unrestricted Linux capabilities.

Build:

```bash
docker build -f Dockerfile.vulnerable -t owasp04:v1 .
```

Run:

```bash
docker run -d \
  --name insecure-container \
  --privileged \
  owasp04:v1
```

---

# Secure Configuration

The secure container:

- Runs as a dedicated **non-root** user (`appuser`).
- Drops all Linux capabilities.
- Prevents privilege escalation.
- Uses a read-only root filesystem.

Build:

```bash
docker build -f Dockerfile.secure -t owasp04:v2 .
```

Run:

```bash
docker run -d \
  --name secure-container \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --read-only \
  owasp04:v2
```

---

# Verification

## Check User

```bash
docker exec -it insecure-container bash
whoami
```

Expected:

```
root
```

---

```bash
docker exec -it secure-container sh
whoami
```

Expected:

```
appuser
```

---

## Check Privileged Mode

```bash
docker inspect insecure-container --format='Privileged={{.HostConfig.Privileged}}'
```

Expected:

```
Privileged=true
```

```bash
docker inspect secure-container --format='Privileged={{.HostConfig.Privileged}}'
```

Expected:

```
Privileged=false
```

---

## Test Read-Only Filesystem

Inside the vulnerable container:

```bash
touch /test.txt
```

Result:

```
Success
```

Inside the secure container:

```bash
touch /test.txt
```

Result:

```
touch: cannot touch '/test.txt': Read-only file system
```

---

# Security Comparison

| Feature | Vulnerable | Secure |
|----------|------------|---------|
| Runs as Root | ✅ Yes | ❌ No |
| Non-Root User | ❌ No | ✅ Yes |
| Privileged Mode | ✅ Enabled | ❌ Disabled |
| Linux Capabilities | Full | Dropped |
| Read-Only Root Filesystem | ❌ No | ✅ Yes |
| Privilege Escalation | Allowed | Prevented |

---

# Screenshots

## 1. Linux Capabilities

Shows the capabilities available to the container.

![Linux Capabilities](Screenshots/capsh_Priviledges.png)

---

## 2. Secure Container Running as Non-Root

The secure container runs as `appuser` instead of `root`.

![Secure Container User](Screenshots/secure_container_appuser.png)

---

## 3. Privileged vs Non-Privileged Container

Comparison of the `Privileged` setting.

- Vulnerable Container → `Privileged=true`
- Secure Container → `Privileged=false`

![Privileged Comparison](Screenshots/priviledges_true_false.png)

---

## 4. Writable Root Filesystem

The vulnerable container allows file creation.

![Writable Filesystem](Screenshots/touch_test.png)

---

## 5. Read-Only Root Filesystem

The secure container blocks filesystem modifications.

![Read-Only Filesystem](Screenshots/touch_Secure_file.png)

---

# Security Best Practices

- Run containers as a non-root user.
- Avoid using the `--privileged` flag.
- Drop unnecessary Linux capabilities using `--cap-drop`.
- Prevent privilege escalation with `--security-opt=no-new-privileges`.
- Use a read-only root filesystem whenever possible.
- Follow the Principle of Least Privilege.

---

# Conclusion

Maintaining proper security contexts is essential for container security. By avoiding privileged containers, running applications as non-root users, dropping unnecessary capabilities, and enabling a read-only filesystem, organizations can significantly reduce the impact of container compromise and improve the overall security posture of Docker deployments.
