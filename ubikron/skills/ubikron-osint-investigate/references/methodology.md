# Generic online OSINT methodology

> **HARD GATE, NO EXCEPTIONS**
> NEVER run a Mimic enrichment, and NEVER classify an input as a strong pivot point, until a Google search in quotes has confirmed it's unique.
> If Google is blocked by a CAPTCHA or bot check, STOP COMPLETELY. Don't run Mimic enrichments as a workaround. Wait for the user to clear the CAPTCHA, do the uniqueness check, then carry on.
> Skipping the check wastes paid API credits and pollutes the case with data that belongs to someone else.

## 1. Is the input unique?

If something is unique, it's a strong pivot point (PP).

**Uniqueness pre-flight, every time:**
1. Search `"<input value>"` on Google, in quotes.
2. Note roughly how many results there are, and scan the first page.
3. Do all the results point to one identity? Yes: strong PP, go on. No: not unique; get more context first (section 3).
4. Names: if the first name OR the surname is rare and the results all point to one person, treat it as unique. A common name ("John Smith") is NOT a strong PP without more context.

Usually unique:
- An email address
- A phone number, if it's a mobile
- A social media profile URL
- Anything that identifies its owner one to one: a company number, a passport number

Unique depending on the value:
- **An alias.** "superman" isn't unique; "superman900" is more so. Use common sense, or search it.
- **A name and surname.** If either is rare. Search it in quotes and look at the hits.
- **A landline or 0800 number.** It could be a company with many employees, or a house with one owner.

Be sure before you call something a strong PP. A PP that isn't unique pulls the whole case in the wrong direction.

## 2. If the input is a strong PP, and only then

### a. Search it, in quotes

Follow this exactly. Don't skip steps or open pages early.

1. **Open page 1 of the results.** Extract every result URL (your browser file says how). Mark each one:
   - SKIP-DUPLICATE: the same content is already on your list via another URL (a Facebook share of an article you've recorded, for example).
   - SKIP-OFF-SUBJECT: demonstrably about a different person you've already ruled out, or a generic concept unrelated to the subject. Never "looks generic" or "looks low quality".
   - VISIT: everything else.
   Don't open anything yet.
2. **Go to the next page of results** and do the same. One page at a time.
3. **Stop paginating when a page gives zero new VISIT results**: every result is SKIP-DUPLICATE or SKIP-OFF-SUBJECT. A mix of the two still means stop. If a page has even one new VISIT result, carry on. Don't stop because results "look less promising"; that's cherry-picking.
   Safety cap: past 10 pages without a stop, pause and ask the user whether to continue. That deep usually means the query is too generic and needs more context.
4. **Build the deduplicated VISIT list and open every URL on it**, in order, and mine each page. The default is VISIT. The ONLY reasons to skip a URL are the two SKIP categories. Never skip because a title looks generic, low quality or obvious. Cherry-picking is the biggest single cause of missed findings.
5. **Sanity check before Mimic.** Count the VISIT list and confirm you opened every one. If you opened fewer than about 80% of the unique-domain results, you're cherry-picking: go back and open the rest.
6. **For each pivotal page**: tag it "Favorite" and note the PPs it gave you.

Don't open any result before pagination has stopped. Don't skip a result on its title: open it and let the page tell you.

### b. Enrich it with Mimic

Run the value through the relevant Mimic services (see `mimic-sequences.md`). Mine the results for information and next-round PPs. After each service, note the service and what it found in memory, and add new PPs to the graph straight away.

## 3. If the input is NOT unique

### a. Search for more context, with well-chosen qualifiers

Which qualifiers depends on how common the bare name is. Work out the regime FIRST by counting namesakes in the bare `"<value>"` results:

- **Regime A: the bare name is already close to unique** (one person dominates the results). You don't need to disambiguate. Qualifiers are only for finding NEW content: pick any WIDE qualifier and paginate.
- **Regime B: a handful of namesakes** (two to five people; the usual case). One good qualifier disambiguates and widens at once. Use a WIDE qualifier that's very likely on any page about the right person: their profession, their field, their city. Run a few in parallel; each opens a different slice of the web.
- **Regime C: a dictionary-common name** ("Gary Smith", "John Lee": hundreds or thousands of people). One qualifier won't do it. STACK them, at least profession + location + employer, just to land on one person. Then add a fourth dimension (a hobby, an affiliation, an event they attended) to widen beyond what they produce themselves.

**Qualifiers, for every regime:**
- WIDE qualifiers describe what the subject IS without being their own brand: profession or role, field of work, location (city, country, region), or an identity adjective. These surface third-party mentions, archives, attendee lists and citations, where early-career data that isn't indexed under their name lives.
- NARROW qualifiers are the subject's OWN company, project, brand or product names: anything they control. They pull results into the subject's own mirror (their blog, their repos, press they control). Run ONE narrow search early to confirm identity and get the headline sources. Don't lean on narrow qualifiers to find new things in later rounds.
- Sanity check: if every result on page 1 is from sites the subject controls or is closely tied to, the qualifier is too narrow. Pick a wider one.
- Cover at least three dimensions: at least one profession or role word, at least one location, at least one identity adjective.
- An identity adjective describes the person without being owned by them: a community label ("OSINT speaker", "open-source maintainer"), a nationality, an alma mater shorthand. Anything a third party would use to describe them in passing.

### b. Ask the user for more context

The value plus the extra context may give you a strong PP again.

The same regime and qualifier rule applies in every later round: when searches on their own brand names stop giving new results, widen with profession, location and identity qualifiers before calling a search dead.

## Mining pages and Mimic results

- **A page from a search**: look for new PPs related to the input. Then go through every section of the profile template (`report.md`) and take anything the page offers for it.
- **Mimic results**: they'll usually contain more PPs. Make sure the input was very unique, OR find context in the results that matches the subject. If you're not sure, ask the user.

## Rounds: the most important part

- The cycle: use a PP in searches and/or Mimic enrichments → mine the results for more PPs and profile information → fill in the profile. Then a new round: for each PP found, start again.
- Before each new round, check the graph and memory: every PP from the last round should be documented. That's your checkpoint.
- At the end of a round, take all the PPs it produced and run the same process on them. Unsure whether a PP belongs in the next round? Ask the user.
- **When to stop**: when you can't find more PPs, or the data makes it clear more won't help the profile. Expect a few hops where you can't tell if you're on track. Take this chain: email → domain → website → tracking code → related website → Wayback Machine → old contact form → phone number. Stop at "related website" and you'd never have found the phone number. If you're unsure whether to stop, ask the user.

## Correcting mistakes

At any stage you may find a wrong assumption from an earlier round: following the wrong trail because a PP was attributed to the wrong identity. This happens often. Fix the profile, adding and removing information. ALWAYS check the whole profile against new information; never just add to it. Document the mistake too, so the user doesn't repeat it.
