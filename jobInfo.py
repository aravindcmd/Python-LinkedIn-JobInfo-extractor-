# paste info_text = "<role>.<company name address>"
info_text = "Full-stack Developer.Garmin Nordic · Uddevalla, Västra Götaland County, Sweden"



words = info_text.split('.')
# print("Words",words)
company_input = words[1].split(' ·')[0]
position_input = words[0].lower()
country_input = words[-1].split(', ')[-1]
street_input =  words[1].split('· ')[1].split(f", {country_input}")[0]


# print(role)
# print(company)
# print(region)
# print(country)

print(r"\newcommand{\position}"+"{%s}"%(position_input))
print(r"\newcommand{\company}"+"{%s}"%(company_input))
print(r"\newcommand{\street}"+"{%s}"%(street_input))
print(r"\newcommand{\state}"+"{%s}"%(country_input))
