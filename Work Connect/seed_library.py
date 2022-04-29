#file will have the list of dictionaries for each company
#will be used to populate the database once all data is collected
#{"company_name": "Company X", "job_scope": {"tech": "www.tech.com", "business": "www.business.com", "finance": "www.finance.com"}}
# )
companies = [
    {"company_name": "Cognizant Technology Solutions", "job_scope": {"tech":"https://www.hcltech.com/rise-at-hcl/entry-level-jobs#cb-6027", "business": "https://www.hcltech.com/rise-at-hcl/entry-level-jobs#cb-6027", "consulting":"https://www.hcltech.com/rise-at-hcl/entry-level-jobs#cb-6027", "marketing":"https://www.hcltech.com/rise-at-hcl/entry-level-jobs#cb-6027", "sales":"https://www.hcltech.com/rise-at-hcl/entry-level-jobs#cb-6027", "legal":"https://www.hcltech.com/rise-at-hcl/entry-level-jobs#cb-6027"}},
    {"company_name": "Infosys", "job_scope": {"tech":"https://jobs.infosys.com/TGnewUI/Search/Home/Home?partnerid=25633&siteid=5440&Codes=BeMore#keyWordSearch=technology&locationSearch=USA", "finance":"https://jobs.infosys.com/TGnewUI/Search/Home/Home?partnerid=25633&siteid=5440&Codes=BeMore#keyWordSearch=consulting&locationSearch=USA"}},
    {"company_name": "Tata Consultancy Services", "job_scope": {"tech":"https://www.tcs.com/careers?country=US&lang=EN", "consulting":"https://www.tcs.com/careers?country=US&lang=EN","business":"https://www.tcs.com/careers?country=US&lang=EN"}},
    {"company_name": "Google", "job_scope": {"tech":"https://careers.google.com/jobs/results/?gclid=CjwKCAjwu_mSBhAYEiwA5BBmf5QD8Kf09kGEEwL2OVuuSgh6F1EWHT3gfoG43x8Qm7QPDFQg14Z-bRoCIdsQAvD_BwE&gclsrc=aw.ds&location=United%20States&q=software%20engineering&src=Online%2FHouse%20Ads%2FBKWS_LATAM", "finance":"https://careers.google.com/jobs/results/?gclid=CjwKCAjwu_mSBhAYEiwA5BBmf5QD8Kf09kGEEwL2OVuuSgh6F1EWHT3gfoG43x8Qm7QPDFQg14Z-bRoCIdsQAvD_BwE&gclsrc=aw.ds&location=United%20States&q=finance&src=Online%2FHouse%20Ads%2FBKWS_LATAM", "marketing":"https://careers.google.com/jobs/results/?gclid=CjwKCAjwu_mSBhAYEiwA5BBmf5QD8Kf09kGEEwL2OVuuSgh6F1EWHT3gfoG43x8Qm7QPDFQg14Z-bRoCIdsQAvD_BwE&gclsrc=aw.ds&location=United%20States&q=marketing&src=Online%2FHouse%20Ads%2FBKWS_LATAM", "sales":"https://careers.google.com/jobs/results/?gclid=CjwKCAjwu_mSBhAYEiwA5BBmf5QD8Kf09kGEEwL2OVuuSgh6F1EWHT3gfoG43x8Qm7QPDFQg14Z-bRoCIdsQAvD_BwE&gclsrc=aw.ds&location=United%20States&q=sales&src=Online%2FHouse%20Ads%2FBKWS_LATAM","legal":"https://careers.google.com/jobs/results/?gclid=CjwKCAjwu_mSBhAYEiwA5BBmf5QD8Kf09kGEEwL2OVuuSgh6F1EWHT3gfoG43x8Qm7QPDFQg14Z-bRoCIdsQAvD_BwE&gclsrc=aw.ds&location=United%20States&q=legal&src=Online%2FHouse%20Ads%2FBKWS_LATAM"}},
    {"company_name": "Ernst & Young", "job_scope": {"tech":"https://eyglobal.yello.co/job_boards/c1riT--B2O-KySgYWsZO1Q?locale=en","consulting":"https://eyglobal.yello.co/job_boards/c1riT--B2O-KySgYWsZO1Q?locale=en","business":"https://eyglobal.yello.co/job_boards/c1riT--B2O-KySgYWsZO1Q?locale=en"}},
    {"company_name": "Capgemini", "job_scope": {"tech":"https://www.capgemini.com/us-en/careers/job-search/?search_term=","business":"https://www.capgemini.com/us-en/careers/job-search/?search_term=","marketing":"https://www.capgemini.com/us-en/careers/job-search/?search_term="}},
    {"company_name": "Deloitte & Touche", "job_scope": {"consulting":"https://apply.deloitte.com/careers/SearchJobs?sort=relevancy&3_5_3=477","finance":"https://apply.deloitte.com/careers/SearchJobs?sort=relevancy&3_5_3=477","legal":"https://apply.deloitte.com/careers/SearchJobs?sort=relevancy&3_5_3=477","communications":"https://apply.deloitte.com/careers/SearchJobs?sort=relevancy&3_5_3=477","marketing":"https://apply.deloitte.com/careers/SearchJobs?sort=relevancy&3_5_3=477"}},
    {"company_name": "Amazon", "job_scope": {"tech":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=technology&city=&country=&region=&county=&query_options=&","hardware":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=hardware&city=&country=&region=&county=&query_options=&","business":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&job_type%5B%5D=Full-Time&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=business&city=&country=&region=&county=&query_options=&","legal":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&job_type%5B%5D=Full-Time&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=legal&city=&country=&region=&county=&query_options=&","marketing":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&job_type%5B%5D=Full-Time&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=marketing&city=&country=&region=&county=&query_options=&","communications":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&job_type%5B%5D=Full-Time&country%5B%5D=USA&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=communications&city=&country=&region=&county=&query_options=&"}},
    {"company_name": "IBM", "job_scope": {"tech":"https://www.ibm.com/employment/#jobs?%23jobs=&job-search=","finance":"https://www.ibm.com/employment/#jobs?%23jobs=&job-search=","legal":"https://www.ibm.com/employment/#jobs?%23jobs=&job-search=","communications":"https://www.ibm.com/employment/#jobs?%23jobs=&job-search="}},
    {"company_name": "Microsoft", "job_scope": {"tech":"https://careers.microsoft.com/us/en/search-results?keywords=technology","hardware":"https://careers.microsoft.com/us/en/search-results?keywords=hardware","sales":"https://careers.microsoft.com/us/en/search-results?keywords=marketing","marketing":"https://careers.microsoft.com/us/en/search-results?keywords=marketing","business":"https://careers.microsoft.com/us/en/search-results?keywords=","finance":"https://careers.microsoft.com/us/en/search-results?keywords=","legal":"https://careers.microsoft.com/us/en/search-results?keywords="}},
    {"company_name": "Accenture", "job_scope": {"consulting":"https://www.accenture.com/us-en/careers/jobsearch?jk=technology%20consulting&sb=0&pg=1&vw=0&is_rj=0&sk=management%20consulting","tech":"https://www.accenture.com/us-en/careers/jobsearch?jk=Technology&sb=0&pg=1&vw=0&is_rj=0","business":"https://www.accenture.com/us-en/careers/jobsearch?jk=corporate+functions&sb=0&pg=1&vw=0&is_rj=0","finance":"https://www.accenture.com/us-en/careers/jobsearch?jk=corporate+functions&sb=0&pg=1&vw=0&is_rj=0"}},
    {"company_name": "Hcl America", "job_scope": {"tech":"https://www.hcltech.com/rise-at-hcl/entry-level-jobs#cb-6027","consulting":"https://www.hcltech.com/rise-at-hcl/entry-level-jobs#cb-6027"}},
    {"company_name": "Wipro", "job_scope": {"tech":"https://careers.wipro.com/careers-home/jobs?keywords=software&sortBy=relevance&page=1&country=United%20States","business":"https://careers.wipro.com/careers-home/jobs?country=United%20States&page=1&keywords=business&sortBy=relevance","sales":"https://careers.wipro.com/careers-home/jobs?keywords=Sales&country=United%20States&page=1"}},
    {"company_name": "Tech Mahindra", "job_scope": {"tech":"https://careers.techmahindra.com/"}},
    {"company_name": "Larsen & Toubro Infotech", "job_scope": {"tech":"https://careers.lntinfotech.com/search/?createNewAlert=false&q=technology&optionsFacetsDD_country=US&optionsFacetsDD_location=&locationsearch=","business":"https://careers.lntinfotech.com/search/?createNewAlert=false&q=business&optionsFacetsDD_country=US&optionsFacetsDD_location=&locationsearch=","consulting":"https://careers.lntinfotech.com/search/?createNewAlert=false&q=consulting&optionsFacetsDD_country=US&optionsFacetsDD_location=&locationsearch="}},
    {"company_name": "Facebook", "job_scope": {"tech":"https://www.metacareers.com/areas-of-work/Facebook%20App/?p[divisions][0]=Facebook&divisions[0]=Facebook&teams[0]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&offices[0]=Remote%2C%20US&offices[1]=Miami%2C%20Florida&offices[2]=New%20Albany%2C%20OH&offices[3]=Huntsville%2C%20AL&offices[4]=Atlanta%2C%20GA&offices[5]=Newton%20County%2C%20GA&offices[6]=Prineville%2C%20OR&offices[7]=Pittsburgh%2C%20PA&offices[8]=Gallatin%2C%20TN&offices[9]=DeKalb%2C%20IL&offices[10]=Chicago%2C%20IL&offices[11]=Mesa%2C%20AZ&offices[12]=Menlo%20Park%2C%20CA&offices[13]=Los%20Angeles%2C%20CA&offices[14]=Mountain%20View%2C%20CA&offices[15]=Northridge%2C%20CA&offices[16]=San%20Francisco%2C%20CA&offices[17]=Santa%20Clara%2C%20CA&offices[18]=Altoona%2C%20IA&offices[19]=Boston%2C%20MA&offices[20]=Austin%2C%20TX&offices[21]=Dallas%2C%20TX&offices[22]=Fort%20Worth%2C%20TX&offices[23]=Fremont%2C%20CA&offices[24]=Sunnyvale%2C%20CA&offices[25]=Sausalito%2C%20CA&offices[26]=Burlingame%2C%20CA&offices[27]=Foster%20City%2C%20CA&offices[28]=Irvine%2C%20CA&offices[29]=Detroit%2C%20MI&offices[30]=Eagle%20Mountain%2C%20Utah&offices[31]=Ashburn%2C%20VA&offices[32]=Henrico%2C%20VA&offices[33]=Reston%2C%20VA&offices[34]=Papillion%2C%20NE&offices[35]=Sarpy%20County%2C%20NE&offices[36]=Los%20Lunas%2C%20NM&offices[37]=Redmond%2C%20WA&offices[38]=Seattle%2C%20WA&offices[39]=Bellevue%2C%20WA&offices[40]=New%20York%2C%20NY&offices[41]=Forest%20City%2C%20NC&offices[42]=Washington%2C%20DC&offices[43]=Denver%2C%20CO","engineering":"https://www.metacareers.com/areas-of-work/Facebook%20App/?p[divisions][0]=Facebook&divisions[0]=Facebook&teams[0]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&offices[0]=Remote%2C%20US&offices[1]=Miami%2C%20Florida&offices[2]=New%20Albany%2C%20OH&offices[3]=Huntsville%2C%20AL&offices[4]=Atlanta%2C%20GA&offices[5]=Newton%20County%2C%20GA&offices[6]=Prineville%2C%20OR&offices[7]=Pittsburgh%2C%20PA&offices[8]=Gallatin%2C%20TN&offices[9]=DeKalb%2C%20IL&offices[10]=Chicago%2C%20IL&offices[11]=Mesa%2C%20AZ&offices[12]=Menlo%20Park%2C%20CA&offices[13]=Los%20Angeles%2C%20CA&offices[14]=Mountain%20View%2C%20CA&offices[15]=Northridge%2C%20CA&offices[16]=San%20Francisco%2C%20CA&offices[17]=Santa%20Clara%2C%20CA&offices[18]=Altoona%2C%20IA&offices[19]=Boston%2C%20MA&offices[20]=Austin%2C%20TX&offices[21]=Dallas%2C%20TX&offices[22]=Fort%20Worth%2C%20TX&offices[23]=Fremont%2C%20CA&offices[24]=Sunnyvale%2C%20CA&offices[25]=Sausalito%2C%20CA&offices[26]=Burlingame%2C%20CA&offices[27]=Foster%20City%2C%20CA&offices[28]=Irvine%2C%20CA&offices[29]=Detroit%2C%20MI&offices[30]=Eagle%20Mountain%2C%20Utah&offices[31]=Ashburn%2C%20VA&offices[32]=Henrico%2C%20VA&offices[33]=Reston%2C%20VA&offices[34]=Papillion%2C%20NE&offices[35]=Sarpy%20County%2C%20NE&offices[36]=Los%20Lunas%2C%20NM&offices[37]=Redmond%2C%20WA&offices[38]=Seattle%2C%20WA&offices[39]=Bellevue%2C%20WA&offices[40]=New%20York%2C%20NY&offices[41]=Forest%20City%2C%20NC&offices[42]=Washington%2C%20DC&offices[43]=Denver%2C%20CO","design":"https://www.metacareers.com/areas-of-work/Facebook%20App/?p[divisions][0]=Facebook&divisions[0]=Facebook&teams[0]=University%20Grad%20-%20Engineering%2C%20Tech%20%26%20Design&offices[0]=Remote%2C%20US&offices[1]=Miami%2C%20Florida&offices[2]=New%20Albany%2C%20OH&offices[3]=Huntsville%2C%20AL&offices[4]=Atlanta%2C%20GA&offices[5]=Newton%20County%2C%20GA&offices[6]=Prineville%2C%20OR&offices[7]=Pittsburgh%2C%20PA&offices[8]=Gallatin%2C%20TN&offices[9]=DeKalb%2C%20IL&offices[10]=Chicago%2C%20IL&offices[11]=Mesa%2C%20AZ&offices[12]=Menlo%20Park%2C%20CA&offices[13]=Los%20Angeles%2C%20CA&offices[14]=Mountain%20View%2C%20CA&offices[15]=Northridge%2C%20CA&offices[16]=San%20Francisco%2C%20CA&offices[17]=Santa%20Clara%2C%20CA&offices[18]=Altoona%2C%20IA&offices[19]=Boston%2C%20MA&offices[20]=Austin%2C%20TX&offices[21]=Dallas%2C%20TX&offices[22]=Fort%20Worth%2C%20TX&offices[23]=Fremont%2C%20CA&offices[24]=Sunnyvale%2C%20CA&offices[25]=Sausalito%2C%20CA&offices[26]=Burlingame%2C%20CA&offices[27]=Foster%20City%2C%20CA&offices[28]=Irvine%2C%20CA&offices[29]=Detroit%2C%20MI&offices[30]=Eagle%20Mountain%2C%20Utah&offices[31]=Ashburn%2C%20VA&offices[32]=Henrico%2C%20VA&offices[33]=Reston%2C%20VA&offices[34]=Papillion%2C%20NE&offices[35]=Sarpy%20County%2C%20NE&offices[36]=Los%20Lunas%2C%20NM&offices[37]=Redmond%2C%20WA&offices[38]=Seattle%2C%20WA&offices[39]=Bellevue%2C%20WA&offices[40]=New%20York%2C%20NY&offices[41]=Forest%20City%2C%20NC&offices[42]=Washington%2C%20DC&offices[43]=Denver%2C%20CO","business":"https://www.metacareers.com/areas-of-work/Facebook%20App/?p[divisions][0]=Facebook&divisions[0]=Facebook&teams[0]=University%20Grad%20-%20Business&offices[0]=Remote%2C%20US&offices[1]=Miami%2C%20Florida&offices[2]=New%20Albany%2C%20OH&offices[3]=Huntsville%2C%20AL&offices[4]=Atlanta%2C%20GA&offices[5]=Newton%20County%2C%20GA&offices[6]=Prineville%2C%20OR&offices[7]=Pittsburgh%2C%20PA&offices[8]=Gallatin%2C%20TN&offices[9]=DeKalb%2C%20IL&offices[10]=Chicago%2C%20IL&offices[11]=Mesa%2C%20AZ&offices[12]=Menlo%20Park%2C%20CA&offices[13]=Los%20Angeles%2C%20CA&offices[14]=Mountain%20View%2C%20CA&offices[15]=Northridge%2C%20CA&offices[16]=San%20Francisco%2C%20CA&offices[17]=Santa%20Clara%2C%20CA&offices[18]=Altoona%2C%20IA&offices[19]=Boston%2C%20MA&offices[20]=Austin%2C%20TX&offices[21]=Dallas%2C%20TX&offices[22]=Fort%20Worth%2C%20TX&offices[23]=Fremont%2C%20CA&offices[24]=Sunnyvale%2C%20CA&offices[25]=Sausalito%2C%20CA&offices[26]=Burlingame%2C%20CA&offices[27]=Foster%20City%2C%20CA&offices[28]=Irvine%2C%20CA&offices[29]=Detroit%2C%20MI&offices[30]=Eagle%20Mountain%2C%20Utah&offices[31]=Ashburn%2C%20VA&offices[32]=Henrico%2C%20VA&offices[33]=Reston%2C%20VA&offices[34]=Papillion%2C%20NE&offices[35]=Sarpy%20County%2C%20NE&offices[36]=Los%20Lunas%2C%20NM&offices[37]=Redmond%2C%20WA&offices[38]=Seattle%2C%20WA&offices[39]=Bellevue%2C%20WA&offices[40]=New%20York%2C%20NY&offices[41]=Forest%20City%2C%20NC&offices[42]=Washington%2C%20DC&offices[43]=Denver%2C%20CO"}},
    {"company_name": "WalMart Associates", "job_scope": {"tech":"https://careers.walmart.com/technology","finance":"https://careers.walmart.com/corporate","business":"https://careers.walmart.com/corporate","healthcare":"https://careers.walmart.com/healthcare"}},
    {"company_name": "L&T Technology Services", "job_scope": {"tech":"https://jobs.ltts.com/search/?createNewAlert=false&q=technology&locationsearch=","hardware":"https://jobs.ltts.com/search/?createNewAlert=false&q=hardware&locationsearch="}},
    {"company_name": "Syntel", "job_scope": {"tech":"https://jobs.atos.net/search/?createNewAlert=false&q=technology&optionsFacetsDD_country=&optionsFacetsDD_city=&optionsFacetsDD_customfield2=&optionsFacetsDD_customfield3=&optionsFacetsDD_department=&locationsearch=","hardware":"https://jobs.atos.net/search/?createNewAlert=false&q=hardware&optionsFacetsDD_country=&optionsFacetsDD_city=&optionsFacetsDD_customfield2=&optionsFacetsDD_customfield3=&optionsFacetsDD_department=&locationsearch=united+states","business":"https://jobs.atos.net/search/?createNewAlert=false&q=business&optionsFacetsDD_country=&optionsFacetsDD_city=&optionsFacetsDD_customfield2=&optionsFacetsDD_customfield3=&optionsFacetsDD_department=&locationsearch=united+states","marketing":"https://jobs.atos.net/search/?createNewAlert=false&q=marketing&optionsFacetsDD_country=&optionsFacetsDD_city=&optionsFacetsDD_customfield2=&optionsFacetsDD_customfield3=&optionsFacetsDD_department=&locationsearch=united+states"}},
    {"company_name": "Stripe", "job_scope": {"engineering":"https://stripe.com/jobs/search?t=engineering&l=chicago%2Cnewyork%2Cremote%2Csanfrancisco%2Cseattle%2Cwashingtondc&s=fulltime", "business":"https://stripe.com/jobs/search?t=business&l=chicago%2Cnewyork%2Cremote%2Csanfrancisco%2Cseattle%2Cwashingtondc&s=fulltime","finance":"https://stripe.com/jobs/search?t=finance&l=chicago%2Cnewyork%2Cremote%2Csanfrancisco%2Cseattle%2Cwashingtondc&s=fulltime","legal":"https://stripe.com/jobs/search?t=legal&l=chicago%2Cnewyork%2Cremote%2Csanfrancisco%2Cseattle%2Cwashingtondc&s=fulltime","operations":"https://stripe.com/jobs/search?t=operations&l=chicago%2Cnewyork%2Cremote%2Csanfrancisco%2Cseattle%2Cwashingtondc&s=fulltime","tech":"https://stripe.com/jobs/search?t=product-and-technical&l=chicago%2Cnewyork%2Cremote%2Csanfrancisco%2Cseattle%2Cwashingtondc&s=fulltime","design":"https://stripe.com/jobs/search?t=design&l=chicago%2Cnewyork%2Cremote%2Csanfrancisco%2Cseattle%2Cwashingtondc&s=fulltime"}},
    {"company_name": "Salesforce", "job_scope": {"tech":"https://salesforce.wd1.myworkdayjobs.com/External_Career_Site/10/refreshFacet/318c8bb6f553100021d223d9780d30be","marketing":"https://stripe.com/jobs/search?t=business&l=chicago%2Cnewyork%2Cremote%2Csanfrancisco%2Cseattle%2Cwashingtondc&s=fulltime","finance":"https://salesforce.wd1.myworkdayjobs.com/External_Career_Site/12/refreshFacet/318c8bb6f553100021d223d9780d30be","legal":"https://salesforce.wd1.myworkdayjobs.com/External_Career_Site/16/refreshFacet/318c8bb6f553100021d223d9780d30be"}},
    {"company_name": "Amazon Web Services", "job_scope": {"tech":"https://salesforce.wd1.myworkdayjobs.com/External_Career_Site/10/refreshFacet/318c8bb6f553100021d223d9780d30be","sales":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&category%5B%5D=sales-advertising-account-management&job_type%5B%5D=Full-Time&country%5B%5D=USA&business_category%5B%5D=amazon-web-services&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&", "marketing":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&category%5B%5D=marketing-pr&job_type%5B%5D=Full-Time&country%5B%5D=USA&business_category%5B%5D=amazon-web-services&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&", "business":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&category%5B%5D=marketing-pr&job_type%5B%5D=Full-Time&country%5B%5D=USA&business_category%5B%5D=amazon-web-services&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&","hardware":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&category%5B%5D=hardware-development&job_type%5B%5D=Full-Time&country%5B%5D=USA&business_category%5B%5D=amazon-web-services&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&","datascience":"https://www.amazon.jobs/en/search?offset=0&result_limit=10&sort=relevant&category%5B%5D=data-science&job_type%5B%5D=Full-Time&country%5B%5D=USA&business_category%5B%5D=amazon-web-services&distanceType=Mi&radius=24km&latitude=&longitude=&loc_group_id=&loc_query=&base_query=&city=&country=&region=&county=&query_options=&"}},
    {"company_name": "Apple", "job_scope": {"tech":"https://jobs.apple.com/en-us/search?location=united-states-USA&team=apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT+machine-learning-infrastructure-MLAI-MLI+deep-learning-and-reinforcement-learning-MLAI-DLRL+natural-language-processing-and-speech-technologies-MLAI-NLP+computer-vision-MLAI-CV+applied-research-MLAI-AR","hardware":"https://jobs.apple.com/en-us/search?location=united-states-USA&team=acoustic-technologies-HRDWR-ACT+analog-and-digital-design-HRDWR-ADD+architecture-HRDWR-ARCH+battery-engineering-HRDWR-BE+camera-technologies-HRDWR-CAM+display-technologies-HRDWR-DISP+engineering-project-management-HRDWR-EPM+environmental-technologies-HRDWR-ENVT+health-technology-HRDWR-HT+machine-learning-and-ai-HRDWR-MCHLN+mechanical-engineering-HRDWR-ME+process-engineering-HRDWR-PE+reliability-engineering-HRDWR-REL+sensor-technologies-HRDWR-SENT+silicon-technologies-HRDWR-SILT+system-design-and-test-engineering-HRDWR-SDE+wireless-hardware-HRDWR-WT","marketing":"https://jobs.apple.com/en-us/search?location=united-states-USA&team=services-marketing-MKTG-SVCM+product-marketing-MKTG-PM+marketing-communications-MKTG-MKTCM+corporate-communications-MKTG-CRPCM","sales":"https://jobs.apple.com/en-us/search?location=united-states-USA&team=apple-store-sales-SLDEV-ARS+retail-partner-sales-SLDEV-CRC+sales-planning-and-operations-SLDEV-SO","business":"https://jobs.apple.com/en-us/search?location=united-states-USA&team=business-development-SLDEV-BUSDEV+account-management-SLDEV-CC+field-and-solutions-engineering-SLDEV-FSE","finance":"https://jobs.apple.com/en-us/search?location=united-states-USA&team=business-development-SLDEV-BUSDEV+account-management-SLDEV-CC+field-and-solutions-engineering-SLDEV-FSE+finance-CORSV-FIN", "legal":"https://jobs.apple.com/en-us/search?location=united-states-USA&team=legal-CORSV-LEG"}},
    {"company_name": "Intel", "job_scope": {"tech":"https://jobs.intel.com/page/show/search-results#t=Jobs&sort=relevancy&layout=table&f:@countryfullname=[United%20States]&f:@employeetype=[Engineering,Software%20Engineering,Information%20Technology]","marketing":"https://jobs.intel.com/page/show/search-results#t=Jobs&sort=relevancy&layout=table&f:@countryfullname=[United%20States]&f:@employeetype=[Marketing]","sales":"https://jobs.intel.com/page/show/search-results#t=Jobs&sort=relevancy&layout=table&f:@countryfullname=[United%20States]&f:@employeetype=[Sales]"}},
    {"company_name": "Compunnel Software Group", "job_scope": {"healthcare":"https://app.stafflinepro.com/jobs?keyword=&location=","tech":"https://app.stafflinepro.com/jobs?keyword=&location=","business":"https://app.stafflinepro.com/jobs?keyword=&location=","marketing":"https://app.stafflinepro.com/jobs?keyword=&location="}},
    {"company_name": "Goldman Sachs", "job_scope": {"tech":"https://hdpc.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/requisitions?lastSelectedFacet=AttributeChar8&location=United%20States&locationId=300000000229164&locationLevel=country&selectedCategoriesFacet=300000016154093;300000016154101&selectedFlexFieldsFacets=%22AttributeChar6%257CNew+Associate+%2528FT%2529%253BNew+Analyst+%2528FT%2529%257C%257CAttributeChar8%257CEngineering+Division%22","finance":"https://hdpc.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/requisitions?lastSelectedFacet=AttributeChar8&location=United%20States&locationId=300000000229164&locationLevel=country&selectedCategoriesFacet=300000016154093;300000016154101&selectedFlexFieldsFacets=%22AttributeChar6%257CNew+Associate+%2528FT%2529%253BNew+Analyst+%2528FT%2529%257C%257CAttributeChar8%257CConsumer+and+Wealth+Management%253BAsset+Management%253BGlobal+Markets+Division%253BInvestment+Banking+Division%22"}},
    {"company_name": "Erp Analysts", "job_scope": {"consulting":"https://erpa.wd5.myworkdayjobs.com/ERPA?timeType=38b4d3993ec801872a273cc7a7147300&locations=a5956270549c01ef2fa9e362d518846e&workerSubType=a5956270549c0144aa2cf93a7518d90b"}},
    {"company_name": "Adobe", "job_scope": {}},
    {"company_name": "Zs Associates", "job_scope": {}},
    {"company_name": "T-Mobile", "job_scope": {}},
    {"company_name": "Sap America", "job_scope": {}},
    {"company_name": "The Mathworks", "job_scope": {}},
    {"company_name": "Prokarma", "job_scope": {}},
    {"company_name": "Expedia", "job_scope": {}},
    {"company_name": "Persistent Systems", "job_scope": {}},
    {"company_name": "Natsoft", "job_scope": {}},
    {"company_name": "Iris Software", "job_scope": {}},
    {"company_name": "Micron Technology", "job_scope": {}},
    {"company_name": "Infoshare Systems", "job_scope": {}},
    {"company_name": "American Express Travel Related Services", "job_scope": {}},
    {"company_name": "Optum Services", "job_scope": {}},
    {"company_name": "The Boston Consulting Group", "job_scope": {}},
    {"company_name": "Ciber Global", "job_scope": {}},
    {"company_name": "Bloomberg", "job_scope": {}},
    {"company_name": "Stanford University", "job_scope": {}},
    {"company_name": "Juniper Networks", "job_scope": {}},
    {"company_name": "Qualcomm Technologies", "job_scope": {}},
    {"company_name": "Randstad Technologies", "job_scope": {}},
    {"company_name": "Pricewaterhousecoopers Advisory Services", "job_scope": {}},
    {"company_name": "Mphasis", "job_scope": {}},
    {"company_name": "Uber", "job_scope": {}},
    {"company_name": "Virtusa", "job_scope": {}},
    {"company_name": "LinkedIn", "job_scope": {}},
    {"company_name": "Mastech Digital Technologies", "job_scope": {}},
    {"company_name": "Capital One Services", "job_scope": {}},
    {"company_name": "Mindtree", "job_scope": {}},
    {"company_name": "Hexaware Technologies", "job_scope": {}},
    {"company_name": "VM Ware", "job_scope": {}},
    {"company_name": "Synechron", "job_scope": {}},
    {"company_name": "Paypal", "job_scope": {}},
    {"company_name": "Oracle", "job_scope": {}},
    {"company_name": "Ust Global", "job_scope": {}},
    {"company_name": "Tesla", "job_scope": {}},
    {"company_name": "Bank Of America", "job_scope": {}},
    {"company_name": "Kpmg", "job_scope": {}},
    {"company_name": "Populus Group", "job_scope": {}},
    {"company_name": "Cisco Systems", "job_scope": {}},
    {"company_name": "Citicorp Credit Services", "job_scope": {}},
    {"company_name": "Cummins", "job_scope": {}},
    {"company_name": "Hcl Global Systems", "job_scope": {}},
    {"company_name": "Marlabs", "job_scope": {}},
    {"company_name": "Cerner", "job_scope": {}},
    {"company_name": "Comcast Cable Communications", "job_scope": {}},
    {"company_name": "V-Soft Consulting Group", "job_scope": {}},
    {"company_name": "Avco Consulting", "job_scope": {}},
    {"company_name": "Ebay", "job_scope": {}},
    {"company_name": "Kforce", "job_scope": {"tech": "https://www.kforce.com/find-work/search-jobs/#/?t=&l=%5B%5D", "finance": "https://www.kforce.com/find-work/search-jobs/#/?t=&l=%5B%5D"}},
    {"company_name": "Quest Global Services-NA", "job_scope": {"hardware": "https://krb-sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=30174&siteid=5116#keyWordSearch=&locationSearch=United%20States", "business": "https://krb-sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=30174&siteid=5116#keyWordSearch=&locationSearch=United%20States", "tech": "https://krb-sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=30174&siteid=5116#keyWordSearch=&locationSearch=United%20States"}},
    {"company_name": "Htc Global Services", "job_scope": {"tech": "https://www.htc.com/us/working/careers/", "marketing": "https://www.htc.com/us/working/careers/"}},
    {"company_name": "Collaborate Solutions", "job_scope": {"tech": "https://collaborative.wd1.myworkdayjobs.com/CollegeGrads/jobs?Location_Country=bc33aa3152ec42d4995f4791a106ed09", "business": "https://collaborative.wd1.myworkdayjobs.com/CollegeGrads/jobs?Location_Country=bc33aa3152ec42d4995f4791a106ed09"}},
    {"company_name": "Morgan Stanley Services Group", "job_scope": {"tech": "https://www.morganstanley.com/careers/career-opportunities-search#", "finance": "https://www.morganstanley.com/careers/career-opportunities-search#", "sales": "https://www.morganstanley.com/careers/career-opportunities-search#", "legal": "https://www.morganstanley.com/careers/career-opportunities-search#"}},
    {"company_name": "Barclays Services", "job_scope": {"tech": "https://search.jobs.barclays/search-jobs/United%20States/22545/2/6252001/39x76/-98x5/50/2", "marketing": "https://search.jobs.barclays/search-jobs/United%20States/22545/2/6252001/39x76/-98x5/50/2", "analytics": "https://search.jobs.barclays/search-jobs/United%20States/22545/2/6252001/39x76/-98x5/50/2", "finance": "https://search.jobs.barclays/search-jobs/United%20States/22545/2/6252001/39x76/-98x5/50/2", "legal": "https://search.jobs.barclays/search-jobs/United%20States/22545/2/6252001/39x76/-98x5/50/2"}},
    {"company_name": "Dell", "job_scope": {"hardware": "https://jobs.dell.com/location/united-states-jobs/375/6252001/2", "finance": "https://jobs.dell.com/location/united-states-jobs/375/6252001/2", "tech": "https://jobs.dell.com/location/united-states-jobs/375/6252001/2", "legal": "https://jobs.dell.com/location/united-states-jobs/375/6252001/2", "marketing": "https://jobs.dell.com/location/united-states-jobs/375/6252001/2", "sales": "https://jobs.dell.com/location/united-states-jobs/375/6252001/2"}},
    {"company_name": "Anthem", "job_scope": {}},
    {"company_name": "Blackrock Financial Management", "job_scope": {"tech": "https://careers.blackrock.com/job-search-results/?parent_category=Technology&addtnl_categories=Americas", "legal": "https://careers.blackrock.com/job-search-results/?parent_category=Legal%20%26%20Compliance&addtnl_categories=Americas", "marketing": "https://careers.blackrock.com/job-search-results/?parent_category=Marketing%20%26%20Communications&addtnl_categories=Americas", "sales": "https://careers.blackrock.com/job-search-results/?parent_category=Sales%20%26%20Relationship%20Management&addtnl_categories=Americas", "finance": "https://careers.blackrock.com/job-search-results/?parent_category=Finance%20%26%20Internal%20Audit&addtnl_categories=Americas", "business": "https://careers.blackrock.com/job-search-results/?parent_category=Business%20Management%20%26%20Strategy&addtnl_categories=Americas"}},
    {"company_name": "Intuit", "job_scope": {"tech": "https://jobs.intuit.com/location/united-states-jobs/27595/6252001/2", "business": "https://jobs.intuit.com/search-jobs?glat=38.9309&glon=-77.0843", "finance": "https://jobs.intuit.com/search-jobs?glat=38.93090057373047&glon=-77.08429718017578", "legal": "https://jobs.intuit.com/search-jobs?glat=38.93090057373047&glon=-77.08429718017578", "marketing": "https://jobs.intuit.com/search-jobs?glat=38.93090057373047&glon=-77.08429718017578", "sales": "https://jobs.intuit.com/search-jobs?glat=38.93090057373047&glon=-77.08429718017578"}},
    {"company_name": "Ntt Data Services", "job_scope": {"tech": "https://us.nttdata.com/en/careers", "business": "https://us.nttdata.com/en/careers", "legal": "https://us.nttdata.com/en/careers", "finance": "https://us.nttdata.com/en/careers", "marketing": "https://us.nttdata.com/en/careers"}},
    {"company_name": "Databricks", "job_scope": {"tech": "https://databricks.com/company/careers/open-positions?department=it&location=united-states", "legal": "https://databricks.com/company/careers/open-positions?department=legal&location=united-states", "finance": "https://databricks.com/company/careers/open-positions?department=finance&location=united-states", "marketing": "https://databricks.com/company/careers/open-positions?department=marketing&location=united-states", "sales": "https://databricks.com/company/careers/open-positions?department=sales&location=united-states"}}
]
