# Screenshots

## 1. Installing Software Inside a Running Container (Vulnerable)

The vulnerable container allows packages to be installed after deployment. This modifies the running container and violates the immutable container principle.

```bash
apt update
apt install -y curl
```

![Installing curl](Screenshots/curl%20installation-insecure.png)

---

## 2. Verifying the Installed Package

After installation, the `curl` binary is available inside the running container, demonstrating that the container has been manually modified.

```bash
curl --version
```

![Curl Version](Screenshots/curl%20version.png)

---

## 3. Creating Files Inside the Running Container

A file is manually created inside the container, further illustrating that changes can be made after deployment.

```bash
touch hacked.txt
```

![File Creation](Screenshots/file-creation-insecure.png)

---

## 4. Removing and Recreating the Container

The modified container is removed and recreated from the original image. Since the image was never updated, all manual changes are lost.

```bash
docker rm -f immutable-vulnerable

docker run -d --name immutable-vulnerable owasp08:v1
```

![Container Recreation](Screenshots/container%20remove-insecure.png)

---

## 5. Manual Changes Are Lost

After recreating the container, the previously created file no longer exists. This demonstrates that modifications made directly inside a running container are not persistent.

```bash
ls
```

![File Lost](Screenshots/file%20lost-insecure.png)

---

## 6. Package No Longer Exists

Since the container was recreated from the original image, the manually installed package is no longer available.

```bash
curl --version
```

![Curl Not Found](Screenshots/curl%20not%20found-insecure.png)

---

## 7. Secure Image

The secure image includes `curl` during the image build process. No manual modifications are required after deployment.

```bash
curl --version
```

![Secure Container](Screenshots/curl-secure.png)
