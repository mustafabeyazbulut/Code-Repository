USE [master]
GO
CREATE DATABASE [OzdilekServisTakip] ON
( FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL10_50.SQLEXPRESS\MSSQL\DATA\OzdilekBtServisTakip.mdf' ),
( FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL10_50.SQLEXPRESS\MSSQL\DATA\OzdilekBtServisTakip_log.ldf' )
 FOR ATTACH
GO