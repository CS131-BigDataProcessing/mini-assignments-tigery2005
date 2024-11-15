#!/bin/bash

# Define the paths
HOME_DIR="/Users/tiger/mini-assignments-tigery2005"
BACKUP_DIR="$HOME_DIR/Yang-T_A9/backup_folder"
BACKUP_FILE="$BACKUP_DIR/home_backup.tar.gz"

tar --exclude="$BACKUP_DIR" -czf "$BACKUP_FILE" "$HOME_DIR"


