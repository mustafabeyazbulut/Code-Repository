using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Data.SqlClient;
using System.IO;
using System.Configuration;
using System.Data.OleDb;
using System.Data.Common;
using System.Data.Sql;


namespace GeoLocationFingerprint
{
   public class Excell
    {
        #excell to json
        public static void ExcelToJson()
        {
            string path = @"C:\Users\user\Desktop\GeoLocationFingerprint\GeoLocationFingerprint\GeoLocationFingerprint\bin\Debug\GeoLocationFingerprint.xlsx";
            string conString = string.Empty;
            string extension = Path.GetExtension(path);
            string sheetName = "Sheet1";
            DataTable dt = new DataTable();
            switch (extension)
            {
                case ".xls": //Excel 97-03.
                    conString = ConfigurationManager.ConnectionStrings["Excel03ConString"].ConnectionString;
                    break;
                case ".xlsx": //Excel 07 and above.
                    conString = ConfigurationManager.ConnectionStrings["Excel07ConString"].ConnectionString;
                    break;
            }
            conString = string.Format(conString, path, sheetName);
            using (OleDbConnection con = new OleDbConnection(conString))
            {
                using (OleDbCommand cmd = new OleDbCommand())
                {
                    using (OleDbDataAdapter oda = new OleDbDataAdapter())
                    {
                        cmd.Connection = con;
                        //Get the name of First Sheet.
                        con.Open();
                        DataTable dtExcelSchema;
                        dtExcelSchema = con.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null);
                        sheetName = dtExcelSchema.Rows[0]["TABLE_NAME"].ToString();
                        con.Close();
                        //Read Data from First Sheet.
                        con.Open();
                        cmd.CommandText = "SELECT * From [" + sheetName + "]";
                        oda.SelectCommand = cmd;
                        oda.Fill(dt);
                        con.Close();
                    }
                }
            }
            //Bind Data to GridView.
            //GridView1.DataSource = dt;
            //GridView1.DataBind();
        }
        
    }
}
