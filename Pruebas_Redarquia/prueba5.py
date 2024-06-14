texto =texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Praesent ac diam ut justo aliquam iaculis id eu magna. Cras nulla lectus,
tristique non imperdiet eget, aliquam quis sem. Aliquam suscipit, ex eu
elementum efficitur, ante ipsum finibus metus, vitae blandit massa tellus
et diam. Maecenas porta feugiat efficitur. Etiam ut diam quis velit
malesuada vulputate. Quisque in risus gravida, finibus massa vel,
ultrices nisl. Ut placerat semper ligula id aliquam. Donec ac commodo
risus, a tincidunt dui. Phasellus at nisi nulla. Nulla facilisi. Fusce in
tristique est, at convallis leo.
Nulla facilisi. Etiam ac convallis risus. Nulla faucibus rhoncus justo,
eu scelerisque ex luctus sit amet. Duis imperdiet dui quis dui luctus
pretium. Duis volutpat orci ultricies orci posuere ultrices. Donec eget
turpis aliquet, varius enim quis, commodo nibh. Vivamus mi felis, semper
a felis vitae, rhoncus sodales justo. In condimentum, justo quis
venenatis congue, sem purus congue quam, in bibendum elit sem ut nibh.
Nullam lorem sem, porta vitae nunc in, commodo semper magna. Praesent
hendrerit egestas nulla a ultrices. Etiam sed eleifend nibh. Sed varius
rutrum diam at vulputate. Etiam vulputate eu lacus quis varius.
Vestibulum egestas eleifend scelerisque. Aliquam erat volutpat. Aliquam
posuere non erat eget mollis. Suspendisse et eleifend neque. Sed quis
orci eu sem auctor ultrices sit amet sit amet leo. Nunc convallis, est id
vulputate facilisis, felis ex tempor sem, a vestibulum ipsum nulla at
mauris. Phasellus leo felis, interdum id enim sit amet, eleifend cursus
urna.
Praesent urna leo, pretium in tellus in, venenatis volutpat justo.
Maecenas est est, auctor quis dui et, porta volutpat libero. Quisque
tincidunt fermentum lorem, at tempus sem viverra ac. Aliquam odio sapien,
tincidunt ut magna quis, pellentesque dictum mi. Mauris a ligula congue,
fringilla mi at, tincidunt lorem. In eget nibh et diam tempus tincidunt.
Praesent facilisis, ligula in mattis sodales, ipsum massa auctor velit,
sed maximus purus magna sit amet sapien. Cras dapibus neque tempor massa
aliquet, id finibus ligula molestie. Nullam nec erat turpis. Integer a
consequat mi, sed placerat leo.
Maecenas sit amet justo lacus. Praesent vitae libero velit. Orci varius
natoque penatibus et magnis dis parturient montes, nascetur ridiculus
mus. Sed quis felis volutpat, sodales quam in, suscipit sapien. Vivamus
pellentesque eget ligula nec blandit. Fusce rutrum id diam et pulvinar.
Integer lobortis ante id congue aliquam. Integer fermentum feugiat
ultrices. Morbi rhoncus vestibulum semper. Vivamus eu erat dapibus,
ultricies diam nec, accumsan enim. Praesent purus ipsum, viverra et ipsum
sit amet, vulputate laoreet tellus. Phasellus eu nibh fringilla,
convallis leo id, aliquam diam. Nullam elit erat, imperdiet nec arcu
convallis, sodales hendrerit est. Aenean eget consectetur libero."""

texto = texto.replace(',', '').replace('.', '').lower()
texto = texto.split()
 
palabras = []

for word in texto:
    repeated_word = False
    for palabra in palabras:
        if word == palabra['Palabra']:
            repeated_word = True
            palabra['Conteo']+=1

    
    else:
        if repeated_word is False:
            palabras.append({

            'Palabra': word,
            'Conteo': 1
        })

top_ten = []


while len(top_ten) < 10:
    max = None
    for palabra in palabras:
        if max == None:
            if palabra not in top_ten:
                max = palabra
        else:
            if max['Conteo'] < palabra['Conteo'] and palabra not in top_ten:
                max = palabra
    
    top_ten.append(max)

print(top_ten)