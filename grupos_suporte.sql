CREATE TABLE grupos_suporte (
    id SERIAL PRIMARY KEY,                -- ID autoincrementável como chave primária
    nome VARCHAR(50) NOT NULL UNIQUE,    -- Nome do grupo, único e obrigatório
    descricao TEXT,                      -- Descrição opcional do grupo
    data_criacao DATE DEFAULT CURRENT_DATE  -- Data de criação do grupo
);

-- Comentários para documentação
COMMENT ON TABLE grupos_suporte IS 'Tabela para armazenar grupos de suporte';
COMMENT ON COLUMN grupos_suporte.id IS 'Identificador único do grupo';
COMMENT ON COLUMN grupos_suporte.nome IS 'Nome do grupo de suporte';
COMMENT ON COLUMN grupos_suporte.descricao IS 'Descrição do propósito ou função do grupo';
COMMENT ON COLUMN grupos_suporte.data_criacao IS 'Data de criação do grupo';

-- Inserção de dados de exemplo
INSERT INTO grupos_suporte (nome, descricao) VALUES
    ('Rede', 'Suporte para problemas de conectividade e redes'),
    ('Hardware', 'Manutenção e suporte de equipamentos físicos'),
    ('Software', 'Suporte para sistemas e aplicativos');