using TsaArsiv.Data.Models;
using TsaArsiv.Data.Repositories.Base;
using TsaArsiv.Data.Services;
using Microsoft.EntityFrameworkCore;
using System.Linq;
using Microsoft.AspNetCore.Mvc.Rendering;
using System.Collections.Generic;
using System.Threading;
using Microsoft.AspNetCore.Hosting;
using System.Xml.Serialization;
using System.IO;
using TsaArsiv.Data.XmlLang.Models;
using System.Xml;
using System.Xml.Linq;
using System.Linq.Expressions;
using System.Reflection;
using System;
using TsaArsiv.Data.XmlLang;
using Buran.Core.Library.Utils;

namespace TsaArsiv.Data.Repositories
{
    public class LanguageResourceRepository : GenericIdRepository<XmlResourceItem>
    {

        private IWebHostEnvironment _hostingEnvironment;
        public LanguageResourceRepository(IWebHostEnvironment hostingEnvironment)
            : base(new AppData())
        {
            _hostingEnvironment = hostingEnvironment;
        }

        public LanguageResourceRepository(DbContext context)
            : base(context)
        {

        }

        public LanguageResourceRepository() : base(new AppData())
        {
        }

        public IQueryable GetListGrid(string lang)
        {
            var list = new List<XmlResourceItem>();
            var dataLanguage = new XmlResource();
            var folder = Path.Combine(Consts.HostingEnvironment.ContentRootPath, @"Languages");
            var files = Directory.GetFiles(folder, "*.xml");
            var language = Path.GetFileNameWithoutExtension(files[0]);
            foreach (var file in files)
            {
                var languagex = Path.GetFileNameWithoutExtension(file);
                if (languagex != lang)
                    continue;
                XDocument xmlFile = XDocument.Load(file);
                var query = from c in xmlFile.Descendants("Item") select c;
                var resources = (from a in query
                                 select new XmlResourceItem
                                 {
                                     Name = a.FirstAttribute.Value.ToString(),
                                     Value = a.Value,
                                     LangCode = languagex,
                                 }).ToList();
                list.AddRange(resources);

            }
            IQueryable<XmlResourceItem> queryx = list.AsQueryable();
            return queryx;
        }

        public override IQueryable<XmlResourceItem> GetList(Expression<Func<XmlResourceItem, bool>> filter = null)
        {

            var list = new List<XmlResourceItem>();
            var dataLanguage = new XmlResource();
            var folder = Path.Combine(Consts.HostingEnvironment.ContentRootPath, @"Languages");
            var files = Directory.GetFiles(folder, "*.xml");
            var language = Path.GetFileNameWithoutExtension(files[0]);
            foreach (var file in files)
            {
                var languagex = Path.GetFileNameWithoutExtension(file);
                XDocument xmlFile = XDocument.Load(file);
                var query = from c in xmlFile.Descendants("Item") select c;
                var resources = (from a in query
                                 select new XmlResourceItem
                                 {
                                     Name = a.FirstAttribute.Value.ToString(),
                                     Value = a.Value,
                                     LangCode= languagex,
                                 }).ToList();
                list.AddRange(resources);

            }
            IQueryable<XmlResourceItem> queryx = list.AsQueryable();
            if (filter != null)
                queryx = queryx.Where(filter);
            return queryx;
        }

        public XmlResourceItem EditLanguageResource(XmlResourceItem item)
        {
            var dataLanguage = new XmlResource();
            var folder = Path.Combine(Consts.HostingEnvironment.ContentRootPath, @"Languages");
            var files = Directory.GetFiles(folder, "*.xml");
            var language = Path.GetFileNameWithoutExtension(files[0]);
            foreach (var file in files)
            {
                var languagex = Path.GetFileNameWithoutExtension(file);
                if (languagex != item.LangCode)
                    continue;
                XDocument xmlFile = XDocument.Load(file);
                var element = xmlFile.Descendants("Item")
                   .Where(arg => arg.Attribute("Name").Value == item.Name)
                   .Single();
                var elementValue = element.Elements("Value");
                elementValue.Single().Value = item.Value;
                //todo
                xmlFile.Save(file);
            }
            XmlLangResource.LoadLanguages(Consts.HostingEnvironment, @"Languages", "tr");
            return item;
        }
        public XmlResourceItem GetEditItem(XmlResourceItem item)
        {
            try
            {
                if (item.LangCode==null)
                {
                    item.LangCode = "tr";
                }
                var returnItem = new XmlResourceItem();
                var dataLanguage = new XmlResource();
                var folder = Path.Combine(Consts.HostingEnvironment.ContentRootPath, @"Languages");
                var files = Directory.GetFiles(folder, "*.xml");
                var language = Path.GetFileNameWithoutExtension(files[0]);
                foreach (var file in files)
                {
                    var languagex = Path.GetFileNameWithoutExtension(file);
                    if (languagex != item.LangCode)
                        continue;
                    XDocument xmlFile = XDocument.Load(file);
                    var element = xmlFile.Descendants("Item")
                       .Where(arg => arg.Attribute("Name").Value == item.Name)
                       .Select(x => new XmlResourceItem
                       {
                           Name = x.Attribute("Name").Value,
                           Value = x.Value,
                       }).FirstOrDefault();
                    returnItem = element;
                }
               
                return returnItem;
            }
            catch (Exception e)
            {
                throw new Exception("HATA"+e.Message);
            }
          
        }
        public XmlResourceItem AddNewItem(XmlResourceItem item)
        {
            var itemVarMi = GetEditItem(item);
            if (itemVarMi!=null)
            {
                if(itemVarMi.Value==null)
                      return item;
                
                
                return item;
            }
            var dataLanguage = new XmlResource();
            var folder = Path.Combine(Consts.HostingEnvironment.ContentRootPath, @"Languages");
            var files = Directory.GetFiles(folder, "*.xml");
            var language = Path.GetFileNameWithoutExtension(files[0]);
          
            foreach (var file in files)
            {
                var languagex = Path.GetFileNameWithoutExtension(file);
                if (languagex != item.LangCode)
                    continue;
                XDocument xmlFile = XDocument.Load(file);
                var characters = xmlFile.Descendants("Items").FirstOrDefault();
                if (characters != null)
                {
                    characters.Add((new XElement("Item",
                    new XAttribute("Name", item.Name),
                    new XElement("Value", item.Value))));
                    xmlFile.Save(file);
                }
            }
            XmlLangResource.LoadLanguages(Consts.HostingEnvironment, @"Languages", "tr");
            return item;
        }
        //public int GetLastID()
        //{
           
        //    try
        //    {
        //        var dataLanguage = new XmlResource();
        //        var folder = Path.Combine(Consts.HostingEnvironment.ContentRootPath, @"Languages");
        //        var files = Directory.GetFiles(folder, "*.xml");
        //        var language = Path.GetFileNameWithoutExtension(files[0]);
        //        XDocument xmlFile = XDocument.Load(files[0]);
        //        int maxNr = xmlFile.Descendants("Item")
        //        .Max(x => (int)x.Attribute("ID"));
        //        return maxNr;
        //    }
        //    catch (Exception e)
        //    {
        //        throw new Exception("HATA"+e.Message);
        //    }
        //}
    }
}