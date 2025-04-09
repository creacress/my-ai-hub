FROM ubuntu:22.04

# Évite les prompts interactifs
ENV DEBIAN_FRONTEND=noninteractive

# Installation des dépendances minimales + installation Ollama
RUN apt-get update && \
    apt-get install -y curl gnupg lsb-release ca-certificates && \
    curl https://ollama.com/install.sh | bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Exposition du port API Ollama
EXPOSE 11434

# Lancement du serveur Ollama
CMD ["ollama", "serve"]
