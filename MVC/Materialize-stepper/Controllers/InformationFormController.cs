using Buran.Core.Library.LogUtil;
using Buran.Core.MvcLibrary.AdminPanel.Controllers;
using Buran.Core.MvcLibrary.AdminPanel.Controllers2;
using Buran.Core.MvcLibrary.AdminPanel.Controls;
using Buran.Core.MvcLibrary.AdminPanel.Utils;
using Buran.Core.MvcLibrary.XmlLang;
using Kanola.Areas.Carrier.Utils.XmlLang;
using Kanola.Areas.Operations.Utils;
using Kanola.Data.Models;
using Kanola.Data.Models.Carrier;
using Kanola.Data.Models.DocBase;
using Kanola.Data.Repositories;
using Kanola.Data.Repositories.Carrier;
using Kanola.Data.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using System;
using System.Linq;
using System.Security.Cryptography;
using System.Threading.Tasks;

namespace Kanola.Areas.Carrier.Controllers
{
    [Area("Carrier")]
    [AllowAnonymous]
    public class InformationFormController : Edit2Controller<CarrierInformationForm, AppData>
    {
        private CarrierInformationFormRepository RepoItem { get { return Repo as CarrierInformationFormRepository; } }
        private readonly CarrierLanguageRepository _repoCarrierLanguage;
        private readonly AppUserRepository _repoAppUser;
       
        public InformationFormController(AppData context) 
            : base(false,context)
        {
            Repo= new CarrierInformationFormRepository(_context);
            _repoCarrierLanguage = new CarrierLanguageRepository(_context);
            _repoAppUser = new AppUserRepository(_context);
        }

        public override void OnIndex(int? subId = null)
        {
            base.OnIndex(subId);

            var button = PageMenu.Items.First(d => d.ItemType == EditPageMenuItemType.Insert);
            PageMenu.Items.Remove(button);
            ViewBag.Title = "Information Form";
        }

        public override IActionResult ListView(int? subId = null)
        {
            return base.ListView(subId);
        }

        public IActionResult LanguageList()
        {
            var carrierLanguage = _repoCarrierLanguage.GetSelect2();
            return PartialView(carrierLanguage);
        }
        public IActionResult ActivityList()
        {
            return PartialView();
        }
        public IActionResult InformationFormEditor(CarrierActivity activity)
        {
            var model = new CarrierInformationForm();
            model.Activity = activity;

            while(true)
            {
                var uniqueNumber = GenerateUniqueNumber();
                var item = RepoItem.GetByUniqueNumberCheck(uniqueNumber);
                if (item)
                {
                    model.UniqueNumber = uniqueNumber;
                    break;
                }
            }
            return PartialView(model);  
        }
        [HttpPost]
        public async Task<IActionResult> CarrierInformationSave(CarrierInformationForm item)
        {
            var r = new JsonResultViewModel();
            try
            {
                if (string.IsNullOrEmpty(item.UniqueNumber)) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_UniqueNumber")+" is required");
                if (string.IsNullOrEmpty(item.Activity.ToString())) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_Activity") + " is required");
                if (false && string.IsNullOrEmpty(item.ReferanceNumber)) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_ReferanceNumber") + " is required");
                if (string.IsNullOrEmpty(item.HawlageCompanyName)) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_HawlageCompanyName") + " is required");
                if (string.IsNullOrEmpty(item.LicencePlates.ToString())) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_LicencePlates") + " is required");
                if (false && string.IsNullOrEmpty(item.ContainerNo)) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_ContainerNo") + " is required");
                if (string.IsNullOrEmpty(item.DriverName)) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_DriverName") + " is required" );
                if (string.IsNullOrEmpty(item.DriverSurname)) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_DriverSurname") + " is required");
                if (string.IsNullOrEmpty(item.Volume1.ToString())) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_Volume1") + " is required");
                if (false && string.IsNullOrEmpty(item.Volume2.ToString())) 
                    throw new Exception(XmlCarrierLangHtmlExtender.L("CarrierInformationForm_Volume2") + " is required");

                RepoItem.CurrentUserId = 1;
                var model = RepoItem.GetByUniqueNumber(item.UniqueNumber);
                if (model==null)
                {
                    await RepoItem.CreateAsync(item);
                }
                else
                {
                    model= item;
                    await RepoItem.EditAsync(model);
                }
                r.Ok = true;
                //r.Url = Url.Action("ShowCommercial", new { id = model.Id, t = DateTime.Now.Ticks, p = Guid.NewGuid() });
            }
            catch (Exception ex)
            {
                r.Error = Logger.GetErrorMessage(ex);
            }
            return Json(r);
        }
        private string GenerateUniqueNumber()
        {
            DateTime currentDate = DateTime.Now;
            int year = currentDate.Year;
            int month = currentDate.Month;
            int day = currentDate.Day;

            Random random = new Random();
            int randomNumber = random.Next(1000, 9999); // Örnek olarak 1000 ile 9999 arasında rastgele bir sayı
            string uniqueNumber = $"{year}{month:D2}{day:D2}{randomNumber}";
            return uniqueNumber;
        }

        [HttpPost]
        public JsonResult GetWeighbridgeData()
        {
            try
            {
                var cloudWeighClient = new CloudWeighClient();
                var cloudWeightList = cloudWeighClient.GetWeight();

                string[] parts = cloudWeightList.result.Split(' ');
                if (parts.Length > 0)
                {
                    int.TryParse(parts[0], out int kg);
                    return Json(new { success = true, kg });
                }
                return Json(new { success = false, kg = 0 });
            }
            catch
            {
                return Json(new { success = false, kg = 0 });
            }

        }

        [HttpPost]
        public IActionResult ChangeXmlLangCode(string code)
        {
            if (!string.IsNullOrEmpty(code))
            {
                XmlCarrierLangHtmlExtender.ChangeLanguageCode(code);
                Kanola.Data.Utils.XmlLang.XmlCarrierLangHtmlExtender.ChangeLanguageCode(code);
            }
            var deger= XmlCarrierLangHtmlExtender.GetLanguageCode();
            return Json(deger);
        }

    }
}
