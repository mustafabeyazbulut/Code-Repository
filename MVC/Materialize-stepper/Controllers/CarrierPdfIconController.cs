using Buran.Core.MvcLibrary.AdminPanel.Controllers2;
using Kanola.Data.Models.Carrier;
using Kanola.Data.Repositories.Carrier;
using Kanola.Data.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Hosting;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using System.IO;
using System;

namespace Kanola.Areas.Carrier.Controllers
{
    [Area("Carrier")]
    [Authorize(Roles = "admin")]
    public class CarrierPdfIconController : Edit2Controller<CarrierPdfIcon, AppData>
    {
        private readonly UserManager<AppUser> _userManager;
        private readonly IWebHostEnvironment _hostingEnvironment;
        private CarrierPdfIconRepository RepoItem => Repo as CarrierPdfIconRepository;
        public CarrierPdfIconController(UserManager<AppUser> userManager, AppData context, IWebHostEnvironment hostingEnvironment) 
            : base(false, context)
        {
            Repo = new CarrierPdfIconRepository(_context);
            _userManager = userManager;
            _hostingEnvironment = hostingEnvironment;
        }
        public override IActionResult Index(int? subId = null)
        {
            return base.Index(subId);
        }
        public override IQueryable OnListDataLoad(int? subId = null)
        {
            return RepoItem.GetListGrid();
        }

        public override Task<CarrierPdfIcon> GetShowItem(int id)
        {
            return RepoItem.GetItemShow(id);
        }
        public override void OnCreateSaveItem(CarrierPdfIcon item)
        {
            try
            {
                var user = _userManager.GetUserAsync(User).Result;
                RepoItem.CurrentUserId = user.Id;

                var searchItem = RepoItem.GetList().Where(d => d.IconName == item.IconName).FirstOrDefault();
                if (searchItem != null)
                {
                    //ModelState.AddModelError("IconName", "There is a record with this icon name");
                    throw new Exception("There is a record with this icon name");

                }
                else
                {
                    if (item.IconImageFile != null && item.IconImageFile.Length > 0)
                    {
                        string uniqueFileName = UploadIconAsync(item.IconImageFile, item.IconName).Result;
                        item.IconFile = uniqueFileName;
                    }
                    base.OnCreateSaveItem(item);
                }
                
            }
            catch (Exception ex)
            {
                throw new Exception(ex.Message);
            }
            

        }
        public override void OnEditSaveItem(CarrierPdfIcon item)
        {
            try
            {
                var user = _userManager.GetUserAsync(User).Result;
                RepoItem.CurrentUserId = user.Id;

                if (item.IconImageFile != null && item.IconImageFile.Length > 0)
                {
                    var deleteIcon = DeleteIconAsync(item.IconFile).Result;

                    string uniqueFileName = UploadIconAsync(item.IconImageFile, item.IconName).Result;
                    item.IconFile = uniqueFileName;
                }


                base.OnEditSaveItem(item);
            }
            catch(Exception ex)
            {
                throw new Exception(ex.Message);
            }
            
        }
        public override Task<IActionResult> Delete(int id, string grid)
        {
            var item = RepoItem.GetItemShow(id).Result;

            var deleteIcon = DeleteIconAsync(item.IconFile).Result;
            return base.Delete(id, grid);
        }
        public Task<string> UploadIconAsync(IFormFile IconImageFile, string uniqueFileName)
        {
            string folderPath = Path.Combine(_hostingEnvironment.WebRootPath, "Store/Carrier/CarrierPdfIcon");
            if (!Directory.Exists(folderPath))
            {
                Directory.CreateDirectory(folderPath);
            }

            string fileExtension = Path.GetExtension(IconImageFile.FileName);
            uniqueFileName = $"{uniqueFileName}{fileExtension}";


            string filePath = Path.Combine(folderPath, uniqueFileName);

            // Dosyayı bu yola kaydedin
            using (var fileStream = new FileStream(filePath, FileMode.Create))
            {
                IconImageFile.CopyTo(fileStream);
            }
            return Task.FromResult(uniqueFileName);
        }

        public Task<string> DeleteIconAsync(string FileName)
        {
            if (FileName == null) return Task.FromResult(FileName);
            string folderPath = Path.Combine(_hostingEnvironment.WebRootPath, "Store/Carrier/CarrierPdfIcon");

            string filePath = Path.Combine(folderPath, FileName);

            if (System.IO.File.Exists(filePath))
            {
                System.IO.File.Delete(filePath);
            }
            return Task.FromResult(FileName);
        }

    }
}
