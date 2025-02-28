
# import asyncio
# from playwright.async_api import async_playwright
# from datetime import datetime
# from database.mongo_client import insert_data

# # List of cybersecurity blogs to scrape
# BLOG_SOURCES = [
#     "https://www.cm-alliance.com/cybersecurity-blog",
#     "https://www.ibm.com/blog/category/cybersecurity/",
#     "https://cyberhoot.com/category/blog/",
#     "https://www.sans.org/blog/",
#     "https://www.tarlogic.com/blog/category/cybersecurity/",
#     "https://www.infosecurity-magazine.com/blogs/",
# ]

# async def scrape_blog():
#     """Scrapes blog sources and extracts cyber threat intelligence."""
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         context = await browser.new_context()
#         page = await context.new_page()

#         all_articles = []

#         for source in BLOG_SOURCES:
#             await page.goto(source, timeout=60000)

#             articles = await page.evaluate("""() => {
#                 return [...document.querySelectorAll('article, .post, .blog-post')].map(article => {
#                     return {
#                         title: article.querySelector('h2, h3, .title')?.innerText || '',
#                         url: article.querySelector('a')?.href || '',
#                         description: article.querySelector('p')?.innerText || ''
#                     };
#                 });
#             }""")

#             for article in articles:
#                 if article["title"] and article["url"]:
#                     extracted_data = {
#                         "source": source,
#                         "title": article["title"],
#                         "url": article["url"],
#                         "date": datetime.utcnow().isoformat(),
#                         "description": article["description"],
#                         "classification": "Unknown",  # Placeholder
#                         "attack_method": [],
#                         "attack_vector": [],
#                         "attacker_profile": {},
#                         "ioc": [],
#                         "target_industry": "Unknown",
#                         "tech_stack_targeted": []
#                     }
#                     all_articles.append(extracted_data)

#         await browser.close()

#         if all_articles:
#             insert_data(all_articles)