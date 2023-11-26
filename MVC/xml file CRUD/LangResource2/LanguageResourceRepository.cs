using Buran.Core.MvcLibrary.XmlLang;
using Buran.Core.MvcLibrary.XmlLang.Models;
using Kanola.Data.Models;
using Kanola.Data.Models.Carrier;
using Kanola.Data.Repositories.Base;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Linq.Expressions;
using System.Text;
using System.Threading.Tasks;
using System.Xml;
using System.Xml.Linq;
using static Azure.Core.HttpHeader;

namespace Kanola.Data.Repositories.Carrier
{
   
    public class LanguageResourceRepository : GenericIdRepository<LanguageResource>
    {
        private IWebHostEnvironment _hostingEnvironment;
        private string folderPath = Path.Combine(Consts.HostingEnvironment.ContentRootPath, "Areas/Carrier/", @"Languages");
        public LanguageResourceRepository(IWebHostEnvironment hostingEnvironment)
            : base(new AppData())
        {
            _hostingEnvironment = hostingEnvironment;
        }
        public LanguageResourceRepository(DbContext context) : base(context)
        {
        }
        public LanguageResourceRepository() : base(new AppData())
        {
        }
        public override IQueryable<LanguageResource> GetList(Expression<Func<LanguageResource, bool>> filter = null)
        {
            var xmlFiles = Directory.GetFiles(folderPath, "*.xml");

            var resources = xmlFiles
                .SelectMany(file =>
                {
                    var languageCode = Path.GetFileNameWithoutExtension(file);

                    var xmlDocument = XDocument.Load(file);

                    return xmlDocument.Descendants("Item")
                        .Select(item => new LanguageResource
                        {
                            Name = item.FirstAttribute.Value.ToString(),
                            Value = item.Value,
                            LangCode = languageCode,
                            LangName= item.FirstAttribute.Value.ToString()
                        });
                })
                .ToList();

            IQueryable<LanguageResource> query = resources.AsQueryable();

            query = filter != null ? query.Where(filter) : query;

            return query;
        }

        public List<LanguageResource> GetListName(string langName)
        {
            var xmlFiles = Directory.GetFiles(folderPath, "*.xml");

            var resources = xmlFiles
                .SelectMany(file =>
                {
                    var languageCode = Path.GetFileNameWithoutExtension(file);

                    var xmlDocument = XDocument.Load(file);

                    return xmlDocument.Descendants("Item")
                        .Select(item => new LanguageResource
                        {
                            Name = item.FirstAttribute.Value.ToString(),
                            Value = item.Value,
                            LangCode = languageCode,
                            lastName = item.FirstAttribute.Value.ToString()
                        });
                })
            .ToList();

            var query = resources.Where(d => d.Name == langName).ToList();

            return query;
        }
        public LanguageResource GetItemName(string name, string langCode)
        {
            var xmlFiles = Directory.GetFiles(folderPath, "*.xml");

            var resources = xmlFiles
                .SelectMany(file =>
                {
                    var languageCode = Path.GetFileNameWithoutExtension(file);

                    var xmlDocument = XDocument.Load(file);

                    return xmlDocument.Descendants("Item")
                        .Select(item => new LanguageResource
                        {
                            Name = item.FirstAttribute.Value.ToString(),
                            Value = item.Value,
                            LangCode = languageCode,
                            lastName = item.FirstAttribute.Value.ToString()
                        });
                })
                .ToList();

            var query = resources.Where(d => d.Name == name && d.LangCode == langCode).FirstOrDefault();

            return query;
        }

       

        public List<LanguageResource> EditItems(List<LanguageResource> items)
        {
            foreach (var item in items)
            {
               EditItem(item);
            }
            return items;
        }

        public LanguageResource EditItem(LanguageResource item)
        {
            var filePath = Path.Combine(folderPath, $"{item.LangCode}.xml");

            if (File.Exists(filePath))
            {
                var xmlDocument = XDocument.Load(filePath);

                var existingItem = xmlDocument.Descendants("Item")
                    .FirstOrDefault(e => e.Attribute("Name")?.Value == item.lastName);

                if (existingItem != null)
                {
                    // Kaynak mevcut, değerini güncelle
                    existingItem.Attribute("Name").Value = item.Name;
                    existingItem.Element("Value").Value = string.IsNullOrEmpty(item.Value) ? " " : item.Value;
                    xmlDocument.Save(filePath);
                } 
               
            }
            return item;
        }
        public void DeleteItem(LanguageResource item)
        {
            var xmlFiles = Directory.GetFiles(folderPath, "*.xml");
            foreach (var filePath in xmlFiles)
            {
                XDocument xmlDoc = XDocument.Load(filePath);

                var existingItem = xmlDoc.Descendants("Item")
                    .FirstOrDefault(e => e.Attribute("Name")?.Value == item.Name);

                if (existingItem != null)
                {
                    existingItem.Remove();
                    xmlDoc.Save(filePath);
                }
            }



        }

        public List<LanguageResource> CreateItems(List<LanguageResource> items)
        {
            foreach (var item in items)
            {
                CreateItem(item);
            }
            return items;
        }
        public void CreateAll(LanguageResource item)
        {
            var xmlFiles = Directory.GetFiles(folderPath, "*.xml");
            foreach (var filePath in xmlFiles)
            {
                // XML dosyasını yükle
                XDocument xmlDoc = XDocument.Load(filePath);

                // Belirtilen Name değerine sahip bir kayıt var mı diye kontrol et
                bool nameExists = xmlDoc.Root.Elements("Item")
                    .Any(element => element.Attribute("Name")?.Value == $"{item.Name}");

                // Eğer aynı Name değerine sahip bir kayıt yoksa, yeni Item öğesini oluştur ve ekleyin
                if (!nameExists)
                {
                    // Yeni Item öğesini oluştur
                    XElement newItem = new XElement("Item");
                    newItem.SetAttributeValue("Name", $"{item.Name}");

                    // Item öğesinin içine Value öğesini ekleyin
                    XElement valueElement = new XElement("Value", item.Value);

                    // Value öğesini Item öğesine ekleyin
                    newItem.Add(valueElement);

                    // Root öğesine yeni Item öğesini ekleyin
                    xmlDoc.Root.Add(newItem);

                    // XML dosyasını kaydet
                    xmlDoc.Save(filePath);
                }
            }
        }
        public LanguageResource CreateItem(LanguageResource item)
        {
            if(string.IsNullOrEmpty(item.Name)) return null;
            var languagePath = Path.Combine(folderPath, $"{item.LangCode}.xml");
            

            if (File.Exists(languagePath))
            {
                // XML dosyasını yükle
                XDocument xmlDoc = XDocument.Load(languagePath);

                // Yeni Item öğesini oluştur
                XElement newItem = new XElement("Item");
                newItem.SetAttributeValue("Name", $"{item.Name}");

                // Item öğesinin içine Value öğesini ekleyin
                XElement valueElement = new XElement("Value", item.Value);

                // Value öğesini Item öğesine ekle
                newItem.Add(valueElement);

                // Root öğesine yeni Item öğesini ekleyin
                xmlDoc.Root.Add(newItem);

                // XML dosyasını kaydet
                xmlDoc.Save(languagePath);
            }
            

            return item;
        }
    }
}
