import psycopg2
from psycopg2.extras import Json

# Dados estruturados fornecidos
dados = {
    'cliente_id': 7211,
    'os_encerrada_impedir_estorno': True,
    'servico_online_mac': 'E0:B6:68:C5:A1:8D',
    'cliente_email': 'willamessilva544@gmail.com',
    'endereco_id': 27761,
    'os_prioridade': 2,
    'os_status': 1,
    'os_observacao': '',
    'endereco_complemento': 'VILLAGE DEL VILLE , BLOCO 1, APARTAMENTO 304',
    'os_motivo_descricao': 'Financeiro',
    'os_tecnicos_auxiliares': [],
    'os_servicoprestado': 'Paulo e enderson 27/03\ncarnê entregue ',
    'os_data_finalizacao': '2025-03-27T08:46:27',
    'plano': '600 MB',
    'os_protocolo': '250324172600',
    'os_close_edit': False,
    'servico_online': True,
    'contrato_status': ' Ativo ',
    'nas_ip': '172.16.132.12',
    'servico_ip': '100.65.12.234',
    'endereco_pontoreferencia': '',
    'contrato_pop': 'TERESINA-PI',
    'os_data_cadastro': '2025-03-24T17:27:26.367691',
    'os_id': 25273,
    'os_setor': '',
    'servico_id': '10339',
    'os_tecnico_responsavel': 'suporte02',
    'plano_id': 8,
    'contrato_endereco_ll': '',
    'os_data_agendamento': '2025-03-27T17:30:56',
    'servico_online_ipv6_pd': None,
    'contrato_id': 10341,
    'cliente_contato': '(86) 99419-6626',
    'contrato_status_data': '24/03/2025 11:35:35',
    'endereco_numero': 'SN',
    'os_setor_id': '',
    'servico_login': '7211',
    'servico_mac': 'E0:B6:68:C5:A1:8D',
    'cliente': 'MARIA APARECIDA NUNES DA SILVA',
    'endereco_bairro': 'VERDE CAP',
    'endereco_uf': 'PI',
    'os_motivo_id': 5,
    'plano_download': '614400kbps',
    'plano_upload': '307200kbps',
    'endereco_logradouro': 'RUA FLOR DO TEMPO, 8505',
    'servico_tipo': 1,
    'servico_password': '123',
    'os_djson': {},
    'os_conteudo': 'entregar carnê',
    'servico_online_ip': '100.65.12.234',
    'contrato_status_id': '1',
    'endereco_cidade': 'TERESINA',
    'os_lancamento_comodato': False,
    'os_status_txt': 'Encerrada',
    'contrato_pop_id': 1,
    'os_encerrada_impedir_lancamento_avulso': True,
    'endereco_ll': ''
}

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

    # Valores para o INSERT
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

    # Executando o INSERT
    cursor.execute(insert_query, valores)
    conn.commit()
    print("Dados inseridos com sucesso!")

except psycopg2.Error as e:
    print(f"Erro ao conectar ou inserir dados: {e}")
    conn.rollback()

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
