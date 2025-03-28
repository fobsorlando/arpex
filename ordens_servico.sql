CREATE TABLE ordens_servico (
    cliente_id INTEGER NOT NULL,
    os_encerrada_impedir_estorno BOOLEAN DEFAULT FALSE,
    servico_online_mac VARCHAR(17),
    cliente_email VARCHAR(255),
    endereco_id INTEGER NOT NULL,
    os_prioridade INTEGER,
    os_status INTEGER,
    os_observacao TEXT,
    endereco_complemento VARCHAR(255),
    os_motivo_descricao VARCHAR(100),
    os_tecnicos_auxiliares JSONB DEFAULT '[]'::jsonb,
    os_servicoprestado TEXT,
    os_data_finalizacao TIMESTAMP,
    plano VARCHAR(50),
    os_protocolo VARCHAR(20),
    os_close_edit BOOLEAN DEFAULT FALSE,
    servico_online BOOLEAN DEFAULT FALSE,
    contrato_status VARCHAR(50),
    nas_ip INET,
    servico_ip INET,
    endereco_pontoreferencia TEXT,
    contrato_pop VARCHAR(100),
    os_data_cadastro TIMESTAMP,
    os_id INTEGER PRIMARY KEY,
    os_setor VARCHAR(100),
    servico_id VARCHAR(20),
    os_tecnico_responsavel VARCHAR(100),
    plano_id INTEGER,
    contrato_endereco_ll TEXT,
    os_data_agendamento TIMESTAMP,
    servico_online_ipv6_pd VARCHAR(50),
    contrato_id INTEGER,
    cliente_contato VARCHAR(20),
    contrato_status_data VARCHAR(20),
    endereco_numero VARCHAR(10),
    os_setor_id VARCHAR(20),
    servico_login VARCHAR(20),
    servico_mac VARCHAR(17),
    cliente VARCHAR(255),
    endereco_bairro VARCHAR(100),
    endereco_uf CHAR(2),
    os_motivo_id INTEGER,
    plano_download VARCHAR(20),
    plano_upload VARCHAR(20),
    endereco_logradouro VARCHAR(255),
    servico_tipo INTEGER,
    servico_password VARCHAR(50),
    os_djson JSONB DEFAULT '{}'::jsonb,
    os_conteudo TEXT,
    servico_online_ip INET,
    contrato_status_id VARCHAR(10),
    endereco_cidade VARCHAR(100),
    os_lancamento_comodato BOOLEAN DEFAULT FALSE,
    os_status_txt VARCHAR(50),
    contrato_pop_id INTEGER,
    os_encerrada_impedir_lancamento_avulso BOOLEAN DEFAULT FALSE,
    endereco_ll TEXT
);

-- Adicionando alguns índices úteis
CREATE INDEX idx_os_protocolo ON ordens_servico (os_protocolo);
CREATE INDEX idx_cliente_id ON ordens_servico (cliente_id);
CREATE INDEX idx_os_data_cadastro ON ordens_servico (os_data_cadastro);
