CREATE TABLE [Streamlit].[TOP].[TOPAtaskaitos]
(
	[Vardas] [varchar](100)  NOT NULL,
	[Pavarde] [varchar](100)  NOT NULL,
	[El_Pastas] [varchar](100)  NOT NULL,
	[Pavadinimas] [varchar](255)  NOT NULL,
	[Savininkas] [varchar](100)  NOT NULL,
	[Tema] [varchar](255)  NOT NULL,
	[Kategorija] [varchar](100)  NOT NULL,
	[Papildoma_Kategorija] [varchar](100)  NOT NULL,
	[Skyrius] [varchar](100)  NOT NULL,
	[Kiti_Skyriai] [varchar](255)  NULL,
	[Naudojimo_Daznumas] [varchar](50)  NOT NULL,
	[Naudojama_ESO_BL_Lentoje] [varchar](10)  NOT NULL,
	[Iseina_I_Isore] [varchar](10)  NOT NULL,
	[Komentarai_Pastabos] [varchar](500)  NULL,
	[DateAdded] [datetime2](3)  NOT NULL
)
GO

CREATE TABLE [Streamlit].[TOP].[Dokumentacija]
(
    [Pavadinimas] VARCHAR(255),                -- Report Title (Natural key for joining)
    [Tool_Name] VARCHAR(255),                  -- Tool Name (Natural key for joining)
    [Tool_URL] VARCHAR(255),                   -- Tool URL
    [Workspace_URL] VARCHAR(255),              -- Workspace URL
    [Executor] VARCHAR(255),                   -- Executor
    [Clients] VARCHAR(255),                    -- Clients
    [Tool_Type] VARCHAR(500),                  -- Tool Types (comma-separated if multiple)
    [Purpose] VARCHAR(1000),                   -- Purpose of the report
    [Selected_Processes] VARCHAR(500),         -- Processes (comma-separated if multiple)
    [Topics] VARCHAR(500),                     -- Topics (comma-separated if multiple)
    [Tags] VARCHAR(500),                       -- Tags (comma-separated if provided)
    [Orchestrator] VARCHAR(50),                -- Orchestrator (Yes/No)
    [GitLab_Integration] VARCHAR(50),          -- GitLab Integration (Yes/No)
    [External_Tool] VARCHAR(50),               -- External Tool (Yes/No)
    [Data_Gateway] VARCHAR(50),                -- Data Gateway (Yes/No)
    [RLS] VARCHAR(50),                         -- RLS (Yes/No)
    [Fabric_Elements] VARCHAR(500),            -- Fabric elements (comma-separated if multiple)
    [Comments] VARCHAR(1000),                  -- Comments (free text)
    [DataSource_Type] VARCHAR(255),            -- Data Source Type (for each source row)
    [Details] VARCHAR(500),                    -- Details of the Data Source
    [Code_Fragment] VARCHAR(2000),             -- Code Fragment
    [Code_Comment] VARCHAR(2000),              -- Code Comment
    [DateAdded] DATETIME2(3)                   -- Date the record was added
)
