#!/bin/bash

# Go to the home directory and clone Scripts repo
cd "$HOME" || exit
git clone https://github.com/portugueseTorch/Scripts || exit

# Create a new directory in home to store the scripts
mkdir .scripts || exit
cp Scripts/*.py ./.scripts

# Creating the alias - ADD YOUR NEW ONES HERE
ZSH_FILE="$HOME/.zshrc"
BASH_FILE="$HOME/.bashrc"

# New project alias
if ! grep "proj=" "$ZSH_FILE" &>  ! grep "proj=" "$BASH_FILE" &> /dev/null; then
	printf "\nalias proj=\"python3 %s/.scripts/new_project.py\"\n" "$HOME" >> "$ZSH_FILE"
	printf "\nalias proj=\"python3 %s/.scripts/new_project.py\"\n" "$HOME" >> "$BASH_FILE"
	echo "Alias \"proj\" created"
fi

# New module alias
if ! grep "new=" "$ZSH_FILE" &>  ! grep "new=" "$BASH_FILE" &> /dev/null; then
	printf "\nalias new=\"python3 %s/.scripts/new_module.py\"\n" "$HOME" >> "$ZSH_FILE"
	printf "\nalias new=\"python3 %s/.scripts/new_module.py\"\n" "$HOME" >> "$BASH_FILE"
	echo "Alias \"new\" created"
fi

# New class alias
if ! grep "class=" "$ZSH_FILE" &>  ! grep "class=" "$BASH_FILE" &> /dev/null; then
	printf "\nalias class=\"python3 %s/.scripts/new_class.py\"\n" "$HOME" >> "$ZSH_FILE"
	printf "\nalias class=\"python3 %s/.scripts/new_class.py\"\n" "$HOME" >> "$BASH_FILE"
	echo "Alias \"class\" created"
fi

# Delete git repo
rm -rf "$HOME/Scripts"

# Automatically renews the shell session
exec "$SHELL" || exit
