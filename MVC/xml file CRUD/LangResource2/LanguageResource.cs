using Buran.Core.MvcLibrary.Grid;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

namespace Kanola.Data.Models.Carrier
{
    public class LanguageResource 
    {
        [XmlAttribute]
        public string Name { get; set; }

        [NotMapped]
        public string lastName { get; set; }

        public string Value { get; set; }
        public string LangCode { get; set; }

        [NotMapped]
        public string LangName { get; set; }

        public List<DataGridCommand> GridButtonCommands 
        {
            get
            {
                var m = new List<DataGridCommand>();
                if (true)
                {
                    m.Add(new DataGridCommand
                    {
                        Css = "btn btn-sm btn-default",
                        Title = "<span class='fas fa-edit'></span>",
                        //Url = "/Carrier/LanguageResource/edit/?Name="+Name+ "&LangCode="+LangCode,
                        Url = "/Carrier/LanguageResource/edit/?Name=" + Name ,
                    });
                    m.Add(new DataGridCommand
                    {
                        Css = "btn btn-sm btn-default btnDelete",
                        Title = "<span class='fas fa-trash'></span>",
                        Url = "/Carrier/LanguageResource/delete2/?Name=" + Name + "&LangCode=" + LangCode,
                    });
                }
                return m;
            }
        }
    }
}
