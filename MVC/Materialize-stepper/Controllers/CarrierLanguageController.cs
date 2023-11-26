using Buran.Core.MvcLibrary.AdminPanel.Controllers2;
using Kanola.Data.Models;
using Kanola.Data.Services;
using Kanola.Data.Repositories.Carrier;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Kanola.Data.Models.Carrier;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using System.IO;
using Buran.Core.MvcLibrary.AdminPanel.Controls;
using Buran.Core.MvcLibrary.AdminPanel.Utils;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Hosting.Internal;
using System;
using Buran.Core.MvcLibrary.XmlLang.Models;
using Kanola.Data;
using System.Xml;
using System.Xml.Linq;

namespace Kanola.Areas.Carrier.Controllers
{
    [Area("Carrier")]
    [Authorize(Roles = "admin")]
    public class CarrierLanguageController : Edit2Controller<CarrierLanguage, AppData>
    {
        private readonly UserManager<AppUser> _userManager;
        private ICacheService _cacheProvider;
      
        private readonly IWebHostEnvironment _hostingEnvironment;

        private CarrierLanguageRepository RepoItem => Repo as CarrierLanguageRepository;

        public CarrierLanguageController(AppData context, ICacheService cacheProvider, UserManager<AppUser> userManager, IWebHostEnvironment hostingEnvironment)
            : base(false, context)
        {
            Repo = new CarrierLanguageRepository(_context);
            _cacheProvider = cacheProvider;
            _userManager = userManager;
            _hostingEnvironment = hostingEnvironment;
        }

        public override IQueryable OnListDataLoad(int? subId = null)
        {
            return RepoItem.GetListGrid();
        }
        public override Task<CarrierLanguage> GetShowItem(int id)
        {
            return RepoItem.GetItemShow(id);
        }
        public override void OnCreateSaveItem(CarrierLanguage item)
        {
            
            if (item.FlagImageFile != null && item.FlagImageFile.Length > 0)
            {
                string uniqueFileName = UploadFlagAsync(item.FlagImageFile, item.languageCode).Result;
                item.FlagImage = uniqueFileName;
            }

            string languageFile = CreateXml(item.languageCode).Result;

            var user = _userManager.GetUserAsync(User).Result;
            RepoItem.CurrentUserId = user.Id;
            base.OnCreateSaveItem(item);
        }
        public override void OnEditSaveItem(CarrierLanguage item)
        {
            if (item.FlagImageFile != null && item.FlagImageFile.Length > 0)
            {
                string uniqueFileName = UploadFlagAsync(item.FlagImageFile, item.languageCode).Result;
                item.FlagImage = uniqueFileName;
            }
            var user = _userManager.GetUserAsync(User).Result;
            RepoItem.CurrentUserId = user.Id;
            base.OnEditSaveItem(item);
        }
        public override Task<IActionResult> Delete(int id, string grid)
        {
            var item = RepoItem.GetItemShow(id).Result;

             var deleteFlag=DeleteFlagAsync(item.FlagImage);
             var deleteXml = DeleteXml(item.languageCode);

            
            return base.Delete(id, grid);
        }

        public Task<string> UploadFlagAsync(IFormFile FlagImageFile, string uniqueFileName)
        {
            string folderPath = Path.Combine(_hostingEnvironment.WebRootPath, "Store/Carrier/CarrierLanguage");
            if (!Directory.Exists(folderPath))
            {
                Directory.CreateDirectory(folderPath);
            }

            string fileExtension = Path.GetExtension(FlagImageFile.FileName);
            uniqueFileName = $"{uniqueFileName}{fileExtension}";


            string filePath = Path.Combine(folderPath, uniqueFileName);
          
            // Dosyayı bu yola kaydedin
            using (var fileStream = new FileStream(filePath, FileMode.Create))
            {
                FlagImageFile.CopyTo(fileStream);
            }
            return Task.FromResult(uniqueFileName);
        }
        public Task<string> DeleteFlagAsync(string FileName)
        {
            if (FileName == null) return Task.FromResult(FileName);
            string folderPath = Path.Combine(_hostingEnvironment.WebRootPath, "Store/Carrier/CarrierLanguage");
            
            string filePath = Path.Combine(folderPath, FileName);

            if (System.IO.File.Exists(filePath))
            {
                System.IO.File.Delete(filePath);
            }
            return Task.FromResult(FileName);
        }
        public Task<string> CreateXml(string languageCode)
        {
            string folderPath = Path.Combine(Consts.HostingEnvironment.ContentRootPath, "Areas/Carrier/Languages");
            string xmlFilePath = Path.Combine(folderPath, $"{languageCode}.xml");

            if (!System.IO.File.Exists(xmlFilePath))
            {
                // Eğer belirtilen isimde bir .xml dosyası yoksa, ilk var olan .xml dosyasını kopyala ve adını değiştir.
                string[] existingXmlFiles = Directory.GetFiles(folderPath, "*.xml");
                if (existingXmlFiles.Length > 0)
                {
                    // İlk var olan .xml dosyasını al ve yeni adını ayarla
                    string sourceXmlFilePath = existingXmlFiles[0];
                   System.IO.File.Copy(sourceXmlFilePath, xmlFilePath);

                    // Kopyalanan XML dosyasını yükleyin
                    XDocument copiedXml = XDocument.Load(xmlFilePath);
                    // Tüm <Value> öğelerini seçin ve değerlerini boşaltın
                    foreach (var valueElement in copiedXml.Descendants("Value"))
                    {
                        valueElement.Value = string.Empty; // Değeri boşalt
                    }

                    // Değiştirilmiş XML dosyasını kaydedin
                    copiedXml.Save(xmlFilePath);
                }
                else
                {
                    // Klasörde hiç .xml dosyası yoksa yeni bir dosya oluştur
                    XmlDocument xmlDoc = new XmlDocument();
                    XmlDeclaration xmlDeclaration = xmlDoc.CreateXmlDeclaration("1.0", "utf-8", null);
                    xmlDoc.AppendChild(xmlDeclaration);
                    XmlElement rootElement = xmlDoc.CreateElement("Items");
                    xmlDoc.AppendChild(rootElement);
                    rootElement.InnerXml = "\n";
                    xmlDoc.Save(xmlFilePath);
                }
            }
            return Task.FromResult(xmlFilePath);
        }
        public Task<string> DeleteXml(string LanguageCode)
        {
            string folderPath = Path.Combine(Consts.HostingEnvironment.ContentRootPath, "Areas/Carrier/Languages");
            string xmlFilePath = Path.Combine(folderPath, $"{LanguageCode}.xml");

            if (System.IO.File.Exists(xmlFilePath))
            {
                System.IO.File.Delete(xmlFilePath);
            }
            return Task.FromResult(LanguageCode);
        }

    }
}
