#!/bin/bash

# Go to the home directory and clone Scripts repo
cd "$HOME" || exit
git clone https://github.com/portugueseTorch/CPP_Scripts || exit

# Create a new directory in home to store the scripts
mkdir .scripts || exit
cp CPP_Scripts/*.py ./.scripts

# Creating the alias - ADD YOUR NEW ONES HERE
RC_FILE="$HOME/.zshrc"

# New module alias
if ! grep "new=" "$RC_FILE" &> /dev/null; then
	printf "\nalias new=\"python3 %s/.scripts/new_module.py\"\n" "$HOME" >> "$RC_FILE"
	echo "Alias \"new\" created"
fi

# Delete git repo
rm -rf "$HOME/CPP_Scripts"

# Automatically renews the shell session
exec "$SHELL" || exit
