-- Server-Version: 5.7.32-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `pybroker`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `tradable_values`
--

CREATE TABLE `tradable_values` (
  `symbol` varchar(150) CHARACTER SET latin1 NOT NULL,
  `name` varchar(200) CHARACTER SET latin1 NOT NULL,
  `logo_url` varchar(500) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Daten für Tabelle `tradable_values`
--

INSERT INTO `tradable_values` (`symbol`, `name`, `logo_url`) VALUES
('A', 'Agilent Technologies, Inc.', 'https://logo.clearbit.com/agilent.com'),
('AAL', 'American Airlines Group, Inc.', 'https://logo.clearbit.com/aa.com'),
('AAP', 'Advance Auto Parts Inc Advance ', 'https://logo.clearbit.com/advanceautoparts.com'),
('AAPL', 'Apple Inc.', 'https://logo.clearbit.com/apple.com'),
('ABBV', 'AbbVie Inc.', 'https://logo.clearbit.com/abbvie.com'),
('ABC', 'AmerisourceBergen Corporation', 'https://logo.clearbit.com/amerisourcebergen.com'),
('ABMD', 'ABIOMED, Inc.', 'https://logo.clearbit.com/abiomed.com'),
('ABT', 'Abbott Laboratories', 'https://logo.clearbit.com/abbott.com'),
('ACN', 'Accenture plc', 'https://logo.clearbit.com/accenture.com'),
('ADBE', 'Adobe Inc.', 'https://logo.clearbit.com/adobe.com'),
('ADI', 'Analog Devices, Inc.', 'https://logo.clearbit.com/analog.com'),
('ADM', 'Archer-Daniels-Midland Company', 'https://logo.clearbit.com/adm.com'),
('ADP', 'Automatic Data Processing, Inc.', 'https://logo.clearbit.com/adp.com'),
('ADSK', 'Autodesk, Inc.', 'https://logo.clearbit.com/autodesk.com'),
('AEE', 'Ameren Corporation', 'https://logo.clearbit.com/ameren.com'),
('AEP', 'American Electric Power Company', 'https://logo.clearbit.com/aep.com'),
('AES', 'The AES Corporation', 'https://logo.clearbit.com/aes.com'),
('AFL', 'AFLAC Incorporated', 'https://logo.clearbit.com/aflac.com'),
('AIG', 'American International Group, I', 'https://logo.clearbit.com/aig.com'),
('AIV', 'Apartment Investment and Manage', 'https://logo.clearbit.com/aimco.com'),
('AIZ', 'Assurant, Inc.', 'https://logo.clearbit.com/assurant.com'),
('AJG', 'Arthur J. Gallagher & Co.', 'https://logo.clearbit.com/ajg.com'),
('AKAM', 'Akamai Technologies, Inc.', 'https://logo.clearbit.com/akamai.com'),
('ALB', 'Albemarle Corporation', 'https://logo.clearbit.com/albemarle.com'),
('ALGN', 'Align Technology, Inc.', 'https://logo.clearbit.com/aligntech.com'),
('ALK', 'Alaska Air Group, Inc.', 'https://logo.clearbit.com/alaskaair.com'),
('ALL', 'Allstate Corporation (The)', 'https://logo.clearbit.com/allstate.com'),
('ALLE', 'Allegion plc', 'https://logo.clearbit.com/allegion.com'),
('ALXN', 'Alexion Pharmaceuticals, Inc.', 'https://logo.clearbit.com/alexion.com'),
('AMAT', 'Applied Materials, Inc.', 'https://logo.clearbit.com/appliedmaterials.com'),
('AMCR', 'Amcor plc', 'https://logo.clearbit.com/amcor.com'),
('AMD', 'Advanced Micro Devices, Inc.', 'https://logo.clearbit.com/amd.com'),
('AME', 'AMETEK, Inc.', 'https://logo.clearbit.com/ametek.com'),
('AMGN', 'Amgen Inc.', 'https://logo.clearbit.com/amgen.com'),
('AMP', 'Ameriprise Financial, Inc.', 'https://logo.clearbit.com/ameriprise.com'),
('AMT', 'American Tower Corporation (REI', 'https://logo.clearbit.com/americantower.com'),
('AMZN', 'Amazon.com, Inc.', 'https://logo.clearbit.com/amazon.com'),
('ANET', 'Arista Networks, Inc.', 'https://logo.clearbit.com/arista.com'),
('ANSS', 'ANSYS, Inc.', 'https://logo.clearbit.com/ansys.com'),
('ANTM', 'Anthem, Inc.', 'https://logo.clearbit.com/antheminc.com'),
('AON', 'Aon plc', 'https://logo.clearbit.com/aon.com'),
('AOS', 'A.O. Smith Corporation', 'https://logo.clearbit.com/aosmith.com'),
('APA', 'Apache Corporation', 'https://logo.clearbit.com/apachecorp.com'),
('APD', 'Air Products & Chemicals Inc', ''),
('APH', 'Amphenol Corporation', 'https://logo.clearbit.com/amphenol.com'),
('APTV', 'Aptiv PLC', 'https://logo.clearbit.com/aptiv.com'),
('ARE', 'Alexandria Real Estate Equities', 'https://logo.clearbit.com/are.com'),
('ATO', 'Atmos Energy Corporation', 'https://logo.clearbit.com/atmosenergy.com'),
('ATVI', 'Activision Blizzard, Inc', 'https://logo.clearbit.com/activisionblizzard.com'),
('AVB', 'AvalonBay Communities, Inc.', 'https://logo.clearbit.com/avalonbay.com'),
('AVGO', 'Broadcom Inc.', 'https://logo.clearbit.com/broadcom.com'),
('AVY', 'Avery Dennison Corporation', 'https://logo.clearbit.com/averydennison.com'),
('AWK', 'American Water Works Company Inc', ''),
('AXP', 'American Express Company', 'https://logo.clearbit.com/americanexpress.com'),
('AZO', 'AutoZone, Inc.', 'https://logo.clearbit.com/autozone.com'),
('BA', 'Boeing Company (The)', 'https://logo.clearbit.com/boeing.com'),
('BAC', 'Bank of America Corporation', 'https://logo.clearbit.com/bankofamerica.com'),
('BAX', 'Baxter International Inc.', 'https://logo.clearbit.com/baxter.com'),
('BBY', 'Best Buy Co., Inc.', 'https://logo.clearbit.com/investors.bestbuy.com'),
('BDX', 'Becton, Dickinson and Company', 'https://logo.clearbit.com/bd.com'),
('BEN', 'Franklin Resources, Inc.', 'https://logo.clearbit.com/franklinresources.com'),
('BF-B', 'Brown Forman Inc', 'https://logo.clearbit.com/brown-forman.com'),
('BIIB', 'Biogen Inc.', 'https://logo.clearbit.com/biogen.com'),
('BIO', 'Bio-Rad Laboratories, Inc.', 'https://logo.clearbit.com/bio-rad.com'),
('BK', 'The Bank of New York Mellon', ''),
('BKNG', 'Booking Holdings Inc', ''),
('BKR', 'Baker Hughes Co', ''),
('BLK', 'BlackRock, Inc.', 'https://logo.clearbit.com/blackrock.com'),
('BLL', 'Ball Corporation', 'https://logo.clearbit.com/ball.com'),
('BMY', 'Bristol-Myers Squibb Company', 'https://logo.clearbit.com/bms.com'),
('BR', 'Broadridge Financial Solutions', ''),
('BRK-A', 'Berkshire Hathaway Inc.', 'https://logo.clearbit.com/berkshirehathaway.com'),
('BRK-B', 'Berkshire Hathaway Inc. New', 'https://logo.clearbit.com/berkshirehathaway.com'),
('BSX', 'Boston Scientific', ''),
('BWA', 'BorgWarner Inc.', 'https://logo.clearbit.com/borgwarner.com'),
('BXP', 'Boston Properties', ''),
('C', 'Citigroup Inc.', ''),
('CAG', 'Conagra Brands', ''),
('CAH', 'Cardinal Health, Inc.', 'https://logo.clearbit.com/cardinalhealth.com'),
('CARR', 'Carrier Global Corporation', 'https://logo.clearbit.com/corporate.carrier.com'),
('CAT', 'Caterpillar, Inc.', 'https://logo.clearbit.com/caterpillar.com'),
('CB', 'Chubb Limited', 'https://logo.clearbit.com/chubb.com'),
('CBOE', 'Cboe Global Markets', ''),
('CBRE', 'CBRE Group Inc', 'https://logo.clearbit.com/cbre.com'),
('CCI', 'Crown Castle International Corp.', ''),
('CCL', 'Carnival Corporation', 'https://logo.clearbit.com/carnivalcorp.com'),
('CDNS', 'Cadence Design Systems', ''),
('CDW', 'CDW', ''),
('CE', 'Celanese', ''),
('CERN', 'Cerner Corporation', 'https://logo.clearbit.com/cerner.com'),
('CF', 'CF Industries Holdings Inc', ''),
('CFG', 'Citizens Financial Group, Inc.', 'https://logo.clearbit.com/citizensbank.com'),
('CHD', 'Church & Dwight Company, Inc.', 'https://logo.clearbit.com/churchdwight.com'),
('CHRW', 'C. H. Robinson Worldwide', ''),
('CHTR', 'Charter Communications', ''),
('CI', 'CIGNA Corp.', ''),
('CINF', 'Cincinnati Financial Corporatio', 'https://logo.clearbit.com/cinfin.com'),
('CL', 'Colgate-Palmolive Company', 'https://logo.clearbit.com/colgatepalmolive.com'),
('CLX', 'The Clorox Company', ''),
('CMA', 'Comerica Incorporated', 'https://logo.clearbit.com/comerica.com'),
('CMCSA', 'Comcast Corp.', ''),
('CME', 'CME Group Inc.', ''),
('CMG', 'Chipotle Mexican Grill, Inc.', 'https://logo.clearbit.com/chipotle.com'),
('CMI', 'Cummins Inc.', 'https://logo.clearbit.com/cumminseurope.com'),
('CMS', 'CMS Energy', ''),
('CNC', 'Centene Corporation', 'https://logo.clearbit.com/centene.com'),
('CNP', 'CenterPoint Energy, Inc (Holdin', 'https://logo.clearbit.com/centerpointenergy.com'),
('COF', 'Capital One Financial', ''),
('COG', 'Cabot Oil & Gas Corporation', 'https://logo.clearbit.com/cabotog.com'),
('COO', 'The Cooper Companies', ''),
('COP', 'ConocoPhillips', 'https://logo.clearbit.com/conocophillips.com'),
('COST', 'Costco Wholesale Corporation', 'https://logo.clearbit.com/costco.com'),
('COTY', 'Coty Inc.', 'https://logo.clearbit.com/coty.com'),
('CPB', 'Campbell Soup', ''),
('CPRT', 'Copart Inc', ''),
('CRM', 'Salesforce.com Inc', 'https://logo.clearbit.com/salesforce.com'),
('CSCO', 'Cisco Systems, Inc.', 'https://logo.clearbit.com/cisco.com'),
('CSX', 'CSX Corporation', 'https://logo.clearbit.com/csx.com'),
('CTAS', 'Cintas Corporation', ''),
('CTL', 'CenturyLink Inc', ''),
('CTSH', 'Cognizant Technology Solutions', ''),
('CTVA', 'Corteva', ''),
('CTXS', 'Citrix Systems', ''),
('CVS', 'CVS Health', ''),
('CVX', 'Chevron Corp.', ''),
('CXO', 'Concho Resources Inc.', 'https://logo.clearbit.com/concho.com'),
('D', 'Dominion Energy, Inc.', 'https://logo.clearbit.com/dominionenergy.com'),
('DAL', 'Delta Air Lines Inc.', ''),
('DD', 'DuPont de Nemours Inc', ''),
('DDAIF', 'DAIMLER AG', 'https://logo.clearbit.com/daimler.com'),
('DE', 'Deere & Company', 'https://logo.clearbit.com/deere.com'),
('DFS', 'Discover Financial Services', 'https://logo.clearbit.com/discover.com'),
('DG', 'Dollar General', ''),
('DGX', 'Quest Diagnostics', ''),
('DHI', 'D.R. Horton, Inc.', 'https://logo.clearbit.com/drhorton.com'),
('DHR', 'Danaher Corp.', ''),
('DIS', 'Walt Disney Company (The)', 'https://logo.clearbit.com/thewaltdisneycompany.com'),
('DISCA', 'Discovery Inc. (Class A)', ''),
('DISCK', 'Discovery Inc. (Class C)', ''),
('DISH', 'DISH Network Corporation', 'https://logo.clearbit.com/dish.com'),
('DLR', 'Digital Realty Trust Inc', ''),
('DLTR', 'Dollar Tree, Inc.', 'https://logo.clearbit.com/dollartree.com'),
('DOV', 'Dover Corporation', ''),
('DOW', 'Dow Inc.', ''),
('DPZ', 'Domino\'s Pizza Inc', 'https://logo.clearbit.com/dominos.com'),
('DRE', 'Duke Realty Corp', ''),
('DRI', 'Darden Restaurants, Inc.', 'https://logo.clearbit.com/darden.com'),
('DTE', 'DTE Energy Co.', ''),
('DUK', 'Duke Energy', ''),
('DVA', 'DaVita Inc.', ''),
('DVN', 'Devon Energy Corporation', 'https://logo.clearbit.com/devonenergy.com'),
('DXC', 'DXC Technology Company', 'https://logo.clearbit.com/dxc.technology'),
('DXCM', 'DexCom', ''),
('EA', 'Electronic Arts Inc.', 'https://logo.clearbit.com/ea.com'),
('EBAY', 'eBay Inc.', ''),
('ECL', 'Ecolab Inc.', ''),
('ED', 'Consolidated Edison', ''),
('EFX', 'Equifax, Inc.', 'https://logo.clearbit.com/equifax.com'),
('EIX', 'Edison Int\'l', ''),
('EL', 'Estee Lauder Companies, Inc. (T', 'https://logo.clearbit.com/elcompanies.com'),
('EMN', 'Eastman Chemical', ''),
('EMR', 'Emerson Electric Company', 'https://logo.clearbit.com/emerson.com'),
('EOG', 'EOG Resources', ''),
('EQIX', 'Equinix, Inc.', 'https://logo.clearbit.com/equinix.com'),
('EQR', 'Equity Residential', ''),
('ES', 'Eversource Energy', ''),
('ESS', 'Essex Property Trust, Inc.', 'https://logo.clearbit.com/essexapartmenthomes.com'),
('ETFC', 'E*Trade', ''),
('ETN', 'Eaton Corporation', ''),
('ETR', 'Entergy Corp.', ''),
('EVRG', 'Evergy', ''),
('EW', 'Edwards Lifesciences Corporatio', 'https://logo.clearbit.com/edwards.com'),
('EXC', 'Exelon Corp.', ''),
('EXPD', 'Expeditors', ''),
('EXPE', 'Expedia Group', ''),
('EXR', 'Extra Space Storage', ''),
('F', 'Ford Motor Company', 'https://logo.clearbit.com/ford.com'),
('FANG', 'Diamondback Energy, Inc. - Comm', 'https://logo.clearbit.com/diamondbackenergy.com'),
('FAST', 'Fastenal Co', ''),
('FB', 'Facebook Inc.', ''),
('FBHS', 'Fortune Brands Home & Security', ''),
('FCX', 'Freeport-McMoRan Inc.', ''),
('FDX', 'FedEx Corporation', ''),
('FE', 'FirstEnergy Corp', ''),
('FFIV', 'F5 Networks, Inc.', 'https://logo.clearbit.com/f5.com'),
('FIS', 'Fidelity National Information S', 'https://logo.clearbit.com/fisglobal.com'),
('FISV', 'Fiserv Inc', ''),
('FITB', 'Fifth Third Bancorp', 'https://logo.clearbit.com/53.com'),
('FLIR', 'FLIR Systems', ''),
('FLS', 'Flowserve Corporation', ''),
('FLT', 'FleetCor Technologies, Inc.', 'https://logo.clearbit.com/fleetcor.com'),
('FMC', 'FMC Corporation', ''),
('FOX', 'Fox Corporation', 'https://logo.clearbit.com/foxcorporation.com'),
('FOXA', 'Fox Corporation', 'https://logo.clearbit.com/foxcorporation.com'),
('FRC', 'FIRST REPUBLIC BANK', 'https://logo.clearbit.com/firstrepublic.com'),
('FRT', 'Federal Realty Investment Trust', ''),
('FTI', 'TechnipFMC', ''),
('FTNT', 'Fortinet, Inc.', 'https://logo.clearbit.com/fortinet.com'),
('FTV', 'Fortive Corp', ''),
('GD', 'General Dynamics', ''),
('GE', 'General Electric Company', 'https://logo.clearbit.com/ge.com'),
('GILD', 'Gilead Sciences', ''),
('GIS', 'General Mills', ''),
('GL', 'Globe Life Inc.', ''),
('GLW', 'Corning Inc.', ''),
('GM', 'General Motors', ''),
('GOOG', 'Alphabet Inc.', 'https://logo.clearbit.com/abc.xyz'),
('GOOGL', 'Alphabet Inc. (Class A)', ''),
('GPC', 'Genuine Parts', ''),
('GPN', 'Global Payments Inc.', 'https://logo.clearbit.com/globalpaymentsinc.com'),
('GPS', 'Gap, Inc. (The)', 'https://logo.clearbit.com/gapinc.com'),
('GRMN', 'Garmin Ltd.', ''),
('GS', 'Goldman Sachs Group', ''),
('GWW', 'Grainger (W.W.) Inc.', ''),
('HAL', 'Halliburton Company', 'https://logo.clearbit.com/halliburton.com'),
('HAS', 'Hasbro, Inc.', 'https://logo.clearbit.com/hasbro.com'),
('HBAN', 'Huntington Bancshares', ''),
('HBI', 'Hanesbrands Inc', ''),
('HCA', 'HCA Healthcare, Inc.', 'https://logo.clearbit.com/hcahealthcare.com'),
('HD', 'Home Depot', ''),
('HES', 'Hess Corporation', ''),
('HFC', 'HollyFrontier Corp', ''),
('HIG', 'Hartford Financial Svc.Gp.', ''),
('HII', 'Huntington Ingalls Industries', ''),
('HLT', 'Hilton Worldwide Holdings Inc', ''),
('HOLX', 'Hologic', ''),
('HON', 'Honeywell Int\'l Inc.', ''),
('HPE', 'Hewlett Packard Enterprise', ''),
('HPQ', 'HP Inc.', 'https://logo.clearbit.com/hp.com'),
('HRB', 'H&R Block', ''),
('HRL', 'Hormel Foods Corp.', ''),
('HSIC', 'Henry Schein, Inc.', 'https://logo.clearbit.com/henryschein.com'),
('HST', 'Host Hotels & Resorts', ''),
('HSY', 'The Hershey Company', ''),
('HUM', 'Humana Inc.', ''),
('HWM', 'Howmet Aerospace', ''),
('IBM', 'International Business Machines', 'https://logo.clearbit.com/ibm.com'),
('ICE', 'Intercontinental Exchange', ''),
('IDXX', 'IDEXX Laboratories', ''),
('IEX', 'IDEX Corporation', ''),
('IFF', 'International Flavors & Fragrances', ''),
('ILMN', 'Illumina Inc', ''),
('INCY', 'Incyte', ''),
('INFO', 'IHS Markit Ltd.', 'https://logo.clearbit.com/ihsmarkit.com'),
('INTC', 'Intel Corporation', 'https://logo.clearbit.com/intel.com'),
('INTU', 'Intuit Inc.', ''),
('IP', 'International Paper Company', 'https://logo.clearbit.com/internationalpaper.com'),
('IPG', 'Interpublic Group', ''),
('IPGP', 'IPG Photonics Corp.', ''),
('IQV', 'IQVIA Holdings Inc.', ''),
('IR', 'Ingersoll Rand', ''),
('IRM', 'Iron Mountain Incorporated', ''),
('ISRG', 'Intuitive Surgical Inc.', ''),
('IT', 'Gartner, Inc.', 'https://logo.clearbit.com/gartner.com'),
('ITW', 'Illinois Tool Works', ''),
('IVZ', 'Invesco Ltd.', ''),
('J', 'Jacobs Engineering Group Inc.', 'https://logo.clearbit.com/jacobs.com'),
('JBHT', 'J. B. Hunt Transport Services', ''),
('JCI', 'Johnson Controls International', ''),
('JKHY', 'Jack Henry & Associates', ''),
('JNJ', 'Johnson & Johnson', ''),
('JNPR', 'Juniper Networks', ''),
('JPM', 'JPMorgan Chase & Co.', ''),
('K', 'Kellogg Company', 'https://logo.clearbit.com/kelloggcompany.com'),
('KEY', 'KeyCorp', ''),
('KEYS', 'Keysight Technologies', ''),
('KHC', 'Kraft Heinz Co', ''),
('KIM', 'Kimco Realty', ''),
('KLAC', 'KLA Corporation', ''),
('KMB', 'Kimberly-Clark', ''),
('KMI', 'Kinder Morgan', ''),
('KMX', 'Carmax Inc', ''),
('KO', 'Coca-Cola Company (The)', 'https://logo.clearbit.com/coca-colacompany.com'),
('KR', 'Kroger Company (The)', 'https://logo.clearbit.com/thekrogerco.com'),
('KSS', 'Kohl\'s Corp.', ''),
('KSU', 'Kansas City Southern', ''),
('L', 'Loews Corporation', 'https://logo.clearbit.com/loews.com'),
('LB', 'L Brands Inc.', ''),
('LDOS', 'Leidos Holdings', ''),
('LEG', 'Leggett & Platt', ''),
('LEN', 'Lennar Corp.', ''),
('LH', 'Laboratory Corp. of America Holding', ''),
('LHX', 'L3Harris Technologies', ''),
('LIN', 'Linde plc', 'https://logo.clearbit.com/linde.com'),
('LKQ', 'LKQ Corporation', ''),
('LLY', 'Lilly (Eli) & Co.', ''),
('LMT', 'Lockheed Martin Corp.', ''),
('LNC', 'Lincoln National', ''),
('LNT', 'Alliant Energy Corp', ''),
('LOW', 'Lowe\'s Cos.', ''),
('LRCX', 'Lam Research Corporation', 'https://logo.clearbit.com/lamresearch.com'),
('LUV', 'Southwest Airlines', ''),
('LVS', 'Las Vegas Sands Corp.', 'https://logo.clearbit.com/sands.com'),
('LW', 'Lamb Weston Holdings Inc', ''),
('LYB', 'LyondellBasell Industries NV', 'https://logo.clearbit.com/lyondellbasell.com'),
('LYV', 'Live Nation Entertainment', ''),
('MA', 'Mastercard Incorporated', 'https://logo.clearbit.com/mastercard.com'),
('MAA', 'Mid-America Apartment Communiti', 'https://logo.clearbit.com/maac.com'),
('MAR', 'Marriott Int\'l.', ''),
('MAS', 'Masco Corp.', ''),
('MCD', 'McDonald\'s Corporation', 'https://logo.clearbit.com/corporate.mcdonalds.com'),
('MCHP', 'Microchip Technology', ''),
('MCK', 'McKesson Corp.', ''),
('MCO', 'Moody\'s Corp', ''),
('MDLZ', 'Mondelez International', ''),
('MDT', 'Medtronic plc.', 'https://logo.clearbit.com/medtronic.com'),
('MET', 'MetLife Inc.', ''),
('MGM', 'MGM Resorts International', ''),
('MHK', 'Mohawk Industries', ''),
('MKC', 'McCormick & Co.', ''),
('MKTX', 'MarketAxess', ''),
('MLM', 'Martin Marietta Materials', ''),
('MMC', 'Marsh & McLennan', ''),
('MMM', '3M Company', 'https://logo.clearbit.com/3m.com'),
('MNST', 'Monster Beverage', ''),
('MO', 'Altria Group Inc', ''),
('MOS', 'The Mosaic Company', ''),
('MPC', 'Marathon Petroleum', ''),
('MRK', 'Merck & Co.', ''),
('MRO', 'Marathon Oil Corp.', ''),
('MS', 'Morgan Stanley', ''),
('MSCI', 'MSCI Inc', 'https://logo.clearbit.com/msci.com'),
('MSFT', 'Microsoft Corporation', 'https://logo.clearbit.com/microsoft.com'),
('MSI', 'Motorola Solutions Inc.', ''),
('MTB', 'M&T Bank Corp.', ''),
('MTD', 'Mettler Toledo', ''),
('MU', 'Micron Technology', ''),
('MXIM', 'Maxim Integrated Products Inc', ''),
('MYL', 'Mylan N.V.', ''),
('NBL', 'Noble Energy', ''),
('NCLH', 'Norwegian Cruise Line Holdings', ''),
('NDAQ', 'Nasdaq Inc.', ''),
('NEE', 'NextEra Energy', ''),
('NEM', 'Newmont Corporation', ''),
('NFLX', 'Netflix, Inc.', 'https://logo.clearbit.com/netflix.com'),
('NI', 'NiSource Inc.', ''),
('NKE', 'Nike Inc.', ''),
('NLOK', 'NortonLifeLock', ''),
('NLSN', 'Nielsen Holdings', ''),
('NOC', 'Northrop Grumman', ''),
('NOV', 'National Oilwell Varco Inc.', ''),
('NOW', 'ServiceNow', ''),
('NRG', 'NRG Energy', ''),
('NSC', 'Norfolk Southern Corp.', ''),
('NTAP', 'NetApp, Inc.', 'https://logo.clearbit.com/netapp.com'),
('NTRS', 'Northern Trust Corp.', ''),
('NUE', 'Nucor Corp.', ''),
('NVDA', 'NVIDIA Corporation', 'https://logo.clearbit.com/nvidia.com'),
('NVR', 'NVR Inc.', ''),
('NWL', 'Newell Brands', ''),
('NWS', 'News Corp. Class B', ''),
('NWSA', 'News Corp. Class A', ''),
('O', 'Realty Income Corporation', ''),
('ODFL', 'Old Dominion Freight Line', ''),
('OKE', 'ONEOK', ''),
('OMC', 'Omnicom Group', ''),
('ORCL', 'Oracle Corp.', ''),
('ORLY', 'O\'Reilly Automotive, Inc.', 'https://logo.clearbit.com/oreillyauto.com'),
('OTIS', 'Otis Worldwide', ''),
('OXY', 'Occidental Petroleum', ''),
('PAYC', 'Paycom Software, Inc.', 'https://logo.clearbit.com/paycom.com'),
('PAYX', 'Paychex Inc.', ''),
('PBCT', 'People\'s United Financial', ''),
('PCAR', 'PACCAR Inc.', ''),
('PEAK', 'Healthpeak Properties', ''),
('PEG', 'Public Service Enterprise Group (PSEG)', ''),
('PEP', 'PepsiCo Inc.', ''),
('PFE', 'Pfizer, Inc.', 'https://logo.clearbit.com/pfizer.com'),
('PFG', 'Principal Financial Group', ''),
('PG', 'Procter & Gamble', ''),
('PGR', 'Progressive Corp.', ''),
('PH', 'Parker-Hannifin', ''),
('PHM', 'PulteGroup', ''),
('PKG', 'Packaging Corporation of America', ''),
('PKI', 'PerkinElmer', ''),
('PLD', 'Prologis', ''),
('PM', 'Philip Morris International', ''),
('PNC', 'PNC Financial Services', ''),
('PNR', 'Pentair plc', ''),
('PNW', 'Pinnacle West Capital', ''),
('PPG', 'PPG Industries', ''),
('PPL', 'PPL Corp.', ''),
('PRGO', 'Perrigo', ''),
('PRU', 'Prudential Financial', ''),
('PSA', 'Public Storage', ''),
('PSX', 'Phillips 66', ''),
('PVH', 'PVH Corp.', ''),
('PWR', 'Quanta Services Inc.', ''),
('PXD', 'Pioneer Natural Resources', ''),
('PYPL', 'PayPal Holdings, Inc.', 'https://logo.clearbit.com/paypal.com'),
('QCOM', 'QUALCOMM Inc.', ''),
('QRVO', 'Qorvo', ''),
('RCL', 'D/B/A Royal Caribbean Cruises L', 'https://logo.clearbit.com/rclinvestor.com'),
('RE', 'Everest Re Group Ltd.', ''),
('REG', 'Regency Centers Corporation', ''),
('REGN', 'Regeneron Pharmaceuticals', ''),
('RF', 'Regions Financial Corp.', ''),
('RHI', 'Robert Half International', ''),
('RJF', 'Raymond James Financial Inc.', ''),
('RL', 'Ralph Lauren Corporation', ''),
('RMD', 'ResMed Inc.', 'https://logo.clearbit.com/resmed.com'),
('ROK', 'Rockwell Automation Inc.', ''),
('ROL', 'Rollins Inc.', ''),
('ROP', 'Roper Technologies', ''),
('ROST', 'Ross Stores', ''),
('RSG', 'Republic Services Inc', ''),
('RTX', 'Raytheon Technologies Corporati', 'https://logo.clearbit.com/rtx.com'),
('SAP', 'SAP  SE', 'https://logo.clearbit.com/sap.com'),
('SBAC', 'SBA Communications', ''),
('SBUX', 'Starbucks Corporation', 'https://logo.clearbit.com/starbucks.com'),
('SCHW', 'Charles Schwab Corporation', ''),
('SEE', 'Sealed Air', ''),
('SHW', 'Sherwin-Williams', ''),
('SIVB', 'SVB Financial', ''),
('SJM', 'JM Smucker', ''),
('SLB', 'Schlumberger Ltd.', ''),
('SLG', 'SL Green Realty', ''),
('SNA', 'Snap-on', ''),
('SNPS', 'Synopsys Inc.', ''),
('SO', 'Southern Company', ''),
('SPG', 'Simon Property Group Inc', ''),
('SPGI', 'S&P Global Inc.', ''),
('SRE', 'Sempra Energy', ''),
('STE', 'STERIS plc', ''),
('STT', 'State Street Corp.', ''),
('STX', 'Seagate Technology', ''),
('STZ', 'Constellation Brands', ''),
('SWK', 'Stanley Black & Decker', ''),
('SWKS', 'Skyworks Solutions', ''),
('SYF', 'Synchrony Financial', ''),
('SYK', 'Stryker Corp.', ''),
('SYY', 'Sysco Corp.', ''),
('T', 'AT&T Inc.', ''),
('TAP', 'Molson Coors Beverage Company', ''),
('TDG', 'TransDigm Group', ''),
('TDY', 'Teledyne Technologies', ''),
('TEL', 'TE Connectivity Ltd.', ''),
('TFC', 'Truist Financial', ''),
('TFX', 'Teleflex', ''),
('TGT', 'Target Corp.', ''),
('TIF', 'Tiffany & Co.', ''),
('TJX', 'TJX Companies Inc.', ''),
('TMO', 'Thermo Fisher Scientific', ''),
('TMUS', 'T-Mobile US, Inc.', 'https://logo.clearbit.com/t-mobile.com'),
('TPR', 'Tapestry Inc.', ''),
('TROW', 'T. Rowe Price Group', ''),
('TRV', 'The Travelers Companies Inc.', ''),
('TSCO', 'Tractor Supply Company', ''),
('TSLA', 'Tesla, Inc.', 'https://logo.clearbit.com/tesla.com'),
('TSN', 'Tyson Foods', ''),
('TT', 'Trane Technologies plc', ''),
('TTWO', 'Take-Two Interactive', ''),
('TWTR', 'Twitter, Inc.', 'https://logo.clearbit.com/twitter.com'),
('TXN', 'Texas Instruments', ''),
('TXT', 'Textron Inc.', ''),
('TYL', 'Tyler Technologies', ''),
('UA', 'Under Armour (Class C)', ''),
('UAA', 'Under Armour (Class A)', ''),
('UAL', 'United Continental Holdings, In', 'https://logo.clearbit.com/united.com'),
('UDR', 'UDR Inc.', ''),
('UHS', 'Universal Health Services', ''),
('ULTA', 'Ulta Beauty', ''),
('UNH', 'United Health Group Inc.', ''),
('UNM', 'Unum Group', ''),
('UNP', 'Union Pacific Corp', ''),
('UPS', 'United Parcel Service', ''),
('URI', 'United Rentals Inc.', ''),
('USB', 'U.S. Bancorp', ''),
('V', 'Visa Inc.', 'https://logo.clearbit.com/usa.visa.com'),
('VAR', 'Varian Medical Systems', ''),
('VFC', 'VF Corporation', ''),
('VIAC', 'ViacomCBS', ''),
('VLO', 'Valero Energy', ''),
('VMC', 'Vulcan Materials', ''),
('VNO', 'Vornado Realty Trust', ''),
('VRSK', 'Verisk Analytics', ''),
('VRSN', 'Verisign Inc.', ''),
('VRTX', 'Vertex Pharmaceuticals Inc', ''),
('VTR', 'Ventas Inc', ''),
('VZ', 'Verizon Communications', ''),
('WAB', 'Wabtec Corporation', ''),
('WAT', 'Waters Corporation', ''),
('WBA', 'Walgreens Boots Alliance', ''),
('WDC', 'Western Digital', ''),
('WEC', 'WEC Energy Group', ''),
('WELL', 'Welltower Inc.', ''),
('WFC', 'Wells Fargo', ''),
('WHR', 'Whirlpool Corp.', ''),
('WLTW', 'Willis Towers Watson', ''),
('WM', 'Waste Management Inc.', ''),
('WMB', 'Williams Companies', ''),
('WMT', 'Walmart Inc.', 'https://logo.clearbit.com/stock.walmart.com'),
('WRB', 'W. R. Berkley Corporation', ''),
('WRK', 'WestRock', ''),
('WST', 'West Pharmaceutical Services', ''),
('WU', 'Western Union Co', ''),
('WY', 'Weyerhaeuser', ''),
('WYNN', 'Wynn Resorts Ltd', ''),
('XEL', 'Xcel Energy Inc', ''),
('XLNX', 'Xilinx', ''),
('XOM', 'Exxon Mobil Corp.', ''),
('XRAY', 'Dentsply Sirona', ''),
('XRX', 'Xerox', ''),
('XYL', 'Xylem Inc.', ''),
('YUM', 'Yum! Brands Inc', ''),
('ZBH', 'Zimmer Biomet Holdings', ''),
('ZBRA', 'Zebra Technologies', ''),
('ZION', 'Zions Bancorp', ''),
('ZTS', 'Zoetis', '');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `tradable_values_prices`
--

CREATE TABLE `tradable_values_prices` (
  `id` int(11) NOT NULL,
  `symbol` varchar(250) NOT NULL,
  `market_value` float NOT NULL,
  `timestamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `transactions`
--

CREATE TABLE `transactions` (
  `transaction_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `symbol` varchar(250) NOT NULL,
  `course_id` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `transaction_type` enum('buy','sell') NOT NULL,
  `transaction_fee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `users`
--

CREATE TABLE `users` (
  `userID` int(11) NOT NULL,
  `first_name` varchar(150) CHARACTER SET latin1 NOT NULL,
  `last_name` varchar(150) CHARACTER SET latin1 NOT NULL,
  `email` varchar(200) CHARACTER SET latin1 NOT NULL,
  `auth_password` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `money_available` float NOT NULL,
  `starting_capital` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `user_authkey`
--

CREATE TABLE `user_authkey` (
  `userID` int(11) NOT NULL,
  `auth_key` varchar(128) NOT NULL,
  `expiry` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `user_settings`
--

CREATE TABLE `user_settings` (
  `id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `user_setting` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `value` varchar(150) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `tradable_values`
--
ALTER TABLE `tradable_values`
  ADD PRIMARY KEY (`symbol`);

--
-- Indizes für die Tabelle `tradable_values_prices`
--
ALTER TABLE `tradable_values_prices`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`transaction_id`),
  ADD KEY `TradableValuePricesID` (`course_id`),
  ADD KEY `UserTransactions` (`user_id`);

--
-- Indizes für die Tabelle `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userID`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indizes für die Tabelle `user_authkey`
--
ALTER TABLE `user_authkey`
  ADD PRIMARY KEY (`auth_key`),
  ADD UNIQUE KEY `auth_key` (`auth_key`),
  ADD KEY `UserIDAuthkey` (`userID`);

--
-- Indizes für die Tabelle `user_settings`
--
ALTER TABLE `user_settings`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `tradable_values_prices`
--
ALTER TABLE `tradable_values_prices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=191;
--
-- AUTO_INCREMENT für Tabelle `transactions`
--
ALTER TABLE `transactions`
  MODIFY `transaction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT für Tabelle `users`
--
ALTER TABLE `users`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
--
-- AUTO_INCREMENT für Tabelle `user_settings`
--
ALTER TABLE `user_settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
--
-- Constraints der exportierten Tabellen
--

--
-- Constraints der Tabelle `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `TradableValuePricesID` FOREIGN KEY (`course_id`) REFERENCES `tradable_values_prices` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `UserTransactions` FOREIGN KEY (`user_id`) REFERENCES `users` (`userID`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints der Tabelle `user_authkey`
--
ALTER TABLE `user_authkey`
  ADD CONSTRAINT `UserIDAuthkey` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`) ON DELETE CASCADE ON UPDATE NO ACTION;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
