using Buran.Core.MvcLibrary.AdminPanel.Controllers2;
using Kanola.Data.Models;
using Kanola.Data.Models.Carrier;
using Kanola.Data.Repositories.Carrier;
using Kanola.Data.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using System.Linq.Expressions;
using System;
using System.Linq;
using Buran.Core.MvcLibrary.XmlLang;
using Buran.Core.MvcLibrary.AdminPanel.Controls;
using Buran.Core.MvcLibrary.Resource;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Kanola.Areas.Carrier.Controllers
{
    [Area("Carrier")]
    [Authorize(Roles = "admin")]
    public class LanguageResourceController : List2Controller<LanguageResource, AppData>
    {
        private LanguageResourceRepository RepoItem => Repo as LanguageResourceRepository;
        private readonly UserManager<AppUser> _userManager;
        private readonly CarrierLanguageRepository _repoCarrierLanguage;
        public LanguageResourceController(AppData context, ICacheService cacheProvider, UserManager<AppUser> userManager)
           : base(false, context)
        {
            Repo = new LanguageResourceRepository(_context);
            _userManager = userManager;
            _repoCarrierLanguage = new CarrierLanguageRepository(_context);
        }
        public override IActionResult Index(int? subId = null)
        {

            //return base.Index(subId);
            return RedirectToAction("List");
        }
        public IActionResult List(int? subId = null)
        {

            var carrierLanguage = _repoCarrierLanguage.GetListSelect();

            ViewBag.Title = XmlLangHtmlExtender.L("LanguageResource_ListTitle");
            var button = new EditorPageMenuItem
            {
                ItemType = EditPageMenuItemType.Insert,
                Title = UI.New,
                IconClass = "fas fa-plus",
                Url = Url.Action("Create"),
            };
            PageMenu.Items.Add(button);

            ViewBag.PageMenu = PageMenu;

            return View(carrierLanguage);
        }

        public override IActionResult ListView2(string subId = null)
        {
            Expression<Func<LanguageResource, bool>> filter = null;

            if (!string.IsNullOrEmpty(subId))
            {
                filter = item => item.LangCode == subId;
            }
            var query = Repo.GetList(filter);



            return PartialView(query.ToList());
        }
        public IActionResult Create()
        {
            ViewBag.CreateMode = true;
            BuildCreateMenu();
            ViewBag.Title = XmlLangHtmlExtender.L("LanguageResource_CreateItem");
            ViewBag.PageMenu = PageMenu;

            var languageItems = _repoCarrierLanguage.GetListSelect();


            List<LanguageResource> languageResources = new List<LanguageResource>();
            foreach (var languageItem in languageItems)
            {
                var item = new LanguageResource();
                item.LangName = languageItem.Text;
                item.LangCode = languageItem.Value;
                languageResources.Add(item);
            }

            return View(languageResources);
        }

        [HttpPost]
        public IActionResult Create(int keepEdit, List<LanguageResource> items)
        {
            foreach (var item in items)
            {
                item.Name = items[0].Name;
            }
            if (ModelState.IsValid)
            {
                items = RepoItem.CreateItems(items);
            }
            if (keepEdit == 0) return RedirectToAction("List");

            if (keepEdit == 1) return RedirectToAction("Edit", new { Name = items.FirstOrDefault().Name });

            if (keepEdit == 2) return RedirectToAction("Create", new { Name = items.FirstOrDefault().Name });

            return View(items);
        }

        public IActionResult Edit(string Name)
        {
            ViewBag.EditMode = true;
            BuildEditMenu();
            ViewBag.Title = XmlLangHtmlExtender.L("LanguageResource_EditItem");
            ViewBag.PageMenu = PageMenu;


            var items = RepoItem.GetListName(Name);

            foreach (var item in items)
            {
                var text = _repoCarrierLanguage.GetListSelect().Where(d => d.Value == item.LangCode).FirstOrDefault();
                if (text != null) {
                    item.LangName = text.Text;
                }
                
            }


            return View(items);
        }

        [HttpPost]
        public IActionResult Edit(int keepEdit, List<LanguageResource> items)
        {
            foreach (var item in items)
            {
                item.Name = items[0].Name;
            }
            ViewBag.EditMode = true;
            if (ModelState.IsValid)
            {
                var item = RepoItem.EditItems(items);

            }
            if (keepEdit == 0) return RedirectToAction("List");

            if (keepEdit == 1) return RedirectToAction("Edit", new { Name = items.FirstOrDefault().Name });


            return View(items);
        }


        [HttpPost]
        public IActionResult Delete2(string Name, string LangCode)
        {
            if (ModelState.IsValid)
            {
                var item = RepoItem.GetItemName(Name, LangCode);
                RepoItem.DeleteItem(item);
                return RedirectToAction("List");
            }
            return RedirectToAction("List");
        }

    }
}
