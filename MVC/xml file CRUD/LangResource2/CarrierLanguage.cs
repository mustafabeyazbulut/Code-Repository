using Kanola.Data.Models.Base;
using System;
using System.ComponentModel.DataAnnotations;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.AspNetCore.Http;
using Kanola.Data.Models.ContractModels;

namespace Kanola.Data.Models.Carrier
{
    public class CarrierLanguage : BaseCreateEntity
    {

        [Display(Name = "CarrierLanguage_languageCode")]
        [StringLength(4, ErrorMessage = "StringLength")]
        public string languageCode { get; set; } 

        [Display(Name = "CarrierLanguage_languageName")]
        public string languageName { get; set; } 

        [Display(Name = "CarrierLanguage_FlagImage")]
        public string FlagImage { get; set; }

        [NotMapped] 
        public IFormFile FlagImageFile { get; set; }

        [Display(Name = "CarrierLanguage_IsDefault")]
        public bool IsDefault { get; set; } = false;

        [Display(Name = "CarrierLanguage_IsDeleted")]
        public bool IsDeleted { get; set; } = false;

    }
}
