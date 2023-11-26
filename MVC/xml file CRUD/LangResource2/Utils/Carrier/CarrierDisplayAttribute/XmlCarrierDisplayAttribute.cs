using Kanola.Data.Utils.XmlLang;
using System;
using System.ComponentModel;

namespace Kanola.Data.Utils.CarrierDisplayAttribute
{
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field | AttributeTargets.Parameter, AllowMultiple = false)]
    public class XmlCarrierDisplayAttribute : DisplayNameAttribute
    {
        private string resourceKey;

        public XmlCarrierDisplayAttribute(string resourceKey)
        {
            this.resourceKey = resourceKey;
        }

        public override string DisplayName
        {
            get
            {
                // Her seferinde DisplayName değerini hesaplayın
                return XmlCarrierLangHtmlExtender.L(resourceKey);
            }
        }
    }

    //[AttributeUsage(AttributeTargets.Property | AttributeTargets.Field | AttributeTargets.Parameter, AllowMultiple = false)]
    //public class XmlCarrierDisplayAttribute : DisplayNameAttribute
    //{
    //    public XmlCarrierDisplayAttribute(string resourceKey) : base(XmlCarrierLangHtmlExtender.L(resourceKey))
    //    {
    //    }
    //}
}
