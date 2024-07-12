#!/bin/bash

# Array of URLs
urls=(
  "https://www.example.com"
  "https://www.google.com"
  "https://www.wikipedia.org"
  "https://www.github.com"
  "https://www.reddit.com"
)

# Function to open a random URL in Brave
open_random_url() {
  num_urls=${#urls[@]}
  random_index=$((RANDOM % num_urls))
  random_url=${urls[$random_index]}
  brave-browser "$random_url"
}

# Infinite loop to keep opening random URLs
while true; do
  open_random_url
done
