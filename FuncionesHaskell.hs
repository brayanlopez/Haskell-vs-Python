sumar::[Int]->Int
sumar [ ] = 0
sumar (x:xs) = x + sumar(xs)

invertir::Ord a=>[a]->[a]
invertir [ ] = [ ]
invertir (x:xs) = (invertir xs)++[x]

igualLista:: Eq a => [a]->[a]->Bool
igualLista l1 l2 = l1 == l2

lista_ordenada::Ord a=>[a]->Bool
lista_ordenada [] = True
lista_ordenada [_] = True
lista_ordenada (x:y:xs) = (x<=y) && lista_ordenada (y:xs)

mostrar_ubicacion::Ord a=>[a]->Int->a
mostrar_ubicacion l n = l!!n

--mayor::[Int]->Int
--mayor (x:xs)
--	x > mayor(xs) = x
--	otherwise = mayor(xs)

mayor::[Int]->Int
mayor[x]=x
mayor(x:xs)
   |x>mayor(xs) = x
   |otherwise = mayor(xs)

contarpares::[Int]->Int
contarpares []=0
contarpares lista= length [x | x <- lista, mod x 2 ==0]

cuadrados::[Int]->[Int]
cuadrados [ ] = [ ]
cuadrados l = [x*x| x <- l]



factorial ::Int -> Int
factorial 0 = 1