#!/bin/bash

emojis=("🙂" "😃" "🥳" "🎉" "📁" "📂" "📚" "🌈" "🎨️" "7️⃣" "5️⃣" "4️⃣" "🌟" "🔥" "⚡️" "✨" "🌟" "💡" "🔒" "🔑" "💎" "🌞" "🌙" "🌸" "🍀" "🌊" "⭐️")

numFolders=25

if [ -d "emojis" ]; then
  rm -rf emojis
fi

mkdir emojis

total=${#emojis[@]}
for ((i=0; i<="$total"-1; i++))
do
   folder_name="$i-${emojis[*]:$i}"
   mkdir emojis/"$folder_name"
done