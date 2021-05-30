create database testPy

use testPy

drop table personas_empresas
drop table personas
drop table empresas




create table personas
(
	id_persona			int				not null,
	nombre_persona		varchar(80)		not null,
	dni					int				not null
	primary key(id_persona)
)
go


create table empresas
(
	id_empresa			int				not null,
	nombre_empresa		varchar(80)		not null,
	primary key(id_empresa)	
)
go


create table personas_empresas
(
	id_persona			int				not null,
	id_empresa			int				not null,
	primary key (id_persona,id_empresa),
	foreign key (id_persona) references personas,
	foreign key (id_empresa) references empresas
)
go


insert into personas(id_persona, nombre_persona, dni)
values (1,'Gustavo',11222333) , (2,'Nico', 55666777) , (3,'Enzo',50999888)


insert into empresas(id_empresa, nombre_empresa)
values (1,'Intel') , (2,'Mercado Libre')


insert into personas_empresas(id_persona,id_empresa)
values(1,1),(1,2),(2,2)


select p.nombre_persona, e.nombre_empresa 
from personas p
join personas_empresas pe on pe.id_persona = p.id_persona
join empresas e on pe.id_empresa = e.id_empresa 
where p.id_persona = 1


select * from personas
