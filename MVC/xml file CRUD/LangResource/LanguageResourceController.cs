using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using TsaArsiv.Data.Models;
using TsaArsiv.Data.Services;
using Microsoft.AspNetCore.Identity;
using TsaArsiv.Data.Repositories;
using System.Threading.Tasks;
using System;
using Buran.Core.MvcLibrary.Extenders;
using TsaArsiv.Data.Utils;
using Buran.Core.MvcLibrary.Utils;
using Buran.Core.MvcLibrary.AdminPanel.Utils;
using System.IO;
using Buran.Core.Library.LogUtil;
using System.Linq;
using TsaArsiv.Data.XmlLang.Models;
using Buran.Core.MvcLibrary.AdminPanel.Controls;
using Buran.Core.MvcLibrary.Resource;
using TsaArsiv.Data.XmlLang;
using TsaArsiv.Engine.AdminPanel;

namespace TsaArsiv.Areas.Manager.Controllers
{
    [Area("Manager")]
    [Authorize(Roles = "admin")]
    public class LanguageResourceController : List2Controller<XmlResourceItem, AppData>
    {
        private readonly UserManager<AppUser> _userManager;
        private LanguageResourceRepository RepoItem => Repo as LanguageResourceRepository;

        public LanguageResourceController(AppData context, ICacheService cacheProvider, UserManager<AppUser> userManager)
            : base(false, context)
        {
            Repo = new LanguageResourceRepository(_context);
            _userManager = userManager;
        }

        public override IActionResult Index(int? subId = null)
        {
            return base.Index(subId);
        }

        public override IActionResult ListView2(string subId = null)
        {

            return base.ListView2(subId);
        }

        public override IQueryable OnListDataLoad2(string subId = null)
        {
            return RepoItem.GetListGrid(subId);
        }
      
        public override void OnIndex(int? subId = null)
        {
            //PageMenu.Items.Add(new EditorPageMenuItem
            //{
            //    ItemType = EditPageMenuItemType.Insert,
            //    Title = UI.New,
            //    IconClass = "fas fa-plus",
            //    Url = Url.Action("Create"),
            //});
            base.OnIndex(subId);
        }
        #region PROFILE


        public IActionResult LanguageResourcex()
        {
            ViewBag.Title = XmlLangHtmlExtender.L("ProfileTitle");

            var model = new XmlResourceItem();
            try
            {

            }
            catch (Exception ex)
            {
                ModelState.AddModelError(string.Empty, Logger.GetErrorMessage(ex));
            }
            return View(model);
        }

        public IActionResult LanguageResourceEdit(string Name,string LangCode)
        {
            ViewBag.Title = XmlLangHtmlExtender.L("Language_Edit");
            var xml = new XmlResourceItem();
            try
            {
                var Item = new XmlResourceItem()
                {
                    Value = "",
                    Name = Name,
                    LangCode=LangCode,
                };
                var element = RepoItem.GetEditItem(Item);
                xml = element;
                xml.LangCode = LangCode;
            }
            catch (Exception ex)
            {
                ModelState.AddModelError(string.Empty, Logger.GetErrorMessage(ex));
            }
            return View(xml);
        }

        [HttpPost]
        public IActionResult LanguageResourceEdit(XmlResourceItem item)
        {
            ViewBag.Title = XmlLangHtmlExtender.L("Language_Edit");
            try
            {
                var element = RepoItem.GetEditItem(item);
               
                if (element != null)
                {
                    item= RepoItem.EditLanguageResource(item);
                    return RedirectToAction("Index");
                }
                else
                    ModelState.AddModelError(string.Empty, XmlLangHtmlExtender.L("UserNotFound"));
            }
            catch (Exception ex)
            {
                ModelState.AddModelError(string.Empty, Logger.GetErrorMessage(ex));
            }
            return View(item);
        }
        #endregion





    }
}
