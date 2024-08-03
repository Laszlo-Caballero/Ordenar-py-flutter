import os, sys, shutil

def Ordenar():
    if len(sys.argv) != 2:
        print("No hay carpeta")
        return 
    
    carpeta = os.listdir(sys.argv[1])

    

    extensiones = ["pdf", "rar", "jpg", "exe", "png", "zip", "jpeg", "py", "html", "key", "ini", "key", "xls", "txt", "reg"]
    archivos_por_extension = {ext: [] for ext in extensiones}
    archivos_por_extension["other"] = []

    for ext in extensiones:
        try:
            os.mkdir(f"{sys.argv[1]}/{ext}")
        except:
            pass
        
    try:
        os.mkdir(f"{sys.argv[1]}/other")
    except:
        pass

    for nombre in carpeta:
        carpetaext = nombre.split(".")[-1]
        if carpetaext in archivos_por_extension and "." in nombre :  
            archivos_por_extension[carpetaext].append(nombre)
        else:
            archivos_por_extension["other"].append(nombre)

    for ext, arc in archivos_por_extension.items():
            for archivo in arc:
                try:
                    if not archivo in extensiones:
                        origen = f"{sys.argv[1]}/{archivo}"
                        destino = f"{sys.argv[1]}/{ext}/{archivo}"
                        shutil.move(origen, destino)
                        print(f"{origen=}, {destino=}")
                except:
                    print("no se pudo mover") 


