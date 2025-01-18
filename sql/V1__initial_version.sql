-- Photo 테이블 생성
CREATE TABLE photo (
          id INT PRIMARY KEY AUTO_INCREMENT,
          photo_url VARCHAR(255) NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
          updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

-- Memory 테이블 생성
CREATE TABLE memory (
          id INT PRIMARY KEY AUTO_INCREMENT,
          music_title VARCHAR(100) NOT NULL,
          music_link VARCHAR(255) NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
          updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
          friend VARCHAR(50) NOT NULL,
          diary TEXT NOT NULL,
          feeling INT NOT NULL,
          image VARCHAR(255) NOT NULL,
          photo_id INT NOT NULL
);

-- Friend 테이블 생성
CREATE TABLE friend (
          id INT PRIMARY KEY AUTO_INCREMENT,
          name VARCHAR(50) NOT NULL,
          photo VARCHAR(255) NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
          updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL
);

-- Keyword 테이블 생성
CREATE TABLE keyword (
          id INT PRIMARY KEY AUTO_INCREMENT,
          keyword VARCHAR(100) NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Memory-Friend 매핑 테이블 생성
CREATE TABLE memory_friend_mapping (
          id INT PRIMARY KEY AUTO_INCREMENT,
          memory_id INT NOT NULL,
          friend_id INT NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Memory-Keyword 매핑 테이블 생성
CREATE TABLE memory_keyword_mapping (
          id INT PRIMARY KEY AUTO_INCREMENT,
          memory_id INT NOT NULL,
          keyword_id INT NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);