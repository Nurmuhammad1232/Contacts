create table contacts
(
    id    serial       not null
        constraint contacts_pk
            primary key,
    name  varchar(100) not null,
    phone varchar(13)  not null
);

alter table contacts
    owner to postgres;

create unique index contacts_phone_uindex
    on contacts (phone);