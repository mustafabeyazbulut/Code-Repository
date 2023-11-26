use master
go
select [name], is_cdc_enabled From sys.databases


-------------------------------
use NANOSTS
go
exec sys.sp_cdc_enable_db
go
----------------------------
use [NANOSTS]
go
select [name] from sys.tables
where is_tracked_by_cdc=1
------------------------------------
use NANOSTS
go
EXEC sys.sp_cdc_enable_table
@source_schema	=N'dbo',
@source_name	=N'Tbl_H_HammaddeGiris'
@role_name		=Null
----------------------------------------
