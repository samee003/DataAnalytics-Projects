SELECT name FROM sys.databases;
CREATE DATABASE covid19_db;
USE covid19_db;

/*
Queries used for Tableau Project
*/
-- 1. 
SELECT SUM(new_cases) AS total_cases, SUM(cast(new_deaths as int)) AS total_deaths, SUM(cast(new_deaths as int))/SUM(New_Cases)*100 AS DeathPercentage
FROM covid19_db..CovidDeaths
WHERE continent is not null 
--Group By date
ORDER BY 1,2;


-- 2. 
SELECT location, SUM(cast(new_deaths as int)) AS TotalDeathCount
FROM covid19_db..CovidDeaths
Where continent IS NULL
AND location NOT IN ('World', 'European Union', 'International')
GROUP BY location
ORDER BY TotalDeathCount DESC;


-- 3.
SELECT Location, Population, MAX(total_cases) AS HighestInfectionCount,  Max((total_cases/population))*100 AS PercentPopulationInfected
FROM covid19_db..CovidDeaths
GROUP BY Location, Population
ORDER BY PercentPopulationInfected DESC;


--4.
SELECT Location, Population,date, MAX(total_cases) AS HighestInfectionCount,  Max((total_cases/population))*100 AS PercentPopulationInfected
FROM covid19_db..CovidDeaths
GROUP BY Location, Population, date
ORDER BY PercentPopulationInfected DESC;