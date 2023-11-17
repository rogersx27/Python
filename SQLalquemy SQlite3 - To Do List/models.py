from flask_sqlalchemy import SQLAlchemy

# Conexión DB
db = SQLAlchemy()

#Columns rules
class Tasks(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean)

    def __init__(self, content, done):
        super().__init__()
        self.content = content
        self.done = done

    def __str__(self):
        return "\nContent: {}. Done: {}.\n" .format(
            self.content,
            self.done
        )

    def serialize(self):
        return {
            "id": self.rowid,
            "content": self.content,
            "done": self.done
        }