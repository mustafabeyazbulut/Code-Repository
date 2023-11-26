using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Xml.Serialization;

namespace TsaArsiv.Data.XmlLang.Models
{
    public class XmlResource
    {
      
        public List<XmlResourceItem> Items { get; set; }

        public XmlResource()
        {
            Items = new List<XmlResourceItem>();
        }
    }

    public class XmlResourceItem
    {
        [XmlAttribute]
        public string Name { get; set; }

        public string Value { get; set; }
        public string LangCode { get; set; }
    }
}