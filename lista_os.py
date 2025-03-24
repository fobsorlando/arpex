import requests
import json

url = "https://digitalnetpith.sgp.tsmx.com.br/api/os/list/"
#  "pop_id": 1,
#  "contrato_id": 3085,
#  "cliente_id": 1,
#  "data_finalizacao": "2025-03-31",
# "status_encerrada": 1
#  "agendamento_final": "2025-03-31",

payload = json.dumps({
  "app": "MONITORAMENTO",
  "token": "6e848212-f717-446c-b811-d66a664ea0f1",
  "agendamento_inicial": "2025-03-01",
  "agendamento_final": "2025-03-31",
  "status_encerrada": 1
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print (type(json.dumps(response.text)))

my_json = json.loads(response.text)

print (len(my_json))

for resp in my_json:
    print ('Id do servico : ',resp['servico_id'],' Protocolo OS : ',resp['os_protocolo'])
    print ('Cliente : ',resp['cliente_id'],'-',resp['cliente'] ,'Data : ',resp['contrato_status_data'],'Plano : ',resp['plano'])
    print ('Conteudo da OS : ',resp['os_conteudo'])
    print ('Tecnico Responsavel : ',resp['os_tecnico_responsavel'])
    print ('Aqui: ',resp['os_servicoprestado'])
    print ('--------------------------------------------------------------------')
