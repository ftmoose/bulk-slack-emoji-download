#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

if [ $(find . -name emojis | wc -l) -gt 0 ]; then
	echo -e "${GREEN}Clearing old emojis folder..${NC}"
	rm -rf ./emojis/*
else
	echo -e "${GREEN}Creating emojis folder..${NC}"
	mkdir emojis
fi

echo -e "${GREEN}Looking into your slack workspace..${NC}"
python3 buildData.py
echo -e "${GREEN}Downloading your emojis${NC}"
echo -e "${RED}PRESS CMD-Z or CTRL-Z TO EXIT${NC}"
python3 downloadData.py
echo ""
echo -e "${GREEN}Successfully Completed!${NC}"
 
