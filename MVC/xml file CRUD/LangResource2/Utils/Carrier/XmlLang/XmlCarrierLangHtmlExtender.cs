using Buran.Core.Library.Utils;
using Buran.Core.MvcLibrary.XmlLang;
using Buran.Core.MvcLibrary.XmlLang.Models;
using Kanola.Data;
using Kanola.Data.Repositories.Carrier;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Xml.Linq;

namespace Kanola.Data.Utils.XmlLang
{
    public class XmlCarrierLangHtmlExtender
    {

        private static string folderPath = Path.Combine(Consts.HostingEnvironment.ContentRootPath, "Areas/Carrier/", @"Languages");

        private static string LanguageCode  = "nl";
        public static string L(string text)
        {
            if (text.IsEmpty())
                return string.Empty;
            return GetResource(text, LanguageCode);
        }
     
        public static string L(string text, string code)
        {
            if (text.IsEmpty())
                return string.Empty;
            return GetResource(text, code);
        }

        private static string GetResource(string text, string code)
        {
            var languagePath = Path.Combine(folderPath, $"{code}.xml");

            if (File.Exists(languagePath))
            {
                var xmlDocument = XDocument.Load(languagePath);

                var existingItem = xmlDocument.Descendants("Item")
                    .FirstOrDefault(e => e.Attribute("Name")?.Value == text);

                if (existingItem != null)
                {
                    return existingItem.Element("Value").Value;
                }
            }
            return text;
        }

        public static void ChangeLanguageCode(string code)
        {
            LanguageCode = code;
        }

        public static string GetLanguageCode()
        {
            return LanguageCode;
        }
    }


}
