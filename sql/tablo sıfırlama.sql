TRUNCATE TABLE Tbl_Servis

DELETE FROM Tbl_Per_Personel
DBCC CHECKIDENT ('NANOSTS.dbo.Tbl_Per_Personel',RESEED, 999)

