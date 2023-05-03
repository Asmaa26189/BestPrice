using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace bestPrice.Models
{
    public class ProductPrice
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        [Required]
        public double Price { get; set; }
        public DateTime Date { get; set; }
        [Required]
        public String Place { get; set; }
        public byte[] Image { get; set; }
        public String Comments { get; set; }
        [Required]
        public int ProductId { get; set; }
        [Required]
        public int BrandId { get; set; }

        public Product Product { get; set; }
        public Brand Brand { get; set; }

    }
}
