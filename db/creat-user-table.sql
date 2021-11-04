create table "User" (
    "Id" uuid NOT NULL constraint todo_pk primary key,
    "Username" varchar(120) NOT NULL,
    "Password" varchar(120) NOT NULL,
    "Created" date NOT NULL,
);