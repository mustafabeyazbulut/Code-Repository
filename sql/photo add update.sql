insert TblCeoMessages(CeoMessageID,CeoPhoto)
select 3,CeoPhoto.* from OPENROWSET(BULK 'C:\Image\logo.jpg',SINGLE_BLOB) CeoPhoto

update TblCeoMessages set CeoPhoto=(SELECT  BulkColumn FROM OPENROWSET(BULK  N'C:\7.jpg', SINGLE_BLOB) AS x) where CeoMessageID=3