from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from ssldeploy import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    fname: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=False)
    mname: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=False)
    lname: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=False)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class TargetSystem(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    fqdn: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=False)
    description: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    systemType: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=False)
    cert_format: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=False)
    cert_filename: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    cert_path: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    key_filename: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)

    def __repr__(self):
        return '<Target {}>'.format(self.fqdn)
    