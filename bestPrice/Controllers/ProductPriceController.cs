using bestPrice.Models;
using bestPrice.ViewModels;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using NToastNotify;

namespace bestPrice.Controllers
{
    public class ProductPriceController : Controller
    {
        private readonly ApplicationDbContext _context;

        public ProductPriceController(ApplicationDbContext context)
        {
            _context = context;
        }
        public async Task<IActionResult> Index()
        {
            // write click and add empty razer view(cshtml) in views 
            var productPrice = await _context.ProductPrices.OrderByDescending(m => m.Price).ToListAsync();
            return View(productPrice);
            //var product = await _context.Products.OrderByDescending(m => m.Name).ToListAsync();
            //return View(product);
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create(ProductPriceFormViewModel model)
        {
            model.Products = await _context.Products.OrderBy(m => m.Name).ToListAsync();
            model.Brands = await _context.Brands.OrderBy(m => m.Name).ToListAsync();
            return View();
            //var errors = ModelState.Values.SelectMany(v => v.Errors);
            //if (!ModelState.IsValid)
            //{
            //    return View("Create", model);
            //}

            //var files = Request.Form.Files;

            //if (!files.Any())
            //{
            //    model.Genres = await _context.Genres.OrderBy(m => m.Name).ToListAsync();
            //    ModelState.AddModelError("Poster", "Please select movie poster!");
            //    return View("Create", model);
            //}

            //var poster = files.FirstOrDefault();
            //if (!_allowedExtenstions.Contains(Path.GetExtension(poster.FileName).ToLower()))
            //{
            //    model.Genres = await _context.Genres.OrderBy(m => m.Name).ToListAsync();
            //    ModelState.AddModelError("Poster", "Only .PNG, .JPG images are allowed!");
            //    return View("Create", model);
            //}
            //if (poster.Length > _maxAllowedPosterSize)
            //{
            //    model.Genres = await _context.Genres.OrderBy(m => m.Name).ToListAsync();
            //    ModelState.AddModelError("Poster", "Poster cannot be more than 1 MB!");
            //    return View("Create", model);
            //}

            //using var dataStream = new MemoryStream();

            //await poster.CopyToAsync(dataStream);

            //var movies = new Movie
            //{
            //    Title = model.Title,
            //    GenreId = model.GenreId,
            //    Year = model.Year,
            //    Rate = model.Rate,
            //    StoryLine = model.StoryLine,
            //    Poster = dataStream.ToArray()
            //};

            //_context.Movies.Add(movies);
            //_context.SaveChanges();

            //_toastNotification.AddSuccessToastMessage("Movie Created Successfully");

            //return RedirectToAction(nameof(Index));
        }
    }
}
