import boto3

#Crea funcion para listar tablas de dynamodb
def listar_tablas():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)

listar_tablas()