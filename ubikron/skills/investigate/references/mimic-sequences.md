# Mimic sequences: shortcuts by input type

Before running any Mimic service, check whether the case already has the result for this input (`fetch-all-mimic-results`). If it does, read it from there; don't run it again. And remember the hard gate: no enrichment until the input is confirmed unique.

These workflows are specific to particular Mimic providers and websites, and often get results faster. Which services exist depends on the user's server: check with `list-mimic-services`.

## Email address
1. Run LeakCheck and Dehashed for leaked passwords. If a password isn't a common one, run it back through LeakCheck and Dehashed to find other email addresses that use it. Look through those for ones that could be the subject. Don't discard throwaway addresses like frwaf22@gmail.com; only remove the ones that clearly aren't related.
2. Run OSINT Industries, Predicta or Epieos for social media profiles. Visit each one and mine it. If you're not logged in to a network, ask the user to log in.
3. Run WhoisXMLAPI to see whether the address registered any domains. Look at the sites on each domain, especially vanity domains tied directly to the subject.

## Phone number
1. Leak databases store numbers in different formats. Try with and without the country code, with and without the area code, with and without a plus sign. Run each format through Dehashed, LeakCheck and WhoisXMLAPI.
2. Look for the number being tied to someone or something other than the subject. You're looking for shared numbers.

## Name
1. FIRST confirm it's unique (the hard gate). Only then, run Dehashed on it. Look for email addresses in the results that could be the subject's, and use context to rule out the ones that aren't.
2. If it's unique, search for it on social networks with the custom search engine at https://cse.google.com/cse?cx=009983555355237802955:_kirhgouogi. Put the query in the `q` parameter, in quotes.
3. If it's unique, also run the name and surname with no space between them as an alias (below).

## Alias
1. Use Dehashed, LeakCheck and Predicta to find social media profiles.
2. Use the WhatsMyName enrichment, or the WhatsMyName website, to see which sites the alias is used on. Visit each one and mine it for PPs.

## Website
1. Look for old versions on the Wayback Machine, right back to the first. Mine old pages for contact details and other PPs.
2. Look on BuiltWith for relationships with other websites. Visit them and mine for new PPs.

## Physical address
Visit it in Google Maps street view. Read the signboards for contact details.

## Photo of a person
If it's a reasonably good photo, use reverse image or reverse face search services and look at the pages where the same person appears. These services make mistakes, so use the context of each page to judge whether it's really the subject.
