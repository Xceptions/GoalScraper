### Goal Crawler

Project uses beautiful soup and requests to crawl **[livescores]**("http://www.livescores.com/soccer/")
to fetch football scores that occurred within the week.
It is scheduled to run weekly with **airflow**

The output file is a multisheet excel workbook, created using pandas