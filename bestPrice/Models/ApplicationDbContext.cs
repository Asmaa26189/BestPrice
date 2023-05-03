using Microsoft.EntityFrameworkCore;

namespace bestPrice.Models
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) :base(options)
        {

        }
        public DbSet<Product> Products { get; set; }
        public DbSet<Brand> Brands { get; set; }
        public DbSet<ProductPrice> ProductPrices { get; set; }


    }
}
