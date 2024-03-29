import sqlite3

class PasswordData:
    def __init__(self, data_path) -> None:
        self.db = sqlite3.connect(f"{data_path}/data.db",
            check_same_thread=False)
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS "Archive" (
            "name"	TEXT NOT NULL,
            "password"	TEXT NOT NULL,
            "file_path"	TEXT NOT NULL,
            "timestamp" DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY("file_path") REFERENCES "File"("file_path") ON DELETE CASCADE,
            PRIMARY KEY("name")
        );
        CREATE TABLE IF NOT EXISTS "File" (
            "file_path"	TEXT NOT NULL,
            "size"	INTEGER,
            "mtime"	INTEGER,
            "state"	TEXT NOT NULL DEFAULT "new",
	        PRIMARY KEY("file_path")
        );
        """)

    def add_files(self, files):
        self.db.executescript("""
        DELETE FROM File
        WHERE state IS "new";
        UPDATE File
        SET state = "archived"
        WHERE state IS "update";
        """)

        data = []
        for file in files:
            data.append([
                file["file_path"], 
                file["size"], 
                file["mtime"], 

                file["mtime"],
                file["file_path"], 
            ])

        self.db.executemany("""
        INSERT INTO File (file_path, size, mtime, state)
        VALUES (?, ?, ?, "new")
        ON CONFLICT(file_path) DO UPDATE SET
            state = CASE WHEN ? > (SELECT mtime FROM File WHERE file_path = ?)
            THEN "update" ELSE "archived" END;
        """, data)
        self.db.commit()

    def get_files(self):
        return [{
            "file_path": file_path,
            "size": size,
            "mtime": mtime,
            "state": state,
        } for (file_path, size, mtime, state) in self.db.execute("""
        SELECT file_path, size, mtime, state
        FROM File
        """)]

    def write(self, file, archive):
        def write_Archive():
            self.db.execute("""
            INSERT OR IGNORE INTO Archive (name, password, file_path) VALUES (?, ?, ?)
            """,[archive["name"], archive["password"], file["file_path"]])

        def update_File():
            files_data = (file["size"], file["mtime"], file["file_path"]) 
            self.db.execute("""
            UPDATE File
            SET size = ?,
                mtime = ?,
                state = "archived"
            WHERE file_path IS ?
            """, files_data)

        update_File()
        write_Archive()
        self.db.commit()

    def find(self, file_path):
        archive = [
            {
                "name": name,
                "password": password,
            }
            for (name, password, timestamp) in self.db.execute("""
                SELECT name, password, MAX(timestamp) AS timestamp
                FROM Archive
                WHERE file_path IS ?;
            """, (file_path,))
        ][0]
        return archive
