CREATE TABLE Recordings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    camera_id INT,
    timestamp DATETIME,
    file_path VARCHAR(255),
    FOREIGN KEY (camera_id) REFERENCES Cameras(id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Cameras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);
