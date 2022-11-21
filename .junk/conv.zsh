#!/usr/bin/env /usr/bin/zsh


DIRECTORY="/storage/media/test_01"
FILENAME="ffc4802d0f7b478db293d6003aa630da932a06799954de20c753907e5a1dbcfdff1eba3fffefaf13183c966027a35ce8473bb577f840b9272b5822c01afdf564.jpg"

doOneWebp() {
  magick $1 \
    -quality 90 \
    -define webp:near-lossless=90 \
    -define webp:auto-filter=true \
    -define webp:method=6 \
    -define webp:filter-sharpness=7 \
    -define webp:filter-strength=100 \
    -define webp:filter-type=1 \
    -define webp:image-hint=photo \
    "$1.webp"
}

#for FILENAME in $(find $DIRECTORY -name "*.jpg")
#do
#  doOneWebp $FILENAME
#done


#for FILENAME in $(find $DIRECTORY -name "*.png")
#do
#  doOneWebp $FILENAME
#done

# doOne "$DIRECTORY/$FILENAME"
# magick "$DIRECTORY/$FILENAME" -quality 100 "$DIRECTORY/$FILENAME.webp"
