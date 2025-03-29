import requests
import json
from psycopg2.extras import Json
import psycopg2



# Configuração da conexão com o banco de dados
try:
    conn = psycopg2.connect(
        dbname="arpex",  # Substitua pelo nome do seu banco
        user="postgres",      # Substitua pelo seu usuário
        password="1234",    # Substitua pela sua senha
        host="localhost",        # Ajuste conforme necessário
        port="5432"              # Porta padrão do PostgreSQL
    )
    cursor = conn.cursor()
except psycopg2.Error as e:
    print(f"erro ao conectar: {e}")
    conn.rollback()

# Query de INSERT
insert_query = """
    INSERT INTO ordens_servico (
        cliente_id, os_encerrada_impedir_estorno, servico_online_mac, cliente_email, endereco_id,
        os_prioridade, os_status, os_observacao, endereco_complemento, os_motivo_descricao,
        os_tecnicos_auxiliares, os_servicoprestado, os_data_finalizacao, plano, os_protocolo,
        os_close_edit, servico_online, contrato_status, nas_ip, servico_ip,
        endereco_pontoreferencia, contrato_pop, os_data_cadastro, os_id, os_setor,
        servico_id, os_tecnico_responsavel, plano_id, contrato_endereco_ll, os_data_agendamento,
        servico_online_ipv6_pd, contrato_id, cliente_contato, contrato_status_data, endereco_numero,
        os_setor_id, servico_login, servico_mac, cliente, endereco_bairro,
        endereco_uf, os_motivo_id, plano_download, plano_upload, endereco_logradouro,
        servico_tipo, servico_password, os_djson, os_conteudo, servico_online_ip,
        contrato_status_id, endereco_cidade, os_lancamento_comodato, os_status_txt, contrato_pop_id,
        os_encerrada_impedir_lancamento_avulso, endereco_ll
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s
    )
    """

#  "cliente_id": 1,
#  "data_finalizacao": "2025-03-31",
# "status_encerrada": 1
#  "agendamento_final": "2025-03-31",
url = "https://digitalnetpith.sgp.tsmx.com.br/api/os/list/"

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

for dados in my_json:
    print(f"Inserindo Dados OS: {dados['os_id']}")
    print (dados)
    break
    valores = (
        dados['cliente_id'], dados['os_encerrada_impedir_estorno'], dados['servico_online_mac'],
        dados['cliente_email'], dados['endereco_id'], dados['os_prioridade'], dados['os_status'],
        dados['os_observacao'], dados['endereco_complemento'], dados['os_motivo_descricao'],
        Json(dados['os_tecnicos_auxiliares']), dados['os_servicoprestado'], dados['os_data_finalizacao'],
        dados['plano'], dados['os_protocolo'], dados['os_close_edit'], dados['servico_online'],
        dados['contrato_status'], dados['nas_ip'], dados['servico_ip'], dados['endereco_pontoreferencia'],
        dados['contrato_pop'], dados['os_data_cadastro'], dados['os_id'], dados['os_setor'],
        dados['servico_id'], dados['os_tecnico_responsavel'], dados['plano_id'], dados['contrato_endereco_ll'],
        dados['os_data_agendamento'], dados['servico_online_ipv6_pd'], dados['contrato_id'],
        dados['cliente_contato'], dados['contrato_status_data'], dados['endereco_numero'],
        dados['os_setor_id'], dados['servico_login'], dados['servico_mac'], dados['cliente'],
        dados['endereco_bairro'], dados['endereco_uf'], dados['os_motivo_id'], dados['plano_download'],
        dados['plano_upload'], dados['endereco_logradouro'], dados['servico_tipo'], dados['servico_password'],
        Json(dados['os_djson']), dados['os_conteudo'], dados['servico_online_ip'], dados['contrato_status_id'],
        dados['endereco_cidade'], dados['os_lancamento_comodato'], dados['os_status_txt'],
        dados['contrato_pop_id'], dados['os_encerrada_impedir_lancamento_avulso'], dados['endereco_ll']
    )


    try:
        # Executando o INSERT
        cursor.execute(insert_query, valores)
        conn.commit()
        print("Dados inseridos com sucesso!")
    
    except psycopg2.Error as e:
        print(f"Erro ao inserir ou inserir dados: {e}")
        conn.rollback()
    

    #print ('Id do servico : ',resp['servico_id'],' Protocolo OS : ',resp['os_protocolo'])
    #print ('Cliente : ',resp['cliente_id'],'-',resp['cliente'] ,'Data : ',resp['contrato_status_data'],'Plano : ',resp['plano'])
    #print ('Conteudo da OS : ',resp['os_conteudo'])
    #print ('Tecnico Responsavel : ',resp['os_tecnico_responsavel'])
    #print ('Aqui: ',resp['os_servicoprestado'])
    #print ('--------------------------------------------------------------------')

if cursor:
   cursor.close()
if conn:
   conn.close()
