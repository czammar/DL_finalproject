# Deep Learning Project

Proyecto final el Curso de Deep Learning

**Nota:**

A través del archivo Flickr8k.token.txt se da la relación de id de las imágenes con los textos correspondientes. En total se da cuenta de `40,460`, sin embargo existen 5 registros de comentarios cuya imagen no es provista en la imágenes:

| ID                            | Text                                                  |
|-------------------------------|-------------------------------------------------------|
| 2258277193_586949ec62.jpg.1#0 | people waiting for the subway                         |
| 2258277193_586949ec62.jpg.1#1 | Some people looking out windows in a large building . |
| 2258277193_586949ec62.jpg.1#2 | Three people are waiting on a train platform .        |
| 2258277193_586949ec62.jpg.1#3 | Three people standing at a station .                  |
| 2258277193_586949ec62.jpg.1#4 | two woman and one man standing near train tracks .    |

Se puede emplear el siguiente comando de bash para buscar la imagen dentro de la correspondiente carpeta:

```
ls Flicker8k_Dataset | egrep "2258277193"
