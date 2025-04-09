FROM ubuntu:24.10

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y curl gnupg lsb-release ca-certificates && \
    curl https://ollama.com/install.sh | bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Charge le modèle au build
RUN ollama pull llama3

EXPOSE 11434

# Lance le modèle automatiquement
CMD ["ollama", "run", "llama3"]
