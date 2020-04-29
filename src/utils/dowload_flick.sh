#! bin/bash

# Descargamos los datos al directorio de trabajo
wget https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip
wget https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip

# Descomprime la info
unzip Flickr8k_Dataset.zip
unzip Flickr8k_text.zip