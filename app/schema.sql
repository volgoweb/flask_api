drop table if exists tasks;
create table tasks (
    id integer primary key autoincrement,
    title text not null,
    text text
);