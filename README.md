# prueba_tecnica_Daniel
1. Hacer fork de este repositorio
2. realizar un CRUD en django acorde al modelo usando el orm y formularios(de html no es necesario mirar los formularios de Django)
3. implementar las rutas solicitadas
4. subir los cambios y hacer un PULL REQUEST  de este modelo 
## modelo
### cliente 
    - nombre
    - apellido
### producto
    - tipo
    - codigo
    - nombre
    - precio
### factura (tabla pivote)
    - producto
    - cliente
## rutas
### cliente
   Este modelo solo usara un CRUD 
   - cliente/crear->crear un cliente nuevo
   - cliente/actualizar/{id}->actualizar un cliente especifico
   - cliente/eliminar/{id}->eliminar un cliente especifico
   - cliente/consultar-> consultar todos los clientes
   - cliente/consultar/{id} -> consultar un cliente especifico
### producto
   - producto/crear->crear un producto nuevo
   - producto/actualizar/{id}->actualizar un producto determinado
   - producto/eliminar/{id}->eliminar un producto determinado
   - producto/consultar/{id}->consultar un producto especifico
   - producto/consultar->consultar todos los productos
    
### otras rutas
  - ventas/{cliente_id}-> consultar todos los productos que ha comprado un cliente determinado y el total
    
