edat=int(input("quina edat tens? "))
if edat > 17:
    print("tens",edat, "per tant, ets MAJOR D'EDAT")
    if edat == 18:
        print("és el teu primer any sent major")
else:
    print("tens",edat, "per tant, NO ETS MAJOR D'EDAT")
