#!/bin/bash
# vault_script_catalog.sh: Catalog .py and .ps1 files in the Anacostia Vault
# Path: /mnt/c/Users/digitalscorpyun/sankofa_temple/Anacostia/vault_ops/vault_script_catalog.sh
echo "[Catalog Initiated @ $(date)]" >> /mnt/c/Users/digitalscorpyun/sankofa_temple/Anacostia/logs/vault_env_refinery.log
find /mnt/c/Users/digitalscorpyun/projects_2025 -type f \( -name "*.py" -o -name "*.ps1" \) -exec ls -l --time-style=long-iso {} \; | awk '{print $6, $7, $8, $5, $9}' > /mnt/c/Users/digitalscorpyun/sankofa_temple/Anacostia/vault_catalog.txt
echo "[Catalog Completed @ $(date)]" >> /mnt/c/Users/digitalscorpyun/sankofa_temple/Anacostia/logs/vault_env_refinery.log
