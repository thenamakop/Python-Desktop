x="""Lorem ipsum dolor sit amet, consectetur adipisicing elit. Debitis vel soluta
delectus numquam itaque, rerum sunt, harum doloremque? Architecto quae iure vitae
ipsam tenetur pariatur. Repellendus deleniti enim impedit, nobis voluptate sequi
vitae, earum iste! Aperiam voluptatum praesentium aliquid reiciendis, assumenda
libero nobis unde repellat, quibusdam vel earum nam veniam veritatis tempora
pariatur saepe incidunt, animi eum expedita, similique sunt! Libero culpa
sapiente expedita nam nobis nemo necessitatibus accusantium consequuntur nihil
optio. Reprehenderit est, voluptatem sunt, dolores ad molestiae, nemo cum
consequatur, eveniet officia tempore! Temporibus eum, autem facilis odio modi
dolorum itaque unde adipisci, voluptate tenetur aliquid rem quas."""
y = []
string=''
for i in range(len(x)):
    if x[i]== ",":
        y.append(string)
        string=''
    else:
        string += x[i]
print(y)