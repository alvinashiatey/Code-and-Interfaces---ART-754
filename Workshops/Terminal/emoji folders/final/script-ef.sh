#!/bin/bash
#This script creates a specified number of folders with names from a random string of emojis

emojis=("🙂" "😃" "🥳" "🎉" "📁" "📂" "📚" "🌈" "🎨️" "7️⃣" "5️⃣" "4️⃣" "🌟" "🔥" "⚡️" "✨" "🌟" "💡" "🔒" "🔑" "💎" "🌞" "🌙" "🌸" "🍀" "🌊" "⭐️")

numFolders=20

if [ -d "emojis" ]; then
  rm -rf emojis
fi
mkdir emojis

for ((i=0; i<numFolders; i++)); do
  name=$(printf "%s\n" "${emojis[@]}" | sort --random-sort | tr -d '\n')
  mkdir emojis/"$name"
done

# Uncomment to try this other loop, remember to comment the one above
#for ((i=1; i<=${#emojis[@]}; i++))
#do
#    folder_name="${emojis[*]:0:$i}"
#    mkdir emojis/"$folder_name"
#done

# A reversed version of the above loop
#total=${#emojis[@]}
#for ((i=0; i<="$total"-1; i++))
#do
#    folder_name="$i-${emojis[*]:$i}"
#    mkdir emojis/"$folder_name"
#done


# dont forget to make the script executable
# chmod +x script-ef.sh