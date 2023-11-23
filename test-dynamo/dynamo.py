import boto3

#Crea funcion para listar tablas de dynamodb
def listar_tablas():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)


#Crear una funcion para crear una tabla de dynamodb con capacidad bajo demanda
def crear_tabla_dynamodb(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=nombre_tabla,
        KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH' #Partition key
                }
            ],
        AttributeDefinitions=[
                {
                    'AttributeName':'id',
                    'AttributeType':'S'
                }
            ],
            BillingMode='PAY_PER_REQUEST'
            )
    print('Tabla creada exitosamente')

#insert item in dynamodb table
def insert_item_dynamodb(nombre_tabla, id, nombre, apellido):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    table.put_item(
        Item={
            'id': id,
            'nombre': nombre,
            'apellido': apellido
        }
        )
    print("Se insertó el elemento correctamente")
    
#leer los elementos de una tabla de dynamodb
def leer_elementos_dynamodb(nombre_tabla):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    response = table.scan()
    items = response['Items']
    for item in items:
        print(item)


opcion = 1;

while opcion != 0:
    print("Ingrese la opción que desea")
    print("1. Listar tablas de dynamodb de la cuenta")
    print("2. Crear tabla de dynamodb")
    print("3. Insertar Datos a la tabla")
    print("4. Leer elementos de la tabla")
    print("0. Salir")
    opcion = int(input())
    if opcion == 1:
        listar_tablas()
    elif opcion == 2:
        nombre_tabla = input("Ingrese el nombre de la tabla : ")
        crear_tabla_dynamodb(nombre_tabla)
    elif opcion == 3:
        insert_item_dynamodb('tbl_samuel','1','samuel','jimenez')
    elif opcion == 4: 
        leer_elementos_dynamodb("tbl_samuel")
        



