using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using bestPrice.Models;

namespace bestPrice.ViewModels
{
    public class ProductPriceFormViewModel
    {
        public int Id { get; set; }
        [Required]
        public double Price { get; set; }
        public DateTime Date { get; set; }
        [Required]
        public String Place { get; set; }
        public byte[] Image { get; set; }
        public String Comments { get; set; }
        [Required]
        [Display(Name = "Product")]
        public int ProductId { get; set; }
        [Required]
        [Display(Name = "Brand")]
        public int BrandId { get; set; }

        public IEnumerable<Product>? Products { get; set; }
        public IEnumerable<Brand>? Brands { get; set; }
    }
}
