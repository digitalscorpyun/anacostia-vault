---
id: dockerize_node_wsl_lab
title: Dockerize a Node.js App (Local WSL) — Hands-on Lab README
category: learning_journal
style: CodeRitual
path: learning_journal/ibm_ai_developer/dockerize_node_wsl_lab
created: 2025-08-25
updated: 2025-08-25
status: active
priority: normal
summary: Step-by-step local walkthrough of IBM Module 2 Dockerfile lab on WSL Ubuntu with Docker, from zero to running container, plus troubleshooting.
longform_summary: >
  Beginner-safe, command-by-command guide: verify Docker, create a tiny Node app,
  write Dockerfile and .dockerignore, build, run (detached/foreground), verify with curl,
  stop/clean, and fix common issues (0.0.0.0 binding, CMD vs npm start, IPv4/IPv6, logs).
tags: [docker, nodejs, wsl, ubuntu, ibm_ai_developer, devops, ci_cd, containers]
cssclasses: [Tyrian-Purple, CodeRitual]
synapses: []
key_themes: [reproducibility, portability, DevSecOps, beginner_onramp, troubleshooting]
bias_analysis: Minimal risk; operational how-to with security notes (port, env, deps).
grok_ctx_reflection: Clean room build proved; errors reproduced and resolved (connection reset, CMD mismatch).
quotes: []
adinkra: Eban
linked_notes: [learning_journal/ibm_ai_developer, obsidian_fortress/configs/ubuntu_env_refinery]
---
You’re right—the body got clipped. Here’s a **complete drop-in replacement** for everything **after** your YAML frontmatter.

---

> **Prologue (ScorpyunStyle)**  
> We containerize the spark, seal it in steel, ship it anywhere.  
> No more “works on my machine.” The shrine runs the same, every time.

## 0) Prereqs (WSL Ubuntu 24.04)

You’re in Ubuntu (WSL2) and Docker works.

```bash
docker --version
docker run hello-world
```

Tip: keep two terminals—**T1** run app, **T2** test/manage.

## 1) Make a tiny Node app

```bash
mkdir -p ~/node-docker-lab && cd ~/node-docker-lab
npm init -y
npm pkg set scripts.start="node server.js"
cat > server.js <<'EOF'
const http=require('http');
const PORT=3000, HOST='0.0.0.0'; // bind for Docker
http.createServer((req,res)=>{
  res.statusCode=200;
  res.setHeader('Content-Type','text/plain; charset=utf-8');
  res.end('Hello from Dockerized Node 👋\n');
}).listen(PORT,HOST,()=>console.log(`Listening on http://${HOST}:${PORT}`));
EOF
```

**Why:** Minimal server; `0.0.0.0` makes it reachable from outside the container.

## 2) Write the Dockerfile

```dockerfile
# Dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install --omit=dev
COPY . .
ENV NODE_ENV=production
EXPOSE 3000
CMD ["node","server.js"]
```

**Why these lines:** `FROM` = base; `WORKDIR` = context; copy/`npm install` caches deps; `EXPOSE` documents port; `CMD` starts the app.

## 3) Ignore junk

```bash
cat > .dockerignore <<'EOF'
node_modules
.git
npm-debug.log
Dockerfile
docker-compose.yml
.env
EOF
```

Keeps images slim and builds fast.

## 4) Build the image

```bash
docker build -t node-app .
```

Creates an image called `node-app` from your Dockerfile.

## 5) Run the container

### A) Detached (background)

```bash
docker run -d --name node-app -p 3000:3000 node-app
docker ps             # see it “Up”
docker logs node-app  # Ctrl+C to stop viewing logs
```

### B) Foreground (see live output)

```bash
docker rm -f node-app 2>/dev/null || true
docker run --name node-app -p 3000:3000 node-app
# When done, press Ctrl+C here to stop it.
```

## 6) Verify from the second terminal (T2)

```bash
curl -v http://localhost:3000
```

**Expected:** `HTTP/1.1 200 OK` and “Hello from Dockerized Node 👋”.

## 7) Stop & clean

- If running **detached**:
    

```bash
docker stop node-app
docker rm node-app
```

- If running **foreground**: press **Ctrl+C** in that window, then:
    

```bash
docker rm node-app
```

Closing an extra terminal **does not** stop a detached container.

## 8) Troubleshooting (beginner-safe)

- **Connection reset / empty reply**
    
    - Ensure server binds `0.0.0.0` (see `server.js`).
        
    - Rebuild clean:
        
        ```bash
        docker rm -f node-app
        docker build --no-cache -t node-app .
        docker run -d --name node-app -p 3000:3000 node-app
        ```
        
    - Force IPv4 test:
        
        ```bash
        curl -4v http://localhost:3000
        ```
        
- **Port mismatch**
    
    - App uses `3000`. Match `EXPOSE 3000` and `-p 3000:3000`.
        
- **Wrong entry file**
    
    - If your app file isn’t `server.js`, update the Dockerfile `CMD`.
        
- **Peek inside container (Alpine shell)**
    
    ```bash
    docker exec -it node-app ash
    # (optional) apk add --no-cache curl
    ```
    
- **Native deps error during install**
    
    - Add before `npm install`:
        
        ```dockerfile
        RUN apk add --no-cache python3 make g++
        ```
        

## 9) What these commands mean (plain English)

- `cat <<'EOF' … EOF` → writes a file with the content you typed.
    
- `docker build -t node-app .` → turns Dockerfile into an image.
    
- `docker run …` → starts a container from that image.
    
- `-d` = background; `-p A:B` maps host port A → container port B.
    
- `docker ps` = list running containers.
    
- `docker logs node-app` = see app output; **Ctrl+C** exits log view.
    
- `docker stop` / `docker rm` = stop and remove containers.
    
- `docker exec -it node-app ash` = open a shell inside the container.
    

## 10) Quick cheatsheet

```bash
# build
docker build -t node-app .
# run
docker run -d --name node-app -p 3000:3000 node-app
# verify
curl http://localhost:3000
# logs/status
docker logs -f node-app
docker ps
# stop/clean
docker stop node-app && docker rm node-app
```

## Appendix (optional): Multi-stage (smaller prod images)

```dockerfile
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM deps AS build
COPY . .
RUN npm run build || true

FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
EXPOSE 3000
CMD ["node","dist/server.js"]
```

> **Close (ScorpyunStyle)**  
> Ship the code, keep the rhythm. Same hymn on every machine—ritual complete.