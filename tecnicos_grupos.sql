CREATE TABLE tecnicos_grupos (
    tecnico_id INTEGER NOT NULL,          -- Referência ao ID do técnico
    grupo_id INTEGER NOT NULL,            -- Referência ao ID do grupo
    data_associacao DATE DEFAULT CURRENT_DATE, -- Data em que a associação foi feita
    PRIMARY KEY (tecnico_id, grupo_id),   -- Chave primária composta
    FOREIGN KEY (tecnico_id) REFERENCES tecnicos_suporte(id) ON DELETE CASCADE,
    FOREIGN KEY (grupo_id) REFERENCES grupos_suporte(id) ON DELETE CASCADE
);

-- Comentários para documentação
COMMENT ON TABLE tecnicos_grupos IS 'Tabela de associação entre técnicos e grupos de suporte';
COMMENT ON COLUMN tecnicos_grupos.tecnico_id IS 'ID do técnico associado';
COMMENT ON COLUMN tecnicos_grupos.grupo_id IS 'ID do grupo associado';
COMMENT ON COLUMN tecnicos_grupos.data_associacao IS 'Data em que o técnico foi associado ao grupo';

-- Inserção de dados de exemplo
INSERT INTO tecnicos_grupos (tecnico_id, grupo_id) VALUES
    (1, 1),  -- João Silva no grupo Rede
    (2, 2),  -- Maria Oliveira no grupo Hardware
    (3, 3),  -- Pedro Santos no grupo Software
    (4, 1),  -- Ana Costa no grupo Rede
    (5, 3);  -- Lucas Almeida no grupo Software