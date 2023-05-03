using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace bestPrice.Models
{
    public class Brand
    {
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }
        [Required,MaxLength(100)]
        public string Name { get; set; }    
               
    }
}
