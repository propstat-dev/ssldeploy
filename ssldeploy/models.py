from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from ssldeploy import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    user_email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    user_fname: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=False)
    user_mname: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=False)
    user_lname: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=False)
    user_displayname: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=False)
    user_security_groups: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)  # Comma-separated list of groups

    def __repr__(self):
        return '<User {}>'.format(self.user_username)

class TargetSystem(db.Model):
    system_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    system_fqdn: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=False)
    system_description: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    system_Type: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=False)
    system_cert_format: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=False)
    system_cert_filename: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    system_cert_path: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    system_key_filename: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    system_last_validated: so.Mapped[sa.TIMESTAMP] = so.mapped_column(sa.TIMESTAMP, index=True, unique=False)


    def __repr__(self):
        return '<Target {}>'.format(self.fqdn)

class Organization(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    primary_domain: so.Mapped[str] = so.mapped_column(sa.String(256), index=True, unique=False)
    ldap_google_enabled: so.Mapped[bool] = so.mapped_column(sa.Boolean, index=False, unique=False)
    ldap_ms_enabled: so.Mapped[bool] = so.mapped_column(sa.Boolean, index=False, unique=False)

    def __repr__(self):
        return '<Organization {}>'.format(self.name)