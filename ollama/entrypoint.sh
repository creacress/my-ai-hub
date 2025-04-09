#!/bin/bash
# Pull le modèle si absent, puis le lance
ollama serve &
sleep 3
ollama pull llama3
wait
