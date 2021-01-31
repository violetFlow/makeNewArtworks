# makeNewArtworks
Making derectories batch program for new artworks.\
You can easily making your artworks derectories and initialize files.

## Installation

### Test Environment
  * python 3.8.5
  * Ubuntu 20.04 LTS

### Command 
```bash
  git clone https://github.com/violetFlow/makeNewArtworks.git
```

## Usage
```bash
  python3 excuteBatch.py param1 pram2
```
pram1 is new artworks folder name. \
param2 is category ('Commision', 'Original creation' , 'Second creation')

## route.txt
You can set the file route.\
line1: making new artwork folder root directories.\
line2: default template exel location.\
line3: default pureref file location.\
line4: default clipstudios file location.

example:
```
/mnt/d/Creative/illustration/Work/
/mnt/d/Creative/illustration/Work/template.xlsx
/mnt/d/Creative/illustration/Work/NewScene.pur
/mnt/d/Creative/illustration/Work/NewClip.clip
```
