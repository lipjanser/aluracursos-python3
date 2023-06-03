import json
import teste

def lambda_handler(event, context):
    # TODO implement
    print (event)
    teste.executar_testes(event)
    return event
