#!/bin/bash
cd "$(dirname "$0")"
echo "A iniciar a sincronização com o servidor da Hostinger..."
python3 publicar-hostinger.py
echo "Processo finalizado."