def Raise (landscape, a, b):
    pos = a - 1 
    while pos != b :
        landscape[pos] = landscape[pos]+1
        pos += 1
    

def Depress (landscape, a, b):
    pos = a - 1 
    while pos != b :
        landscape[pos] = landscape[pos]-1
        pos += 1

def Hill (landscape, a, b):
    a = a-1
    b = b-1
    landscape[a] += 1
    landscape[b] += 1

    contMayorQue = 1
    contadorDeMovimientoX = 1
    contadorDeMovimientoY = 2


    if ( (b-a) % 2 == 0):
        cont_mitad = 1
        midad = (b-a)/2
        
        while ( (b - a) > contMayorQue and cont_mitad != midad):
            
            landscape[a+contadorDeMovimientoX] += contadorDeMovimientoY
            landscape[b-contadorDeMovimientoX] += contadorDeMovimientoY

            contadorDeMovimientoX += 1
            contadorDeMovimientoY += 1
            contMayorQue += 2
            cont_mitad += 1

        landscape[a+contadorDeMovimientoX] += contadorDeMovimientoY
    
    else:
        while (b - a > contMayorQue):

            landscape[a+contadorDeMovimientoX] += contadorDeMovimientoY
            landscape[b-contadorDeMovimientoX] += contadorDeMovimientoY

            contadorDeMovimientoX += 1
            contadorDeMovimientoY += 1
            contMayorQue += 2

def Valley(landscape, a, b):
    a = a-1
    b = b-1
    landscape[a] -= 1
    landscape[b] -= 1

    contMayorQue = 1
    contadorDeMovimientoX = 1
    contadorDeMovimientoY = 2


    if ( (b-a) % 2 == 0):
        cont_mitad = 1
        midad = (b-a)/2
        
        while ( (b - a) > contMayorQue and cont_mitad != midad):
            
            landscape[a+contadorDeMovimientoX] -= contadorDeMovimientoY
            landscape[b-contadorDeMovimientoX] -= contadorDeMovimientoY

            contadorDeMovimientoX += 1
            contadorDeMovimientoY += 1
            contMayorQue += 2
            cont_mitad += 1

        landscape[a+contadorDeMovimientoX] -= contadorDeMovimientoY
    
    else:
        while (b - a > contMayorQue):

            landscape[a+contadorDeMovimientoX] -= contadorDeMovimientoY
            landscape[b-contadorDeMovimientoX] -= contadorDeMovimientoY

            contadorDeMovimientoX += 1
            contadorDeMovimientoY += 1
            contMayorQue += 2

