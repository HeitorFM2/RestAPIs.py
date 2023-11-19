\c Rest-API

CREATE TABLE users (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NULL,
    deleted_at TIMESTAMP NULL
);

CREATE TABLE games (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    available BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NULL,
    deleted_at TIMESTAMP NULL
);

CREATE TABLE bought_game (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    game_id CHAR(36) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NULL,
    deleted_at TIMESTAMP NULL
);

ALTER TABLE bought_game ADD CONSTRAINT fk_bought_game_1
FOREIGN KEY (game_id) 
REFERENCES games (id);

ALTER TABLE bought_game ADD CONSTRAINT fk_Bought_game_2
FOREIGN KEY (user_id) 
REFERENCES users (id);

INSERT INTO users (
    id,
    name,
    mail
) VALUES (
    '7816bda8-6bd0-4d0e-b908-b5432dc8b5e2',
    'Heitor Melegate',
    'heitorfm.dev@gmail.com'
);

INSERT INTO games (
    id,
    name,
    description,
    price
) VALUES (
    'e6cef59d-4d2e-4290-aeb3-4aba1c6099ba',
    'Horizon Zero Dawn',
    'In Horizon Zero Dawn, embark on a riveting action-adventure as Aloy, a skilled hunter in a post-apocalyptic world dominated by robotic creatures. Uncover secrets, master combat, and explore stunning landscapes',
    110
);