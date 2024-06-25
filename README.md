Explicación informe de cobertura.
En primer lugar se hizo una prueba de cobertura del codigo con pytest y coverage, los datos arrojados fueron los siguientes:


Name              Stmts   Miss  Cover
-------------------------------------
Pruebas.py           11      0   100%
test_Pruebas.py      29      2    93%
-------------------------------------
TOTAL                40      2    95%


Esto indicaba que habian 2 lineas de codigo no probadas; aun así este reporte se subio al repositorio remoto.
Al revisar el error de esto, se hizo la revisión adecuada y se detecto que habian 2 funciones de testeo que tenian el mismo nombre.
Después de hacer esto se realizaron otra vez las pruebas unitarias, este fue el resultado:


Name              Stmts   Miss  Cover
-------------------------------------
Pruebas.py           11      0   100%
test_Pruebas.py      29      0   100%
-------------------------------------
TOTAL                40      0   100%


Podemos ver como se ha podido probar el 100% del código, esto indica, en gran medida, que el código funciona.
Si los asserts hubieran sido falsos (funciones de operacion que no funcionan), se pudo haber observado esto al notar que los "print" siguientes al accert no pudieron ser probados.
Como se pudo probar el 100%, la logica de nuestro codigo funciona correctamente.
