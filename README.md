# flask_db_prj
Flask DB api 

Set up Database
```
login as postgres user:
sudo -u postgres psql

create database testdb;
create user dbuser1 with encrypted password 'rbu123';
grant all privileges on database testdb to dbuser1;


psql -h localhost -d testdb -U dbuser1 -W
testdb=> \dt; --> describe table

Get the schema from existing table: 
pg_dump -h localhost -t 'public.students' --schema-only testdb

Create table:

CREATE TABLE public.students (id integer NOT NULL,name character varying(200) NOT NULL,division character varying,status character varying(100),created_at timestamp without time zone,updated_at timestamp without time zone);

ALTER TABLE public.students OWNER TO dbuser1;

CREATE SEQUENCE public.students_id_seq AS integer START WITH 1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1;

ALTER TABLE public.students_id_seq OWNER TO dbuser1;

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);

ALTER TABLE ONLY public.students ADD CONSTRAINT students_name_key UNIQUE (name);

ALTER TABLE ONLY public.students ADD CONSTRAINT students_pkey PRIMARY KEY (id);


Describe table:

testdb=> \d students;
                                        Table "public.students"
   Column   |            Type             | Collation | Nullable |               Default
------------+-----------------------------+-----------+----------+--------------------------------------
 id         | integer                     |           | not null | nextval('students_id_seq'::regclass)
 name       | character varying(200)      |           | not null |
 division   | character varying           |           |          |
 status     | character varying(100)      |           |          |
 created_at | timestamp without time zone |           |          |
 updated_at | timestamp without time zone |           |          |
Indexes:
    "students_pkey" PRIMARY KEY, btree (id)
    "students_name_key" UNIQUE CONSTRAINT, btree (name)

```
