CREATE TABLE tecnicos_suporte (
    id SERIAL PRIMARY KEY,                -- ID autoincrementável como chave primária
    nome VARCHAR(100) NOT NULL,          -- Nome do técnico, obrigatório
    email VARCHAR(100) UNIQUE NOT NULL,  -- E-mail único e obrigatório
    turno VARCHAR(20) NOT NULL,          -- Turno de trabalho (ex.: Manhã, Tarde, Noite)
    data_cadastro DATE DEFAULT CURRENT_DATE  -- Data de cadastro, padrão é a data atual
);

-- Comentários para documentação
COMMENT ON TABLE tecnicos_suporte IS 'Tabela para armazenar dados de técnicos de suporte';
COMMENT ON COLUMN tecnicos_suporte.id IS 'Identificador único do técnico';
COMMENT ON COLUMN tecnicos_suporte.nome IS 'Nome completo do técnico';
COMMENT ON COLUMN tecnicos_suporte.email IS 'E-mail de contato do técnico';
COMMENT ON COLUMN tecnicos_suporte.turno IS 'Turno de trabalho do técnico';
COMMENT ON COLUMN tecnicos_suporte.data_cadastro IS 'Data de cadastro do técnico';

-- Inserção de dados de exemplo (opcional)
INSERT INTO tecnicos_suporte (nome, email, turno) VALUES
    ('João Silva', 'joao@empresa.com', 'Manhã'),
    ('Maria Oliveira', 'maria@empresa.com', 'Tarde'),
    ('Pedro Santos', 'pedro@empresa.com', 'Noite'),
    ('Ana Costa', 'ana@empresa.com', 'Manhã'),
    ('Lucas Almeida', 'lucas@empresa.com', 'Tarde');