using Kanola.Data.Models;
using Kanola.Data.Models.Carrier;
using Kanola.Data.Models.WasteOperations;
using Kanola.Data.Repositories.Base;
using Kanola.Data.ViewModels.Carrier;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Kanola.Data.Repositories.Carrier
{
    public class CarrierLanguageRepository : GenericIdRepository<CarrierLanguage>
    {
        public CarrierLanguageRepository()
           : base(new AppData())
        {

        }
        public CarrierLanguageRepository(DbContext context) : base(context)
        {
        }
        public CarrierLanguage GetDefault2()
        {
            return Conn.CarrierLanguages
                .Where(d => d.IsDefault)
                .FirstOrDefault();
        }
        public async Task<CarrierLanguage> GetItemShow(int id)
        {
            return await Conn.CarrierLanguages
                .Where(d => !d.IsDeleted && d.Id == id)
                .FirstOrDefaultAsync();
        }
        public List<CarrierLanguage> GetList()
        {             return Conn.CarrierLanguages
                               .Where(d => !d.IsDeleted)
                               .Select(d => new CarrierLanguage
                               {
                                      Id = d.Id,
                                      languageCode = d.languageCode,
                                      languageName = d.languageName,
                                      FlagImage = d.FlagImage,
                                      FlagImageFile = d.FlagImageFile,
                               })
                               .AsNoTracking().OrderBy(d => d.languageName).ToList();
        }
        public List<LanguageSelect2> GetSelect2 ()
        {
            return Conn.CarrierLanguages
                               .Where(d => !d.IsDeleted)
                               .Select(d => new LanguageSelect2
                               {
                                   id = d.languageCode,
                                   languageCode = d.languageCode,
                                   languageName = d.languageName,
                                   FlagImage = d.FlagImage,
                               })
                               .AsNoTracking().OrderBy(d => d.languageName).ToList();
        }

        public IQueryable<CarrierLanguage> GetListGrid()
        {
            return Conn.CarrierLanguages
                .Where(d => !d.IsDeleted)
                .AsNoTracking().OrderBy(d => d.languageName);
        }
        public List<SelectListItem> GetListSelect()
        {
            return Conn.CarrierLanguages
                .Where(d => !d.IsDeleted)
                .Select(d => new SelectListItem
                {
                    Text = d.languageName,
                    Value = d.languageCode
                }).ToList();
        }
       
    }
}
